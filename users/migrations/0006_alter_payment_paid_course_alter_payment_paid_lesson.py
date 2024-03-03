# Generated by Django 5.0.2 on 2024-03-02 18:19

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lms', '0005_alter_course_options_alter_lesson_options_and_more'),
        ('users', '0005_alter_payment_paid_course_alter_payment_paid_lesson_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='paid_course',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='lms.course'),
        ),
        migrations.AlterField(
            model_name='payment',
            name='paid_lesson',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='lms.lesson'),
        ),
    ]
