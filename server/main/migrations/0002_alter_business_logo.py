# Generated by Django 5.0.7 on 2024-07-18 13:35

import pathlib
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='business',
            name='logo',
            field=models.ImageField(blank=True, upload_to=pathlib.PureWindowsPath('E:/Python/AdministratorChatBot/server/static/media/photos')),
        ),
    ]
