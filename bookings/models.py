from django.conf import settings
from django.db import models
from django.contrib.auth.models import User

class Table(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=2000)
    active = models.BooleanField(default=1)

class Booking(models.Model):
    creator = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='author')
    table = models.ForeignKey(Table, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=2000)
    max_participants = models.IntegerField(default=0)
    start_date = models.DateTimeField(auto_now=False, auto_now_add=False)
    end_date = models.DateTimeField(auto_now=False, auto_now_add=False)
    attendants = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='attendant')

class Member(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    alias = models.CharField(max_length=100)
