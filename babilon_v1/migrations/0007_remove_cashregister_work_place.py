# Generated by Django 2.2.7 on 2019-11-24 06:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('babilon_v1', '0006_cashregister'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cashregister',
            name='work_place',
        ),
    ]