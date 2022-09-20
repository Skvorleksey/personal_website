# Generated by Django 4.0.5 on 2022-07-13 12:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='EmailEntry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('send_to', models.EmailField(max_length=254, verbose_name='Адрес получателя')),
                ('subject', models.CharField(max_length=150, verbose_name='Тема письма')),
                ('text', models.TextField(verbose_name='Текст поста')),
                ('created_datetime', models.DateTimeField(auto_now=True, verbose_name='Дата и время создания')),
                ('sent_datetime', models.DateTimeField(verbose_name='Дата и время отправки')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Рассылка',
                'verbose_name_plural': 'Рассылки',
            },
        ),
    ]
