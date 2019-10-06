# Generated by Django 2.2.5 on 2019-10-03 07:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('babilon', '0007_auto_20191003_0843'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='pizza',
            field=models.BooleanField(blank=True, null=True, verbose_name='Składnik do pizzy?'),
        ),
        migrations.CreateModel(
            name='Clients',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=128, verbose_name='Imie')),
                ('lastname', models.CharField(max_length=128, verbose_name='Nazwisko')),
                ('phone_number', models.CharField(max_length=128, verbose_name='Miasto')),
                ('status', models.IntegerField(blank=True, choices=[(1, 'Vip'), (1, 'Normal'), (2, 'Podejrzany')], null=True, verbose_name='Status klienta')),
                ('info', models.CharField(max_length=128, verbose_name='Info')),
                ('adress', models.ManyToManyField(related_name='Adresy_klienta', to='babilon.Adress', verbose_name='Adres klienta')),
            ],
        ),
    ]
