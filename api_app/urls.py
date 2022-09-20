from django.urls import path
from . import views


app_name = 'api_app'

urlpatterns = [
    path('users/', views.UserListAPIView.as_view(), name='user_list_api'),
    path('users/<int:pk>/', views.UserDetailAPIView.as_view(), name='user_detail_api'),
    path('posts/', views.PostsListView.as_view(), name='post_list_api'),
    path('posts/<int:pk>/', views.PostDetailView.as_view(), name='post_detail'),
    path('posts/by_author_id/<int:pk>/', views.AuthorsPostsListView.as_view(), name='posts_of_author'),
]
