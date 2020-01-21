# Generated by Django 2.2.7 on 2020-01-06 08:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('babilon_v1', '0031_auto_20200102_1354'),
    ]

    operations = [
        migrations.AddField(
            model_name='purchases',
            name='barman_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Buyer', to=settings.AUTH_USER_MODEL, verbose_name='Wprowadzający'),
        ),
    ]