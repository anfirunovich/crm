from django.db import models
from django.contrib.auth.models import AbstractBaseUser


class User(AbstractBaseUser):

    email = models.EmailField(max_length=255, verbose_name="email", unique=True)
    password = models.CharField(max_length=8, verbose_name="password")

    admin = models.BooleanField(default=False)