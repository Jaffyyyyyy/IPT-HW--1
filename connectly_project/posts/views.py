from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import User, Post
from .serializers import UserSerializer, PostSerializer
from django.shortcuts import get_object_or_404 # For more robust error handling

# User Views
class UserListCreateView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly] # Allow anyone to read, but only authenticated to create

class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly] # Allow anyone to read, but only authenticated to update/delete
    # Optionally, add a custom permission to allow users to only edit their own profile

from .permissions import IsPostAuthor

# Post Views
class PostListCreateView(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly] # Allow anyone to read, but only authenticated to create

    def perform_create(self, serializer):
        # Set the author of the post to the currently authenticated user
        serializer.save(author=self.request.user)

class PostDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsPostAuthor] # ADDED IsPostAuthor
