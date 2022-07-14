from datetime import timezone

from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Post(models.Model):
    name = models.CharField(max_length=128, blank=True)
    description = models.TextField(max_length=500,  blank=True)


    def __str__(self):
        return self.name

class Comments(models.Model):
    post = models.ForeignKey(User, on_delete=models.CASCADE , related_name="comments")
    author = models.CharField(max_length=100)
    text = models.TextField()
    date_coment = models.DateTimeField(auto_now_add=False)
    active = models.BooleanField(default=False)


    def prouve(self):
        self.prouveder_comment = True
        self.save()

    def __str__(self):
        return self.text















