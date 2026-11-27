from django.db import models
from django.contrib.auth.models import User


class Course(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    code = models.CharField(max_length=20)
    name = models.CharField(max_length=100)
    meetingDays = models.CharField(max_length=20)
    startTime = models.TimeField()
    endTime = models.TimeField()
    building = models.CharField(max_length=50)
    room = models.CharField(max_length=20)
    professorName = models.CharField(max_length=100)
    officeHours = models.CharField(max_length=100, blank=True)
    officeLocation = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.code