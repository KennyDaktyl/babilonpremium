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

from django.core.serializers.json import DjangoJSONEncoder

matplotlib.use("Agg")
from matplotlib import pyplot as plt

# plt.use("Agg")

from matplotlib.ticker import FuncFormatter


def active_drivers(drivers):
    for driver in drivers:
        if driver.day_when_active != datetime.now().date():
            driver.active = False
            driver.save()


def last_day_of_month(date_value):
    return date_value.replace(
        day=monthrange(date_value.year, date_value.month)[1])


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

    driver_courses_count = (Orders.objects.filter(type_of_order="3").filter(
        status="4").filter(date__gte=date_start).filter(
            date__lte=date_end).filter(workplace_id=pizzeria).filter(
                driver_id=self).count)
    return driver_courses_count


def counter_cursers_cash(self, date_start, date_end, pizzeria):
    driver_courses = (Orders.objects.filter(type_of_order="3").filter(
        status="4").filter(date__gte=date_start).filter(
            date__lte=date_end).filter(workplace_id=pizzeria).filter(
                driver_id=self).filter(pay_method=1))
    cash = 0
    for order in driver_courses:
        cash += order.order_total_price2()
    cash = round(cash, 2)
    return cash


def counter_cursers_card(self, date_start, date_end, pizzeria):
    driver_courses = (Orders.objects.filter(type_of_order="3").filter(
        status="4").filter(date__gte=date_start).filter(
            date__lte=date_end).filter(workplace_id=pizzeria).filter(
                driver_id=self).filter(pay_method=2))
    card = 0
    for order in driver_courses:
        card += order.order_total_price2()
    card = round(card, 2)
    return card


def counter_cursers_card_counter(self, date_start, date_end, pizzeria):
    driver_courses_card_count = (Orders.objects.filter(
        type_of_order="3").filter(status="4").filter(
            date__gte=date_start).filter(date__lte=date_end).filter(
                workplace_id=pizzeria).filter(driver_id=self).filter(
                    pay_method=2).count)

    return driver_courses_card_count


def counter_cursers_online_1(self, date_start, date_end, pizzeria):
    driver_courses = (Orders.objects.filter(type_of_order="3").filter(
        status="4").filter(date__gte=date_start).filter(
            date__lte=date_end).filter(workplace_id=pizzeria).filter(
                driver_id=self).filter(pay_method=3))
    card = 0
    for order in driver_courses:
        card += order.order_total_price2()
    card = round(card, 2)
    return card


def counter_cursers_online_1_count(self, date_start, date_end, pizzeria):
    driver_courses = (Orders.objects.filter(type_of_order="3").filter(
        status="4").filter(date__gte=date_start).filter(
            date__lte=date_end).filter(workplace_id=pizzeria).filter(
                driver_id=self).filter(pay_method=3))
    count = len(driver_courses)
    return count


def counter_cursers_online_2(self, date_start, date_end, pizzeria):
    driver_courses = (Orders.objects.filter(type_of_order="3").filter(
        status="4").filter(date__gte=date_start).filter(
            date__lte=date_end).filter(workplace_id=pizzeria).filter(
                driver_id=self).filter(pay_method=4))
    card = 0
    for order in driver_courses:
        card += order.order_total_price2()
    card = round(card, 2)
    return card


def counter_cursers_online_2_count(self, date_start, date_end, pizzeria):
    driver_courses = (Orders.objects.filter(type_of_order="3").filter(
        status="4").filter(date__gte=date_start).filter(
            date__lte=date_end).filter(workplace_id=pizzeria).filter(
                driver_id=self).filter(pay_method=4))
    count = len(driver_courses)
    return count


def counter_cursers_online_3(self, date_start, date_end, pizzeria):
    driver_courses = (Orders.objects.filter(type_of_order="3").filter(
        status="4").filter(date__gte=date_start).filter(
            date__lte=date_end).filter(workplace_id=pizzeria).filter(
                driver_id=self).filter(pay_method=5))
    card = 0
    for order in driver_courses:
        card += order.order_total_price2()
    card = round(card, 2)
    return card


def counter_cursers_online_3_count(self, date_start, date_end, pizzeria):
    driver_courses = (Orders.objects.filter(type_of_order="3").filter(
        status="4").filter(date__gte=date_start).filter(
            date__lte=date_end).filter(workplace_id=pizzeria).filter(
                driver_id=self).filter(pay_method=5))
    count = len(driver_courses)
    return count


