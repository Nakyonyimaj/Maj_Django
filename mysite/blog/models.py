from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Posts(models.Model):
    title = models.CharField(max_length=250)
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    
    
    def __str__(self):
        return self.title
