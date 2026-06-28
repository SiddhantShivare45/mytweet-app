from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Tweet(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    text=models.TextField(max_length=250)
    photo=models.ImageField(upload_to='Tweetphotos/',blank=True,null=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.user.username}-{self.text[:10]}'
    

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=150, blank=True)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.name} - {self.subject[:20]}'