def counter_cursers_online_4(self, date_start, date_end, pizzeria):
    driver_courses = (Orders.objects.filter(type_of_order="3").filter(
        status="4").filter(date__gte=date_start).filter(
            date__lte=date_end).filter(workplace_id=pizzeria).filter(
                driver_id=self).filter(pay_method=6))
    card = 0
    for order in driver_courses:
        card += order.order_total_price2()
    card = round(card, 2)
    return card


def counter_cursers_online_4_count(self, date_start, date_end, pizzeria):
    driver_courses = (Orders.objects.filter(type_of_order="3").filter(
        status="4").filter(date__gte=date_start).filter(
            date__lte=date_end).filter(workplace_id=pizzeria).filter(
                driver_id=self).filter(pay_method=6))
    count = len(driver_courses)
    return count


def counter_cursers_online_5(self, date_start, date_end, pizzeria):
    driver_courses = (Orders.objects.filter(type_of_order="3").filter(
        status="4").filter(date__gte=date_start).filter(
            date__lte=date_end).filter(workplace_id=pizzeria).filter(
                driver_id=self).filter(pay_method=7))
    card = 0
    for order in driver_courses:
        card += order.order_total_price2()
    card = round(card, 2)
    return card


def counter_cursers_online_5_count(self, date_start, date_end, pizzeria):
    driver_courses = (Orders.objects.filter(type_of_order="3").filter(
        status="4").filter(date__gte=date_start).filter(
            date__lte=date_end).filter(workplace_id=pizzeria).filter(
                driver_id=self).filter(pay_method=7))
    count = len(driver_courses)
    return count


def download(request, path):
    file_path = os.path.join(settings.MEDIA_ROOT, path)
    if os.path.exists(file_path):
        with open(file_path, "rb") as fh:
            response = HttpResponse(fh.read(),
                                    content_type="application/vnd.ms-excel")
            response[
                "Content-Disposition"] = "inline; filename=" + os.path.basename(
                    file_path)
            return response
    raise Http404


def counter_active_orders_in_car_count(self, date_start, date_end, pizzeria):
    driver_active_order = (Orders.objects.filter(type_of_order="3").filter(
        status="3").filter(date__gte=date_start).filter(
            date__lte=date_end).filter(workplace_id=pizzeria).filter(
                driver_id=self)).count()
    return driver_active_order


def set_code_number():
    cat_list = [1, 2]
    category = Category.objects.filter(category_number__in=cat_list)
    # category = Category.objects.all()
    products = Products.objects.filter(category__in=category)
    for el in products:
        el.code_number = (str(el.category.category_number) +
                          str(el.pizza_number) +
                          str(int(el.product_size.id) + 2))
        el.save()


def delivery_avg(pizzeria):
    orders = (Orders.objects.filter(status=4).filter(type_of_order=3).filter(
        workplace_id=pizzeria))
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
            x = timedelta(
                hours=order.time_start.hour,
                minutes=order.time_start.minute,
            )
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
                    delivery_time_group_10_12.append(
                        round(int(time_delivery / 60), 0))
                    # delivery_time_group_10_12.append(time_order)

            if group_14 > x > group_12:
                minutes = round(int(time_delivery / 60), 0)
                if minutes > 10:
                    delivery_time_group_12_14.append(
                        round(int(time_delivery / 60), 0))
                    # delivery_time_group_12_14.append(time_order)

            if group_16 > x > group_14:
                minutes = round(int(time_delivery / 60), 0)
                if minutes > 10:
                    delivery_time_group_14_16.append(
                        round(int(time_delivery / 60), 0))
                    # delivery_time_group_14_16.append(time_order)

            if group_18 > x > group_16:
                minutes = round(int(time_delivery / 60), 0)
                if minutes > 10:
                    delivery_time_group_16_18.append(
                        round(int(time_delivery / 60), 0))
                    # delivery_time_group_16_18.append(time_order)

            if group_20 > x > group_18:
                minutes = round(int(time_delivery / 60), 0)
                if minutes > 10:
                    delivery_time_group_18_20.append(
                        round(int(time_delivery / 60), 0))
                    # delivery_time_group_18_20.append(time_order)

            if group_22 > x > group_20:
                minutes = round(int(time_delivery / 60), 0)
                if minutes > 10:
                    delivery_time_group_20_22.append(
                        round(int(time_delivery / 60), 0))
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
        ))

    df = pd.DataFrame(order_details)

    for el in orders:
        if el != None:
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
    if len(orders) > 0:
        d1 = df_orders(orders)
        # d1 = pd.read_excel(os.path.join(settings.MEDIA_ROOT, "orders.xlsx"))
        # orders_date = d1["date"][0:3]
        # print(orders_date)
        # orders_total_price = d1["Total_price"]
        d1 = d1[["date", "Total_price"]]
        d1 = d1.groupby(pd.Grouper("date")).sum()
        d = d1.plot.bar(
            lw=2,
            colormap="jet",
            rot=45,
            fontsize=12,
        )
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
        d3 = "Brak wyników"
        return d3


