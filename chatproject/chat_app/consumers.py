import json
from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.tokens import AccessToken
from django.db import transaction


User = get_user_model()


class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.user = await self.get_user_from_token()
        if not self.user:
            await self.close()
        else:
            self.room_name = self.scope['url_route']['kwargs']['room_name']
            self.room_group_name = f'chat_{self.room_name}'

            # Fetch or create the chat room
            self.room = await self.get_or_create_room(self.room_name)

            # Add the WebSocket to the chat group
            await self.channel_layer.group_add(
                self.room_group_name,
                self.channel_name
            )

            await self.accept()

            # Load and send previous chat messages to the user
            await self.load_chat_history(self.room_name)

    @database_sync_to_async
    def get_or_create_room(self, room_name):
        from .models import ChatRoom  # Import here
        with transaction.atomic():
            room, created = ChatRoom.objects.get_or_create(name=room_name)
            if created:
                room.save()

            # Refresh from db to ensure we have the latest state
            room.refresh_from_db()

            # Add the user to the room participants
            if not room.participants.filter(id=self.user.id).exists():
                room.participants.add(self.user)

            # Save again to ensure all changes are committed
            room.save()

        return room

    @database_sync_to_async
    def add_participant(self, room_name, user):
        from .models import ChatRoom  # Import here
        room, created = ChatRoom.objects.get_or_create(name=room_name)

        # Check if the user is already a participant
        if not room.participants.filter(id=user.id).exists():
            room.participants.add(user.id)  # Add user to the room participants

    @database_sync_to_async
    def get_user_from_token(self):
        token = self.scope['query_string'].decode().split('=')[1]
        try:
            access_token = AccessToken(token)
            user = User.objects.get(id=access_token['user_id'])  # Use get_user_model() for User
            return user
        except Exception as e:
            print(f"Token error: {e}")  # Debugging info
            return None

    @database_sync_to_async
    def get_chat_history(self, room_name):
        from .models import ChatRoom  # Import here
        room = ChatRoom.objects.get(name=room_name)
        return list(room.messages.order_by('timestamp').values('sender__username', 'content', 'timestamp'))

    async def load_chat_history(self, room_name):
        messages = await self.get_chat_history(room_name)
        for message in messages:
            # Convert the 'timestamp' field to an ISO formatted string
            timestamp = message['timestamp'].isoformat() if message['timestamp'] else None
            await self.send(text_data=json.dumps({
                'message': message['content'],
                'user_id': message['sender__username'],
                'timestamp': timestamp  # Use the ISO formatted timestamp
            }))

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        user_id = self.user.id

        # Save the message in the database
        await self.save_message(user_id, self.room_name, message)

        # Broadcast the message to the room
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message,
                'user_id': self.user.username
            }
        )

    async def chat_message(self, event):
        message = event['message']
        user_id = event['user_id']

        await self.send(text_data=json.dumps({
            'message': message,
            'user_id': user_id
        }))

    @database_sync_to_async
    def save_message(self, user_id, room_name, message):
        from .models import ChatRoom, Message  # Import here
        user = User.objects.get(id=user_id)
        room = ChatRoom.objects.get(name=room_name)
        Message.objects.create(sender=user, room=room, content=message)
