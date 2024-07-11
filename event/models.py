from django.db import models
from django.contrib import admin
from user.models import User, Client


# Model for save base info about every session. Have relations to client (model 'EventClient')
# and to workers (model 'EventUser')
class Event(models.Model):
    scheduled_day = models.DateField()
    scheduled_time = models.TimeField()
    description = models.TextField()
    is_confirmed = models.BooleanField(default=False)


# Submodels for create relations between User, Client and Event
class EventUser(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class EventClient(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ['id', 'scheduled_day', 'scheduled_time', 'is_confirmed']
    list_filter = ['is_confirmed']
    search_fields = ['scheduled_day']
    ordering = ['id']
