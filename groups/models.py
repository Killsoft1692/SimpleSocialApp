from django.contrib.auth.models import User
from django.db import models


class Group(models.Model):
    name = models.CharField(max_length=256)
    description = models.TextField(blank=True)
    followers = models.ManyToManyField(User, related_name='member_of', blank=True)
    likes = models.ManyToManyField(User, blank=True, related_name='+')

    def __str__(self):
        return self.name
