# Generated by Django 2.2.7 on 2019-11-24 09:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('babilon_v1', '0009_auto_20191124_1030'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orders',
            name='date',
            field=models.DateField(auto_now_add=True),
        ),
    ]
