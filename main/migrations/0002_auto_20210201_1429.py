# Generated by Django 3.1.6 on 2021-02-01 14:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='comment',
            field=models.CharField(default=1, max_length=255, verbose_name='Комментарий'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='order',
            name='service',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.service', verbose_name='Услуга'),
        ),
        migrations.AlterField(
            model_name='order',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.user', verbose_name='Клиент'),
        ),
    ]
