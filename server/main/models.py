from pathlib import Path
from django.core.validators import RegexValidator
from django.db import models
from django.contrib import admin


class Business(models.Model):
    name = models.CharField()
    email = models.EmailField()
    short_info = models.TextField()
    full_info = models.TextField()
    phone = models.CharField(max_length=10, validators=[RegexValidator(r'^\d{10}$', message='Phone number must be exactly 10 digits')])
    address = models.TextField()
    logo = models.ImageField(upload_to=Path(__file__).resolve().parent.parent/'static'/'media'/'photos', blank=True)

    class Meta:
        verbose_name = 'Business'
        verbose_name_plural = 'Businesses'


@admin.register(Business)
class BusinessAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'address')
