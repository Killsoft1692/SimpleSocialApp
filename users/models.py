from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    friends = models.ManyToManyField(User, related_name='friends', blank=True)

    def __str__(self):
        return '{} profile'.format(self.user.username)
