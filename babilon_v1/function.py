import os
import json
import urllib.request
import googlemaps
from .models import *
from django.core.exceptions import ObjectDoesNotExist
from smsapi.client import SmsApiPlClient

from datetime import datetime, timedelta
from calendar import monthrange

from django.conf import settings
from django.http import HttpResponse, Http404

import pandas as pd
import numpy as np
import matplotlib

matplotlib.use("Agg")
from matplotlib import pyplot as plt

# plt.use("Agg")


from matplotlib.ticker import FuncFormatter

year = datetime.now().year
month = datetime.now().month
day = datetime.now().day


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
    except:
        pizzeria_active = request.user.work_place.first()
        pizzeria_set_id = pizzeria_active.id

    request.session["pizzeria"] = pizzeria_active.id

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
    cash = round(cash, 2)
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
    card = round(card, 2)
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
    card = round(card, 2)
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
    card = round(card, 2)
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
    card = round(card, 2)
    return card


def download(request, path):
    file_path = os.path.join(settings.MEDIA_ROOT, path)
    if os.path.exists(file_path):
        with open(file_path, "rb") as fh:
            response = HttpResponse(fh.read(), content_type="application/vnd.ms-excel")
            response["Content-Disposition"] = "inline; filename=" + os.path.basename(
                file_path
            )
            return response
    raise Http404


def set_code_number():
    cat_list = [1, 2]
    category = Category.objects.filter(category_number__in=cat_list)
    products = Products.objects.filter(category__in=category)
    for el in products:
        el.code_number = (
            str(el.category.category_number)
            + str(el.pizza_number)
            + str(int(el.product_size.id) + 2)
        )
        el.save()


def delivery_avg(pizzeria):
    orders = (
        Orders.objects.filter(status=4)
        .filter(type_of_order=3)
        .filter(workplace_id=pizzeria)
    )
    numbers = []
    delivery_time_group_10_12 = []
    delivery_time_group_12_14 = []
    delivery_time_group_14_16 = []
    delivery_time_group_16_18 = []
    delivery_time_group_18_20 = []
    delivery_time_group_20_22 = []
    group_10 = timedelta(hours=10, minutes=00)
    group_12 = timedelta(hours=12, minutes=00)
    group_14 = timedelta(hours=14, minutes=00)
    group_16 = timedelta(hours=16, minutes=00)
    group_18 = timedelta(hours=18, minutes=00)
    group_20 = timedelta(hours=20, minutes=00)
    group_22 = timedelta(hours=22, minutes=00)
    if len(orders) > 0:
        for order in orders:
            x = timedelta(hours=order.time_start.hour, minutes=order.time_start.minute,)
            y = timedelta(
                hours=order.time_delivery_in.hour,
                minutes=order.time_delivery_in.minute,
            )
            order_hour = order.time_start.hour
            order_minute = order.time_start.minute
            time_order = str(order_hour) + ":" + str(order_minute)
            time_delivery = (y - x).total_seconds()

            if group_12 > x > group_10:
                minutes = round(int(time_delivery / 60), 0)
                if minutes > 10:
                    delivery_time_group_10_12.append(round(int(time_delivery / 60), 0))
                    # delivery_time_group_10_12.append(time_order)

            if group_14 > x > group_12:
                minutes = round(int(time_delivery / 60), 0)
                if minutes > 10:
                    delivery_time_group_12_14.append(round(int(time_delivery / 60), 0))
                    # delivery_time_group_12_14.append(time_order)

            if group_16 > x > group_14:
                minutes = round(int(time_delivery / 60), 0)
                if minutes > 10:
                    delivery_time_group_14_16.append(round(int(time_delivery / 60), 0))
                    # delivery_time_group_14_16.append(time_order)

            if group_18 > x > group_16:
                minutes = round(int(time_delivery / 60), 0)
                if minutes > 10:
                    delivery_time_group_16_18.append(round(int(time_delivery / 60), 0))
                    # delivery_time_group_16_18.append(time_order)

            if group_20 > x > group_18:
                minutes = round(int(time_delivery / 60), 0)
                if minutes > 10:
                    delivery_time_group_18_20.append(round(int(time_delivery / 60), 0))
                    # delivery_time_group_18_20.append(time_order)

            if group_22 > x > group_20:
                minutes = round(int(time_delivery / 60), 0)
                if minutes > 10:
                    delivery_time_group_20_22.append(round(int(time_delivery / 60), 0))
                    # delivery_time_group_20_22.append(time_order)
            numbers.append(time_order)
            numbers.append(order.number)
            numbers.append(round(int(time_delivery / 60), 0))
        # print(delivery_time_group_10_12)
        # print(numbers)

        def Average(lst):
            if len(lst) > 0:
                return int(sum(lst) / len(lst))
            else:
                # zero = "Pusta tablica"
                zero = len(lst)
                return int(zero)

        group_10 = Average(delivery_time_group_10_12)
        group_12 = Average(delivery_time_group_12_14)
        group_14 = Average(delivery_time_group_14_16)
        group_16 = Average(delivery_time_group_16_18)
        group_18 = Average(delivery_time_group_18_20)
        group_20 = Average(delivery_time_group_20_22)

        avr_minutes = {
            "10-12": [group_10, len(delivery_time_group_10_12)],
            "12-14": [group_12, len(delivery_time_group_12_14)],
            "14-16": [group_14, len(delivery_time_group_14_16)],
            "16-18": [group_16, len(delivery_time_group_16_18)],
            "18-20": [group_18, len(delivery_time_group_18_20)],
            "20-22": [group_20, len(delivery_time_group_20_22)],
        }
        # print(avr_minutes)
        return avr_minutes
    else:
        avr_minutes = []
        return avr_minutes


