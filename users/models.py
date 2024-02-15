from django.db import models
from django.contrib.auth.models import AbstractUser

NULLABLE = {
    'null': True, 'blank': True
}


class User(AbstractUser):
    first_name = models.CharField(max_length=155, verbose_name='first_name')
    last_name = models.CharField(max_length=155, verbose_name='last_name')
    email = models.EmailField(unique=True, verbose_name='email')
    town = models.CharField(max_length=155, **NULLABLE, verbose_name='town')
    phone = models.IntegerField(unique=True, **NULLABLE, verbose_name='phone')
    image = models.ImageField(**NULLABLE, verbose_name='image')
