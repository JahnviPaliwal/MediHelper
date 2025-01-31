# models.py
from django.db import models

class UserProfile(models.Model):
    age = models.PositiveIntegerField()
    sex = models.CharField(max_length=100)
    bmi = models.FloatField()
    children = models.PositiveIntegerField()
    smoker = models.CharField(max_length=100)
    region = models.CharField(max_length=100)
    charges = models.FloatField()

    def __str__(self):
        return self.sex
