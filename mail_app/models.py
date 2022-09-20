from django.db import models
from personal_site.settings import AUTH_USER_MODEL


class EmailEntry(models.Model):
    author = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE)
    send_to = models.EmailField(verbose_name='Адрес получателя')
    created_at = models.DateTimeField(auto_now=True, verbose_name='Дата и время создания',)
    sent_datetime = models.DateTimeField(verbose_name='Дата и время отправки')

    class Meta:
        verbose_name = "Рассылка"
        verbose_name_plural = "Рассылки"
