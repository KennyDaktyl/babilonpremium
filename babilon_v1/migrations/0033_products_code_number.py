# Generated by Django 2.2.7 on 2020-01-10 13:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('babilon_v1', '0032_purchases_barman_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='code_number',
            field=models.CharField(default='', max_length=128, verbose_name='Kod produktu'),
        ),
    ]