# Generated by Django 2.2.7 on 2019-11-20 14:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('babilon_v1', '0003_products_pizza_number'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='products',
            options={'ordering': ('category', 'pizza_number', 'product_name', 'product_size'), 'verbose_name_plural': 'Produkty'},
        ),
    ]