from django.contrib.auth.models import User
from django.db import models

class Notice(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField()
    date_sended = models.DateTimeField(auto_now_add=True)
