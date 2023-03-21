# models.py
from django.db import models
class Hero(models.Model):
    name = models.CharField(max_length=60)
    alias = models.CharField(max_length=60)
    age = models.CharField(max_length=60,null=True)
    def __str__(self):
        return self.name

class Task(models.Model):
    name = models.CharField(max_length=60)
    status = models.CharField(max_length=60)
    def __str__(self):
        return self.name