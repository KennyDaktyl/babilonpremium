# Generated by Django 2.2.5 on 2019-10-06 08:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('babilon', '0043_positionorder_quantity'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='beff_topps_price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=19, null=True, verbose_name='Cena za dodatek mięsny'),
        ),
        migrations.AddField(
            model_name='products',
            name='cake_modyfy',
            field=models.BooleanField(blank=True, null=True, verbose_name='Czy ser w rantach możliwy'),
        ),
        migrations.AddField(
            model_name='products',
            name='cake_topps_price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=19, null=True, verbose_name='Cena za ser w rantach'),
        ),
        migrations.AddField(
            model_name='products',
            name='cheese_topps_price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=19, null=True, verbose_name='Cena za dodatek serowy'),
        ),
        migrations.AddField(
            model_name='products',
            name='vege_topps_price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=19, null=True, verbose_name='Cena za dodatek warzywny'),
        ),
    ]
