from django.shortcuts import render

# Create your views here.
# posts/views.py
from rest_framework import generics

from .models import Post, Orders
from .serializers import PostSerializer, OrdersSerializer


class PostList(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class PostDetail(generics.RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class OrdersDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Orders.objects.all()
    serializer_class = OrdersSerializer