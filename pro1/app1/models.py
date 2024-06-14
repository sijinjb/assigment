from django.db import models
from django.contrib.auth.models import AbstractUser,Group

class user(AbstractUser):
    groups = models.ManyToManyField(Group, related_name='user_groups')  # Custom name
    email=models.EmailField(unique=True)


class registration(models.Model):
    groups = models.ManyToManyField(Group, related_name='registration_groups')  # Custom name
    email=models.EmailField(unique=True)
    name=models.CharField(max_length=100)
    mobile=models.CharField(max_length=15)
    


