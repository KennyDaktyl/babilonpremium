from django.db import models
from django.contrib.auth.models import AbstractUser
from babilon.choices_field import *
from django.db.models import Count

from datetime import datetime

month = datetime.now().month
year = datetime.now().year


class EmployeePosition(models.Model):
    positionname = models.CharField(verbose_name="Stanowisko w firmie",
                                    max_length=64)
    rateph = models.IntegerField(verbose_name="Stawka na godzinę")
    agreement = models.IntegerField(verbose_name="Rodzaj zatrudnienia",
                                    choices=Rodzaj_Umowy,
                                    null=True,
                                    blank=True)

    def __str__(self):
        return str(self.positionname)


class MyUser(AbstractUser):
    position = models.ForeignKey("EmployeePosition",
                                 on_delete=models.CASCADE,
                                 null=True,
                                 blank=True)
    phone = models.IntegerField(verbose_name="Numer telefonu pracownika",
                                null=True,
                                blank=True)

    work_in = models.ManyToManyField("Pizzeria",
                                     verbose_name="Zatrudniony w:",
                                     related_name="work_in",
                                     blank=True)
    work_in_today = models.ForeignKey("Pizzeria",
                                      on_delete=models.CASCADE,
                                      null=True,
                                      blank=True,
                                      verbose_name="Miejsce pracy dzisiaj")
    adress = models.ForeignKey("Address",
                               null=True,
                               blank=True,
                               on_delete=models.CASCADE)
    info = models.TextField(verbose_name="Info", null=True, blank=True)

    def __str__(self):
        return str(self.username) + ", " + str(self.first_name) + ", " + str(
            self.last_name)


class Clients(models.Model):

    firstlastname = models.CharField(verbose_name="Imię Nazwisko",
                                     max_length=64,
                                     null=True,
                                     blank=True)
    phone_number = models.CharField(verbose_name="Numer telefonu",
                                    max_length=9)
    adrress = models.ManyToManyField("Address",
                                     verbose_name="Adres klienta",
                                     related_name="Adresy_klienta")
    status = models.IntegerField(verbose_name="Status klienta",
                                 choices=STATUS_KLIENTA,
                                 null=True,
                                 blank=True)
    info = models.CharField(verbose_name="Info",
                            max_length=128,
                            null=True,
                            blank=True)

    def __str__(self):
        return str(self.firstlastname) + ", " + str(
            self.phone_number) + ", " + str(self.adrress) + ", " + str(
                self.status)


class Address(models.Model):
    address = models.CharField(verbose_name="Adres", max_length=128)

    quantity = models.IntegerField(verbose_name="Licznik wyboru", default=1)

    class Meta:
        ordering = ("quantity", )

    def __str__(self):
        return str(self.id) + "," + str(self.address)


class Pizzeria(models.Model):
    name = models.CharField(verbose_name="Nazwa pizzerii", max_length=128)
    adress = models.ForeignKey("Address",
                               null=True,
                               blank=True,
                               on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id) + ", " + str(self.name)


class Category(models.Model):
    name = models.CharField(verbose_name="Kategoria produktu", max_length=128)

    def __str__(self):
        return str(self.name)


class ProductSize(models.Model):
    size = models.CharField(verbose_name="Rozmiar", max_length=64)
    menu = models.ForeignKey('MainMenu',
                             verbose_name="Rozmiar kategori",
                             blank=True,
                             null=True,
                             on_delete=models.CASCADE,
                             related_name="Menu_rozmiar")

    pizza = models.BooleanField(verbose_name="Pizza", null=True, blank=True)

    bottle = models.BooleanField(verbose_name="Butelka", null=True, blank=True)
    sauce = models.BooleanField(verbose_name="Sos", null=True, blank=True)
    pizza_box = models.BooleanField(verbose_name="Sos", null=True, blank=True)

    vege_topps_price = models.FloatField(
        verbose_name="Cena dodatku warzywnego", null=True, blank=True)
    beef_topps_price = models.FloatField(verbose_name="Cena dodatku mięsnego",
                                         null=True,
                                         blank=True)
    cheese_topps_price = models.FloatField(
        verbose_name="Cena dodatku serowego", null=True, blank=True)
    extra_topps_price = models.FloatField(verbose_name="Cena dodatku extra_1",
                                          null=True,
                                          blank=True)

    sauce_price = models.DecimalField(verbose_name="Cena dodatkowego sosu",
                                      null=True,
                                      blank=True,
                                      max_digits=19,
                                      decimal_places=2)

    class Meta:
        ordering = ("size", )

    def __str__(self):
        return str(self.size)


