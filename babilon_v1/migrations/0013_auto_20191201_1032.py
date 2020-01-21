# Generated by Django 2.2.7 on 2019-12-01 09:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('babilon_v1', '0012_auto_20191127_1118'),
    ]

    operations = [
        migrations.AddField(
            model_name='positionorder',
            name='toppings',
            field=models.ManyToManyField(blank=True, related_name='order_position_toppings', to='babilon_v1.Products', verbose_name='Dodatki'),
        ),
        migrations.AlterField(
            model_name='positionorder',
            name='toppings_change_plus',
            field=models.ManyToManyField(blank=True, related_name='pizza_change_toppings_plus', to='babilon_v1.Products', verbose_name='Dodatki do dania plus'),
        ),
    ]