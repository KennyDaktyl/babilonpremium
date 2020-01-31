from django.db import models
from django.contrib.auth.models import AbstractUser
from babilon_v1.choice_field import *
from django.db.models import Count

from datetime import datetime
from django.utils import timezone

month = datetime.now().month
year = datetime.now().year


class MyUser(AbstractUser):
    active = models.BooleanField(verbose_name="Aktywny",
                                 null=True,
                                 blank=True,
                                 default=False)
    day_when_active = models.DateField(null=True, blank=True)
    profession = models.IntegerField(verbose_name="Stanowisko osoby",
                                     choices=JOB_STATUS,
                                     null=True,
                                     blank=True)
    work_place = models.ManyToManyField("WorkPlace",
                                        verbose_name="Możliwe miejsca pracy",
                                        blank=True,
                                        related_name="work_place")
    phone_number = models.CharField(verbose_name="Numer telefonu",
                                    max_length=9,
                                    null=True,
                                    blank=True)

    user_address = models.ForeignKey("Address",
                                     verbose_name="Adres osoby",
                                     null=True,
                                     blank=True,
                                     on_delete=models.CASCADE,
                                     related_name="user_address")
    rate_per_hour = models.FloatField(verbose_name="Stawka na godzinę",
                                      null=True,
                                      blank=True)
    rate_per_drive = models.FloatField(verbose_name="Stawka za wyjazd",
                                       null=True,
                                       blank=True)
    type_of_employment = models.IntegerField(
        verbose_name="Rodzaj zatrudnienia",
        choices=CONTRACT_TYPE,
        null=True,
        blank=True)
    driver_status = models.IntegerField(verbose_name="Status kierowcy",
                                        choices=DRIVER_STATUS,
                                        null=True,
                                        blank=True,
                                        default=1)
    info = models.TextField(verbose_name="Info", null=True, blank=True)

   
    def counter_cursers_cash(self, date_start, date_end, pizzeria):
        driver_courses = Orders.objects.filter(type_of_order="3").filter(
            status="4").filter(date__gte=date_start).filter(
                date__lte=date_end).filter(workplace_id=pizzeria).filter(
                    driver_id=self)
        cash = 0
        for order in driver_courses:
            cash += order.order_total_price2()

        return cash

    class Meta:
        ordering = ("first_name", "last_name")
        verbose_name_plural = 'Osoby w firmie'

    def __str__(self):
        return str(self.id) + ", " + str(self.username) + ", " + str(
            self.first_name) + ", " + str(self.last_name)


class Address(models.Model):

    client_id = models.ForeignKey(
        "Clients",
        verbose_name="Klient",
        null=True,
        blank=True,
        on_delete=models.CASCADE,
    )
    street = models.CharField(verbose_name="Ulica",
                              null=True,
                              blank=True,
                              max_length=128)
    city = models.CharField(verbose_name="Miasto",
                            null=True,
                            blank=True,
                            max_length=64,
                            default="Kraków")
    post_code = models.CharField(verbose_name="Kod pocztowy",
                                 null=True,
                                 blank=True,
                                 max_length=6)
    choice_count = models.IntegerField(verbose_name="Licznik wyboru",
                                       default=1)

    class Meta:
        ordering = (
            # "client_id",
            "-choice_count",
            "street",            
        )
        verbose_name_plural = 'Adresy'

    def __str__(self):
        return str(self.id) + ", " + str(self.street)


class Clients(models.Model):
    work_place = models.ForeignKey("WorkPlace",
                                   verbose_name="Klient pizzerii",
                                   null=True,
                                   blank=True,
                                   default=1,
                                   on_delete=models.CASCADE,
                                   related_name="client_region")

    client_name = models.CharField(verbose_name="Imię Nazwisko",
                                   max_length=64,
                                   null=True,
                                   blank=True)
    phone_number = models.CharField(verbose_name="Numer telefonu",
                                    max_length=15)

    status = models.IntegerField(verbose_name="Status klienta",
                                 choices=CLIENT_STATUS,
                                 null=True,
                                 blank=True,
                                 default=1)
    info = models.CharField(verbose_name="Info",
                            max_length=256,
                            null=True,
                            blank=True)

    def __str__(self):
        return str(self.id)+str(self.client_name) + ", " + str(
            self.phone_number) + ", " + str(self.work_place)