class ToppingCategory(models.Model):
    name = models.CharField(verbose_name="Nazwa dodatku", max_length=64)
    price = models.IntegerField(verbose_name="Cena za dodatek",
                                null=True,
                                blank=True)
    size = models.ForeignKey("ProductSize",
                             verbose_name="Rozmiar",
                             blank=True,
                             null=True,
                             on_delete=models.CASCADE,
                             related_name="topping_size")

    class Meta:
        ordering = ("name", "size")

    def __str__(self):
        return str(self.id) + " " + str(self.name) + " " + str(
            self.size) + " " + str(self.price)


class Products(models.Model):
    menu_category = models.ForeignKey("MainMenu",
                                      verbose_name="Kategoria w Menu",
                                      blank=True,
                                      null=True,
                                      on_delete=models.CASCADE,
                                      related_name="cat_menu")

    name = models.CharField(verbose_name="Nazwa productu", max_length=128)

    size = models.ForeignKey("ProductSize",
                             verbose_name="Rozmiar",
                             blank=True,
                             null=True,
                             on_delete=models.CASCADE,
                             related_name="Product_size")
    quantity = models.IntegerField(verbose_name="Ilosc",
                                   null=True,
                                   blank=True,
                                   default=1)
    toppings = models.ManyToManyField("Products",
                                      verbose_name="Składniki",
                                      related_name="pizza_component",
                                      blank=True)
    change_toppings = models.CharField(verbose_name="Zaminy w składnikach",
                                       max_length=128,
                                       null=True,
                                       blank=True,
                                       default="")
    change_extra_toppings = models.CharField(
        verbose_name="Zaminy w składnikach",
        max_length=128,
        null=True,
        blank=True,
        default="")
    cake_info = models.CharField(verbose_name="Zaminy w składnikach",
                                 max_length=128,
                                 null=True,
                                 blank=True,
                                 default="")
    cake_modyfy = models.BooleanField(verbose_name="Czy ser w rantach możliwy",
                                      null=True,
                                      blank=True)
    component = models.IntegerField(verbose_name="component",
                                    choices=RODZAJ_SKŁADNIKA,
                                    null=True,
                                    blank=True)
    pizza_freestyle = models.BooleanField(verbose_name="Pizza freestyle",
                                          default=False)

    cake = models.BooleanField(verbose_name="Składnik do ciasta?",
                               null=True,
                               blank=True)

    extra_price = models.FloatField(verbose_name="Cena dodatków",
                                    null=True,
                                    blank=True,
                                    default=0)
    price = models.FloatField(verbose_name="Cena podstawowa",
                              null=True,
                              blank=True)
    discount = models.IntegerField(verbose_name="Rabat",
                                   default=0,
                                   null=True,
                                   blank=True)
    tax = models.ForeignKey('Vat',
                            on_delete=models.CASCADE,
                            verbose_name="Stawka VAT",
                            null=True,
                            blank=True)

    class Meta:
        ordering = (
            "menu_category",
            "name",
            "size",
        )

    @property
    def suma(self):
        suma = self.price * self.quantity
        return suma

    @property
    def suma_discount(self):
        suma = (((self.price * self.quantity) * (self.discount) * 0.01))
        return suma

    @property
    def price_pizzamix(self):
        suma = []
        for el in self.pizza_componets.all():
            suma.append(el.quantity * el.price)
        suma = sum(suma)
        return suma

    @property
    def total_price(self):

        total = self.extra_price + self.price
        return total

    @property
    def show_price_size(self):
        size = ProductSize.objects.filter(pizza=True)
        pizzas = Products.objects.filter(size__in=size)
        name = self.name
        for pizza in pizzas:
            for el in size:
                print(self.name)
                print(pizza.name)
                if el.id == pizza.size.id and self.name == pizza.name:
                    price = pizza.price
                else:
                    price = "Brak produktu"
        return price
        # for el in size:
        #     print(el.id)
        # # for el in pizzas:
        # #     print(el.id)

    def __str__(self):
        return str(self.name) + ", " + str(self.size)


