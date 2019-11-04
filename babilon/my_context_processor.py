from babilon.models import MainMenu, ProductSize, Products, Orders

from django.core.exceptions import ObjectDoesNotExist

from .function import *


def menu(request):
    menu = MainMenu.objects.all()
    ctx = {
        "menu": menu,
        "version": "1.0",
    }
    return ctx


def products(request):
    products = Products.objects.filter(menu_category__name="Pizza")
    ctx = {
        "products": products,
        "version": "1.0",
    }
    return ctx


def order(request):

    try:
        order = Orders.objects.get(active=True)

    except ObjectDoesNotExist:
        order = Orders()
        order.active = True
        order.number = new_number(1)
        order.save()

    ctx = {
        "order": order,
        "version": "1.0",
    }
    return ctx


def pizza_sizes(request):
    sizes = ProductSize.objects.filter(pizza=True)
    ctx = {
        "pizza_sizes": sizes,
        "version": "1.0",
    }
    return ctx


# def pracownicy(request):
#     pracownicy = MyUser.objects.all().order_by("username")
#     ctx = {
#         "pracownicy": pracownicy,
#         "version": "1.0",
#     }
#     return ctx