class WorkPlace(models.Model):
    workplace_name = models.CharField(verbose_name="Nazwa pizzerii",
                                      max_length=128)
    address = models.ForeignKey("Address",
                                verbose_name="Adres pizzerii",
                                on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id) + ", " + str(self.workplace_name)


class ProductSize(models.Model):
    size_name = models.CharField(verbose_name="Rozmiar produktu",
                                 max_length=64)

    pizza = models.BooleanField(verbose_name="Rozmiary dla pizzy?",
                                null=True,
                                blank=True)
    bottle = models.BooleanField(verbose_name="Rozmairy napoi?",
                                 null=True,
                                 blank=True)
    fast_food = models.BooleanField(verbose_name="Rozmiary fast_food?",
                                    null=True,
                                    blank=True)

    vege_topps_price = models.FloatField(
        verbose_name="Cena dodatku warzywnego", null=True, blank=True)
    beef_topps_price = models.FloatField(verbose_name="Cena dodatku mięsnego",
                                         null=True,
                                         blank=True)
    cheese_topps_price = models.FloatField(
        verbose_name="Cena dodatku serowego", null=True, blank=True)
    extra_topps_price = models.FloatField(verbose_name="Cena dodatku extra",
                                          null=True,
                                          blank=True)
    extra_1_topps_price = models.FloatField(
        verbose_name="Cena dodatku extra_1", null=True, blank=True)
    extra_2_topps_price = models.FloatField(
        verbose_name="Cena dodatku extra_2", null=True, blank=True)
    extra_3_topps_price = models.FloatField(
        verbose_name="Cena dodatki wg extra_3", null=True, blank=True)
    extra_4_topps_price = models.FloatField(
        verbose_name="Cena dodatki wg extra_4", null=True, blank=True)

    class Meta:
        ordering = ("size_name", )
        verbose_name_plural = 'Rozmiary produktów'

    def __str__(self):
        return str(self.size_name)



class Category(models.Model):
    category_number = models.IntegerField(verbose_name="Numer kategorii",
                                          null=True,
                                          blank=True,
                                          default=0)
    category_name = models.CharField(verbose_name="Kategoria menu",
                                     max_length=128)
    display = models.BooleanField(
        verbose_name="Czy ma być wyświeltlana w menu?", default=False)

    class Meta:
        ordering = (
            "category_number",
            "category_name",
        )
        verbose_name_plural = 'Kategoria produktu'

    def __str__(self):
        return str(self.id) + ", " + str(self.category_name)


