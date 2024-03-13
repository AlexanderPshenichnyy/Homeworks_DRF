from django.contrib.auth.models import AbstractUser
from django.db import models

from config.settings import NULLABLE
from lms.models import Course, Lesson


class User(AbstractUser):
    first_name = models.CharField(max_length=155, verbose_name='first_name')
    last_name = models.CharField(max_length=155, verbose_name='last_name')
    email = models.EmailField(unique=True, verbose_name='email')
    town = models.CharField(max_length=155, **NULLABLE)
    phone = models.IntegerField(unique=True, **NULLABLE)
    image = models.ImageField(upload_to='users/avatar/', **NULLABLE)

    def __str__(self):
        return f'{self.first_name}, {self.last_name}'

    class Meta:
        verbose_name = 'User',
        verbose_name_plural = 'Users'


class Payment(models.Model):
    class PaymentType(models.TextChoices):
        CASH = 'cash', 'Cash'
        BANK = 'bank', 'Bank'

    user = models.ForeignKey(User, on_delete=models.SET_NULL, **NULLABLE)
    date_of_payment = models.DateTimeField(auto_now=True, verbose_name='date_of_payment')
    paid_course = models.ForeignKey(Course, on_delete=models.SET_NULL, **NULLABLE)
    paid_lesson = models.ForeignKey(Lesson, on_delete=models.SET_NULL, **NULLABLE)
    amount = models.IntegerField(verbose_name='payment amount')
    payment_type = models.CharField(max_length=20, choices=PaymentType.choices, verbose_name='payment method')
    url = models.URLField(max_length=300, verbose_name="url", **NULLABLE)

    class Meta:
        verbose_name = 'paid'
        verbose_name_plural = 'paids'
        ordering = ('user', 'date_of_payment', 'paid_course', 'paid_lesson')
