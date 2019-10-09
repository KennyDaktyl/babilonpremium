from babilon.models import *
from django.core.exceptions import ObjectDoesNotExist


def add_position_to_order(product_add):
    orderPosition = PositionOrder()
    orderPosition.price = product_add.price
    orderPosition.extra_price = product_add.extra_price
    quantity = 1
    orderPosition.quantity = quantity
    orderPosition.position = "{}x {} Rozmiar:{}, Cena{}".format(
        quantity, product_add.name, product_add.size, product_add.price)
    orderPosition.save()

    for el in product_add.toppings.all():
        orderPosition.toppings.add(el)
        orderPosition.save()

    # try:
    #     order = Orders.objects.get(active=True)
    # except ObjectDoesNotExist:
    #     order = Orders()
    #     order.active = True
    #     orderId = order.id
    #     order.save()
    # order.position.add(orderPosition)
    # order.save()
    return orderPosition


def new_positionOrder(product_add):

    orderPosition = product_add
    print(orderPosition)

    try:
        order = Orders.objects.get(active=True)
        order.position.add(orderPosition)
        order.save()
    except ObjectDoesNotExist:
        order = Orders()
        order.active = True
        orderId = order.id
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