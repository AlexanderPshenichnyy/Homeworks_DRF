from django.contrib.auth.models import AbstractUser
from django.db import models

from config.settings import NULLABLE
from lms.models import Course, Lesson


class User(AbstractUser):
    first_name = models.CharField(max_length=155, verbose_name='first_name')
    last_name = models.CharField(max_length=155, verbose_name='last_name')
    email = models.EmailField(unique=True, verbose_name='email')
    town = models.CharField(max_length=155, **NULLABLE, verbose_name='town')
    phone = models.IntegerField(unique=True, **NULLABLE, verbose_name='phone')
    image = models.ImageField(upload_to='users/avatar/', **NULLABLE, verbose_name='image')

    def __str__(self):
        return f'{self.first_name}, {self.last_name}'

    class Meta:
        verbose_name = 'User',
        verbose_name_plural = 'Users'


class Payment(models.Model):
    class PaymentType(models.TextChoices):
        CASH = 'cash', 'Cash'
        BANK = 'bank', 'Bank'

    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='user')
    date_of_payment = models.DateTimeField(auto_now=True, verbose_name='date_of_payment')
    paid_course = models.ForeignKey(Course, on_delete=models.CASCADE, **NULLABLE, verbose_name='paid_course')
    paid_lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, **NULLABLE, verbose_name='paid_lesson')
    amount = models.DecimalField(max_digits=12, decimal_places=2, verbose_name='сумма оплаты')
    payment_type = models.CharField(max_length=20, choices=PaymentType.choices, verbose_name='способ оплаты')

    def __str__(self):
        return f'{self.user} - {self.paid_course if self.paid_course else self.paid_lesson} - {self.amount}'

    class Meta:
        verbose_name = 'paid'
        verbose_name_plural = 'paid'
        ordering = ('user', 'date_of_payment')