def diagram_income_by_hours(orders):
    import matplotlib.pyplot as plt

    plt.rcParams["figure.figsize"] = (20, 8)
    orders = orders
    print(len(orders))
    if len(orders) > 0:
        d1 = df_orders(orders)
        orders_date = d1["date"]
        orders_total_price = d1["Total_price"]
        d1 = d1[["date", "Total_price"]]
        d1 = d1.groupby(pd.Grouper("date")).sum()
        d = d1.plot.bar(
            lw=2,
            colormap="jet",
            rot=45,
            fontsize=13,
        )
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
        d3 = "Brak wyników"
        return d3


def orders_by_hours(orders):
    import matplotlib.pyplot as plt

    plt.rcParams["figure.figsize"] = (20, 8)
    orders = orders
    if len(orders) > 0:
        group_10_11 = []
        group_11_12 = []
        group_12_13 = []
        group_13_14 = []
        group_14_15 = []
        group_15_16 = []
        group_16_17 = []
        group_17_18 = []
        group_18_19 = []
        group_19_20 = []
        group_20_21 = []
        group_21_22 = []
        group_10 = timedelta(hours=10, minutes=00)
        group_11 = timedelta(hours=11, minutes=00)
        group_12 = timedelta(hours=12, minutes=00)
        group_13 = timedelta(hours=13, minutes=00)
        group_14 = timedelta(hours=14, minutes=00)
        group_15 = timedelta(hours=15, minutes=00)
        group_16 = timedelta(hours=16, minutes=00)
        group_17 = timedelta(hours=17, minutes=00)
        group_18 = timedelta(hours=18, minutes=00)
        group_19 = timedelta(hours=19, minutes=00)
        group_20 = timedelta(hours=20, minutes=00)
        group_21 = timedelta(hours=21, minutes=00)
        group_22 = timedelta(hours=22, minutes=00)
        if len(orders) > 0:
            for order in orders:
                x = timedelta(
                    hours=order.time_start.hour,
                    minutes=order.time_start.minute,
                )
                order_hour = order.time_start.hour
                order_minute = order.time_start.minute
                time_order = str(order_hour) + ":" + str(order_minute)

                if group_11 > x > group_10:
                    group_10_11.append(order)

                if group_12 > x > group_11:
                    group_11_12.append(order)

                if group_13 > x > group_12:
                    group_12_13.append(order)

                if group_14 > x > group_13:
                    group_13_14.append(order)

                if group_15 > x > group_14:
                    group_14_15.append(order)

                if group_16 > x > group_15:
                    group_15_16.append(order)

                if group_17 > x > group_16:
                    group_16_17.append(order)

                if group_18 > x > group_17:
                    group_17_18.append(order)

                if group_19 > x > group_18:
                    group_18_19.append(order)

                if group_20 > x > group_19:
                    group_19_20.append(order)

                if group_21 > x > group_20:
                    group_20_21.append(order)

                if group_22 > x > group_21:
                    group_21_22.append(order)

            group_10 = len(group_10_11)
            group_11 = len(group_11_12)
            group_12 = len(group_12_13)
            group_13 = len(group_13_14)
            group_14 = len(group_14_15)
            group_15 = len(group_15_16)
            group_16 = len(group_15_16)
            group_17 = len(group_17_18)
            group_18 = len(group_18_19)
            group_19 = len(group_19_20)
            group_20 = len(group_20_21)
            group_21 = len(group_21_22)
            order_by_hour = {
                "10-11": group_10,
                "11-12": group_11,
                "12-13": group_12,
                "13-14": group_13,
                "14-15": group_14,
                "15-16": group_15,
                "16-17": group_16,
                "17-18": group_17,
                "18-19": group_18,
                "19-20": group_19,
                "20-21": group_20,
                "21-22": group_21,
            }
            # print(order_by_hour)
            keys = []
            values = []
            for key, value in order_by_hour.items():
                keys.append(key)
                values.append(value)
            x = keys
            y = values
            data_dict = {"Godziny": keys, "Zamówienia": values}
            dframe = pd.DataFrame(data_dict)
            d3 = dframe.plot.bar(x="Godziny",
                                 y="Zamówienia",
                                 rot=0,
                                 fontsize=13)
            d3.set_xlabel("Grupy godzinowe", fontsize=38)
            d3.set_ylabel("Zamówienia", fontsize=38)
            d3.figure.suptitle("Wykres godzinowy", fontsize=38)
            plt.savefig("pizzeria/static/media/orders_by_hours.png")
            plt.close("all")
            return d3
    else:
        d3 = "Brak wyników"
        return d3


