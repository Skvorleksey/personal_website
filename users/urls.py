from django.urls import path, include
from . import views


app_name = 'users'

urlpatterns = [
    path('sign_up', views.CreateUserView.as_view(), name='sign_up'),
    path('', include('django.contrib.auth.urls')),
    path('', views.UsersListView.as_view(), name='users_list'),
    path('<int:pk>/', views.UserDetailView.as_view(), name='user_detail'),
    path('update', views.UpdateUserView.as_view(), name='update'),
]
