from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    type = (
        ('admin','admin'),
        ('user','user')
    )

    name = models.CharField(max_length=255, null=False)
    email = models.CharField(max_length=255, unique=True, null=True)
    password = models.CharField(max_length=255, null=False)
    user_type = models.CharField(max_length=50, choices=type, default='user')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']