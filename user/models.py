from django.contrib import admin
from django.contrib.auth.models import AbstractUser
from django.db import models


# Information model of users and admins
class User(AbstractUser):
    is_admin = models.BooleanField(default=False)
    email = models.EmailField()
    age = models.IntegerField()
    phonenumber = models.IntegerField(max_length=10)
    photo = models.ImageField(upload_to='static/media/photos/users/')
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


# Submodel to 'User' (1-to-1 relations) of links to workers social nets like FB and Instagram or personal webpage
class UserSocials(models.Model):
    user = models.OneToOneField(User, name='portfolio_links', on_delete=models.CASCADE)
    facebook = models.URLField(blank=True, null=True)
    instagram = models.URLField(blank=True, null=True)
    patreon = models.URLField(blank=True, null=True)
    twitter = models.URLField(blank=True, null=True)
    personal_website = models.URLField(blank=True, null=True)


# Clients DB model
class Client(models.Model):
    phonenumber = models.IntegerField(max_length=10, unique=True)
    password = models.CharField(max_length=50, blank=False)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    registration_date = models.DateField(auto_now_add=True)


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name', 'username', 'is_admin']
    search_fields = ['is_admin', 'username']
    ordering = ['id']


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'phonenumber']
    search_fields = ['phonenumber']
    ordering = ['id']
