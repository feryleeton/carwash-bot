# Generated by Django 3.1.6 on 2021-02-01 18:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_order_time_slot'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='time_slot',
            field=models.CharField(choices=[('9:30', '9:30'), ('10:30', '10:30'), ('12:00', '12:00'), ('13:00', '13:00'), ('15:00', '15:00'), ('16:00', '16:00'), ('17:00', '17:00'), ('18:00', '18:00')], max_length=25, null=True, verbose_name='Время'),
        ),
    ]
