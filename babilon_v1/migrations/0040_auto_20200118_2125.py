# Generated by Django 2.2.7 on 2020-01-18 20:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('babilon_v1', '0039_auto_20200115_1918'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clients',
            name='work_place',
            field=models.ForeignKey(blank=True, default=1, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='client_region', to='babilon_v1.WorkPlace', verbose_name='Klient pizzerii'),
        ),
    ]