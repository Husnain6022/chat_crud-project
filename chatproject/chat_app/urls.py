from django.urls import path
from . import views

urlpatterns = [
    # URL for accessing the chat room
    path('chat/<str:room_name>/', views.chat_view, name='chat-room'),
]
