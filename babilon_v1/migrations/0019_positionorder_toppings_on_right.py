# Generated by Django 2.2.7 on 2019-12-09 10:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('babilon_v1', '0018_auto_20191208_1449'),
    ]

    operations = [
        migrations.AddField(
            model_name='positionorder',
            name='toppings_on_right',
            field=models.ManyToManyField(blank=True, related_name='order_position_toppings_on_right', to='babilon_v1.Products', verbose_name='Dodatki na prawej'),
        ),
    ]
