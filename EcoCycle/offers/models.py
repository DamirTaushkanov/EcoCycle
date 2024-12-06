from django.db import models
from items.models import Products
class Offers(models.Model):
    sender_item = models.ManyToManyField(Products, related_name='sender_item')
    addressee_products = models.ManyToManyField(Products, related_name='addressee_products')
    date = models.DateTimeField(auto_now_add=True)
    accept = models.BooleanField(default=False)
# Create your models here.
