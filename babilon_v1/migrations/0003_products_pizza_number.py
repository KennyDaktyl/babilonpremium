# Generated by Django 2.2.7 on 2019-11-20 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('babilon_v1', '0002_auto_20191120_0706'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='pizza_number',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='Numer pizzy'),
        ),
    ]