from django.db import models
from datetime import time

from django.db.models import CharField


# Create your models here.
class Room(models.Model):
    name = models.CharField(max_length=100)
    floor_number = models.IntegerField(default=2)
    room_number = CharField(max_length=1)

    def __str__(self):
        return f"{self.name} {self.room_number} on floor {self.floor_number}"

class Meeting(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateField()
    start_time = models.TimeField(default=time(10))
    duration = models.IntegerField(default=1)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title} at {self.start_time} on {self.date}"

