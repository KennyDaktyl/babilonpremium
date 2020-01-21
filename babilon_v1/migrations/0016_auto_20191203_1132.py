# Generated by Django 2.2.7 on 2019-12-03 10:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('babilon_v1', '0015_auto_20191201_1335'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productsize',
            name='product_price',
        ),
        migrations.AddField(
            model_name='productsize',
            name='extra_1_topps_price',
            field=models.FloatField(blank=True, null=True, verbose_name='Cena dodatku extra_1'),
        ),
        migrations.AddField(
            model_name='productsize',
            name='extra_2_topps_price',
            field=models.FloatField(blank=True, null=True, verbose_name='Cena dodatku extra_2'),
        ),
        migrations.AddField(
            model_name='productsize',
            name='extra_3',
            field=models.FloatField(blank=True, null=True, verbose_name='Cena dodatki wg extra_3'),
        ),
        migrations.AddField(
            model_name='productsize',
            name='extra_4',
            field=models.FloatField(blank=True, null=True, verbose_name='Cena dodatki wg extra_4'),
        ),
        migrations.AddField(
            model_name='productsize',
            name='extra_topps_price',
            field=models.FloatField(blank=True, null=True, verbose_name='Cena dodatku extra'),
        ),
        migrations.AlterField(
            model_name='products',
            name='type_of_ingredient',
            field=models.IntegerField(blank=True, choices=[(1, 'Warzywny'), (2, 'Mięsny'), (3, 'Serowy'), (4, 'Dodatki extra'), (5, 'Rodzaj ciasta'), (6, 'Sosy płatne'), (7, 'Sosy darmowe'), (8, 'Dodatki extra_1'), (9, 'Dodatki extra_2'), (10, 'Dodatki extra_3'), (11, 'Dodatki extra_4')], null=True, verbose_name='Rodzaj składnika'),
        ),
    ]
