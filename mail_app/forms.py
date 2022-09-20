from django.forms import ModelForm, DateTimeField, DateTimeInput
from django.forms import widgets
from .models import EmailEntry


class SendMailForm(ModelForm):
    sent_datetime = DateTimeField(widget=widgets.DateTimeInput(attrs={'type':'datetime-local'}), label='Дата и время отправки')

    class Meta:
        model = EmailEntry
        fields = ('send_to', 'sent_datetime',)
