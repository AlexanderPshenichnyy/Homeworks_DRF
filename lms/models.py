from django.db import models
from config import settings
from config.settings import NULLABLE, AUTH_USER_MODEL


class Course(models.Model):
    """Model for Course"""
    owner = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='course author', **NULLABLE)

    title = models.CharField(max_length=155, verbose_name='course')
    description = models.TextField(verbose_name='description')
    preview = models.ImageField(upload_to='course/preview/', **NULLABLE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Course'
        verbose_name_plural = 'Courses'
        ordering = ['-id']


class Lesson(models.Model):
    """
    Model for Lesson
    """
    title = models.CharField(max_length=155, verbose_name='title')
    description = models.TextField(verbose_name='description')
    preview = models.ImageField(**NULLABLE)
    link = models.TextField(verbose_name='link')

    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='lesson', verbose_name='course_id')
    owner = models.ForeignKey(
        AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='lesson author', **NULLABLE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Lesson'
        verbose_name_plural = 'Lessons'
        ordering = ['-id']


class Subscription(models.Model):
    """Model for Subscription"""
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    course = models.ForeignKey('Course', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user} : {self.course}'

    class Meta:
        verbose_name = 'Subscription'
        verbose_name_plural = 'Subscriptions'
