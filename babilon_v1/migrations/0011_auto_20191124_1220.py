# Generated by Django 2.2.7 on 2019-11-24 11:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('babilon_v1', '0010_auto_20191124_1031'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='orders',
            options={'ordering': ('-id',), 'verbose_name_plural': 'Zamówienia'},
        ),
        migrations.AddField(
            model_name='purchases',
            name='const_cost',
            field=models.BooleanField(default=False, verbose_name='Koszty stałe-miesięczne'),
        ),
        migrations.AlterField(
            model_name='purchases',
            name='type_of_cost',
            field=models.IntegerField(choices=[(0, 'Zakup towarów'), (1, 'Wypłata z kasy'), (2, 'Wypłata pracownikom'), (3, 'Inne wydatki')], verbose_name='Rodzaj wydatku: '),
        ),
    ]