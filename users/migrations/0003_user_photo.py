# Generated by Django 4.0.5 on 2022-07-06 07:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_user_company_user_hobby'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='photo',
            field=models.ImageField(blank=True, default='images/user_profile/default_avatar.png', upload_to='images/user_profile/', verbose_name='Фото'),
        ),
    ]
