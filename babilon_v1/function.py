import os
import json
import urllib.request
import googlemaps
from .models import *
from django.core.exceptions import ObjectDoesNotExist
from smsapi.client import SmsApiPlClient

from datetime import datetime
from calendar import monthrange

from django.conf import settings
from django.http import HttpResponse, Http404

year = datetime.now().year
month = datetime.now().month
day = datetime.now().day

# from googlemaps import get_my_key


def active_drivers(drivers):
    for driver in drivers:
        if driver.day_when_active != datetime.now().date():
            driver.active = False
            driver.save()


def last_day_of_month(date_value):
    return date_value.replace(day=monthrange(date_value.year, date_value.month)[1])


def get_pizzeria_session(request):
    try:
        pizzeria_set_id = request.session["pizzeria"]
        pizzeria_active = WorkPlace.objects.get(pk=pizzeria_set_id)
        # print('jest')
        # print(request.session['pizzeria'])
    except:
        pizzeria_active = request.user.work_place.first()
        # print(pizzeria_active)
        pizzeria_set_id = pizzeria_active.id
        # print('nie ma')

    request.session["pizzeria"] = pizzeria_active.id
    # print(request.session['pizzeria'])

    return pizzeria_active


def toppings(product):
    toppings = []
    for el in product.toppings.all():
        toppings.append(el)
    vegecounter = 0
    beefcounter = 0
    cheesecounter = 0
    extracounter = 0
    cakecounter = 0
    for el in toppings:
        if el.type_of_ingredient == 1:
            vegecounter += 1
        if el.type_of_ingredient == 2:
            beefcounter += 1
        if el.type_of_ingredient == 3:
            cheesecounter += 1
        if el.type_of_ingredient == 4:
            extracounter += 1
        if el.type_of_ingredient == 5:
            cakecounter += 1
    addvege_pay_control = vegecounter
    beef_pay_control = beefcounter
    cheese_pay_control = cheesecounter
    extra_pay_control = extracounter
    cake_pay_control = cakecounter
    vege_pay = vegecounter
    beef_pay = beefcounter
    cheese_pay = cheesecounter
    extra_pay = extracounter
    cake_pay = cakecounter
    toppings_counter = {
        "vegecounter": vegecounter,
        "beefcounter": beefcounter,
        "cheesecounter": cheesecounter,
        "extracounter": extracounter,
    }
    return toppings_counter


def counter_cursers(self, date_start, date_end, pizzeria):

    driver_courses_count = (
        Orders.objects.filter(type_of_order="3")
        .filter(status="4")
        .filter(date__gte=date_start)
        .filter(date__lte=date_end)
        .filter(workplace_id=pizzeria)
        .filter(driver_id=self)
        .count
    )
    return driver_courses_count


def counter_cursers_cash(self, date_start, date_end, pizzeria):
    driver_courses = (
        Orders.objects.filter(type_of_order="3")
        .filter(status="4")
        .filter(date__gte=date_start)
        .filter(date__lte=date_end)
        .filter(workplace_id=pizzeria)
        .filter(driver_id=self)
        .filter(pay_method=1)
    )
    cash = 0
    for order in driver_courses:
        cash += order.order_total_price2()
    cash=round(cash,2)
    return cash


def counter_cursers_card(self, date_start, date_end, pizzeria):
    driver_courses = (
        Orders.objects.filter(type_of_order="3")
        .filter(status="4")
        .filter(date__gte=date_start)
        .filter(date__lte=date_end)
        .filter(workplace_id=pizzeria)
        .filter(driver_id=self)
        .filter(pay_method=2)
    )
    card = 0
    for order in driver_courses:
        card += order.order_total_price2()
    card=round(card,2)
    return card


def counter_cursers_card_counter(self, date_start, date_end, pizzeria):
    driver_courses_card_count = (
        Orders.objects.filter(type_of_order="3")
        .filter(status="4")
        .filter(date__gte=date_start)
        .filter(date__lte=date_end)
        .filter(workplace_id=pizzeria)
        .filter(driver_id=self)
        .filter(pay_method=2)
        .count
    )

    return driver_courses_card_count


def counter_cursers_online_1(self, date_start, date_end, pizzeria):
    driver_courses = (
        Orders.objects.filter(type_of_order="3")
        .filter(status="4")
        .filter(date__gte=date_start)
        .filter(date__lte=date_end)
        .filter(workplace_id=pizzeria)
        .filter(driver_id=self)
        .filter(pay_method=3)
    )
    card = 0
    for order in driver_courses:
        card += order.order_total_price2()
    card=round(card,2)
    return card


def counter_cursers_online_2(self, date_start, date_end, pizzeria):
    driver_courses = (
        Orders.objects.filter(type_of_order="3")
        .filter(status="4")
        .filter(date__gte=date_start)
        .filter(date__lte=date_end)
        .filter(workplace_id=pizzeria)
        .filter(driver_id=self)
        .filter(pay_method=4)
    )
    card = 0
    for order in driver_courses:
        card += order.order_total_price2()
    card=round(card,2)
    return card