def df_orders(orders):
    orders = orders
    order_total = []
    products_in = []
    order_details = list(
        orders.values(
            "id",
            "date",
            "workplace_id",
            "number",
            "driver_id",
            "status",
            "time_start",
            "time_zero",
            "barman_id",
            "driver_id",
            "type_of_order",
            "pay_method",
            "address",
            "start_delivery_time",
            "time_delivery_in",
            "sms_send",
            "discount",
            "info",
            "printed",
        )
    )

    df = pd.DataFrame(order_details)

    for el in orders:
        order_total.append(el.order_total_price_new)
        products_in.append(el.products_in)
    df["Products"] = products_in
    df["Total_price"] = order_total
    # df = pd.DataFrame(list(orders.values('id','date', 'workplace_id', 'number','driver_id','status','time_start','time_zero','barman_id','driver_id','type_of_order','pay_method','address','start_delivery_time','time_delivery_in','sms_send','discount','info','printed','positionorder')))
    df.index += 1
    df.to_excel(os.path.join(settings.MEDIA_ROOT, "orders.xlsx"))
    return df


def diagram_income(orders):
    import matplotlib.pyplot as plt

    plt.rcParams["figure.figsize"] = (20, 10)
    orders = orders
    if len(orders)>0:
        d1 = df_orders(orders)
        # d1 = pd.read_excel(os.path.join(settings.MEDIA_ROOT, "orders.xlsx"))
        # orders_date = d1["date"][0:3]
        # print(orders_date)
        # orders_total_price = d1["Total_price"]
        d1 = d1[["date", "Total_price"]]
        d1 = d1.groupby(pd.Grouper("date")).sum()
        d = d1.plot.bar(lw=2, colormap="jet", rot=45, fontsize=12,)
        plt.step(1, 1)
        d.plot(title="Wykres przychodów")
        d.set_ylabel("Przychód", fontsize=38)
        # d.set_xlabel("Dzień", fontsize=18)
        d.figure.suptitle("Wykres przychodów", fontsize=38)

        # plt.show()
        try:
            os.remove("pizzeria/static/media/the_best_pizza.png")
        except:
            pass
        d.figure.savefig("pizzeria/static/media/income.png")
        plt.close("all")
        return d1
    else:
        d3='Brak wyników'
        return d3


def diagram_income_by_hours(orders):
    import matplotlib.pyplot as plt

    plt.rcParams["figure.figsize"] = (20, 8)
    orders = orders
    print(len(orders))
    if len(orders)>0:
        d1 = df_orders(orders)
        orders_date = d1["date"]
        orders_total_price = d1["Total_price"]
        d1 = d1[["date", "Total_price"]]
        d1 = d1.groupby(pd.Grouper("date")).sum()
        d = d1.plot.bar(lw=2, colormap="jet", rot=45, fontsize=13,)
        plt.step(1, 1)
        d.plot(title="Wykres przychodów")
        d.set_ylabel("Przychód", fontsize=38)
        # d.set_xlabel("Dzień", fontsize=18)
        d.figure.suptitle("Wykres przychodów", fontsize=38)

        # plt.show()
        try:
            os.remove("pizzeria/static/media/the_best_pizza.png")
        except:
            pass
        d.figure.savefig("pizzeria/static/media/income.png")
        plt.close("all")
        return d1
    else:
        d3='Brak wyników'
        return d3