class Vat(models.Model):
    vatrate = models.IntegerField(verbose_name="Stawka VAT",
                                  null=True,
                                  blank=True)

    def __str__(self):
        return str(self.vatrate)


class Orders(models.Model):
    active = models.BooleanField(null=True, blank=True, default=False)
    data = models.DateTimeField(auto_now_add=True)
    pizzeria = models.ForeignKey('Pizzeria',
                                 on_delete=models.CASCADE,
                                 verbose_name="Pizzeria",
                                 null=True,
                                 blank=True)
    number = models.CharField(verbose_name="Numer zamówienia",
                              max_length=64,
                              null=True,
                              blank=True)
    status = models.IntegerField(verbose_name="Status zamówienia",
                                 choices=STATUS_ZAMOWIENIA,
                                 default=1)
    delivery = models.IntegerField(verbose_name="Rodzaj zamówienia",
                                   choices=RODZAJ_DOSTAWY,
                                   default=1)
    client = models.ForeignKey('Clients',
                               on_delete=models.CASCADE,
                               verbose_name="Klient",
                               null=True,
                               blank=True)
    address = models.ForeignKey('Address',
                                on_delete=models.CASCADE,
                                verbose_name="Adres",
                                null=True,
                                blank=True)
    position = models.ManyToManyField('PositionOrder',
                                      verbose_name="Pozycja zamowienia",
                                      blank=True,
                                      related_name="pozition_order")
    other = models.ManyToManyField("Products",
                                   blank=True,
                                   verbose_name="Dodatkowe produkty")
    paymethod = models.IntegerField(verbose_name="Płatność zamówienia",
                                    choices=PŁATNOŚĆ,
                                    default=1)
    driver = models.ForeignKey('MyUser',
                               on_delete=models.CASCADE,
                               verbose_name="Kierowca",
                               null=True,
                               blank=True)
    time_get = models.TimeField(verbose_name="Czas wywywozu",
                                blank=True,
                                null=True)
    time_in = models.TimeField(verbose_name="Czas dostarczenia",
                               blank=True,
                               null=True)

    class Meta:
        ordering = ("-data", )

    @property
    def total_price(self):
        total = []
        product = self.position.all()
        for el in product:
            total.append(el.total_price)
        return round(sum(total), 2)

    def __str__(self):
        return str(self.number)


