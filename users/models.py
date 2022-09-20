from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    photo = models.ImageField(verbose_name='Фото',
                              blank=True,
                              default='images/user_profile/default_avatar.png',
                              upload_to='images/user_profile/')
    company = models.CharField(max_length=100, blank=True, verbose_name='Место работы')
    hobby = models.CharField(max_length=100, blank=True, verbose_name='Хобби')
