from django.db import models
from config import settings
from config.settings import NULLABLE, AUTH_USER_MODEL


class Course(models.Model):
    owner = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='course author', **NULLABLE)

    title = models.CharField(max_length=155, verbose_name='course')
    description = models.TextField(verbose_name='description')
    preview = models.ImageField(upload_to='course/preview/', **NULLABLE, verbose_name='preview')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Course'
        verbose_name_plural = 'Courses'
        ordering = ['-id']


class Lesson(models.Model):
    title = models.CharField(max_length=155, verbose_name='title')
    description = models.TextField(verbose_name='description')
    preview = models.ImageField(**NULLABLE, verbose_name='preview')
    link = models.TextField(verbose_name='link')

    course_id = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='course_id')
    owner = models.ForeignKey(
        AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='lesson author', **NULLABLE
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Lesson'
        verbose_name_plural = 'Lessons'
        ordering = ['-id']


class Subscription(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    course = models.ForeignKey('Course', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user}: {self.course} - {self.issubscr}'

    class Meta:
        verbose_name = 'Subscription'
        verbose_name_plural = 'Subscriptions'