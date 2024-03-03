# Generated by Django 5.0.2 on 2024-02-15 19:31

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lms', '0002_alter_course_preview'),
        ('users', '0003_alter_user_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='users/avatar/', verbose_name='image'),
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_of_payment', models.DateTimeField(auto_now=True, verbose_name='date_of_payment')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=12, verbose_name='сумма оплаты')),
                ('payment_type', models.CharField(choices=[('cash', 'Cash'), ('bank', 'Bank')], max_length=20, verbose_name='способ оплаты')),
                ('paid_course', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='lms.course', verbose_name='paid_course')),
                ('paid_lesson', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='lms.lesson', verbose_name='paid_lesson')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='user')),
            ],
            options={
                'verbose_name': 'paid',
                'verbose_name_plural': 'paid',
                'ordering': ('user', 'date_of_payment'),
            },
        ),
    ]