# Generated by Django 2.2.7 on 2020-01-13 09:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('babilon_v1', '0037_auto_20200113_1047'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orders',
            name='closed',
            field=models.BooleanField(default=False, verbose_name='Zamknięte'),
        ),
    ]