# Generated by Django 4.0.5 on 2022-07-13 12:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mail_app', '0002_remove_emailentry_created_datetime_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='emailentry',
            name='created_datetime',
            field=models.DateTimeField(auto_now=True, verbose_name='Дата и время создания'),
        ),
    ]