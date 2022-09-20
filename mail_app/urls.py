from django.urls import path
from . import views

app_name = 'mail_app'

urlpatterns = [
    path('send', views.CreateMail.as_view(), name='send_mail'),
]
