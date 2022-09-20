from celery import shared_task
from django.core.mail import send_mail
from .models import EmailEntry


@shared_task(name='send_scheduled_mail')
def send_scheduled_mail(email_id):
    email_instance = EmailEntry.objects.get(pk=email_id)
    send_mail(
        'Напоминание',
        'Добрый день! Если вы получили это сообщение, то сервис напоминаний работает и может напонить вам о чём-либо после его доработки.',
        'admin@example.com',
        [email_instance.send_to],
        fail_silently=False,
    )
