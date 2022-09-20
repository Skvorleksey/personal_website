from rest_framework import generics
from users.models import User
from .serializers import UserSerializer, PostSerializer
from blog.models import BlogPost
from rest_framework import permissions
from .permissions import IsAuthorOrReadOnly
from datetime import datetime


class UserListAPIView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetailAPIView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class PostsListView(generics.ListCreateAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = PostSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(
            author=self.request.user,
            edited=False,
            publication_date_time=datetime.now(),
            edited_date_time=datetime.now(),
        )


class PostDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = PostSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsAuthorOrReadOnly)

    def perform_update(self, serializer):
        serializer.save(
            author=self.request.user,
            edited=True,
            edited_date_time=datetime.now(),
        )


class AuthorsPostsListView(generics.ListAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = PostSerializer

    def get_queryset(self):
        return super().get_queryset().filter(
            author_id=self.kwargs['pk']
        )
