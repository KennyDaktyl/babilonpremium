# Generated by Django 2.2.7 on 2020-01-15 18:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('babilon_v1', '0038_auto_20200113_1048'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='address',
            options={'ordering': ('-choice_count', 'street'), 'verbose_name_plural': 'Adresy'},
        ),
        migrations.AlterField(
            model_name='clients',
            name='phone_number',
            field=models.CharField(max_length=15, verbose_name='Numer telefonu'),
        ),
    ]