# Generated by Django 2.2.5 on 2019-10-03 06:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('babilon', '0006_category_pizza_products_productsize'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='pizza_components',
            field=models.IntegerField(choices=[(1, 'Warzywny'), (2, 'Mięsny'), (3, 'Podstawowy'), (4, 'Wyrób ciasta')], verbose_name='Rodzaj składnika'),
        ),
    ]
