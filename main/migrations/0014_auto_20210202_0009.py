# Generated by Django 3.1.6 on 2021-02-02 00:09

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0013_auto_20210202_0007'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2021, 2, 2, 0, 9, 25, 929663), null=True, verbose_name='время создания'),
        ),
        migrations.AlterField(
            model_name='order',
            name='lead_time',
            field=models.DateTimeField(default=datetime.datetime(2021, 2, 2, 0, 9, 25, 929730), null=True, verbose_name='время выполнения'),
        ),
    ]
