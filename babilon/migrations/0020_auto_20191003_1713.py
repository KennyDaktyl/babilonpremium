# Generated by Django 2.2.5 on 2019-10-03 15:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('babilon', '0019_products_menu_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orders',
            name='pizza',
        ),
        migrations.RemoveField(
            model_name='products',
            name='pizza_components',
        ),
        migrations.AddField(
            model_name='orders',
            name='product',
            field=models.ManyToManyField(blank=True, related_name='pizza_orders', to='babilon.Products', verbose_name='Jaka pizza'),
        ),
        migrations.AddField(
            model_name='products',
            name='component',
            field=models.IntegerField(blank=True, choices=[(1, 'Warzywny'), (2, 'Mięsny'), (3, 'Podstawowy'), (4, 'Wyrób ciasta')], null=True, verbose_name='component'),
        ),
        migrations.AddField(
            model_name='products',
            name='pizza_componets',
            field=models.ManyToManyField(related_name='pizza_component', to='babilon.Products', verbose_name='Składniki'),
        ),
        migrations.AddField(
            model_name='products',
            name='pizza_freestyle',
            field=models.BooleanField(blank=True, null=True, verbose_name='Pizza freestyle'),
        ),
        migrations.AlterField(
            model_name='products',
            name='pizza',
            field=models.BooleanField(blank=True, null=True, verbose_name='Pizza?'),
        ),
        migrations.DeleteModel(
            name='Pizza',
        ),
    ]
