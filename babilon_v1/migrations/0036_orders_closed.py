# Generated by Django 2.2.7 on 2020-01-13 09:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('babilon_v1', '0035_auto_20200113_0827'),
    ]

    operations = [
        migrations.AddField(
            model_name='orders',
            name='closed',
            field=models.BooleanField(default=False, verbose_name='otwarte'),
        ),
    ]