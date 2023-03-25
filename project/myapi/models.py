# models.py
from django.db import models
class Task(models.Model):
    name = models.CharField(max_length=60)
    status = models.CharField(max_length=60)
    def __str__(self):
        return self.name