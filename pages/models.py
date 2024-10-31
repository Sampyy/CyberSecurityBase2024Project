from django.utils.timezone import now
from django.db import models
from django.contrib.auth.models import User

class Account(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    firstquestion = models.TextField(default='null')
    secondquestion = models.TextField(default='null')
    def __str__(self):
        return self.user.username


class Message(models.Model):
    content = models.TextField(default='null')
    sender = models.ForeignKey(Account, on_delete=models.CASCADE,related_name='sender')
    receiver = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='receiver')
    def __str__(self):
        return self.content + ' from: ' + self.sender.user.username + ', to: ' + self.receiver.user.username + ', on: '
    
