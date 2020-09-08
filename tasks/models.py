from django.conf import settings
from django.db import models
from django.utils import timezone


class Task(models.Model):
    title = models.CharField(max_length=200)
    additional_participants = models.CharField(max_length=200)
    due_date = models.DateTimeField(blank=True, null=True)
    complete = models.BooleanField(default=False)

    def __str__(self):
        return self.title