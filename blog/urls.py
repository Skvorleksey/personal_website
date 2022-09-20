from django.urls import path
from .views import PostsListView, PostsDetailView, PostCreateView, PostUpdateView


app_name = 'blog'

urlpatterns = [
    path('posts', PostsListView.as_view(), name='posts'),
    path('posts/<int:pk>/', PostsDetailView.as_view(), name='post_details'),
    path('posts/create/', PostCreateView.as_view(), name='create_post'),
    path('posts/update/<int:pk>/', PostUpdateView.as_view(), name='update_post'),
]
