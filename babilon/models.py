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
    adress = models.ForeignKey("Adress",
                               null=True,
                               blank=True,
                               on_delete=models.CASCADE)
    info = models.TextField(verbose_name="Info", null=True, blank=True)

    def __str__(self):
        return str(self.username) + ", " + str(self.first_name) + ", " + str(
            self.last_name)


class Clients(models.Model):
    firstname = models.CharField(verbose_name="Imie", max_length=128)
    lastname = models.CharField(verbose_name="Nazwisko", max_length=128)
    phone_number = models.CharField(verbose_name="Numer telefonu",
                                    max_length=128)
    adress = models.ManyToManyField("Adress",
                                    verbose_name="Adres klienta",
                                    related_name="Adresy_klienta")
    status = models.IntegerField(verbose_name="Status klienta",
                                 choices=STATUS_KLIENTA,
                                 null=True,
                                 blank=True)
    info = models.CharField(verbose_name="Info", max_length=128)

    def __str__(self):
        return str(self.lastname) + ", " + str(self.phone_number) + ", " + str(
            self.adress) + ", " + str(self.status) + ", " + str(self.info)


class Adress(models.Model):
    street = models.CharField(verbose_name="Ulica", max_length=128)
    city = models.CharField(verbose_name="Miasto", max_length=128)
    code = models.CharField(verbose_name="Kod pocztowy", max_length=128)

    def __str__(self):
        return str(self.street) + ", " + str(self.city)


class Pizzeria(models.Model):
    name = models.CharField(verbose_name="Nazwa pizzerii", max_length=128)
    adress = models.ForeignKey("Adress",
                               null=True,
                               blank=True,
                               on_delete=models.CASCADE)


class Category(models.Model):
    name = models.CharField(verbose_name="Kategoria produktu", max_length=128)

    def __str__(self):
        return str(self.name)