def the_best_pizza(pos):
    import matplotlib.pyplot as plt

    plt.style.reload_library()
    plt.rcParams["figure.figsize"] = (40, 15)
    pos_list = []
    if len(pos) > 0:
        for el in pos:
            pos_list.append(
                str(el.product_id.product_name) + " - " + str(el.size_id))

        x = pd.Series(pos_list)
        x = x.value_counts(ascending=False)
        d3 = x[0:10]

        # df = pd.DataFrame({"Nazwa": d2.index, "Ilość": d2[0]})
        d3 = d3.plot.barh(
            x="Nazwa",
            width=0.3,
            y="Ilość",
            rot=0,
            fontsize=23,
        )
        d3.set_xlabel("Ilość", fontsize=48)
        # d3.set_ylabel("Pizza", fontsize=48)
        d3.figure.suptitle("10 najlepszych produktów", fontsize=48)

        # plt.show()
        d3.figure.savefig("pizzeria/static/media/the_best_pizza.png")
        plt.close("all")
        return d3
    else:
        d3 = "Brak wyników"
        return d3


def the_poor_pizza(pos):
    import matplotlib.pyplot as plt

    plt.style.reload_library()
    plt.rcParams["figure.figsize"] = (40, 15)
    pos_list = []
    if len(pos) > 0:
        for el in pos:
            pos_list.append(
                str(el.product_id.product_name) + " - " + str(el.size_id))

        x = pd.Series(pos_list)
        x = x.value_counts(ascending=False)
        d3 = x[-10:]

        # df = pd.DataFrame({"Nazwa": d2.index, "Ilość": d2[0]})
        d3 = d3.plot.barh(
            x="Nazwa",
            width=0.3,
            y="Ilość",
            rot=0,
            fontsize=23,
        )
        d3.set_xlabel("Ilość", fontsize=48)
        d3.step(x=1, y=1)
        # d3.set_ylabel("Pizza", fontsize=48)
        d3.figure.suptitle("10 najgorszych produktów", fontsize=48)
        d3.figure.savefig("pizzeria/static/media/the_poor_pizza.png")
        plt.close("all")
        return d3
    else:
        d3 = "Brak wyników"
        return d3


def send_sms(number, message):
    client = SmsApiPlClient(access_token=os.environ.get("SMS_TOKEN"), )

    try:
        send_results = client.sms.send(to=number, message=message)

        for result in send_results:
            print(result.id, result.points, result.error)
    except:
        pass


def saldo_sms():
    try:
        client = SmsApiPlClient(access_token=os.environ.get("SMS_TOKEN"), )
        r = client.account.balance()
        return r.points
    except:
        return 0


def new_number(pizzeria_id):
    year = datetime.now().year
    month = datetime.now().month
    day = datetime.now().day

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


