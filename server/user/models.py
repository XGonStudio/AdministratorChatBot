from pathlib import Path

from django.contrib.auth.models import AbstractUser
from django.contrib import admin
from django.core.validators import RegexValidator
from django.db import models


GENDER_CHOICES = [
    ('male', 'Чоловік'),
    ('female', 'Жінка')
]
user_photo_path = Path(__file__).resolve().parent.parent/'static'/'media'/'photos'/'workers'


class User(AbstractUser):
    is_admin = models.BooleanField(default=False)
    email = models.EmailField()
    birth = models.DateField(blank=True, null=True)
    gender = models.CharField(max_length=7, choices=GENDER_CHOICES)
    phone_number = models.CharField(max_length=10, validators=[RegexValidator(r'^\d{10}$', message='Phone number must be exactly 10 digits')])
    photo = models.ImageField(upload_to=user_photo_path)
    description = models.TextField()
    location = models.CharField(max_length=50)
    groups = models.ManyToManyField('auth.Group', related_name='user_group', blank=True)
    user_permissions = models.ManyToManyField('auth.Permission', related_name='user_permissions', blank=True)

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'

        def __str__(self):
            return self.verbose_name


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'is_admin', 'gender', 'phone_number')
    search_fields = ['id', 'is_admin', 'gender']
    ordering = ['id']


# Submodel to 'User' (1-to-1 relations) for save links to worker socials like FB and Instagram or personal webpage
class UserSocials(models.Model):
    user = models.OneToOneField(User, name='links', on_delete=models.CASCADE)
    facebook = models.URLField(blank=True, null=True)
    instagram = models.URLField(blank=True, null=True)
    patreon = models.URLField(blank=True, null=True)
    twitter = models.URLField(blank=True, null=True)
    personal_website = models.URLField(blank=True, null=True)


@admin.register(UserSocials)
class UserSocialsAdmin(admin.ModelAdmin):
    list_display = ['id']
