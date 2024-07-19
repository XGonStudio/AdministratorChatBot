from django.core.validators import RegexValidator
from django.db import models
from django.contrib import admin
from user.models import User


STATUS = {
    'confirmed': 'Confirmed',
    'pending': 'Pending',
    'cancelled': 'Cancelled',
    'done': 'Done'
}
class Event(models.Model):
    date = models.DateTimeField(auto_now_add=False)
    description = models.TextField()
    client_phone = models.CharField(max_length=10, validators=[RegexValidator(r'^\d{10}$', message='Phone number must be exactly 10 digits')])
    # is_confirmed = models.BooleanField(default=False, blank=False, null=False)
    worker = models.ForeignKey(User, on_delete=models.CASCADE, related_name='worker', null=True)
    status = models.CharField(max_length=9, choices=STATUS, default=STATUS['pending'])


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('id', 'status', 'date', 'worker', 'client_phone')
    search_fields = ['date', 'client_phone']
    list_filter = ['status']
