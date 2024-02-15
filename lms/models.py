from django.db import models
from config.settings import NULLABLE


class Course(models.Model):
    title = models.CharField(max_length=155, verbose_name='course')
    description = models.TextField(verbose_name='description')
    preview = models.ImageField(upload_to='course/preview/', **NULLABLE, verbose_name='preview')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Course'
        verbose_name_plural = 'Courses'


class Lesson(models.Model):
    title = models.CharField(max_length=155, verbose_name='title')
    description = models.TextField(verbose_name='description')
    preview = models.ImageField(**NULLABLE, verbose_name='preview')
    link = models.TextField(verbose_name='link')

    course_id = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='course_id')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Lesson'
        verbose_name_plural = 'Lessons'