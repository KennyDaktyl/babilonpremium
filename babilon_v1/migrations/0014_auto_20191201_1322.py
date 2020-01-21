# Generated by Django 2.2.7 on 2019-12-01 12:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('babilon_v1', '0013_auto_20191201_1032'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ('category_number', 'category_name'), 'verbose_name_plural': 'Kategoria produktu'},
        ),
        migrations.AddField(
            model_name='category',
            name='category_number',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='Numer kategorii'),
        ),
    ]