class Products(models.Model):
    category = models.ForeignKey(
        "Category",
        verbose_name="Kategoria produktu",
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )
    product_name = models.CharField(verbose_name="Nazwa produktu",
                                    max_length=128)
    
    pizza_number = models.IntegerField(verbose_name="Numer pizzy",
                                       null=True,
                                       blank=True,
                                       default=0)
    product_size = models.ForeignKey(
        "ProductSize",
        verbose_name="Rozmiar produktu",
        blank=True,
        null=True,
        on_delete=models.CASCADE,
    )
    quantity = models.IntegerField(verbose_name="Ilosc",
                                   null=True,
                                   blank=True,
                                   default=1)
    toppings = models.ManyToManyField("Products",
                                      verbose_name="Składniki",
                                      blank=True)
    type_of_ingredient = models.IntegerField(verbose_name="Rodzaj składnika",
                                             choices=INGREDIENT_TYPE,
                                             null=True,
                                             blank=True)
    pizza_premium = models.BooleanField(verbose_name="Pizza premium?",
                                          default=False)
    is_pizza_half = models.BooleanField(verbose_name="Pizza pol_na_pol?",
                                        default=False)
    is_pizza_freestyle = models.BooleanField(verbose_name="Pizza freestyle?",
                                             default=False)
    extra_price = models.FloatField(verbose_name="Cena dodatków",
                                    null=True,
                                    blank=True,
                                    default=0)
    price = models.FloatField(verbose_name="Cena podstawowa",
                              null=True,
                              blank=True,
                              default=0)
    discount = models.IntegerField(verbose_name="Rabat",
                                   default=0,
                                   null=True,
                                   blank=True)
    tax = models.ForeignKey('Vat',
                            on_delete=models.CASCADE,
                            verbose_name="Stawka VAT",
                            null=True,
                            blank=True)
    pizza_topp = models.BooleanField(verbose_name="Dodatek do pizzy",
                                     default=False)
    dish_topp = models.BooleanField(verbose_name="Dodatek do dań",
                                    default=False)
    code_number = models.CharField(verbose_name="Kod produktu",
                                    max_length=128, default="",null=True,
                            blank=True)

    class Meta:
        ordering = (
            "category",
            "pizza_number",
            "type_of_ingredient",
            "product_name",
            "product_size",
        )
        verbose_name_plural = 'Produkty'

    @property
    def suma(self):
        suma = self.price * self.quantity
        return suma

    @property
    def suma_discount(self):
        suma = (((self.price * self.quantity) * (self.discount) * 0.01))
        return suma

    @property
    def total_price(self):

        total = self.extra_price + self.price
        return total
    
    # def code(self):
    #     if self.category.category_number==1 or self.category.category_number==2:
    #         code =str(self.category.category_number) + str(self.pizza_number)+ str(int(self.product_size.id)+2)
    #     return code
    
    # @property
    # def code(self):
    #     if self.category.category_number==1 or self.category.category_number==2:
    #         code =str(self.category.category_number) + str(self.pizza_number)+ str(int(self.product_size.id)+2)
    #     return code

    def __str__(self):
        return str(self.product_name)


class Vat(models.Model):
    vatrate = models.IntegerField(verbose_name="Stawka VAT",
                                  null=True,
                                  blank=True)

    def __str__(self):
        return str(self.vatrate)


