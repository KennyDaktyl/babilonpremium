# Generated by Django 2.2.7 on 2020-01-13 09:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('babilon_v1', '0036_orders_closed'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orders',
            name='closed',
            field=models.BooleanField(default=True, verbose_name='Otwarte'),
        ),
    ]