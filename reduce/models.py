from django.db import models
from django.contrib.auth.models import User


class Link(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    link = models.CharField(max_length=1000)
    shortlink = models.CharField(max_length=200)

    def __str__(self):
        return self.shortlink