class ProductSize(models.Model):
    size = models.CharField(verbose_name="Rozmiar", max_length=64)
    pizza = models.BooleanField(verbose_name="Pizza", null=True, blank=True)
    bottle = models.BooleanField(verbose_name="Butelka", null=True, blank=True)
    sauce = models.BooleanField(verbose_name="Sos", null=True, blank=True)
    pizza_box = models.BooleanField(verbose_name="Sos", null=True, blank=True)

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
    quantity = models.IntegerField(verbose_name="Ilosc",
                                   null=True,
                                   blank=True,
                                   default=1)
    name = models.CharField(verbose_name="Nazwa productu", max_length=128)
    change_info = models.CharField(verbose_name="Zaminy w składnikach",
                                   max_length=128,
                                   null=True,
                                   blank=True)

    pizza = models.BooleanField(verbose_name="Pizza?", null=True, blank=True)
    pizza_componets = models.ManyToManyField("Products",
                                             verbose_name="Składniki",
                                             related_name="pizza_component",
                                             blank=True)
    topping = models.ForeignKey("ToppingCategory",
                                verbose_name="Categoria dodatki pizzy",
                                blank=True,
                                null=True,
                                on_delete=models.CASCADE,
                                related_name="product_category")
    change_toppings = models.CharField(verbose_name="Zaminy w składnikach",
                                       max_length=128,
                                       null=True,
                                       blank=True,
                                       default="")
    beff_topps_price = models.DecimalField(
        verbose_name="Cena za dodatek mięsny",
        null=True,
        blank=True,
        max_digits=19,
        decimal_places=2)
    vege_topps_price = models.DecimalField(
        verbose_name="Cena za dodatek warzywny",
        null=True,
        blank=True,
        max_digits=19,
        decimal_places=2)
    cheese_topps_price = models.DecimalField(
        verbose_name="Cena za dodatek serowy",
        null=True,
        blank=True,
        max_digits=19,
        decimal_places=2)
    cake_topps_price = models.DecimalField(
        verbose_name="Cena za ser w rantach",
        null=True,
        blank=True,
        max_digits=19,
        decimal_places=2)
    cake_modyfy = models.BooleanField(verbose_name="Czy ser w rantach możliwy",
                                      null=True,
                                      blank=True)
    drink = models.BooleanField(verbose_name="Napój?", null=True, blank=True)
    component = models.IntegerField(verbose_name="component",
                                    choices=RODZAJ_SKŁADNIKA,
                                    null=True,
                                    blank=True)
    pizza_freestyle = models.BooleanField(verbose_name="Pizza freestyle",
                                          null=True,
                                          blank=True)
    cake = models.BooleanField(verbose_name="Składnik do ciasta?",
                               null=True,
                               blank=True)
    size = models.ForeignKey("ProductSize",
                             verbose_name="Rozmiar",
                             blank=True,
                             null=True,
                             on_delete=models.CASCADE,
                             related_name="Product_size")
    price = models.DecimalField(verbose_name="Cena produktu",
                                null=True,
                                blank=True,
                                max_digits=19,
                                decimal_places=2)
    extra_price = models.DecimalField(verbose_name="Cena za dodatki",
                                      null=True,
                                      blank=True,
                                      max_digits=19,
                                      decimal_places=2,
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
    menu_category = models.ForeignKey("MainMenu",
                                      verbose_name="Kategoria w Menu",
                                      blank=True,
                                      null=True,
                                      on_delete=models.CASCADE,
                                      related_name="cat_menu")

    class Meta:
        ordering = (
            "menu_category",
            "name",
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
    def total_price_pizzamix(self):
        price_comp = self.price_pizzamix
        total = price_comp + self.price
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
        return str(self.name) + ", " + str(self.size) + ", " + str(
            self.price) + ", " + str(self.tax)


class Vat(models.Model):
    vatrate = models.IntegerField(verbose_name="Stawka VAT",
                                  null=True,
                                  blank=True)

    def __str__(self):
        return str(self.vatrate)


class Orders(models.Model):
    active = models.BooleanField(null=True, blank=True, default=False)
    data = models.DateTimeField(auto_now_add=True)
    number = models.IntegerField(verbose_name="Numer zamówienia",
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
    adress = models.CharField(verbose_name="Adress",
                              max_length=128,
                              null=True,
                              blank=True)
    position = models.ManyToManyField('PositionOrder',
                                      verbose_name="Pozycja zamowienia",
                                      blank=True,
                                      related_name="pozition_order")
    other = models.ManyToManyField("Products",
                                   verbose_name="Dodatkowe produkty")
    paymethod = models.IntegerField(verbose_name="Status zamówienia",
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

    @property
    def total_price(self):
        total = []
        product = self.position.all()
        for el in product:
            suma = el.total_price
            total.append(suma)
        return sum(total)


class PositionOrder(models.Model):
    # order = models.ForeignKey('Order',
    #                           on_delete=models.CASCADE,
    #                           verbose_name="Zamówienie nr.",
    #                           null=True,
    #                           blank=True)
    quantity = models.IntegerField(verbose_name="Ilosc",
                                   null=True,
                                   blank=True,
                                   default=1)
    position = models.CharField(verbose_name="Pozycja zamówienia",
                                max_length=128)
    toppings = models.ManyToManyField("Products",
                                      verbose_name="Składniki",
                                      related_name="pizza_toppings",
                                      blank=True)
    change_topps = models.CharField(verbose_name="Zmiany składników",
                                    max_length=128)
    extra_price = models.DecimalField(verbose_name="Cena dodatków",
                                      null=True,
                                      blank=True,
                                      max_digits=19,
                                      decimal_places=2,
                                      default=0)
    price = models.DecimalField(verbose_name="Cena podstawowa",
                                null=True,
                                blank=True,
                                max_digits=19,
                                decimal_places=2)

    @property
    def total_price(self):
        return (self.extra_price + self.price) * self.quantity

    # def __str__(self):
    #     return str(self.position)
    def __str__(self):
        return str(self.position)


class MainMenu(models.Model):
    name = models.CharField(verbose_name="Kategoria menu", max_length=128)

    def __str__(self):
        return str(self.name)


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
