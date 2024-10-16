from django.urls import path
from .views import ItemAPIView, ItemDetailAPIView

urlpatterns = [
    path('items/', ItemAPIView.as_view(), name='item-list'),  # For list and create
    path('item/', ItemDetailAPIView.as_view(), name='item-detail'),  # For retrieve, update, partial update, delete
]