def google_dist(orders):
    import urllib

    google_key = os.environ.get("GOOGLE_MAPS")
    order_finish = orders
    categorys = Category.objects.all()
    positions_on_order = PositionOrder.objects.filter(order_id=order_finish.id)
    pizzeria = str(order_finish.workplace_id.address.street)
    pizzeria = pizzeria.replace(" ", "")
    pizzeria = pizzeria.replace("ż", "z")
    pizzeria = pizzeria.replace("ń", "n")
    pizzeria = pizzeria.encode("utf-8").strip()
    paid_button = True
    if order_finish.address != "" and order_finish.address != None:
        address = str(order_finish.address.street)
        address = address.replace(" ", "+")
        address = address.replace("ó", "o")
        address = address.replace("ż", "z")
        address = address.replace("ź", "z")
        address = address.replace("ć", "c")
        address = address.replace("Ć", "C")
        address = address.replace("ś", "s")
        address = address.replace("Ś", "S")
        address = address.replace("ź", "z")
        address = address.replace("ń", "n")
        address = address.replace("Ń", "N")
        address = address.replace("ę", "e")
        address = address.replace("ą", "a")
        address = address.replace("ł", "l")
        address = address.replace("Ł", "L")
        address = address.replace("Ż", "Z")
        address = address.replace("Ź", "Z")
        url_maps_2 = ("https://www.google.com/maps/embed/v1/place?key=" +
                      str(google_key) + "&q=" + str(address) + ",krakow")
        address = address.encode("utf-8").strip()
        # geoloc=
        url_maps = (
            "https://maps.googleapis.com/maps/api/distancematrix/json?units=kilometers&origins="
            + str(pizzeria) + ",krakow&destinations=" + str(address) +
            ",krakow&key=" + str(google_key))
        result = json.load(urllib.request.urlopen(url_maps, context=None))
        try:
            driving_time = result["rows"][0]["elements"][0]["duration"]["text"]
        except:
            driving_time = "Błąd adresu"
        try:
            distance = result["rows"][0]["elements"][0]["distance"]["text"]
        except:
            distance = "Błąd adresu"
        ctx = {
            "url_maps_2": url_maps_2,
            "address": address,
            "distance": distance,
            "driving_time": driving_time,
            "google_key": google_key,
            "order": order_finish,
            "positions_on_order": positions_on_order,
            "categorys": categorys,
            "paid_button": paid_button,
        }
    else:

        ctx = {
            "google_key": google_key,
            "order": order_finish,
            "positions_on_order": positions_on_order,
            "categorys": categorys,
            "paid_button": paid_button,
        }

    return ctx


