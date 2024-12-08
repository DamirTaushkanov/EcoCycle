from django.db import models
from django.contrib.auth.models import AbstractUser

from items.models import Products


class Users(AbstractUser):
    def __str__(self):
        return self.username

'''class UserHistory(models.Model):
    user = models.ForeignKey('accounts.Users', on_delete=models.CASCADE)
    activity = models.CharField(max_length=50)
    item = models.ManyToManyField(Products)
    category = models.CharField(max_length=20,blank=False)'''

class Profile(models.Model):
    user = models.OneToOneField('accounts.Users', on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50, default="", blank=True)
    last_name = models.CharField(max_length=50, default="", blank=True)
    profile_pic = models.ImageField(upload_to="account/image/", blank=True)
    bio = models.TextField(default="", blank=True)

    def __str__(self):
        return self.user_id

class Locate(models.Model):
    user = models.OneToOneField('accounts.Users', on_delete=models.CASCADE)
    latitude = models.FloatField()
    longitude = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} ({self.latitude}, {self.longitude})"