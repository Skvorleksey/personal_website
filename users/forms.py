from django import forms
from django.db import models
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import User


class UserCreationForm(UserCreationForm):
    photo = forms.ImageField(required=False)
    username = forms.CharField(help_text='', widget=forms.TextInput, label='Имя пользователя')
    hobby = forms.CharField(help_text='', label='Хобби', required=False)

    class Meta:
        model = User

        fields = ('username', 'photo', 'company', 'hobby')


class UserChangeForm(UserChangeForm):
    photo = forms.ImageField(required=False)
    username = forms.CharField(help_text='', widget=forms.TextInput, label='Имя пользователя')
    hobby = forms.CharField(help_text='', label='Хобби', required=False)

    class Meta:
        model = User
        fields = ('username', 'photo', 'company', 'hobby')
