# Generated by Django 5.0.7 on 2024-07-19 04:45

import pathlib
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_alter_business_logo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='business',
            name='logo',
            field=models.ImageField(blank=True, upload_to=pathlib.PureWindowsPath('E:/Python/BusinesscardChatBot/server/static/media/photos')),
        ),
    ]