class Orders(models.Model):
    active = models.BooleanField(null=True, blank=True, default=False)
    number = models.CharField(verbose_name="Numer zamówienia",
                              max_length=64,
                              null=True,
                              blank=True)
    status = models.IntegerField(verbose_name="Status zamówienia",
                                 choices=ORDER_STATUS,
                                 default=1)
    date = models.DateField(auto_now_add=True)
    time_start = models.TimeField(null=True, blank=True)
    time_zero = models.TimeField(null=True, blank=True)
    workplace_id = models.ForeignKey('Workplace',
                                     on_delete=models.CASCADE,
                                     verbose_name="Pizzeria",
                                     null=True,
                                     blank=True)

    barman_id = models.ForeignKey('MyUser',
                                  on_delete=models.CASCADE,
                                  verbose_name="Barman",
                                  null=True,
                                  blank=True,
                                  related_name="Barman")

    driver_id = models.ForeignKey('MyUser',
                                  on_delete=models.CASCADE,
                                  verbose_name="Kierowca",
                                  null=True,
                                  blank=True,
                                  related_name="Kierowca")

    type_of_order = models.IntegerField(verbose_name="Rodzaj zamówienia",
                                        choices=DELIVERY_TYPE,
                                        default=1)

    address = models.ForeignKey('Address',
                                on_delete=models.CASCADE,
                                verbose_name="Adres",
                                null=True,
                                blank=True)

    pay_method = models.IntegerField(verbose_name="Płatność zamówienia",
                                     choices=PAY_METHOD,
                                     default=1)

    start_delivery_time = models.TimeField(verbose_name="Czas wywozu",
                                           blank=True,
                                           null=True)
    time_delivery_in = models.TimeField(verbose_name="Czas dostarczenia",
                                        blank=True,
                                        null=True)
    sms_send = models.BooleanField(verbose_name="Sms", default=False)
    promo = models.BooleanField(verbose_name="Promocja", default=False)
    closed = models.BooleanField(verbose_name="Zamknięte", default=False)
    discount = models.IntegerField(verbose_name="Rabat",
                                   null=True,
                                   blank=True,
                                   default=0)
    info = models.CharField(verbose_name="Informacje",
                            max_length=256,
                            null=True,
                            blank=True,
                            default="")
    printed = models.BooleanField(verbose_name="Wydrukowano paragon?", default=True)

    class Meta:
        ordering = ("-id", )
        verbose_name_plural = 'Zamówienia'

    @property
    def total(self):
        income = Orders.objects.filter(workplace_id=self.workplace_id)
        total = 0
        for el in income:
            total += el.order_total_price2
        return total

    @property
    def order_total_price(self):
        total = []
        positions_on_order = PositionOrder.objects.filter(order_id=self.id)
        for el in positions_on_order:
            total.append(el.total_price)
        return round(sum(total), 2)

    def order_total_price2(self):
        if self.discount > 0:
            return round((self.order_total_price - (self.order_total_price *(self.discount / 100))), 2)
        elif self.discount == 0:
            return self.order_total_price
        else:
            return round((self.order_total_price - (self.order_total_price *
                                                    (self.discount / (-100)))),
                         2)
    @property                     
    def order_total_price_new(self):
        if self.discount > 0:
            return round((self.order_total_price - (self.order_total_price *(self.discount / 100))), 2)
        elif self.discount == 0:
            return self.order_total_price
        else:
            return round((self.order_total_price - (self.order_total_price *
                                                    (self.discount / (-100)))),
                         2)

    @property
    def income_total(self):
        if self.discount > 0:
            return round((self.order_total_price - (self.order_total_price *
                                                    (self.discount / 100))), 2)
        elif self.discount == 0:
            return self.order_total_price
        else:
            return round((self.order_total_price - (self.order_total_price *
                                                    (self.discount / (-100)))),
                         2)
    @property
    def products_in(self):
        pos=PositionOrder.objects.filter(order_id=self.id)
        products=[]
        for el in pos:
            for q in range(el.quantity):
                products.append(el.product_id.id)
        return products

    def __str__(self):
        return str(self.id) + " - " + str(self.number) + " - " + str(
            self.workplace_id)


