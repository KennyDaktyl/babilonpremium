# Generated by Django 2.2.7 on 2019-12-01 12:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('babilon_v1', '0014_auto_20191201_1322'),
    ]

    operations = [
        migrations.AlterField(
            model_name='positionorder',
            name='change_topps_info_other_side',
            field=models.CharField(blank=True, default='', max_length=1012, null=True, verbose_name='Info o zmianie składników na prawej'),
        ),
    ]
