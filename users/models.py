from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    first_name = models.CharField(max_length=155,  verbose_name='first_name')
    last_name = models.CharField(max_length=155, verbose_name='last_name')
    email = models.EmailField(unique=True, verbose_name='email')
    town = models.CharField(max_length=155, **NULLABLE, verbose_name='town')
    phone = models.IntegerField(unique=True, max_length=11, verbose_name='phone')
    image = models.ImageField(verbose_name='image')
