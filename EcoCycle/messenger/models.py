from django.db import models

class Chat(models.Model):
    name = models.CharField(max_length=255)
    participants = models.ManyToManyField('accounts.Users')

    def __str__(self):
        return self.name

class Message(models.Model):
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE, related_name='messages')
    sender = models.ForeignKey('accounts.Users', on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.sender.username}: {self.content[:50]}'