def orders_by_hours(orders):
    import matplotlib.pyplot as plt

    plt.rcParams["figure.figsize"] = (20, 8)
    orders = orders
    if len(orders)>0:
        group_10_12 = []
        group_12_14 = []
        group_14_16 = []
        group_16_18 = []
        group_18_20 = []
        group_20_22 = []
        group_10 = timedelta(hours=10, minutes=00)
        group_12 = timedelta(hours=12, minutes=00)
        group_14 = timedelta(hours=14, minutes=00)
        group_16 = timedelta(hours=16, minutes=00)
        group_18 = timedelta(hours=18, minutes=00)
        group_20 = timedelta(hours=20, minutes=00)
        group_22 = timedelta(hours=22, minutes=00)
        if len(orders) > 0:
            for order in orders:
                x = timedelta(hours=order.time_start.hour, minutes=order.time_start.minute,)
                order_hour = order.time_start.hour
                order_minute = order.time_start.minute
                time_order = str(order_hour) + ":" + str(order_minute)

                if group_12 > x > group_10:
                    group_10_12.append(order)

                if group_14 > x > group_12:
                    group_12_14.append(order)

                if group_16 > x > group_14:
                    group_14_16.append(order)

                if group_18 > x > group_16:
                    group_16_18.append(order)

                if group_20 > x > group_18:
                    group_18_20.append(order)

                if group_22 > x > group_20:
                    group_20_22.append(order)
            group_10 = len(group_10_12)
            group_12 = len(group_12_14)
            group_14 = len(group_14_16)
            group_16 = len(group_16_18)
            group_18 = len(group_18_20)
            group_20 = len(group_20_22)
            order_by_hour = {
                "10-12": group_10,
                "12-14": group_12,
                "14-16": group_14,
                "16-18": group_16,
                "18-20": group_18,
                "20:22": group_20,
            }
            # print(order_by_hour)
            keys=[]
            values=[]
            for key,value in order_by_hour.items():
                keys.append(key)
                values.append(value)
            x=keys
            y=values
            data_dict={'Godziny':keys,'Zamówienia':values}
            dframe=pd.DataFrame(data_dict)
            d3=dframe.plot.bar(x="Godziny",y="Zamówienia",rot=0, fontsize=13)
            d3.set_xlabel("Grupy godzinowe", fontsize=38)
            d3.set_ylabel("Zamówienia", fontsize=38)
            d3.figure.suptitle("Wykres godzinowy", fontsize=38)
            plt.savefig("pizzeria/static/media/orders_by_hours.png")
            plt.close("all")
            return d3
    else:
        d3='Brak wyników'
        return d3


def the_best_pizza(pos):
    import matplotlib.pyplot as plt

    plt.style.reload_library()
    plt.rcParams["figure.figsize"] = (40, 15)
    pos_list = []
    if len(pos)>0:
        for el in pos:
            pos_list.append(str(el.product_id.product_name) + " - " + str(el.size_id))
        
        x = pd.Series(pos_list)
        x = x.value_counts(ascending=False)
        d3 = x[0:10]

        # df = pd.DataFrame({"Nazwa": d2.index, "Ilość": d2[0]})
        d3 = d3.plot.barh(x="Nazwa", width=0.3, y="Ilość", rot=0, fontsize=23,)
        d3.set_xlabel("Ilość", fontsize=48)
        # d3.set_ylabel("Pizza", fontsize=48)
        d3.figure.suptitle("10 najlepszych produktów", fontsize=48)
        
        # plt.show()
        d3.figure.savefig("pizzeria/static/media/the_best_pizza.png")
        plt.close("all")
        return d3
    else:
        d3='Brak wyników'
        return d3


def the_poor_pizza(pos):
    import matplotlib.pyplot as plt

    plt.style.reload_library()
    plt.rcParams["figure.figsize"] = (40, 15)
    pos_list = []
    if len(pos)>0:
        for el in pos:
            pos_list.append(str(el.product_id.product_name) + " - " + str(el.size_id))

        x = pd.Series(pos_list)
        x = x.value_counts(ascending=False)
        d3 = x[-10:]

        # df = pd.DataFrame({"Nazwa": d2.index, "Ilość": d2[0]})
        d3 = d3.plot.barh(x="Nazwa", width=0.3, y="Ilość", rot=0, fontsize=23,)
        d3.set_xlabel("Ilość", fontsize=48)
        d3.step(x=1, y=1)
        # d3.set_ylabel("Pizza", fontsize=48)
        d3.figure.suptitle("10 najgorszych produktów", fontsize=48)
        d3.figure.savefig("pizzeria/static/media/the_poor_pizza.png")
        plt.close("all")
        return d3
    else:
        d3='Brak wyników'
        return d3

def send_sms(number, message):
    client = SmsApiPlClient(access_token=os.environ.get("SMS_TOKEN"),)

    send_results = client.sms.send(to=number, message=message)

    for result in send_results:
        print(result.id, result.points, result.error)


def new_number(pizzeria_id):

    try:
        last_number = Orders.objects.filter(workplace_id=pizzeria_id).first()
        if last_number != None:
            last_number = last_number
            number_indx = int(last_number.number[:3]) + 1

            ln_day = last_number.date.day

            if ln_day != day:
                number_indx = 1
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
            number_format = f"001/{day}/{month}/{year}"
            return number_format

    except ObjectDoesNotExist:
        pass

