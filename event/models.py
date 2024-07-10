from django.db import models

from user.models import User, Client


class Event(models.Model):
    scheduled_day = models.DateField()
    scheduled_time = models.TimeField()
    description = models.TextField()
    is_confirmed = models.BooleanField(default=False)


class EventUser(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class EventClient(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)