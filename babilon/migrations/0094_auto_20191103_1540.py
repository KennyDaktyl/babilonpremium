# Generated by Django 2.2.6 on 2019-11-03 14:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('babilon', '0093_auto_20191103_1538'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orders',
            name='data',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
