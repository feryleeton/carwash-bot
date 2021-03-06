# Generated by Django 3.1.6 on 2021-02-02 00:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_auto_20210201_1917'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='created',
            field=models.DateTimeField(auto_created=True, null=True, verbose_name='время создания'),
        ),
        migrations.AlterField(
            model_name='service',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main.category', verbose_name='Категория'),
        ),
    ]
