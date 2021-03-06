# Generated by Django 3.0.2 on 2020-11-04 14:26

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='MyUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('active', models.BooleanField(blank=True, default=False, null=True, verbose_name='Aktywny')),
                ('day_when_active', models.DateField(blank=True, null=True)),
                ('profession', models.IntegerField(blank=True, choices=[(0, 'Właściciel'), (1, 'Menager'), (2, 'Barman'), (3, 'Pizzer'), (4, 'Kierowca')], null=True, verbose_name='Stanowisko osoby')),
                ('phone_number', models.CharField(blank=True, max_length=9, null=True, verbose_name='Numer telefonu')),
                ('rate_per_hour', models.FloatField(blank=True, null=True, verbose_name='Stawka na godzinę')),
                ('rate_per_drive', models.FloatField(blank=True, null=True, verbose_name='Stawka za wyjazd')),
                ('type_of_employment', models.IntegerField(blank=True, choices=[(0, 'Umowa o prace'), (1, 'Umowa zlecenie'), (2, 'Brak danych'), (3, 'Licznik wyjazdów')], null=True, verbose_name='Rodzaj zatrudnienia')),
                ('driver_status', models.IntegerField(blank=True, choices=[(1, 'Wolny'), (2, 'W dostawie'), (3, 'Powrót')], default=1, null=True, verbose_name='Status kierowcy')),
                ('info', models.TextField(blank=True, null=True, verbose_name='Info')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
            ],
            options={
                'verbose_name_plural': 'Osoby w firmie',
                'ordering': ('first_name', 'last_name'),
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('street', models.CharField(blank=True, max_length=128, null=True, verbose_name='Ulica')),
                ('city', models.CharField(blank=True, default='Kraków', max_length=64, null=True, verbose_name='Miasto')),
                ('post_code', models.CharField(blank=True, max_length=6, null=True, verbose_name='Kod pocztowy')),
                ('choice_count', models.IntegerField(default=1, verbose_name='Licznik wyboru')),
            ],
            options={
                'verbose_name_plural': 'Adresy',
                'ordering': ('-choice_count', 'street'),
            },
        ),
        migrations.CreateModel(
            name='CashRegister',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cash', models.FloatField(default=0, verbose_name='Gotówka')),
                ('cards', models.FloatField(default=0, verbose_name='Karta')),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_number', models.IntegerField(blank=True, default=0, null=True, verbose_name='Numer kategorii')),
                ('category_name', models.CharField(max_length=128, verbose_name='Kategoria menu')),
                ('display', models.BooleanField(default=False, verbose_name='Czy ma być wyświeltlana w menu?')),
            ],
            options={
                'verbose_name_plural': 'Kategoria produktu',
                'ordering': ('category_number', 'category_name'),
            },
        ),
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('active', models.BooleanField(blank=True, default=False, null=True)),
                ('number', models.CharField(blank=True, max_length=64, null=True, verbose_name='Numer zamówienia')),
                ('status', models.IntegerField(choices=[(1, 'Otwarte'), (2, 'W przygotowaniu'), (3, 'W dostawie'), (4, 'Zrealizowane'), (5, 'Anulowane')], default=1, verbose_name='Status zamówienia')),
                ('date', models.DateField(auto_now_add=True)),
                ('time_start', models.TimeField(blank=True, null=True)),
                ('time_zero', models.TimeField(blank=True, null=True)),
                ('type_of_order', models.IntegerField(choices=[(1, 'Lokal'), (2, 'Wynos'), (3, 'Dostawa')], default=1, verbose_name='Rodzaj zamówienia')),
                ('pay_method', models.IntegerField(choices=[(1, 'Gotówka'), (2, 'Karta'), (3, 'Online_1'), (4, 'Online_2'), (5, 'Online_3')], default=1, verbose_name='Płatność zamówienia')),
                ('start_delivery_time', models.TimeField(blank=True, null=True, verbose_name='Czas wywozu')),
                ('time_delivery_in', models.TimeField(blank=True, null=True, verbose_name='Czas dostarczenia')),
                ('sms_send', models.BooleanField(default=False, verbose_name='Sms')),
                ('sms_time', models.TimeField(blank=True, null=True, verbose_name='Czas smsa')),
                ('promo', models.BooleanField(default=False, verbose_name='Promocja')),
                ('closed', models.BooleanField(default=False, verbose_name='Zamknięte')),
                ('discount', models.IntegerField(blank=True, default=0, null=True, verbose_name='Rabat')),
                ('info', models.CharField(blank=True, default='', max_length=256, null=True, verbose_name='Informacje')),
                ('printed', models.BooleanField(default=True, verbose_name='Wydrukowano paragon?')),
                ('address', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='babilon_v1.Address', verbose_name='Adres')),
                ('barman_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Barman', to=settings.AUTH_USER_MODEL, verbose_name='Barman')),
                ('driver_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Kierowca', to=settings.AUTH_USER_MODEL, verbose_name='Kierowca')),
            ],
            options={
                'verbose_name_plural': 'Zamówienia',
                'ordering': ('-id',),
            },
        ),
        migrations.CreateModel(
            name='ProductSize',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('size_name', models.CharField(max_length=64, verbose_name='Rozmiar produktu')),
                ('pizza', models.BooleanField(blank=True, null=True, verbose_name='Rozmiary dla pizzy?')),
                ('bottle', models.BooleanField(blank=True, null=True, verbose_name='Rozmairy napoi?')),
                ('fast_food', models.BooleanField(blank=True, null=True, verbose_name='Rozmiary fast_food?')),
                ('vege_topps_price', models.FloatField(blank=True, null=True, verbose_name='Cena dodatku warzywnego')),
                ('beef_topps_price', models.FloatField(blank=True, null=True, verbose_name='Cena dodatku mięsnego')),
                ('cheese_topps_price', models.FloatField(blank=True, null=True, verbose_name='Cena dodatku serowego')),
                ('extra_topps_price', models.FloatField(blank=True, null=True, verbose_name='Cena dodatku extra')),
                ('extra_1_topps_price', models.FloatField(blank=True, null=True, verbose_name='Cena dodatku extra_1')),
                ('extra_2_topps_price', models.FloatField(blank=True, null=True, verbose_name='Cena dodatku extra_2')),
                ('extra_3_topps_price', models.FloatField(blank=True, null=True, verbose_name='Cena dodatki wg extra_3')),
                ('extra_4_topps_price', models.FloatField(blank=True, null=True, verbose_name='Cena dodatki wg extra_4')),
            ],
            options={
                'verbose_name_plural': 'Rozmiary produktów',
                'ordering': ('size_name',),
            },
        ),
        migrations.CreateModel(
            name='Vat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vatrate', models.IntegerField(blank=True, null=True, verbose_name='Stawka VAT')),
            ],
        ),
        migrations.CreateModel(
            name='WorkPlace',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('workplace_name', models.CharField(max_length=128, verbose_name='Nazwa pizzerii')),
                ('address', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='babilon_v1.Address', verbose_name='Adres pizzerii')),
            ],
        ),
        migrations.CreateModel(
            name='Purchases',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now=True)),
                ('purchase_name', models.CharField(blank=True, default='', max_length=256, null=True, verbose_name='Nazwa')),
                ('pay_method', models.IntegerField(choices=[(1, 'Gotówka'), (2, 'Karta'), (3, 'Przelew')], default='1', verbose_name='Rodzaj wydatku: ')),
                ('price', models.FloatField(verbose_name='Cena')),
                ('type_purchases', models.IntegerField(choices=[(0, 'Zakup towarów'), (1, 'Wypłata pracownikom'), (2, 'Podatki/ZUS'), (3, 'Koszta stałe'), (4, 'Inne wydatki')], default='0', verbose_name='Rodzaj kosztu: ')),
                ('info', models.CharField(blank=True, default='', max_length=256, null=True, verbose_name='Info')),
                ('barman_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Buyer', to=settings.AUTH_USER_MODEL, verbose_name='Wprowadzający')),
                ('work_place', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='babilon_v1.WorkPlace', verbose_name='Lokal')),
            ],
            options={
                'verbose_name_plural': 'Wydatki',
                'ordering': ('-id',),
            },
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=128, verbose_name='Nazwa produktu')),
                ('pizza_number', models.IntegerField(blank=True, default=0, null=True, verbose_name='Numer pizzy')),
                ('quantity', models.IntegerField(blank=True, default=1, null=True, verbose_name='Ilosc')),
                ('type_of_ingredient', models.IntegerField(blank=True, choices=[(1, 'Warzywny'), (2, 'Mięsny'), (3, 'Serowy'), (4, 'Dodatki extra'), (5, 'Rodzaj ciasta'), (6, 'Sosy płatne'), (7, 'Sosy darmowe'), (8, 'Dodatki extra_1'), (9, 'Dodatki extra_2'), (10, 'Dodatki extra_3'), (11, 'Dodatki extra_4')], null=True, verbose_name='Rodzaj składnika')),
                ('pizza_premium', models.BooleanField(default=False, verbose_name='Pizza premium?')),
                ('is_pizza_half', models.BooleanField(default=False, verbose_name='Pizza pol_na_pol?')),
                ('is_pizza_freestyle', models.BooleanField(default=False, verbose_name='Pizza freestyle?')),
                ('extra_price', models.FloatField(blank=True, default=0, null=True, verbose_name='Cena dodatków')),
                ('price', models.FloatField(blank=True, default=0, null=True, verbose_name='Cena podstawowa')),
                ('discount', models.IntegerField(blank=True, default=0, null=True, verbose_name='Rabat')),
                ('pizza_topp', models.BooleanField(default=False, verbose_name='Dodatek do pizzy')),
                ('dish_topp', models.BooleanField(default=False, verbose_name='Dodatek do dań')),
                ('code_number', models.CharField(blank=True, default='', max_length=128, null=True, verbose_name='Kod produktu')),
                ('is_active', models.BooleanField(default=True, verbose_name='Czy jest dostępny')),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='babilon_v1.Category', verbose_name='Kategoria produktu')),
                ('product_size', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='babilon_v1.ProductSize', verbose_name='Rozmiar produktu')),
                ('tax', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='babilon_v1.Vat', verbose_name='Stawka VAT')),
                ('toppings', models.ManyToManyField(blank=True, to='babilon_v1.Products', verbose_name='Składniki')),
            ],
            options={
                'verbose_name_plural': 'Produkty',
                'ordering': ('category', 'pizza_number', 'type_of_ingredient', 'product_name', 'product_size'),
            },
        ),
        migrations.CreateModel(
            name='PositionOrder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=1, verbose_name='Ilosc')),
                ('halfpizza_name', models.CharField(blank=True, default='', max_length=126, null=True, verbose_name='Nazwa składana z dwóch produktów')),
                ('pizza_half', models.BooleanField(default=False, verbose_name='Pizza pol_na_pol')),
                ('change_topps_info', models.CharField(blank=True, default='', max_length=1012, null=True, verbose_name='Info o zmianie składników')),
                ('change_topps_info_id', models.CharField(blank=True, default="'", max_length=256, null=True, verbose_name='Id o zmianie składników')),
                ('change_topps_info_other_side', models.CharField(blank=True, default='', max_length=1012, null=True, verbose_name='Info o zmianie składników na prawej')),
                ('change_topps_info_right_id', models.CharField(blank=True, default="'", max_length=256, null=True, verbose_name='Id o zmianie składników na prawej')),
                ('cake_info', models.CharField(blank=True, default='', max_length=128, null=True, verbose_name='Zmiany ciasta')),
                ('sauces_free', models.CharField(blank=True, default='', max_length=256, null=True, verbose_name='Sosy darmowe')),
                ('sauces_pay', models.CharField(blank=True, default='', max_length=256, null=True, verbose_name='Sosy płatne')),
                ('extra_price', models.FloatField(blank=True, default=0, null=True, verbose_name='Cena dodatków')),
                ('extra_price_left', models.FloatField(blank=True, default=0, null=True, verbose_name='Cena dodatków na prawej')),
                ('extra_price_right', models.FloatField(blank=True, default=0, null=True, verbose_name='Cena dodatków na prawej')),
                ('info', models.CharField(blank=True, default='', max_length=256, null=True, verbose_name='Informacje')),
                ('price', models.FloatField(verbose_name='Cena podstawowa')),
                ('discount', models.IntegerField(blank=True, default=0, null=True, verbose_name='Rabat')),
                ('freestyle_toppings', models.ManyToManyField(blank=True, related_name='order_position_toppings', to='babilon_v1.Products', verbose_name='Dodatki')),
                ('order_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='babilon_v1.Orders', verbose_name='Zamówienie nr.')),
                ('product_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='babilon_v1.Products', verbose_name='Product na zamówieniu')),
                ('product_id_pizza_right', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Pizza_on_rigth', to='babilon_v1.Products', verbose_name='Pizza prawa')),
                ('size_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='babilon_v1.ProductSize', verbose_name='Rozmiar')),
            ],
            options={
                'verbose_name_plural': 'Pozycje na zamówieniu',
                'ordering': ('-id',),
            },
        ),
        migrations.AddField(
            model_name='orders',
            name='workplace_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='babilon_v1.WorkPlace', verbose_name='Pizzeria'),
        ),
        migrations.CreateModel(
            name='Clients',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client_name', models.CharField(blank=True, max_length=64, null=True, verbose_name='Imię Nazwisko')),
                ('phone_number', models.CharField(max_length=15, verbose_name='Numer telefonu')),
                ('status', models.IntegerField(blank=True, choices=[(0, 'Vip'), (1, 'Normal'), (2, 'Podejrzany')], default=1, null=True, verbose_name='Status klienta')),
                ('info', models.CharField(blank=True, max_length=256, null=True, verbose_name='Info')),
                ('work_place', models.ForeignKey(blank=True, default=1, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='client_region', to='babilon_v1.WorkPlace', verbose_name='Klient pizzerii')),
            ],
        ),
        migrations.AddField(
            model_name='address',
            name='client_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='babilon_v1.Clients', verbose_name='Klient'),
        ),
        migrations.AddField(
            model_name='myuser',
            name='user_address',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_address', to='babilon_v1.Address', verbose_name='Adres osoby'),
        ),
        migrations.AddField(
            model_name='myuser',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions'),
        ),
        migrations.AddField(
            model_name='myuser',
            name='work_place',
            field=models.ManyToManyField(blank=True, related_name='work_place', to='babilon_v1.WorkPlace', verbose_name='Możliwe miejsca pracy'),
        ),
    ]
