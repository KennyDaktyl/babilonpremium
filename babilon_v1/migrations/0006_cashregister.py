# Generated by Django 2.2.7 on 2019-11-24 06:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('babilon_v1', '0005_auto_20191122_1602'),
    ]

    operations = [
        migrations.CreateModel(
            name='CashRegister',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cash', models.FloatField(default=0, verbose_name='Gotówka')),
                ('cards', models.FloatField(default=0, verbose_name='Karta')),
                ('work_place', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='babilon_v1.WorkPlace', verbose_name='Lokal')),
            ],
        ),
    ]