class PositionOrder(models.Model):
    order = models.ForeignKey('Orders',
                              on_delete=models.CASCADE,
                              verbose_name="Zamówienie nr.",
                              null=True,
                              blank=True)
    quantity = models.IntegerField(verbose_name="Ilosc", default=1)
    halfpizza_name = models.CharField(verbose_name="Lewa lub prawa",
                                      max_length=126,
                                      null=True,
                                      blank=True,
                                      default="")
    position = models.ForeignKey(
        'Products',
        on_delete=models.CASCADE,
        verbose_name="Pozycja zamówienia",
        null=True,
        blank=True,
    )
    toppings = models.ManyToManyField("Products",
                                      verbose_name="Dodatki",
                                      related_name="pizza_extra_toppings",
                                      blank=True)

    change_topps = models.CharField(verbose_name="Zmiany składników",
                                    max_length=512,
                                    null=True,
                                    blank=True,
                                    default="")
    change_topps_on_right = models.CharField(
        verbose_name="Zmiany składników na prawej",
        max_length=512,
        null=True,
        blank=True,
        default="")
    cake_info = models.CharField(verbose_name="Zmiany ciasta",
                                 max_length=128,
                                 null=True,
                                 blank=True,
                                 default="")
    add_sauces_free = models.CharField(verbose_name="Sosy darmowe",
                                       max_length=256,
                                       null=True,
                                       blank=True,
                                       default="")
    add_sauces_pay = models.CharField(verbose_name="Sosy płatne",
                                      max_length=256,
                                      null=True,
                                      blank=True,
                                      default="")
    extra_price = models.FloatField(verbose_name="Cena dodatków",
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
    pizza_half = models.BooleanField(verbose_name="Pizza pol_na_pol",
                                     default=False)

    class Meta:
        ordering = ("-id", )

    @property
    def total_price(self):
        if self.discount > 0:
            return round(
                float(
                    ((self.price) - +(float(self.price)) *
                     (float(self.discount) * 0.01) + float(self.extra_price)) *
                    int(self.quantity)), 2)
        if self.discount > 0 and self.extra_price == 0:
            return round(
                float(self.price) - ((float(self.price) *
                                      (float(self.discount) * 0.01))), 2)
        else:

            return round(((float(self.extra_price) + float(self.price)) *
                          int(self.quantity)), 2)

    def __str__(self):
        return str(self.id) + ", " + str(self.position)


class MainMenu(models.Model):
    name = models.CharField(verbose_name="Kategoria menu", max_length=128)

    class Meta:
        ordering = ("name", )

    def __str__(self):
        return str(self.id) + ", " + str(self.name)


class Pizza(models.Model):
    menu_category = models.ForeignKey("MainMenu",
                                      verbose_name="Kategroia w Menu",
                                      blank=True,
                                      null=True,
                                      on_delete=models.CASCADE,
                                      related_name="category")
    name = models.CharField(verbose_name="Nazwa pizzy", max_length=128)
    toppings = models.ManyToManyField("Toppings",
                                      verbose_name="Składniki",
                                      blank=True,
                                      related_name="toppings")
    size = models.ForeignKey("PizzaSize",
                             verbose_name="Rozmiar pizzy",
                             blank=True,
                             null=True,
                             on_delete=models.CASCADE,
                             related_name="pizza_size")
    change_toppings = models.CharField(verbose_name="Zaminy w składnikach",
                                       max_length=128,
                                       null=True,
                                       blank=True)
    price = models.DecimalField(verbose_name="Cena produktu",
                                null=True,
                                blank=True,
                                max_digits=19,
                                decimal_places=2)

    class Meta:
        ordering = (
            "name",
            "size",
        )

    def __str__(self):
        return str(self.name) + " " + str(self.size) + " " + str(self.price)


class Toppings(models.Model):
    name = models.CharField(verbose_name="Nazwa składniku", max_length=128)
    pizza = models.ForeignKey(Pizza,
                              on_delete=models.CASCADE,
                              related_name='skladniki')
    category = models.IntegerField(verbose_name="Rodzaj dodatku",
                                   choices=RODZAJ_DODATKU)
    size = models.ForeignKey("PizzaSize",
                             verbose_name="Rozmiar pizzy",
                             blank=True,
                             null=True,
                             on_delete=models.CASCADE,
                             related_name="topping_size")
    price = models.DecimalField(verbose_name="Cena składnika",
                                null=True,
                                blank=True,
                                max_digits=19,
                                decimal_places=2)

    def __str__(self):
        return str(self.name) + " " + str(self.price) + " ID: " + str(self.id)


class PizzaSize(models.Model):
    size = models.CharField(verbose_name="Rozmiar pizzy", max_length=64)

    def __str__(self):
        return str(self.size)