def counter_cursers_online_3(self, date_start, date_end, pizzeria):
    driver_courses = (
        Orders.objects.filter(type_of_order="3")
        .filter(status="4")
        .filter(date__gte=date_start)
        .filter(date__lte=date_end)
        .filter(workplace_id=pizzeria)
        .filter(driver_id=self)
        .filter(pay_method=5)
    )
    card = 0
    for order in driver_courses:
        card += order.order_total_price2()
    card=round(card,2)
    return card


def download(request, path):
    file_path = os.path.join(settings.MEDIA_ROOT, path)
    print(file_path)
    if os.path.exists(file_path):
        with open(file_path, "rb") as fh:
            response = HttpResponse(fh.read(), content_type="application/vnd.ms-excel")
            response["Content-Disposition"] = "inline; filename=" + os.path.basename(
                file_path
            )
            print(response)
            return response
    raise Http404

def set_code_number():
    cat_list=[1,2]
    category=Category.objects.filter(category_number__in=cat_list)
    products = Products.objects.filter(category__in=category)
    for el in products:
        el.code_number=str(el.category.category_number)+str(el.pizza_number)+str(int(el.product_size.id)+2)
        el.save()
        


# def counter_cursers_card(self, date_start, date_end, pizzeria):
#     driver_courses = Orders.objects.filter(type_of_order="3").filter(
#         status="4").filter(date__gte=date_start).filter(
#             date__lte=date_end).filter(workplace_id=pizzeria).filter(
#                 driver_id=self)
#     cash = 0
#     for order in driver_courses:
#         cash += order.order_total_price2()

#     return cash

# def counter_cursers_cash(self, date_start, date_end, pizzeria):

#     driver_courses = Orders.objects.filter(type_of_order="3").filter(
#         status="4").filter(date__gte=date_start).filter(
#             date__lte=date_end).filter(workplace_id=pizzeria).filter(
#                 driver_id=self)
#     cash = 0
#     for order in driver_courses:
#         cash += order.order_total_price2

#     return cash

# def get_order(request, pizzeria):
#     try:
#         active_order_id = request.session['active_orders']
#         if active_order_id:
#             if active_order_id.barman_id == request.user:
#                 active_order = Orders.objects.get(pk=active_order_id)
#                 active_order.save()
#                 print(active_order_id.barman_id)
#                 print(request.user)
#             else:
#                 active_order = Orders()
#                 active_order.active = True
#                 active_order.save()
#                 active_order.workplace_id = pizzeria
#                 active_order.barman_id = request.user
#                 active_order.number = new_number(pizzeria.id)
#                 active_order.save()
#                 request.session['active_orders'] = active_order.id
#                 print('hello1')

#         else:
#             last_order = Orders.objects.filter(workplace_id=pizzeria).filter(
#                 date__day=day).first()
#             print('hello2')
#             if last_order != None and last_order.active == True:
#                 active_order = last_order
#                 request.session['active_orders'] = active_order.id
#             else:
#                 active_order = Orders()
#                 active_order.active = True
#                 active_order.save()
#                 active_order.workplace_id = pizzeria
#                 active_order.barman_id = request.user
#                 active_order.number = new_number(pizzeria.id)
#                 active_order.save()
#                 request.session['active_orders'] = active_order.id

#     except:
#         last_order = Orders.objects.filter(workplace_id=pizzeria).filter(
#             date__day=day).first()

#         if last_order != None and last_order.active == True and last_order.barman_id == request.user:
#             active_order = last_order
#             request.session['active_orders'] = active_order.id
#             print(active_order)
#             print('hello4')
#         else:
#             active_order = Orders()
#             active_order.active = True
#             active_order.save()
#             active_order.workplace_id = pizzeria
#             active_order.barman_id = request.user
#             active_order.number = new_number(pizzeria.id)
#             active_order.save()
#             request.session['active_orders'] = active_order.id
#             print('hello3')
#             print(active_order.barman_id)
#             print(request.user)

#     return active_order


def send_sms(number, message):
    client = SmsApiPlClient(access_token=os.environ.get("SMS_TOKEN"),)

    send_results = client.sms.send(to=number, message=message)

    for result in send_results:
        print(result.id, result.points, result.error)


def new_number(pizzeria_id):

    try:
        last_number = Orders.objects.filter(workplace_id=pizzeria_id).first()
        print(last_number)
        if last_number != None:
            last_number = last_number
            number_indx = int(last_number.number[:3]) + 1

            ln_day = last_number.date.day

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


# def new_positionOrder(product_add):
#     orderPosition = product_add

#     # print(orderPosition)
#     pizzeria = Pizzeria.objects.get(pk=1)

#     try:
#         order = Orders.objects.filter(active=True).first()
#         order.position.add(orderPosition)
#         orderPosition.order = order
#         orderPosition.save()
#         order.pizzeria = pizzeria
#         order.save()
#     except ObjectDoesNotExist:
#         order = Orders()
#         order.active = True
#         orderId = order.id
#         order.save()
#         orderPosition.order = order
#         orderPosition.save()
#         order.pizzeria = pizzeria
#         order.number = new_number(1)
#         # print(order.number)
#         order.save()
#         order.position.add(orderPosition)
#         order.save()
#     return orderPosition

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
