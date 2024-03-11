# Generated by Django 5.0.2 on 2024-03-10 14:22

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_alter_payment_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='amount',
            field=models.IntegerField(verbose_name='payment_summ'),
        ),
        migrations.AlterField(
            model_name='payment',
            name='payment_type',
            field=models.CharField(choices=[('cash', 'Cash'), ('bank', 'Bank')], max_length=20, verbose_name='payment_method'),
        ),
        migrations.AlterField(
            model_name='payment',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
    ]
