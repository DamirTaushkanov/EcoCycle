from django.db import models

class Products(models.Model):
    user = models.ForeignKey('accounts.Users', on_delete=models.CASCADE)
    title = models.CharField(max_length=100, blank=False)
    count = models.IntegerField(default=0, blank=False)
    categories = models.CharField(max_length=20, blank=False)
    description = models.TextField(max_length=1000, default="", blank=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    trade = models.BooleanField(default=False)
    date_added = models.DateTimeField(auto_now_add=True)
    views_count = models.IntegerField(default=0, blank=False)
    def __str__(self):
        return self.title
class ProductImages(models.Model):
    product = models.ForeignKey('items.Products', on_delete=models.CASCADE)
    images = models.ImageField(upload_to='products/images/')
