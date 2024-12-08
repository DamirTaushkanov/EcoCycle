from django.db import models

class Message(models.Model):
    sender = models.ForeignKey('accounts.Users', related_name='sender', on_delete=models.CASCADE)
    receiver = models.ForeignKey('accounts.Users', related_name='receiver', on_delete=models.CASCADE)
    content = models.TextField()
    sender_product = models.ForeignKey('items.Products', related_name='sender_product', on_delete=models.CASCADE, default=None, null=True)
    receiver_product = models.ForeignKey('items.Products', related_name='receiver_product', on_delete=models.CASCADE, default=None, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.sender.username}: {self.content[:50]}'