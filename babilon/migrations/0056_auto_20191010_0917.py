# Generated by Django 2.2.6 on 2019-10-10 07:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('babilon', '0055_auto_20191010_0912'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productsize',
            name='beef_topps_price',
            field=models.FloatField(blank=True, null=True, verbose_name='Cena dodatku mięsnego'),
        ),
        migrations.AlterField(
            model_name='productsize',
            name='cheese_topps_price',
            field=models.FloatField(blank=True, null=True, verbose_name='Cena dodatku serowego'),
        ),
        migrations.AlterField(
            model_name='productsize',
            name='vege_topps_price',
            field=models.FloatField(blank=True, null=True, verbose_name='Cena dodatku warzywnego'),
        ),
    ]
