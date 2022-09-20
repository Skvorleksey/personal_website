from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User
from .forms import UserCreationForm, UserChangeForm


class CustomUserAdmin(UserAdmin):
    add_form = UserCreationForm
    form = UserChangeForm

    model = User
    list_display = ['username', 'photo', 'hobby', 'company']

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'photo', 'hobby', 'company', 'password1', 'password2')
        }),
    )


admin.site.register(User, CustomUserAdmin)
