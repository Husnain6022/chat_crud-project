from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from .models import Item
from .serializers import ItemSerializer
from bson import ObjectId  # Ensure you have this import at the top


class ItemAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        # Get all items for the authenticated user
        items = Item.objects.filter(owner=request.user)
        serializer = ItemSerializer(items, many=True)
        return Response(serializer.data)

    def post(self, request):
        # Create a new item
        serializer = ItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(owner=request.user)  # Save the item with the owner
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ItemDetailAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get_object(self, pk):
        try:
            # Convert the pk to ObjectId before querying
            return Item.objects.get(_id=ObjectId(pk),
                                    owner=self.request.user)  # Ensure you're using the right field for ObjectId
        except (Item.DoesNotExist, ValueError):
            return None  # Handle ValueError if pk is not a valid ObjectId

    def get(self, request):
        # Get a specific item by its ID
        pk = request.query_params.get('pk', None)
        if pk is None:
            return Response({"detail": "No primary key provided."}, status=status.HTTP_400_BAD_REQUEST)

        item = self.get_object(pk)
        if item is None:
            return Response({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)

        serializer = ItemSerializer(item)
        return Response(serializer.data)

    def put(self, request):
        # Update an existing item

        pk = request.query_params.get('pk', None)
        print(pk)
        print(type(pk))
        if pk is None:
            return Response({"detail": "No primary key provided."}, status=status.HTTP_400_BAD_REQUEST)

        item = self.get_object(pk)
        if item is None:
            return Response({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)

        serializer = ItemSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request):
        # Partially update an existing item
        pk = request.query_params.get('pk', None)
        if pk is None:
            return Response({"detail": "No primary key provided."}, status=status.HTTP_400_BAD_REQUEST)

        item = self.get_object(pk)
        if item is None:
            return Response({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)

        serializer = ItemSerializer(item, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request):
        # Delete an item
        pk = request.query_params.get('pk', None)
        if pk is None:
            return Response({"detail": "No primary key provided."}, status=status.HTTP_400_BAD_REQUEST)

        item = self.get_object(pk)
        if item is None:
            return Response({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)

        item.delete()
        return Response({"detail": "item deleted."},status=status.HTTP_204_NO_CONTENT)