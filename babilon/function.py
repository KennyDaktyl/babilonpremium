from .models import *
from django.core.exceptions import ObjectDoesNotExist

from datetime import datetime

year = datetime.now().year
month = datetime.now().month
day = datetime.now().day


def add_position_to_order(product_add):
    orderPosition = PositionOrder()
    orderPosition.price = product_add.price
    orderPosition.extra_price = product_add.extra_price
    orderPosition.position = product_add
    # orderPosition.discount = 0
    orderPosition.save()
    return orderPosition


def new_number(pizzeria_id):

    try:
        last_number = Orders.objects.filter(pizzeria=pizzeria_id).first()
        print(last_number)
        if last_number != None:
            last_number = last_number
            number_indx = int(last_number.number[:3]) + 1

            ln_day = last_number.data.day

            if ln_day != day:
                number_indx = 1
                print(ln_day)
                print(day)
            # number = (str(number_indx), "/", str(day), "/", str(month), "/",
            #           str(year))
            if number_indx < 10:
                if day > 9:
                    number_format = f"00{number_indx}/{day}/{month}/{year}"
                else:
                    number_format = f"00{number_indx}/0{day}/{month}/{year}"

            if 100 > number_indx > 9:
                if day > 9:
                    number_format = f"0{number_indx}/{day}/{month}/{year}"
                else:
                    number_format = f"0{number_indx}/0{day}/{month}/{year}"
            if 999 > number_indx > 99:
                if day > 9:
                    number_format = f"{number_indx}/{day}/{month}/{year}"
                else:
                    number_format = f"{number_indx}/0{day}/{month}/{year}"
            if number_indx > 999:
                if day > 9:
                    number_format = f"{number_indx}/{day}/{month}/{year}"
                else:
                    number_format = f"{number_indx}/0{day}/{month}/{year}"
            return number_format
        else:
            print("jestem tutaj")
            number_format = f"001/{day}/{month}/{year}"
            return number_format

    except ObjectDoesNotExist:
        pass
        # number_format = f"001/{month}/{year}"
        # return number_format


def new_positionOrder(product_add):
    orderPosition = product_add

    # print(orderPosition)
    pizzeria = Pizzeria.objects.get(pk=1)

    try:
        order = Orders.objects.get(active=True)
        order.position.add(orderPosition)
        order.pizzeria = pizzeria
        order.save()
    except ObjectDoesNotExist:
        order = Orders()
        order.active = True
        orderId = order.id
        order.pizzeria = pizzeria
        order.number = new_number(1)
        # print(order.number)
        order.save()
        order.position.add(orderPosition)
        order.save()
    return orderPosition

    # NewOrderPosition = PositionOrder()
    # NewOrderPosition.save()

    # for el in product_add.toppings.all():
    #     NewOrderPosition.toppings.add(el)

    # NewOrderPosition.price = product_add.price
    # ilosc = int(NewOrderPosition.quantity)
    # NewOrderPosition.save()


# def add_modyfi_position_do_order(product_add, changeTopps):
#     orderPosition = PositionOrder()
#     # orderPosition.price = product_add.price

#     ilosc = int(orderPosition.quantity)
#     orderPosition.save()
#     orderPosition.position = "{}x {} Rozmiar:{}, Cena{}".format(
#         ilosc, product_add.name, product_add.size, product_add.price)
#     orderPosition.save()
#     if changeTopps != None:
#         orderPosition.change_topps = changeTopps
#     orderPosition.save()

#     try:
#         NewOrderPosition = Orders.objects.get(active=True)
#     except ObjectDoesNotExist:
#         NewOrderPosition = Orders()
#         NewOrderPosition.active = True
#         NewOrderPosition = orderPosition.id
#         NewOrderPosition.save()

#     if changeTopps != None:
#         orderPosition.change_topps = changeTopps
#         orderPosition.save()
#     ilosc = int(orderPosition.quantity)
#     try:
#         order = Orders.objects.get(active=True)
#     except ObjectDoesNotExist:
#         order = Orders()
#         order.active = True
#         orderId = order.id
#         order.save()
#     order.position.add(orderPosition)
#     order.save()
#     return orderPosition

# def add_modyfi_position_do_order(product_add, changeTopps):
#     orderPosition = PositionOrder()
#     orderPosition.price = product_add.price

#     ilosc = str(orderPosition.quantity)
#     orderPosition.save()
#     orderPosition.position = "{}x {} Rozmiar:{}, Cena{}".format(
#         ilosc, product_add.name, product_add.size, product_add.price)
#     orderPosition.save()
#     if changeTopps != None:
#         orderPosition.change_topps = changeTopps
#     orderPosition.save()

#     try:
#         order = Orders.objects.get(active=True)
#     except ObjectDoesNotExist:
#         order = Orders()
#         order.active = True
#         orderId = order.id
#         order.save()
#     order.position.add(orderPosition)
#     order.save()
#     return orderPosition