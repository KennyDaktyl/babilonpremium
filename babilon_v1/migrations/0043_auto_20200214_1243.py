# Generated by Django 3.0.3 on 2020-02-14 11:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('babilon_v1', '0042_products_is_active'),
    ]

    operations = [
        migrations.AlterField(
            model_name='positionorder',
            name='order_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='babilon_v1.Orders', verbose_name='Zamówienie nr.'),
        ),
    ]