def local_status(request, form, worker, warning, saldo, pizzerias):
    pizzeria_active = get_pizzeria_session(request)
    income = Orders.objects.filter(workplace_id=pizzeria_active)
    expenses = Purchases.objects.filter(work_place=pizzeria_active)
    total = 0
    cards = 0
    for el in income:
        if el.pay_method == 1:
            total += el.income_total
        else:
            cards += el.income_total
    for el in expenses:
        if el.pay_method == 1:
            total -= el.price
        else:
            cards -= el.price
        total -= el.price
    total = round(total, 2)
    cards = round(cards, 2)

    try:
        date_start = request.session["date_start"]
        date_end = request.session["date_end"]
        # print("jest sesja")
        # print(date_start)

    except:
        # date_start = date.today()
        date_start = datetime.now().date()
        date_start = json.dumps(date_start,
                                sort_keys=True,
                                indent=1,
                                cls=DjangoJSONEncoder)

        request.session["date_start"] = date_start

        # date_end = date.today()
        date_end = datetime.now().date()
        request.session["date_start"] = date_start
        date_end = json.dumps(date_end,
                              sort_keys=True,
                              indent=1,
                              cls=DjangoJSONEncoder)
        request.session["date_end"] = date_end
        # print("brak sesja")
        # print(date_start)
        # print(date_end)

    date_start = str(date_start)
    date_start = date_start.replace('"', "")
    date_end = str(date_end)
    date_end = date_end.replace('"', "")

    today_now = f"{datetime.now().date()}"
    if date_start == date_end and date_end == today_now:
        today_now = f'"{datetime.now().date()}"'
        if str(date_start) != str(today_now):
            date_start = datetime.now().date()
            date_end = datetime.now().date()
            setdate = f"Dzisiaj: {date_start}"
            setdate = setdate.replace('"', " ")

        else:
            setdate = f"Dzisiaj: {date_start}"
            setdate = setdate.replace('"', " ")
    else:
        setdate = f"{date_start} - {date_end}"
        setdate = setdate.replace('"', " ")

    total_orders = (Orders.objects.filter(date__gte=date_start).filter(
        date__lte=date_end).filter(workplace_id=pizzeria_active).count)
    total_orders_done = (Orders.objects.filter(date__gte=date_start).filter(
        date__lte=date_end).filter(workplace_id=pizzeria_active).filter(
            status=4).count)
    income = (Orders.objects.filter(workplace_id=pizzeria_active).filter(
        date__gte=date_start).filter(date__lte=date_end).filter(status=4))
    income_trips = (Orders.objects.filter(workplace_id=pizzeria_active).filter(
        date__gte=date_start).filter(date__lte=date_end).filter(
            type_of_order=3).filter(status=4).count)
    income_online_1 = (Orders.objects.filter(
        workplace_id=pizzeria_active).filter(date__gte=date_start).filter(
            date__lte=date_end).filter(pay_method=3).filter(status=4).count())

    income_online_2 = (Orders.objects.filter(
        workplace_id=pizzeria_active).filter(date__gte=date_start).filter(
            date__lte=date_end).filter(pay_method=4).filter(status=4).count())
    income_online_3 = (Orders.objects.filter(
        workplace_id=pizzeria_active).filter(date__gte=date_start).filter(
            date__lte=date_end).filter(pay_method=5).filter(status=4).count())
    income_online_4 = (Orders.objects.filter(
        workplace_id=pizzeria_active).filter(date__gte=date_start).filter(
            date__lte=date_end).filter(pay_method=6).filter(status=4).count())
    income_online_5 = (Orders.objects.filter(
        workplace_id=pizzeria_active).filter(date__gte=date_start).filter(
            date__lte=date_end).filter(pay_method=7).filter(status=4).count())
    purhases = (Purchases.objects.filter(work_place=pizzeria_active).filter(
        date__gte=date_start).filter(date__lte=date_end))
    income_sum = 0
    purhases_sum = 0
    cash = 0
    cards = 0
    trips = 0
    online_1 = 0
    online_2 = 0
    online_3 = 0
    online_4 = 0
    online_5 = 0
    for el in income:
        income_sum += el.income_total
        income_sum = round(income_sum, 2)

    for el in purhases:
        purhases_sum += el.price

    for el in income:
        if el.pay_method == 1:
            cash += el.income_total
        elif el.pay_method == 2:
            cards += el.income_total
        elif el.pay_method == 3:
            online_1 += el.income_total
        elif el.pay_method == 4:
            online_2 += el.income_total
        elif el.pay_method == 5:
            online_3 += el.income_total
        elif el.pay_method == 6:
            online_4 += el.income_total
        elif el.pay_method == 7:
            online_5 += el.income_total

    for el in purhases:
        if el.pay_method == 1:
            cash -= el.price
        else:
            cards -= el.price
        # total-=el.cost
    cash = round(cash, 2)
    cards = round(cards, 2)

    date_start = str(date_start)
    date_start = date_start.replace('"', "")
    date_end = str(date_end)
    date_end = date_end.replace('"', "")

    orders = (Orders.objects.filter(type_of_order="3").filter(
        status__in=["3", "4"]).filter(date__gte=date_start).filter(
            date__lte=date_end).filter(workplace_id=pizzeria_active))
    # print(orders)

    drivers = []
    for order in orders:
        if order.driver_id not in drivers:
            drivers.append(order.driver_id)

    orders_in_select = [1, 2]
    orders_in_workplace = (Orders.objects.filter(
        type_of_order__in=orders_in_select).filter(status="4").filter(
            date__gte=date_start).filter(date__lte=date_end).filter(
                workplace_id=pizzeria_active))
    cash_in = 0
    cash_in_count = orders_in_workplace.filter(pay_method=1).count()
    card_in = 0
    card_in_count = orders_in_workplace.filter(pay_method=2).count()
    order_in = orders_in_workplace.count()
    online_1_in = 0
    online_1_in_count = orders_in_workplace.filter(pay_method=3).count()
    online_2_in = 0
    online_2_in_count = orders_in_workplace.filter(pay_method=4).count()
    online_3_in = 0
    online_3_in_count = orders_in_workplace.filter(pay_method=5).count()
    online_4_in = 0
    online_4_in_count = orders_in_workplace.filter(pay_method=6).count()
    online_5_in = 0
    online_5_in_count = orders_in_workplace.filter(pay_method=7).count()
    if order_in > 0:
        for el in orders_in_workplace:
            if el.pay_method == 1:
                cash_in += float(el.income_total)
                cash_in = round(cash_in, 2)

            if el.pay_method == 2:
                card_in += float(el.income_total)
                card_in = round(card_in, 2)
            if el.pay_method == 3:
                online_1_in += float(el.income_total)
                online_1_in = round(online_1_in, 2)
            if el.pay_method == 4:
                online_2_in += float(el.income_total)
                online_2_in = round(online_2_in, 2)
            if el.pay_method == 5:
                online_3_in += float(el.income_total)
                online_3_in = round(online_3_in, 2)
            if el.pay_method == 6:
                online_4_in += float(el.income_total)
                online_4_in = round(online_4_in, 2)
            if el.pay_method == 7:
                online_5_in += float(el.income_total)
                online_5_in = round(online_5_in, 2)
    if len(drivers) > 0:
        for driver in drivers:
            driver.counter_cursers = counter_cursers(driver, date_start,
                                                     date_end, pizzeria_active)
            driver.counter_cursers_cash = counter_cursers_cash(
                driver, date_start, date_end, pizzeria_active)
            driver.counter_cursers_card = counter_cursers_card(
                driver, date_start, date_end, pizzeria_active)
            driver.counter_cursers_card_count = counter_cursers_card_counter(
                driver, date_start, date_end, pizzeria_active)
            driver.counter_cursers_online_1 = counter_cursers_online_1(
                driver, date_start, date_end, pizzeria_active)
            driver.counter_cursers_online_1_count = counter_cursers_online_1_count(
                driver, date_start, date_end, pizzeria_active)
            driver.counter_cursers_online_2 = counter_cursers_online_2(
                driver, date_start, date_end, pizzeria_active)
            driver.counter_cursers_online_2_count = counter_cursers_online_2_count(
                driver, date_start, date_end, pizzeria_active)
            driver.counter_cursers_online_3 = counter_cursers_online_3(
                driver, date_start, date_end, pizzeria_active)
            driver.counter_cursers_online_3_count = counter_cursers_online_3_count(
                driver, date_start, date_end, pizzeria_active)
            driver.counter_cursers_online_4 = counter_cursers_online_4(
                driver, date_start, date_end, pizzeria_active)
            driver.counter_cursers_online_4_count = counter_cursers_online_4_count(
                driver, date_start, date_end, pizzeria_active)
            driver.counter_cursers_online_5 = counter_cursers_online_5(
                driver, date_start, date_end, pizzeria_active)
            driver.counter_cursers_online_5_count = counter_cursers_online_5_count(
                driver, date_start, date_end, pizzeria_active)
            driver.counter_active_orders_in_car_count = counter_active_orders_in_car_count(
                driver, date_start, date_end, pizzeria_active)
            driver.save()
            no_courses = False
    else:
        no_courses = True

    date_start = json.dumps(date_start,
                            sort_keys=True,
                            indent=1,
                            cls=DjangoJSONEncoder)
    request.session["date_start"] = date_start

    date_end = json.dumps(date_end,
                          sort_keys=True,
                          indent=1,
                          cls=DjangoJSONEncoder)
    request.session["date_end"] = date_end

    pizzeria_active = get_pizzeria_session(request)
    avg_minutes = delivery_avg(pizzeria_active)
    ctx = {
        "total_orders_done": total_orders_done,
        "cash_in_count": cash_in_count,
        "card_in_count": card_in_count,
        "online_1_in_count": online_1_in_count,
        "online_2_in_count": online_2_in_count,
        "online_3_in_count": online_3_in_count,
        "online_4_in_count": online_4_in_count,
        "online_5_in_count": online_5_in_count,
        "warning": warning,
        "saldo": saldo,
        "avg_minutes": avg_minutes,
        "orders_in_workplace": orders_in_workplace,
        "order_in": order_in,
        "cash_in": cash_in,
        "card_in": card_in,
        "online_1_in": online_1_in,
        "online_2_in": online_2_in,
        "online_3_in": online_3_in,
        "online_4_in": online_4_in,
        "online_5_in": online_5_in,
        "no_courses": no_courses,
        "drivers": drivers,
        "worker": worker,
        "cash": cash,
        "income_sum": income_sum,
        "purhases_sum": purhases_sum,
        "trips": trips,
        "income_trips": income_trips,
        "total_orders": total_orders,
        "income_online_1": income_online_1,
        "income_online_2": income_online_2,
        "income_online_3": income_online_3,
        "income_online_4": income_online_4,
        "income_online_5": income_online_5,
        "cards": cards,
        "online_1": round(online_1, 2),
        "online_2": round(online_2, 2),
        "online_3": round(online_3, 2),
        "online_4": round(online_4, 2),
        "online_5": round(online_5, 2),
        "setdate": setdate,
        "date_start": date_start,
        "pizzerias": pizzerias,
        "form": form,
        "pizzeria_active": pizzeria_active,
    }
    return ctx
