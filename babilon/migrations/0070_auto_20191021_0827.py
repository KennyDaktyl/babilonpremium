# Generated by Django 2.2.6 on 2019-10-21 06:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('babilon', '0069_auto_20191019_0850'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='orders',
            options={'ordering': ('number',)},
        ),
        migrations.AlterField(
            model_name='positionorder',
            name='change_topps',
            field=models.CharField(blank=True, default='', max_length=512, null=True, verbose_name='Zmiany składników'),
        ),
    ]
