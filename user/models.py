from datetime import datetime
from django.contrib import admin
from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    is_admin = models.BooleanField(default=False)
    email = models.EmailField()
    age = models.IntegerField()
    phonenumber = models.IntegerField(max_length=10)
    photo = models.ImageField(upload_to='user/photos/')
    description = models.TextField()
    location = models.CharField()
    session_time = models.IntegerField()
    groups = models.ManyToManyField(
        'auth.Group', related_name='user_group', blank=True
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission', related_name='user_permissions', blank=True
    )

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'

        def __str__(self):
            return self.verbose_name


class UserPortfolio(models.Model):
    user = models.OneToOneField(User, name='portfolio_links', on_delete=models.CASCADE)
    facebook = models.URLField(blank=True, null=True)
    instagram = models.URLField(blank=True, null=True)
    patreon = models.URLField(blank=True, null=True)
    twitter = models.URLField(blank=True, null=True)
    personal_website = models.URLField(blank=True, null=True)


class Client(models.Model):
    phonenumber = models.IntegerField(max_length=10, unique=True)
    password = models.CharField(max_length=50, blank=False)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    registration_date = models.DateField(default=datetime.now)


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name', 'username', 'is_admin']
    search_fields = ['is_admin', 'username']
    ordering = ['id']
