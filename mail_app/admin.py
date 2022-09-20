from django.contrib import admin
from .models import EmailEntry


class EmailEntryAdmin(admin.ModelAdmin):
    list_display = ('author', 'send_to', 'sent_datetime', 'created_at')


admin.site.register(EmailEntry, EmailEntryAdmin)
