# Generated by Django 5.0.2 on 2024-03-02 18:08

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lms', '0005_alter_course_options_alter_lesson_options_and_more'),
        ('users', '0004_alter_user_image_payment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='paid_course',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='lms.course'),
        ),
        migrations.AlterField(
            model_name='payment',
            name='paid_lesson',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='lms.lesson'),
        ),
        migrations.AlterField(
            model_name='user',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='users/avatar/'),
        ),
        migrations.AlterField(
            model_name='user',
            name='phone',
            field=models.IntegerField(blank=True, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='town',
            field=models.CharField(blank=True, max_length=155, null=True),
        ),
    ]