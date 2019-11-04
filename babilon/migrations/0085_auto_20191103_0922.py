# Generated by Django 2.2.6 on 2019-11-03 08:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('babilon', '0084_auto_20191103_0819'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='adress',
            name='city',
        ),
        migrations.RemoveField(
            model_name='adress',
            name='code',
        ),
        migrations.AlterField(
            model_name='adress',
            name='street',
            field=models.CharField(max_length=128, verbose_name='Adres'),
        ),
        migrations.AlterField(
            model_name='clients',
            name='firstlastname',
            field=models.CharField(blank=True, max_length=64, null=True, verbose_name='Imię Nazwisko'),
        ),
        migrations.AlterField(
            model_name='clients',
            name='phone_number',
            field=models.CharField(max_length=9, verbose_name='Numer telefonu'),
        ),
        migrations.AlterField(
            model_name='clients',
            name='status',
            field=models.IntegerField(blank=True, choices=[(0, 'Vip'), (1, 'Normal'), (2, 'Podejrzany')], null=True, verbose_name='Status klienta'),
        ),
    ]