class PositionOrder(models.Model):
    order_id = models.ForeignKey(
        'Orders',
        on_delete=models.CASCADE,
        verbose_name="Zamówienie nr.",
        null=True,
        blank=True,
    )
    quantity = models.IntegerField(verbose_name="Ilosc", default=1)

    product_id = models.ForeignKey(
        'Products',
        on_delete=models.CASCADE,
        verbose_name="Product na zamówieniu",
        null=True,
        blank=True,
    )
    product_id_pizza_right = models.ForeignKey('Products',
                                               on_delete=models.CASCADE,
                                               verbose_name="Pizza prawa",
                                               null=True,
                                               blank=True,
                                               related_name="Pizza_on_rigth")
    size_id = models.ForeignKey(
        'ProductSize',
        on_delete=models.CASCADE,
        verbose_name="Rozmiar",
        null=True,
        blank=True,
    )
    halfpizza_name = models.CharField(
        verbose_name="Nazwa składana z dwóch produktów",
        max_length=126,
        null=True,
        blank=True,
        default="")
    pizza_half = models.BooleanField(verbose_name="Pizza pol_na_pol",
                                     default=False)
    freestyle_toppings = models.ManyToManyField(
        "Products",
        verbose_name="Dodatki",
        related_name="order_position_toppings",
        blank=True)

    change_topps_info = models.CharField(
        verbose_name="Info o zmianie składników",
        max_length=1012,
        null=True,
        blank=True,
        default="")
    change_topps_info_id = models.CharField(
        verbose_name="Id o zmianie składników",
        max_length=256,
        null=True,
        blank=True,
        default="'")
    change_topps_info_other_side = models.CharField(
        verbose_name="Info o zmianie składników na prawej",
        max_length=1012,
        null=True,
        blank=True,
        default="")
    change_topps_info_right_id = models.CharField(
        verbose_name="Id o zmianie składników na prawej",
        max_length=256,
        null=True,
        blank=True,
        default="'")

    cake_info = models.CharField(verbose_name="Zmiany ciasta",
                                 max_length=128,
                                 null=True,
                                 blank=True,
                                 default="")
    sauces_free = models.CharField(verbose_name="Sosy darmowe",
                                   max_length=256,
                                   null=True,
                                   blank=True,
                                   default="")
    sauces_pay = models.CharField(verbose_name="Sosy płatne",
                                  max_length=256,
                                  null=True,
                                  blank=True,
                                  default="")
    extra_price = models.FloatField(verbose_name="Cena dodatków",
                                    null=True,
                                    blank=True,
                                    default=0)
    extra_price_left = models.FloatField(
        verbose_name="Cena dodatków na prawej",
        null=True,
        blank=True,
        default=0)
    extra_price_right = models.FloatField(
        verbose_name="Cena dodatków na prawej",
        null=True,
        blank=True,
        default=0)
    info = models.CharField(verbose_name="Informacje",
                            max_length=256,
                            null=True,
                            blank=True,
                            default="")
    price = models.FloatField(verbose_name="Cena podstawowa", )
    discount = models.IntegerField(verbose_name="Rabat",
                                   null=True,
                                   blank=True,
                                   default=0)

    @property
    def total_price(self):
        if self.discount > 0:
            return round(
                float(
                    ((self.price) - (float(self.price)) *
                     (float(self.discount) * 0.01) + float(self.extra_price)) *
                    int(self.quantity)), 2)
        if self.discount > 0 and self.extra_price == 0:
            return round(
                float(self.price) - ((float(self.price) *
                                      (float(self.discount) * 0.01))), 2)
        else:

            return round(((float(self.extra_price) + float(self.price)) *
                          int(self.quantity)), 2)

    class Meta:
        ordering = ("-id", )
        verbose_name_plural = 'Pozycje na zamówieniu'

    def __str__(self):
        return str(self.id)+", "+str(self.order_id)+", "+str(self.product_id.product_name)


class Purchases(models.Model):
    date = models.DateField(auto_now=True)
    barman_id = models.ForeignKey('MyUser',
                                  on_delete=models.CASCADE,
                                  verbose_name="Wprowadzający",
                                  null=True,
                                  blank=True,
                                  related_name="Buyer")
    work_place = models.ForeignKey('WorkPlace',
                                   on_delete=models.CASCADE,
                                   verbose_name="Lokal",
                                   null=True,
                                   blank=True)
    purchase_name = models.CharField(verbose_name="Nazwa",
                                     max_length=256,
                                     null=True,
                                     blank=True,
                                     default="")
    pay_method = models.IntegerField(
        verbose_name="Rodzaj wydatku: ",
        choices=PAY_METHOD_2,default="1"
    )
    
    price = models.FloatField(verbose_name="Cena", )
    type_purchases = models.IntegerField(
        verbose_name="Rodzaj kosztu: ",
        choices=TYPE_OF_PURCHASE,default="0"
    )

    info = models.CharField(verbose_name="Info",
                                     max_length=256,
                                     null=True,
                                     blank=True,
                                     default="")
    
    

    class Meta:
        ordering = ("-id", )
        verbose_name_plural = 'Wydatki'

    def __str__(self):
        return str(self.id) + ", " + str(self.purchase_name) + ", " + str(
            self.price)


class CashRegister(models.Model):

    cash = models.FloatField(verbose_name="Gotówka", default=0)
    cards = models.FloatField(verbose_name="Karta", default=0)

    def total(self):
        income = Orders.objects.filter(workplace_id=self.work_place)
        total = 0
        for el in income:
            total += el.order_total_price2
        return total