from django.core.validators import RegexValidator
from django.db import models
from django.contrib import admin
from user.models import User


class Event(models.Model):
    date = models.DateTimeField(auto_now_add=False)
    description = models.TextField()
    client_phone = models.CharField(max_length=10, validators=[RegexValidator(r'^\d{10}$', message='Phone number must be exactly 10 digits')])
    is_confirmed = models.BooleanField(default=False)
    worker = models.ForeignKey(User, on_delete=models.CASCADE, related_name='worker', null=True)


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('id', 'is_confirmed', 'date', 'worker', 'client_phone')
    search_fields = ['date', 'client_phone']
    list_filter = ['is_confirmed']
