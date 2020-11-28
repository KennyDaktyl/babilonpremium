from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.template.response import TemplateResponse
from django.shortcuts import render, redirect

from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.core.exceptions import ObjectDoesNotExist

# Generyki i szablony
from django.views import View
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from django.core.files.storage import FileSystemStorage
from django.template.loader import render_to_string
from weasyprint import HTML

from django.db.models import Q
from django.db.models import Count

from django.core.paginator import Paginator

import json
from django.http import JsonResponse
from django.core.serializers.json import DjangoJSONEncoder
from django.core import serializers

from babilon_v1.models import *
from babilon_v1.forms import *
from babilon_v1.function import *

import googlemaps
import urllib.request
import json
import os

from django.utils.timezone import localtime

from datetime import datetime, date, timedelta, time
import calendar

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from babilon_v1.statistic import *

# year_now = datetime.now().year
# month_now = datetime.now().month
# day = datetime.now().day
default_time_zoro_local = 20
default_time_zoro_outside = 40

drivers = MyUser.objects.filter(profession=4)
active_drivers(drivers)
# Create your views here.
import pandas as pd


class UserLoginView(View):
    def get(self, request):
        form = LoginForm()
        drivers = MyUser.objects.filter(profession=4)
        active_drivers(drivers)
        return render(request, "user_login.html", context={"form": form})

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            username, password = form.cleaned_data.values()
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                if request.user.profession == 0:
                    url = "/local_status/"
                    return redirect(url)
                if request.user.profession == 1:
                    url = "/local_status/"
                    return redirect(url)
                if request.user.profession == 4 and request.user.active == True:
                    url = "/driver_mobile_view/" + str(request.user.id)
                    return redirect(url)
                else:
                    error_info = "Dzisiaj nie pracujesz"
                    ctx = {"error_info": error_info}
                    return render(request, "user_login.html", ctx)
            else:
                error_info = "Błąd logowania"
                ctx = {"error_info": error_info}
                return render(request, "user_login.html", ctx)
        return render(request, "user_login.html", context={"form": form})


@login_required
def User_Logout(request):
    logout(request)

    return redirect("/")


@method_decorator(login_required, name="dispatch")
class LocalStatusView(PermissionRequiredMixin, View):
    permission_required = "babilon_v1.view_myuser"

    def get(self, request):
        saldo = float(saldo_sms())
        if saldo < 10.0:
            warning = True
        else:
            warning = False
        year_now = datetime.now().year
        month_now = datetime.now().month
        day = datetime.now().day
        worker = request.user
        form = SetDataStatsForm()
        work_place = worker.work_place.all()
        pizzerias = WorkPlace.objects.all()

        if worker.profession == 0:

            ctx = local_status(request, form, worker, warning, saldo,
                               pizzerias)

            return TemplateResponse(request, "local_status.html", ctx)

        if worker.profession == 1:
            ctx = local_status(request, form, worker, warning, saldo,
                               pizzerias)
            return TemplateResponse(request, "local_status.html", ctx)
        if worker.profession == 2:
            ctx = local_status(request, form, worker, warning, saldo,
                               pizzerias)
            return TemplateResponse(request, "barman_start.html")
        if worker.profession == 4 and worker:

            return TemplateResponse(request, "driver_start.html")

    def post(self, request):
        worker = request.user
        form = SetDataStatsForm(request.POST)
        formT = SetTodayStatsForm(request.POST)
        formM = SetMonthStatsForm(request.POST)

        if form.is_valid():
            date_start = form.cleaned_data["date_start"]
            date_start = json.dumps(date_start,
                                    sort_keys=True,
                                    indent=1,
                                    cls=DjangoJSONEncoder)
            request.session["date_start"] = date_start

            date_end = form.cleaned_data["date_end"]
            date_end = json.dumps(date_end,
                                  sort_keys=True,
                                  indent=1,
                                  cls=DjangoJSONEncoder)
            request.session["date_end"] = date_end
            date_end = request.session["date_end"]
            setdate = date_start + " - " + date_end
            try:
                pizzeria_set_id = request.session["pizzeria"]
                if pizzeria_set_id:
                    pizzeria_active = WorkPlace.objects.get(pk=pizzeria_set_id)
                    ctx = {
                        "worker": worker,
                        "pizzeria_active": pizzeria_active,
                        "setdate": setdate,
                        "date_start": date_start,
                        "date_end": date_end,
                    }
                    return TemplateResponse(request, "local_status.html", ctx)
                else:
                    pizzeria_active = WorkPlace.objects.first()
                    pizzeria_active_id = pizzeria_active.id
                    request.session["pizzeria"] = pizzeria_active_id
                    ctx = {
                        "worker": worker,
                        "pizzeria_active": pizzeria_active,
                        "setdate": setdate,
                        "date_start": date_start,
                        "date_end": date_end,
                    }
                return TemplateResponse(request, "local_status.html", ctx)
            except:

                pizzeria_active = WorkPlace.objects.first()
                pizzeria_active_id = pizzeria_active.id
                request.session["pizzeria"] = pizzeria_active_id
                ctx = {
                    "worker": worker,
                    "pizzeria_active": pizzeria_active,
                    "setdate": setdate,
                    "date_start": date_start,
                    "date_end": date_end,
                }
                return TemplateResponse(request, "local_status.html", ctx)
        else:
            pizzeria = request.POST.get("pizzeria")
            form = SetDataStatsForm()
            if pizzeria:
                request.session["pizzeria"] = pizzeria
                pizzeria_set_id = request.session["pizzeria"]
                pizzeria_active = WorkPlace.objects.get(pk=pizzeria_set_id)
                ctx = {
                    "form": form,
                    "worker": worker,
                    "pizzeria_active": pizzeria_active,
                }
                return TemplateResponse(request, "local_status.html", ctx)

            else:
                pizzeria_set_id = request.session["pizzeria"]
                pizzeria_active = WorkPlace.objects.get(pk=pizzeria_set_id)

                ctx = {
                    "form": form,
                    "worker": worker,
                    "pizzeria_active": pizzeria_active,
                }
                return TemplateResponse(request, "local_status.html", ctx)


# moduł dodawania produktów
@method_decorator(login_required, name="dispatch")
class AddToppView(PermissionRequiredMixin, View):
    permission_required = "babilon_v1.add_products"

    def get(self, request):
        form = AddToppForm()
        type_of_ingredient = INGREDIENT_TYPE_FORM
        type_of_ingredient_list = []
        for el in type_of_ingredient:
            type_of_ingredient_list.append(el[0])
        topps = Products.objects.filter(pizza_topp=True).order_by(
            "type_of_ingredient", "product_name")
        ctx = {
            "form": form,
            "topps": topps,
            "type_of_ingredient_list": type_of_ingredient_list,
        }
        return render(request, "add_topp.html", ctx)

    def post(self, request):
        form = AddToppForm(request.POST)

        if "is_active" in request.POST:
            product_id = request.POST.get("product_id")
            product = Products.objects.get(pk=product_id)
            if product.is_active == True:
                product.is_active = False
            else:
                product.is_active = True
            product.save()
            return redirect("/add_topp/")
        if form.is_valid():
            topp_name = form.cleaned_data["topp_name"]
            type_of_ingredient = form.cleaned_data["type_of_ingredient"]
            new_topp = Products.objects.create(
                product_name=topp_name,
                type_of_ingredient=type_of_ingredient,
                pizza_topp=True,
            )
            return redirect("/add_topp/")
        return redirect("/add_topp/")


@method_decorator(login_required, name="dispatch")
class SetToppsPriceBySize(PermissionRequiredMixin, UpdateView):
    permission_required = "babilon_v1.add_products"
    model = ProductSize
    fields = [
        "vege_topps_price",
        "beef_topps_price",
        "cheese_topps_price",
        "extra_topps_price",
        "extra_1_topps_price",
        "extra_2_topps_price",
        "extra_3_topps_price",
        "extra_4_topps_price",
    ]
    template_name_suffix = "_update_form"
    success_url = "/set_topp_price_by_size/"


@method_decorator(login_required, name="dispatch")
class SetToppPriceBySize(PermissionRequiredMixin, View):
    permission_required = "babilon_v1.add_products"

    def get(self, request):
        vege_topps = Products.objects.filter(type_of_ingredient=1)
        beef_topps = Products.objects.filter(type_of_ingredient=2)
        cheese_topps = Products.objects.filter(type_of_ingredient=3)
        extra_topps_price = Products.objects.filter(type_of_ingredient=5)
        extra_1_topps_price = Products.objects.filter(type_of_ingredient=6)
        extra_2_topps_price = Products.objects.filter(type_of_ingredient=7)
        extra_3_topps_price = Products.objects.filter(type_of_ingredient=8)
        extra_4_topps_price = Products.objects.filter(type_of_ingredient=9)
        pizza_sizes = ProductSize.objects.filter(pizza=True)
        ctx = {
            "pizza_sizes": pizza_sizes,
            "vege_topps": vege_topps,
            "beef_topps": beef_topps,
            "cheese_topps": cheese_topps,
            "extra_topps_price": extra_topps_price,
            "extra_1_topps_price": extra_1_topps_price,
            "extra_2_topps_price": extra_2_topps_price,
            "extra_3_topps_price": extra_3_topps_price,
            "extra_4_topps_price": extra_4_topps_price,
        }
        return render(request, "set_topp_price_by_size.html", ctx)

    def post(self, request):
        form = AddToppForm(request.POST)

        if form.is_valid():
            topp_name = form.cleaned_data["topp_name"]
            type_of_ingredient = form.cleaned_data["type_of_ingredient"]
            new_topp = Products.objects.create(
                product_name=topp_name,
                type_of_ingredient=type_of_ingredient,
                pizza_topp=True,
            )
            return TemplateResponse(request, "local_status.html")


# moduł dodawania produktów
@method_decorator(login_required, name="dispatch")
class AddSauceView(PermissionRequiredMixin, View):
    permission_required = "babilon_v1.add_products"

    def get(self, request):
        form = AddSauceForm()
        lista = [6, 7]
        sauces = Products.objects.filter(
            type_of_ingredient__in=lista).order_by("product_name")
        ctx = {"form": form, "sauces": sauces}
        return render(request, "add_sauce.html", ctx)

    def post(self, request):
        form = AddSauceForm(request.POST)
        if "is_active" in request.POST:
            product_id = request.POST.get("product_id")
            product = Products.objects.get(pk=product_id)
            if product.is_active == True:
                product.is_active = False
            else:
                product.is_active = True
            product.save()
            return redirect("/add_sauce/")
        if form.is_valid():
            sauce_type = form.cleaned_data["sauce_type"]
            sauce_name = form.cleaned_data["sauce_name"]
            price = form.cleaned_data["price"]

            new_sauce = Products()
            new_sauce.product_name = sauce_name
            new_sauce.type_of_ingredient = sauce_type
            if price != None:
                new_sauce.price = price
            else:
                new_sauce.price = 0.00
            new_sauce.save()

            return redirect("/add_sauce/")
        else:
            return redirect("/add_sauce/")


@method_decorator(login_required, name="dispatch")
class AddPizzaView(PermissionRequiredMixin, View):
    permission_required = "babilon_v1.add_products"

    def get(self, request):
        form = AddPizzaForm()
        category = Category.objects.filter(category_name="Pizza")
        pizzas = Products.objects.filter(category__in=category)
        pizza_sizes = ProductSize.objects.filter(pizza=True)
        ctx = {
            "form": form,
            "pizzas": pizzas,
            "pizza_sizes": pizza_sizes,
        }
        return render(request, "add_pizza.html", ctx)

    def post(self, request):
        form = AddPizzaForm(request.POST)

        if "is_active" in request.POST:
            pizza_id = request.POST.get("pizza_id")
            pizza = Products.objects.get(pk=pizza_id)
            if pizza.is_active == True:
                pizza.is_active = False
            else:
                pizza.is_active = True
            pizza.save()
            return redirect("/add_pizza/")

        if form.is_valid():
            pizza_number = form.cleaned_data["pizza_number"]
            pizza_name = form.cleaned_data["pizza_name"]
            toppings = form.cleaned_data["toppings"]
            price_1 = form.cleaned_data["price_1"]
            price_2 = form.cleaned_data["price_2"]
            price_3 = form.cleaned_data["price_3"]
            pizza_freestyle = form.cleaned_data["pizza_freestyle"]
            price_list = [price_1, price_2, price_3]
            pizza_sizes = ProductSize.objects.filter(pizza=True)
            category = Category.objects.get(category_name="Pizza")

            i = 0
            for size in pizza_sizes:
                new_pizza = Products()
                new_pizza.product_size = size
                new_pizza.pizza_number = pizza_number
                new_pizza.product_name = pizza_name
                new_pizza.price = price_list[i]
                new_pizza.category = category
                new_pizza.is_pizza_freestyle = pizza_freestyle
                new_pizza.code_number = (
                    str(new_pizza.category.category_number) +
                    str(pizza_number) +
                    str(int(new_pizza.product_size.id) + 2))
                new_pizza.save()
                for topp in toppings:
                    new_pizza.toppings.add(topp)
                    new_pizza.save()
                new_pizza.code_number = (
                    str(new_pizza.category.category_number) +
                    str(new_pizza.pizza_number) +
                    str(int(new_pizza.product_size.id) + 2))
                new_pizza.save()
                i += 1
            return redirect("/add_pizza/")
        else:
            return redirect("/add_pizza/")


@method_decorator(login_required, name="dispatch")
class AddPizzaPremiumView(PermissionRequiredMixin, View):
    permission_required = "babilon_v1.add_products"

    def get(self, request):
        form = AddPizzaForm()
        category = Category.objects.filter(category_name="Pizza premium")
        pizzas = Products.objects.filter(category__in=category)
        pizza_sizes = ProductSize.objects.filter(pizza=True)
        ctx = {
            "form": form,
            "pizzas": pizzas,
            "pizza_sizes": pizza_sizes,
        }
        return render(request, "add_pizza.html", ctx)

    def post(self, request):
        form = AddPizzaForm(request.POST)

        if "is_active" in request.POST:
            pizza_id = request.POST.get("pizza_id")
            pizza = Products.objects.get(pk=pizza_id)
            if pizza.is_active == True:
                pizza.is_active = False
            else:
                pizza.is_active = True
            pizza.save()
            return redirect("/add_pizza_premium/")

        if form.is_valid():
            pizza_number = form.cleaned_data["pizza_number"]
            pizza_name = form.cleaned_data["pizza_name"]
            toppings = form.cleaned_data["toppings"]
            price_1 = form.cleaned_data["price_1"]
            price_2 = form.cleaned_data["price_2"]
            price_3 = form.cleaned_data["price_3"]
            pizza_freestyle = form.cleaned_data["pizza_freestyle"]
            price_list = [price_1, price_2, price_3]
            pizza_sizes = ProductSize.objects.filter(pizza=True)
            category = Category.objects.get(category_name="Pizza premium")

            i = 0
            for size in pizza_sizes:
                new_pizza = Products()
                new_pizza.product_size = size
                new_pizza.pizza_number = pizza_number
                new_pizza.product_name = pizza_name
                new_pizza.price = price_list[i]
                new_pizza.category = category
                new_pizza.is_pizza_freestyle = pizza_freestyle
                new_pizza.save()
                for topp in toppings:
                    new_pizza.toppings.add(topp)
                    new_pizza.save()
                new_pizza.code_number = (
                    str(new_pizza.category.category_number) +
                    str(new_pizza.pizza_number) +
                    str(int(new_pizza.product_size.id) + 2))
                new_pizza.save()
                i += 1
            return redirect("/add_pizza_premium/")
        else:
            return redirect("/add_pizza_premium/")


@method_decorator(login_required, name="dispatch")
class AddDishView(PermissionRequiredMixin, View):
    permission_required = "babilon_v1.add_products"

    def get(self, request):
        form = AddDishForm()
        category = Category.objects.filter(category_name="Dania obiadowe")
        dishes = Products.objects.filter(category__in=category)
        ctx = {"form": form, "dishes": dishes}
        return render(request, "add_dish.html", ctx)

    def post(self, request):
        form = AddDishForm(request.POST)

        if "is_active" in request.POST:
            product_id = request.POST.get("product_id")
            product = Products.objects.get(pk=product_id)
            if product.is_active == True:
                product.is_active = False
            else:
                product.is_active = True
            product.save()
            return redirect("/add_dish/")

        if form.is_valid():
            category = form.cleaned_data["category"]
            dish_name = form.cleaned_data["dish_name"]
            toppings = form.cleaned_data["toppings"]
            price = form.cleaned_data["price"]

            category = Category.objects.get(pk=category.id)

            new_dish = Products()
            new_dish.product_name = dish_name
            new_dish.category = category
            new_dish.price = price
            new_dish.save()

            if toppings:
                for topp in toppings:
                    new_dish.toppings.add(topp)
                    new_dish.save()
        return redirect("/local_status/")


@method_decorator(login_required, name="dispatch")
class AddToppForDishView(PermissionRequiredMixin, View):
    permission_required = "babilon_v1.add_products"

    def get(self, request):
        form = AddToppForDishForm()
        dish_topps = Products.objects.filter(dish_topp=True)
        ctx = {
            "form": form,
            "dish_topps": dish_topps,
        }
        return render(request, "add_topp_for_dish.html", ctx)

    def post(self, request):
        form = AddToppForDishForm(request.POST)
        if "is_active" in request.POST:
            product_id = request.POST.get("product_id")
            product = Products.objects.get(pk=product_id)
            if product.is_active == True:
                product.is_active = False
            else:
                product.is_active = True
            product.save()
            return redirect("/add_topp_for_dish/")
        if form.is_valid():
            topp_name = form.cleaned_data["topp_name"]
            price = form.cleaned_data["price"]
            new_topp_dish = Products.objects.create(product_name=topp_name,
                                                    dish_topp=True,
                                                    price=price)
            return redirect("/local_status/")


@method_decorator(login_required, name="dispatch")
class AddCategoryView(PermissionRequiredMixin, View):
    permission_required = "miktel.add_category"

    def get(self, request):
        form = AddCategoryForm()
        categorys = Category.objects.all().order_by("category_number")
        ctx = {
            "form": form,
            "categorys": categorys,
        }
        return render(request, "add_category.html", ctx)

    def post(self, request):
        form = AddCategoryForm(request.POST)
        if form.is_valid():
            category_number = form.cleaned_data["category_number"]
            category_name = form.cleaned_data["category_name"]
            new_category = Category.objects.create(
                category_name=category_name,
                category_number=category_number,
                display=True,
            )
            return redirect("/local_status/")


@method_decorator(login_required, name="dispatch")
class AddDrinkView(PermissionRequiredMixin, View):
    permission_required = "babilon_v1.add_products"

    def get(self, request):
        form = AddDrink()
        lista = [4, 5]
        category = Category.objects.filter(category_number__in=lista)
        drinks = Products.objects.filter(category__in=category)
        ctx = {"form": form, "drinks": drinks}
        return render(request, "add_drinks.html", ctx)

    def post(self, request):
        form = AddDrink(request.POST)
        if "is_active" in request.POST:
            product_id = request.POST.get("product_id")
            product = Products.objects.get(pk=product_id)
            if product.is_active == True:
                product.is_active = False
            else:
                product.is_active = True
            product.save()
            return redirect("/add_drink/")
        if form.is_valid():
            category = form.cleaned_data["category_drink"]
            product_size = form.cleaned_data["size_drink"]
            # product_size=ProductSize.objects.get(pk=size_drink)
            drink_name = form.cleaned_data["drink_name"]
            price = form.cleaned_data["price"]

            drink = Products()
            drink.category = category
            drink.product_name = drink_name
            drink.product_size = product_size
            drink.price = round(float(price), 2)
            drink.save()

            return redirect("/add_drink/")


@method_decorator(login_required, name="dispatch")
class ProductsListView(PermissionRequiredMixin, View):
    permission_required = "miktel.change_products"

    def get(self, request):
        products = Products.objects.all()
        categorys = Category.objects.all()
        sizes = ProductSize.objects.all()
        ctx = {
            "products": products,
            "categorys": categorys,
            "sizes": sizes,
        }
        return render(request, "products_list.html", ctx)

    def post(self, request):
        form = AddCategoryForm(request.POST)
        if form.is_valid():
            category_name = form.cleaned_data["category_name"]
            new_category = Category.objects.create(category_name=category_name,
                                                   display=True)
            return redirect("/products_list/")


@method_decorator(login_required, name="dispatch")
class EditProductProView(PermissionRequiredMixin, UpdateView):
    permission_required = "babilon_v1.change_products"
    model = Products
    fields = "__all__"
    template_name_suffix = "_update_form"
    success_url = "/products_list/"


@method_decorator(login_required, name="dispatch")
class ChangeProductView(PermissionRequiredMixin, UpdateView):
    permission_required = "babilon_v1.change_products"
    model = Products
    fields = [
        "product_name",
        "price",
    ]
    template_name_suffix = "_update_form"
    success_url = "/products_list/"


@method_decorator(login_required, name="dispatch")
class DelProductView(PermissionRequiredMixin, DeleteView):
    permission_required = "babilon_v1.delete_products"
    model = Products
    fields = "__all__"
    template_name_suffix = "_confirm_delete"
    success_url = "/products_list/"


# Kasowanie ustawień sesji
@method_decorator(login_required, name="dispatch")
class DelSessionPizzeriaView(PermissionRequiredMixin, View):
    permission_required = "babilon_v1.view_orders"

    def get(self, request):
        # form = SetLocalStatsForm()
        worker = request.user
        # print(worker)
        work_place = worker.work_place.all()

        # pizzerias = WorkPlace.objects.all()
        ctx = {
            # "worker": worker,
            "work_place": work_place,
            # "form": form,
        }
        return TemplateResponse(request, "set_pizzeria.html", ctx)

    def post(self, request):
        # form = SetLocalStatsForm(request.POST)
        worker = request.user
        if "set_pizzeria" in request.POST:
            pizzeria_id = request.POST.get("workplace")

            pizzeria = WorkPlace.objects.get(pk=pizzeria_id)
            request.session["pizzeria"] = pizzeria.id
            try:
                del request.session["active_orders"]
            except:
                pass
        return redirect("/local_status")

        # if form.is_valid():
        #     pizzeria = form.cleaned_data["pizzeria"]
        #     request.session["pizzeria"] = pizzeria.id
        #     try:
        #         del request.session["active_orders"]
        #     except:
        #         pass

        #     return redirect("/local_status")


@method_decorator(login_required, name="dispatch")
class SetSessionDateView(PermissionRequiredMixin, View):
    permission_required = "babilon_v1.change_orders"

    def get(self, request):
        formD = SetDataStatsForm()
        formT = SetTodayStatsForm()
        formM = SetMonthStatsForm()
        worker = request.user
        ctx = {
            "worker": worker,
            "formD": formD,
            "formT": formT,
            "formM": formM,
        }
        return TemplateResponse(request, "set_time.html", ctx)


@method_decorator(login_required, name="dispatch")
class SetTodayDateView(PermissionRequiredMixin, View):
    permission_required = "babilon_v1.change_orders"

    def post(self, request):

        formT = SetTodayStatsForm(request.POST)
        worker = request.user
        if formT.is_valid():
            today_show = formT.cleaned_data["today_show"]
            date_start = json.dumps(today_show,
                                    sort_keys=True,
                                    indent=1,
                                    cls=DjangoJSONEncoder)
            request.session["date_start"] = date_start
            date_end = json.dumps(today_show,
                                  sort_keys=True,
                                  indent=1,
                                  cls=DjangoJSONEncoder)
            request.session["date_end"] = date_end

            return redirect("/local_status")
        else:
            return redirect("/set_today_date")


@method_decorator(login_required, name="dispatch")
class SetMonthDateView(PermissionRequiredMixin, View):
    permission_required = "babilon_v1.change_orders"

    def post(self, request):
        year = datetime.now().year
        month = datetime.now().month
        day = datetime.now().day
        formM = SetMonthStatsForm(request.POST)
        if formM.is_valid():
            month = formM.cleaned_data["month"]
            date_start = datetime(year=int(year), month=int(month),
                                  day=1).date()

            last_day = date_start.replace(
                day=calendar.monthrange(year, date_start.month)[1])
            date_end = last_day

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
            return redirect("/local_status")
        else:
            return redirect("/set_session_date/")


@method_decorator(login_required, name="dispatch")
class SetPeriodDateView(PermissionRequiredMixin, View):
    permission_required = "babilon_v1.change_orders"

    def post(self, request):
        formD = SetDataStatsForm(request.POST)
        if formD.is_valid():
            date_start = formD.cleaned_data["date_start"]
            date_end = formD.cleaned_data["date_end"]
            if date_end < date_start:
                return redirect("/set_session_date/")
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

            return redirect("/local_status")
        else:
            return redirect("/set_session_date/")


# Kierowcy,pracownicy
@method_decorator(login_required, name="dispatch")
class DriverMobileView(PermissionRequiredMixin, View):
    permission_required = "babilon_v1.view_orders"

    def get(self, request, pk):
        driver = request.user
        year = datetime.now().year
        month = datetime.now().month
        day = datetime.now().day
        work_place = request.user.work_place.all
        for el in request.user.work_place.all():
            work_place_id = el.id
        orders = (Orders.objects.filter(type_of_order=3).filter(
            status=2).filter(date__day=day).filter(date__month=month).filter(
                date__year=year).filter(workplace_id=work_place_id).exclude(
                    address=None))
        orders_length = len(orders)
        google_key = os.environ.get("GOOGLE_MAPS")
        url_address = "https://maps.google.com/?q="

        ctx = {
            "orders_length": orders_length,
            "work_place_id": work_place_id,
            "url_address": url_address,
            "google_key": google_key,
            "orders": orders,
            "driver": driver,
        }
        return render(request, "driver_mobile_view.html", ctx)


@method_decorator(login_required, name="dispatch")
class DriverAccountView(PermissionRequiredMixin, View):
    permission_required = "babilon_v1.view_orders"

    def get(self, request, pk):
        year_now = datetime.now().year
        month_now = datetime.now().month
        today = datetime.now().day
        driver = request.user
        work_place = request.user.work_place.all
        for el in request.user.work_place.all():
            work_place_id = el.id

        my_orders = (Orders.objects.filter(status=3).filter(
            type_of_order=3).filter(driver_id=driver).filter(
                date__day=today).filter(date__month=month).filter(
                    date__year=year).filter(workplace_id=work_place_id))
        orders_length = len(my_orders)
        google_key = os.environ.get("GOOGLE_MAPS")
        url_address = "https://maps.google.com/?q="

        orders = (Orders.objects.filter(status=4).filter(
            type_of_order=3).filter(driver_id=driver).filter(
                date__day=today).filter(date__month=month).filter(
                    date__year=year).filter(workplace_id=work_place_id))
        counter = orders.count()
        counter_cash = orders.filter(pay_method="1").count()
        counter_card = orders.filter(pay_method="2").count()
        cash = 0.00
        card = 0.00
        for el in orders:
            if el.pay_method == 1:
                cash += el.order_total_price2()
            if el.pay_method == 2:
                card += el.order_total_price2()
        cash = round(cash, 2)
        card = round(card, 2)
        ctx = {
            "counter": counter,
            "counter_cash": counter_cash,
            "counter_card": counter_card,
            "cash": cash,
            "card": card,
            "orders_length": orders_length,
            "work_place_id": work_place_id,
            "url_address": url_address,
            "google_key": google_key,
            "my_orders": my_orders,
            "driver": driver,
        }
        return render(request, "driver_account_view.html", ctx)


@method_decorator(login_required, name="dispatch")
class MyOrderOutsideDetailsView(PermissionRequiredMixin, View):
    permission_required = "babilon_v1.view_orders"

    def get(self, request, pk):
        year_now = datetime.now().year
        month_now = datetime.now().month
        today = datetime.now().day
        driver = request.user
        work_place = request.user.work_place.all
        for el in request.user.work_place.all():
            work_place_id = el.id
        order = Orders.objects.get(pk=pk)
        positions_on_order = PositionOrder.objects.filter(order_id=order.id)
        google_key = os.environ.get("GOOGLE_MAPS")
        # print(google_key)
        url_address = ('"https://maps.google.com/?q=' +
                       str(order.address.street) + ',Krakow"')
        ctx = {
            "url_address": url_address,
            "google_key": google_key,
            "order": order,
            "driver": driver,
            "positions_on_order": positions_on_order,
        }
        return render(request, "my_order_details.html", ctx)


@method_decorator(login_required, name="dispatch")
class ConfirmCloseOrderView(PermissionRequiredMixin, View):
    permission_required = "babilon_v1.view_orders"

    def get(self, request, pk):
        driver = request.user
        order = Orders.objects.get(pk=pk)
        ctx = {"order": order, "driver": driver}
        return render(request, "driver_confirm_close_order.html", ctx)

    def post(self, request, pk):
        if "close" in request.POST:
            order = Orders.objects.get(pk=pk)
            order.driver_id = request.user
            order.time_delivery_in = datetime.now().time()
            order.status = 4
            order.save()
            return redirect("driver_account", pk=request.user.id)
        if "card" in request.POST:
            order = Orders.objects.get(pk=pk)
            order.pay_method = 2
            order.save()
            return redirect("confirm_close_order", pk=order.id)
        if "cash" in request.POST:
            order = Orders.objects.get(pk=pk)
            order.pay_method = 1
            order.save()
            return redirect("confirm_close_order", pk=order.id)


@method_decorator(login_required, name="dispatch")
class DriverMobileOrderDetailsView(PermissionRequiredMixin, View):
    permission_required = "babilon_v1.view_orders"

    def get(self, request, pk):
        driver = request.user
        work_place = request.user.work_place.all
        for el in request.user.work_place.all():
            work_place_id = el.id
        order = Orders.objects.get(pk=pk)
        if order.driver_id == None:

            positions_on_order = PositionOrder.objects.filter(
                order_id=order.id)
            google_key = os.environ.get("GOOGLE_MAPS")
            # print(google_key)
            url_address = ('"https://maps.google.com/?q=' +
                           str(order.address.street) + ',Krakow"')
            ctx = {
                "url_address": url_address,
                "google_key": google_key,
                "order": order,
                "driver": driver,
                "positions_on_order": positions_on_order,
            }
            return render(request, "driver_mobile_order_details.html", ctx)
        else:
            return redirect("driver_mobile_view", pk=driver.id)


@method_decorator(login_required, name="dispatch")
class ConfirmGetOrderView(PermissionRequiredMixin, View):
    permission_required = "babilon_v1.view_orders"

    def get(self, request, pk):
        driver = request.user
        order = Orders.objects.get(pk=pk)
        ctx = {"order": order}
        return render(request, "drvier_confirm_get_order.html", ctx)

    def post(self, request, pk):
        order = Orders.objects.get(pk=pk)
        if order.driver_id == None:
            order.driver_id = request.user
            order.start_delivery_time = datetime.now().time()
            order.status = 3
            order.save()
        else:
            pass
        return redirect("driver_mobile_view", pk=request.user.id)


# Sprawdzanie statusu zamówien przez ajax


class DriverClosedOrderView(View):
    def get(self, request, pk):
        pizzeria = WorkPlace.objects.get(pk=pk)
        year = datetime.now().year
        month = datetime.now().month
        day = datetime.now().day
        orders = (Orders.objects.filter(workplace_id=pizzeria).filter(
            status=3).filter(type_of_order=3).filter(date__day=day).filter(
                date__month=month).filter(date__year=year))
        len_orders = len(orders)
        data = {"length": len_orders}

        return JsonResponse(data)


class ForDriversOrderView(View):
    def get(self, request, pk):
        year = datetime.now().year
        month = datetime.now().month
        day = datetime.now().day
        pizzeria = WorkPlace.objects.get(pk=pk)
        orders = (Orders.objects.filter(workplace_id=pizzeria).filter(
            status=2).filter(type_of_order=3).filter(date__day=day).filter(
                date__month=month).filter(date__year=year))
        len_orders = len(orders)
        data = {"length": len_orders}
        return JsonResponse(data)


@method_decorator(login_required, name="dispatch")
class OrdersInPlaceView(PermissionRequiredMixin, View):
    permission_required = "babilon_v1.view_myuser"

    def get(self, request, pk):
        user = request.user
        pizzeria_active = get_pizzeria_session(request)
        pizzeria = WorkPlace.objects.get(pk=pk)

        date_start = request.session["date_start"]

        date_end = request.session["date_end"]

        date_start = json.loads(date_start)
        date_end = json.loads(date_end)

        orders = (Orders.objects.filter(type_of_order__in=[1, 2]).filter(
            date__gte=date_start).filter(date__lte=date_end).filter(
                workplace_id=pizzeria_active))
        orders_cash_count = (Orders.objects.filter(
            type_of_order__in=[1, 2]).filter(date__gte=date_start).filter(
                date__lte=date_end).filter(workplace_id=pizzeria).filter(
                    pay_method=1).count())
        orders_card_count = (Orders.objects.filter(
            type_of_order__in=[1, 2]).filter(date__gte=date_start).filter(
                date__lte=date_end).filter(workplace_id=pizzeria).filter(
                    pay_method=2).count())
        on_line_list = [3, 4, 5]
        orders_online_count = (Orders.objects.filter(
            type_of_order__in=[1, 2]).filter(date__gte=date_start).filter(
                date__lte=date_end).filter(workplace_id=pizzeria).filter(
                    pay_method__in=on_line_list).count())

        df = pd.DataFrame(orders)

        with pd.ExcelWriter("path_to_file.xlsx") as writer:
            df.to_excel(writer)
        lista_1 = []
        for el in orders:
            lista_1.append(el.order_total_price2())
        df = pd.DataFrame(lista_1)
        with pd.ExcelWriter("path_to_file.xlsx") as writer:
            df.to_excel(writer)

        ctx = {
            "orders": orders,
            "orders_cash_count": orders_cash_count,
            "orders_card_count": orders_card_count,
            "orders_online_count": orders_online_count,
        }
        return render(request, "driver_orders.html", ctx)

    def post(self, request, pk):
        pizzeria_active = get_pizzeria_session(request)
        pizzeria = WorkPlace.objects.get(pk=pk)
        pay_method = request.POST.get("pay_method")

        date_start = request.session["date_start"]
        date_end = request.session["date_end"]

        date_start = json.loads(date_start)
        date_end = json.loads(date_end)

        if pay_method == "3":
            pay_method_list = [3, 4, 5]
            orders = (Orders.objects.filter(type_of_order__in=[1, 2]).filter(
                date__gte=date_start).filter(date__lte=date_end).filter(
                    workplace_id=pizzeria_active).filter(
                        pay_method__in=pay_method_list))
        else:
            pay_method_list = [3, 4, 5]
            orders = (Orders.objects.filter(type_of_order__in=[1, 2]).filter(
                date__gte=date_start).filter(date__lte=date_end).filter(
                    workplace_id=pizzeria_active).filter(
                        pay_method=pay_method))

        orders_cash_count = (Orders.objects.filter(
            type_of_order__in=[1, 2]).filter(date__gte=date_start).filter(
                date__lte=date_end).filter(
                    workplace_id=pizzeria_active).filter(pay_method=1).count())
        orders_card_count = (Orders.objects.filter(
            type_of_order__in=[1, 2]).filter(date__gte=date_start).filter(
                date__lte=date_end).filter(
                    workplace_id=pizzeria_active).filter(pay_method=2).count())
        on_line_list = [3, 4, 5]
        orders_online_count = (Orders.objects.filter(
            type_of_order__in=[1, 2]).filter(date__gte=date_start).filter(
                date__lte=date_end).filter(
                    workplace_id=pizzeria_active).filter(
                        pay_method__in=on_line_list).count())

        ctx = {
            "orders": orders,
            "orders_cash_count": orders_cash_count,
            "orders_card_count": orders_card_count,
            "orders_online_count": orders_online_count,
        }
        return render(request, "driver_orders.html", ctx)


@method_decorator(login_required, name="dispatch")
class DriverCoursesView(PermissionRequiredMixin, View):
    permission_required = "babilon_v1.view_myuser"

    def get(self, request, pk):
        user = request.user
        pizzeria_active = get_pizzeria_session(request)
        driver = MyUser.objects.get(pk=pk)

        try:
            date_start = request.session["date_start"]
            date_end = request.session["date_end"]

        except:
            date_start = date.day()
            date_start = json.dumps(date_start,
                                    sort_keys=True,
                                    indent=1,
                                    cls=DjangoJSONEncoder)
            request.session["date_start"] = date_start

            date_end = date.day()
            date_end = json.dumps(date_end,
                                  sort_keys=True,
                                  indent=1,
                                  cls=DjangoJSONEncoder)
            request.session["date_end"] = date_end

        date_start = json.loads(date_start)
        date_end = json.loads(date_end)

        orders = (Orders.objects.filter(type_of_order="3").filter(
            date__gte=date_start).filter(date__lte=date_end).filter(
                workplace_id=pizzeria_active).filter(driver_id=driver))
        orders_cash_count = (Orders.objects.filter(type_of_order="3").filter(
            date__gte=date_start).filter(date__lte=date_end).filter(
                workplace_id=pizzeria_active).filter(driver_id=driver).filter(
                    pay_method=1).count())
        orders_card_count = (Orders.objects.filter(type_of_order="3").filter(
            date__gte=date_start).filter(date__lte=date_end).filter(
                workplace_id=pizzeria_active).filter(driver_id=driver).filter(
                    pay_method=2).count())
        on_line_list = [3, 4, 5]
        orders_online_count = (Orders.objects.filter(type_of_order="3").filter(
            date__gte=date_start).filter(date__lte=date_end).filter(
                workplace_id=pizzeria_active).filter(driver_id=driver).filter(
                    pay_method__in=on_line_list).count())

        df = pd.DataFrame(orders)

        with pd.ExcelWriter("path_to_file.xlsx") as writer:
            df.to_excel(writer)
        lista_1 = []
        for el in orders:
            lista_1.append(el.order_total_price2())
        df = pd.DataFrame(lista_1)

        with pd.ExcelWriter("path_to_file.xlsx") as writer:
            df.to_excel(writer)

        # data = serializers.serialize('json', list(orders))
        # print(data)
        # df = pd.read_json(data)
        # with pd.ExcelWriter('path_to_file.xlsx') as writer:
        #     df.to_excel(writer)

        ctx = {
            "orders": orders,
            "orders_cash_count": orders_cash_count,
            "orders_card_count": orders_card_count,
            "orders_online_count": orders_online_count,
        }
        return render(request, "driver_orders.html", ctx)

    def post(self, request, pk):
        pizzeria_active = get_pizzeria_session(request)
        driver = MyUser.objects.get(pk=pk)
        pay_method = request.POST.get("pay_method")

        try:
            date_start = request.session["date_start"]
            date_end = request.session["date_end"]

        except:
            date_start = date.day()
            date_start = json.dumps(date_start,
                                    sort_keys=True,
                                    indent=1,
                                    cls=DjangoJSONEncoder)
            request.session["date_start"] = date_start

            date_end = date.day()
            date_end = json.dumps(date_end,
                                  sort_keys=True,
                                  indent=1,
                                  cls=DjangoJSONEncoder)
            request.session["date_end"] = date_end

        date_start = json.loads(date_start)
        date_end = json.loads(date_end)

        if pay_method == "3":
            pay_method_list = [3, 4, 5]
            orders = (Orders.objects.filter(type_of_order="3").filter(
                date__gte=date_start).filter(date__lte=date_end).filter(
                    workplace_id=pizzeria_active).filter(
                        driver_id=driver).filter(
                            pay_method__in=pay_method_list))
        else:
            pay_method_list = [3, 4, 5]
            orders = (Orders.objects.filter(type_of_order="3").filter(
                date__gte=date_start).filter(date__lte=date_end).filter(
                    workplace_id=pizzeria_active).filter(
                        driver_id=driver).filter(pay_method=pay_method))

        orders_cash_count = (Orders.objects.filter(type_of_order="3").filter(
            date__gte=date_start).filter(date__lte=date_end).filter(
                workplace_id=pizzeria_active).filter(driver_id=driver).filter(
                    pay_method=1).count())
        orders_card_count = (Orders.objects.filter(type_of_order="3").filter(
            date__gte=date_start).filter(date__lte=date_end).filter(
                workplace_id=pizzeria_active).filter(driver_id=driver).filter(
                    pay_method=2).count())
        on_line_list = [3, 4, 5]
        orders_online_count = (Orders.objects.filter(type_of_order="3").filter(
            date__gte=date_start).filter(date__lte=date_end).filter(
                workplace_id=pizzeria_active).filter(driver_id=driver).filter(
                    pay_method__in=on_line_list).count())

        ctx = {
            "orders": orders,
            "orders_cash_count": orders_cash_count,
            "orders_card_count": orders_card_count,
            "orders_online_count": orders_online_count,
        }
        return render(request, "driver_orders.html", ctx)


@method_decorator(login_required, name="dispatch")
class DriversView(PermissionRequiredMixin, View):
    permission_required = "babilon_v1.view_myuser"

    def get(self, request):
        user = request.user
        pizzeria_active = get_pizzeria_session(request)
        drivers = MyUser.objects.filter(work_place=pizzeria_active).filter(
            profession=4)
        form = DriverForm()
        ctx = {"drivers": drivers, "form": form}
        return render(request, "drivers.html", ctx)

    def post(self, request):
        form = DriverForm(request.POST)
        if "password_change" in request.POST:
            password = request.POST.get("password")
            user_id = request.POST.get("user_id")
            user = MyUser.objects.get(pk=user_id)
            user.set_password(password)
            user.save()
            return redirect("/drivers/")
        if form.is_valid():
            username = form.cleaned_data["username"]
            group = form.cleaned_data["group"]
            first_name = form.cleaned_data["first_name"]
            last_name = form.cleaned_data["last_name"]
            rate = form.cleaned_data["rate"]
            phone_number = form.cleaned_data["phone_number"]
            password = form.cleaned_data["password"]
            street = form.cleaned_data["street"]
            city = form.cleaned_data["city"]
            info = form.cleaned_data["info"]

            if street:
                driver_address = Address()
                driver_address.street = street
                driver_address.save()
            if city:
                driver_address.city = city
                driver_address.save()
            workers = MyUser.objects.all()
            for el in workers:
                if str(el.username) == str(username):
                    user = request.user
                    pizzeria_active = get_pizzeria_session(request)
                    drivers = MyUser.objects.filter(
                        work_place=pizzeria_active).filter(profession=4)
                    form = DriverForm()
                    error_info = "Username istnieje"
                    ctx = {
                        "drivers": drivers,
                        "form": form,
                        "error_info": error_info
                    }
                    return render(request, "drivers.html", ctx)

            new_driver = MyUser()
            new_driver.username = username
            new_driver.first_name = first_name
            new_driver.last_name = last_name
            new_driver.phone_number = phone_number
            try:
                new_driver.user_address = driver_address
                new_driver.save()
            except:
                pass
            new_driver.info = info
            new_driver.set_password(password)
            new_driver.profession = 4
            new_driver.rate_per_drive = rate
            new_driver.save()
            pizzeria = get_pizzeria_session(request)

            new_driver.work_place.add(pizzeria)
            new_driver.groups.add(group)
            new_driver.save()

            return redirect("/drivers/")

        else:
            return render(request, "form_errors.html", context={"form": form})


@method_decorator(login_required, name="dispatch")
class SetDriversActiveView(PermissionRequiredMixin, View):
    permission_required = "babilon_v1.view_myuser"

    def get(self, request, pk):
        pizzeria_active = get_pizzeria_session(request)
        driver = MyUser.objects.get(pk=pk)
        if driver.active == True:
            driver.active = False

            driver.save()
        else:
            driver.active = True
            driver.day_when_active = datetime.now().date()
            driver.save()
        return redirect("/drivers/")


@method_decorator(login_required, name="dispatch")
class DelDriverView(PermissionRequiredMixin, DeleteView):
    permission_required = "babilon_v1.delete_myuser"
    model = MyUser
    fields = "__all__"
    template_name_suffix = "_confirm_delete"
    success_url = "/drivers/"


@method_decorator(login_required, name="dispatch")
class MenagersView(PermissionRequiredMixin, View):
    permission_required = "babilon_v1.view_myuser"

    def get(self, request):
        user = request.user
        pizzeria_active = get_pizzeria_session(request)
        menagers = MyUser.objects.filter(work_place=pizzeria_active).filter(
            profession=1)
        form = MenagerForm()
        ctx = {"menagers": menagers, "form": form}
        return render(request, "menagers.html", ctx)

    def post(self, request):
        form = MenagerForm(request.POST)
        if "password_change" in request.POST:
            password = request.POST.get("password")
            user_id = request.POST.get("user_id")
            user = MyUser.objects.get(pk=user_id)
            user.set_password(password)
            user.save()
            return redirect("/menagers/")
        if form.is_valid():
            username = form.cleaned_data["username"]
            first_name = form.cleaned_data["first_name"]
            group = form.cleaned_data["group"]
            last_name = form.cleaned_data["last_name"]
            work_places = form.cleaned_data["work_places"]
            phone_number = form.cleaned_data["phone_number"]
            password = form.cleaned_data["password"]
            street = form.cleaned_data["street"]
            city = form.cleaned_data["city"]
            info = form.cleaned_data["info"]

            if street:
                menager_address = Address()
                menager_address.street = street
                menager_address.save()
            if city:
                menager_address.city = city
                menager_address.save()
            workers = MyUser.objects.all()
            for el in workers:
                if str(el.username) == str(username):
                    user = request.user
                    pizzeria_active = get_pizzeria_session(request)
                    menagers = MyUser.objects.filter(
                        work_place=pizzeria_active).filter(profession=1)
                    form = MenagerForm()
                    error_info = "Username istnieje"
                    ctx = {
                        "menagers": menagers,
                        "form": form,
                        "error_info": error_info
                    }
                    return render(request, "menagers.html", ctx)

            new_menager = MyUser()
            new_menager.username = username
            new_menager.first_name = first_name
            new_menager.last_name = last_name
            new_menager.phone_number = phone_number
            try:
                new_menager.user_address = menager_address
                new_menager.save()
            except:
                pass
            new_menager.info = info
            new_menager.set_password(password)
            new_menager.profession = 1
            new_menager.groups.add(group)
            new_menager.save()
            new_menager.groups.add(group)
            new_menager.save()
            for pizzeria in work_places:
                pizzeria = WorkPlace.objects.get(pk=pizzeria.id)
                new_menager.work_place.add(pizzeria)
                new_menager.save()

            return redirect("/menagers/")

        else:
            return render(request, "form_errors.html", context={"form": form})


@method_decorator(login_required, name="dispatch")
class BarmansView(PermissionRequiredMixin, View):
    permission_required = "babilon_v1.view_myuser"

    def get(self, request):
        user = request.user
        pizzeria_active = get_pizzeria_session(request)
        barmans = MyUser.objects.filter(work_place=pizzeria_active).filter(
            profession=2)
        form = BarmanForm()
        ctx = {"barmans": barmans, "form": form}
        return render(request, "barmans.html", ctx)

    def post(self, request):
        form = BarmanForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            group = form.cleaned_data["group"]
            first_name = form.cleaned_data["first_name"]
            last_name = form.cleaned_data["last_name"]
            work_place = form.cleaned_data["work_place"]
            phone_number = form.cleaned_data["phone_number"]
            password = form.cleaned_data["password"]
            street = form.cleaned_data["street"]
            city = form.cleaned_data["city"]
            info = form.cleaned_data["info"]

            if street:
                barman_address = Address()
                barman_address.street = street
                barman_address.save()
            if city:
                barman_address.city = city
                barman_address.save()
            workers = MyUser.objects.all()
            for el in workers:
                if str(el.username) == str(username):
                    user = request.user
                    pizzeria_active = get_pizzeria_session(request)
                    barmans = MyUser.objects.filter(
                        work_place=pizzeria_active).filter(profession=2)
                    form = MenagerForm()
                    error_info = "Username istnieje"
                    ctx = {
                        "barmans": barmans,
                        "form": form,
                        "error_info": error_info
                    }
                    return render(request, "barmans.html", ctx)

            new_barman = MyUser()
            new_barman.username = username
            new_barman.first_name = first_name
            new_barman.last_name = last_name
            new_barman.phone_number = phone_number
            try:
                new_barman.user_address = barman_address
                new_barman.save()
            except:
                pass
            new_barman.info = info
            new_barman.set_password(password)
            new_barman.profession = 2
            new_barman.save()
            new_barman.groups.add(group)
            new_barman.work_place.add(work_place)
            new_barman.save()

            return redirect("/barmans/")

        else:
            return render(request, "form_errors.html", context={"form": form})


@method_decorator(login_required, name="dispatch")
class PurchaseView(PermissionRequiredMixin, View):
    permission_required = "babilon_v1.view_purchase"

    def get(self, request):
        user = request.user
        pizzeria_active = get_pizzeria_session(request)
        date_start = request.session["date_start"]
        date_end = request.session["date_end"]
        date_start = json.loads(date_start)
        date_end = json.loads(date_end)

        purchaeses = Purchases.objects.filter(
            work_place=pizzeria_active).filter(
                date__range=[date_start, date_end])
        total = 0
        for el in purchaeses:
            total += el.price
        form = AddShoppingForm()
        formReward = AddRewardForm()
        formTax = AddTaxForm()
        formConst = AddConstForm()
        formOther = AddOtherForm()

        # df = pd.DataFrame(list(purchaeses.values()))
        df = pd.DataFrame(
            list(
                purchaeses.values(
                    "id",
                    "date",
                    "work_place",
                    "purchase_name",
                    "pay_method",
                    "type_purchases",
                    "price",
                    "info",
                )))
        df.index += 1
        df.to_excel(os.path.join(settings.MEDIA_ROOT, "path_to_file.xlsx"))

        ctx = {
            "total": total,
            "purchaeses": purchaeses,
            "form": form,
            "formReward": formReward,
            "formTax": formTax,
            "formConst": formConst,
            "formOther": formOther,
        }
        return render(request, "purchaeses.html", ctx)

    def post(self, request):
        pizzeria_active = get_pizzeria_session(request)

        form = AddShoppingForm(request.POST)
        if form:
            if form.is_valid():
                p = Purchases()
                p.work_place = pizzeria_active
                p.barman_id = request.user
                purchase_name_id = form.cleaned_data["shopping_name"]
                p.purchase_name = CONTRACTOR_NAME[int(purchase_name_id)][1]
                p.type_purchases = 0
                p.pay_method = form.cleaned_data["pay_method"]
                p.price = form.cleaned_data["price"]
                p.info = form.cleaned_data["info"]
                p.save()

                return redirect("/purchases/")

        formReward = AddRewardForm(request.POST)
        if formReward:
            if formReward.is_valid():
                p = Purchases()
                p.work_place = pizzeria_active
                p.barman_id = request.user
                worker_id = formReward.cleaned_data["worker"]
                worker = MyUser.objects.get(pk=int(worker_id.id))
                p.purchase_name = (str(worker.username) + ": " +
                                   str(worker.first_name) + " " +
                                   str(worker.last_name))
                p.pay_method = formReward.cleaned_data["pay_method"]
                p.type_purchases = 1
                p.price = formReward.cleaned_data["price"]
                p.info = formReward.cleaned_data["info"]
                p.save()

                return redirect("/purchases/")

        formTax = AddTaxForm(request.POST)
        if formTax:
            if formTax.is_valid():
                p = Purchases()
                p.work_place = pizzeria_active
                p.barman_id = request.user
                tax_name_id = formTax.cleaned_data["tax_name"]
                p.purchase_name = TAX_TYPE[int(tax_name_id)][1]
                p.pay_method = formTax.cleaned_data["pay_method"]
                p.type_purchases = 2
                p.price = formTax.cleaned_data["price"]
                p.info = formTax.cleaned_data["info"]
                p.save()
                return redirect("/purchases/")

        formConst = AddConstForm(request.POST)
        if formConst:
            if formConst.is_valid():
                p = Purchases()
                p.work_place = pizzeria_active
                p.barman_id = request.user
                const_name_id = formConst.cleaned_data["const_name"]
                p.purchase_name = TYPE_OF_FIXED_COST[int(const_name_id)][1]
                p.pay_method = formConst.cleaned_data["pay_method"]
                p.type_purchases = 3
                p.price = formConst.cleaned_data["price"]
                p.info = formConst.cleaned_data["info"]
                p.save()
                return redirect("/purchases/")

        formOther = AddOtherForm(request.POST)
        if formConst:
            if formOther.is_valid():
                p = Purchases()
                p.work_place = pizzeria_active
                p.barman_id = request.user
                p.purchase_name = formOther.cleaned_data["other_name"]
                p.pay_method = formOther.cleaned_data["pay_method"]
                p.type_purchases = 4
                p.price = formOther.cleaned_data["price"]
                p.info = formOther.cleaned_data["info"]
                p.save()
                return redirect("/purchases/")


@method_decorator(login_required, name="dispatch")
class PurchaseCategoryView(PermissionRequiredMixin, View):
    permission_required = "babilon_v1.view_purchase"

    def get(self, request, pk):
        user = request.user
        pizzeria_active = get_pizzeria_session(request)
        date_start = request.session["date_start"]
        date_end = request.session["date_end"]
        date_start = json.loads(date_start)
        date_end = json.loads(date_end)

        purchaeses = (Purchases.objects.filter(
            work_place=pizzeria_active).filter(
                date__range=[date_start, date_end]).filter(type_purchases=pk))

        total = 0
        for el in purchaeses:
            total += el.price
        form = AddShoppingForm()
        formReward = AddRewardForm()
        formTax = AddTaxForm()
        formConst = AddConstForm()
        formOther = AddOtherForm()

        df = pd.DataFrame(
            list(
                purchaeses.values(
                    "id",
                    "date",
                    "work_place",
                    "purchase_name",
                    "pay_method",
                    "type_purchases",
                    "price",
                    "info",
                )))
        df.index += 1
        df.to_excel(os.path.join(settings.MEDIA_ROOT, "path_to_file.xlsx"))

        ctx = {
            "total": total,
            "pk": pk,
            "purchaeses": purchaeses,
            "form": form,
            "formReward": formReward,
            "formTax": formTax,
            "formConst": formConst,
            "formOther": formOther,
        }
        return render(request, "purchaeses.html", ctx)

    def post(self, request, pk):
        pizzeria_active = get_pizzeria_session(request)

        form = AddShoppingForm(request.POST)
        if form:
            if form.is_valid():
                p = Purchases()
                p.work_place = pizzeria_active
                p.barman_id = request.user
                purchase_name_id = form.cleaned_data["shopping_name"]
                p.purchase_name = CONTRACTOR_NAME[int(purchase_name_id)][1]
                p.type_purchases = 0
                p.pay_method = form.cleaned_data["pay_method"]
                p.price = form.cleaned_data["price"]
                p.info = form.cleaned_data["info"]
                p.save()
                return redirect("/purchases/0")

        formReward = AddRewardForm(request.POST)
        if formReward:
            if formReward.is_valid():
                p = Purchases()
                p.work_place = pizzeria_active
                p.barman_id = request.user
                worker_id = formReward.cleaned_data["worker"]
                worker = MyUser.objects.get(pk=int(worker_id.id))
                p.purchase_name = (str(worker.username) + ": " +
                                   str(worker.first_name) + " " +
                                   str(worker.last_name))
                p.pay_method = formReward.cleaned_data["pay_method"]
                p.type_purchases = 1
                p.price = formReward.cleaned_data["price"]
                p.info = formReward.cleaned_data["info"]
                p.save()
                return redirect("/purchases/1")

        formTax = AddTaxForm(request.POST)
        if formTax:
            if formTax.is_valid():
                p = Purchases()
                p.work_place = pizzeria_active
                p.barman_id = request.user
                tax_name_id = formTax.cleaned_data["tax_name"]
                p.purchase_name = TAX_TYPE[int(tax_name_id)][1]
                p.pay_method = formTax.cleaned_data["pay_method"]
                p.type_purchases = 2
                p.price = formTax.cleaned_data["price"]
                p.info = formTax.cleaned_data["info"]
                p.save()
                return redirect("/purchases/2")

        formConst = AddConstForm(request.POST)
        if formConst:
            if formConst.is_valid():
                p = Purchases()
                p.work_place = pizzeria_active
                p.barman_id = request.user
                const_name_id = formConst.cleaned_data["const_name"]
                p.purchase_name = TYPE_OF_FIXED_COST[int(const_name_id)][1]
                p.pay_method = formConst.cleaned_data["pay_method"]
                p.type_purchases = 3
                p.price = formConst.cleaned_data["price"]
                p.info = formConst.cleaned_data["info"]
                p.save()
                return redirect("/purchases/3")

        formOther = AddOtherForm(request.POST)
        if formConst:
            if formOther.is_valid():
                p = Purchases()
                p.work_place = pizzeria_active
                p.barman_id = request.user
                p.purchase_name = formOther.cleaned_data["other_name"]
                p.pay_method = formOther.cleaned_data["pay_method"]
                p.type_purchases = 4
                p.price = formOther.cleaned_data["price"]
                p.info = formOther.cleaned_data["info"]
                p.save()
                return redirect("/purchases/4")


@method_decorator(login_required, name="dispatch")
class EditPurchaseView(PermissionRequiredMixin, UpdateView):
    permission_required = "babilon_v1.change_purchase"

    model = Purchases
    fields = "__all__"
    template_name_suffix = "_update_form"
    success_url = "/purchases/"


@method_decorator(login_required, name="dispatch")
class DelPurchaseView(PermissionRequiredMixin, DeleteView):
    permission_required = "babilon_v1.delete_purchase"

    model = Purchases
    fields = "__all__"
    template_name_suffix = "_confirm_delete"
    success_url = "/purchases/"
    # def get_success_url(self):
    #     return f'/order_details/{self.object.order_id.id}'


@method_decorator(login_required, name="dispatch")
class StatisticsView(PermissionRequiredMixin, DeleteView):
    permission_required = "babilon_v1.view_orders"

    def get(self, request):
        return TemplateResponse(request, "statistics.html")

    def post(self, request):
        pizzeria_id = request.session["pizzeria"]
        pizzeria = WorkPlace.objects.get(pk=pizzeria_id)
        date_start = request.session["date_start"]
        date_end = request.session["date_end"]
        date_start = json.loads(date_start)
        date_end = json.loads(date_end)
        if "income" in request.POST:
            orders = (Orders.objects.filter(status=4).filter(
                workplace_id=pizzeria).filter(
                    date__range=[date_start, date_end]).order_by("date"))
            d3 = diagram_income(orders)
            len_orders = len(orders)
            if type(d3) == str:
                ctx = {"d3": d3}
                return TemplateResponse(request, "statistics.html", ctx)
            img = "/pizzeria/static/media/income.png"
            ctx = {"img": img, "len_orders": len_orders}
            return TemplateResponse(request, "statistics.html", ctx)
        if "the_best_pizza" in request.POST:
            orders = Orders.objects.filter(workplace_id=pizzeria).filter(
                date__range=[date_start, date_end])
            pos = PositionOrder.objects.filter(product_id__category=1).filter(
                order_id__in=orders)
            d3 = the_best_pizza(pos)
            len_orders = len(pos)
            if type(d3) == str:
                ctx = {"d3": d3}
                return TemplateResponse(request, "statistics.html", ctx)
            img = "/pizzeria/static/media/the_best_pizza.png"
            ctx = {"img": img, "len_orders": len_orders}
            return TemplateResponse(request, "statistics.html", ctx)
        if "the_poor_pizza" in request.POST:
            orders = Orders.objects.filter(workplace_id=pizzeria).filter(
                date__range=[date_start, date_end])
            pos = PositionOrder.objects.filter(product_id__category=1).filter(
                order_id__in=orders)
            d3 = the_poor_pizza(pos)
            len_orders = len(pos)
            if type(d3) == str:
                ctx = {"d3": d3}
                return TemplateResponse(request, "statistics.html", ctx)
            img = "/pizzeria/static/media/the_poor_pizza.png"
            ctx = {"img": img, "len_orders": len_orders}
            return TemplateResponse(request, "statistics.html", ctx)
        if "orders_by_hours" in request.POST:
            orders = (Orders.objects.filter(status=4).filter(
                type_of_order=3).filter(workplace_id=pizzeria).filter(
                    date__range=[date_start, date_end]))
            len_orders = len(orders)

            d3 = orders_by_hours(orders)
            if type(d3) == str:
                try:
                    os.remove("pizzeria/static/media/orders_by_hours.png")
                except:
                    pass
                ctx = {"d3": d3}
                return TemplateResponse(request, "statistics.html", ctx)
            img = "/pizzeria/static/media/orders_by_hours.png"
            ctx = {"img": img, "len_orders": len_orders}
            return TemplateResponse(request, "statistics.html", ctx)

        return TemplateResponse(request, "statistics.html")


# Zamówienia


@method_decorator(login_required, name="dispatch")
class ProductsView(PermissionRequiredMixin, View):
    permission_required = "babilon_v1.view_products"

    def get(self, request):
        user = request.user
        pizzeria = get_pizzeria_session(request)
        order = Orders.objects.get(pk=request.session["active_orders"])
        # order=get_order(request,pizzeria)
        products = Products.objects.filter(is_active=True)
        categorys = Category.objects.all()
        pizza_sizes = ProductSize.objects.filter(pizza=True)
        positions_on_order = PositionOrder.objects.filter(order_id=order.id)
        ctx = {
            "order": order,
            "positions_on_order": positions_on_order,
            "products": products,
            "pizza_sizes": pizza_sizes,
            "categorys": categorys,
            "pizzeria": pizzeria,
        }
        return TemplateResponse(request, "main_menu.html", ctx)


@method_decorator(login_required, name="dispatch")
class CategoryProductsView(PermissionRequiredMixin, View):
    permission_required = "babilon_v1.view_products"

    def get(self, request, pk):
        category = Category.objects.get(pk=pk)
        products = Products.objects.filter(category=category).filter(
            is_active=True)

        user = request.user
        pizzeria = get_pizzeria_session(request)
        # order=get_order(request,pizzeria)
        order = Orders.objects.get(pk=request.session["active_orders"])
        categorys = Category.objects.all()
        category_pizza = Category.objects.filter(category_name="Pizza")

        positions_on_order = PositionOrder.objects.filter(order_id=order.id)
        if (category.category_name == "Pizza"
                or category.category_name == "Pizza premium"):
            product_sizes = ProductSize.objects.filter(pizza=True)
            ctx = {
                "order": order,
                "positions_on_order": positions_on_order,
                "products": products,
                "product_sizes": product_sizes,
                "categorys": categorys,
                "category": category,
                "pizzeria": pizzeria,
            }
            return TemplateResponse(request, "pizza_menu.html", ctx)

        else:
            if (category.category_name == "Napoje"
                    or category.category_name == "Napoje 2"):
                product_sizes = ProductSize.objects.filter(bottle=True)
            else:
                product_sizes = []
            ctx = {
                "product_sizes": product_sizes,
                "order": order,
                "positions_on_order": positions_on_order,
                "products": products,
                "categorys": categorys,
                "category": category,
                "pizzeria": pizzeria,
            }
            return TemplateResponse(request, "product_menu.html", ctx)

        # ctx={'order':order,'positions_on_order':positions_on_order,'products':products,'pizza_sizes':pizza_sizes,'categorys':categorys,'category':category,'pizzeria':pizzeria,}
        # return TemplateResponse(request, "pizza_menu.html",ctx)

    def post(self, request, pk):
        size_id = request.POST.get("size")
        product_size = ProductSize.objects.get(pk=size_id)
        category = Category.objects.get(pk=pk)
        products = Products.objects.filter(category=category).filter(
            is_active=True)
        user = request.user
        pizzeria = get_pizzeria_session(request)
        order = Orders.objects.get(pk=request.session["active_orders"])

        categorys = Category.objects.all()
        if (category.category_name == "Pizza"
                or category.category_name == "Pizza premium"):
            product_sizes = ProductSize.objects.filter(pizza=True)
            products = (Products.objects.filter(category=category).filter(
                product_size=product_size).filter(is_active=True))

        else:
            if (category.category_name == "Napoje"
                    or category.category_name == "Napoje 2"):
                product_sizes = ProductSize.objects.filter(bottle=True)
                products = (Products.objects.filter(category=category).filter(
                    product_size=product_size).filter(is_active=True))
            else:
                products = Products.objects.filter(category=category)
        positions_on_order = PositionOrder.objects.filter(order_id=order.id)

        if (category.category_name == "Pizza"
                or category.category_name == "Pizza premium"):
            ctx = {
                "order": order,
                "positions_on_order": positions_on_order,
                "products": products,
                "product_sizes": product_sizes,
                "product_size": product_size,
                "categorys": categorys,
                "category": category,
                "pizzeria": pizzeria,
            }
            return TemplateResponse(request, "pizza_menu.html", ctx)
        else:
            if (category.category_name == "Napoje"
                    or category.category_name == "Napoje 2"):
                product_sizes = ProductSize.objects.filter(bottle=True)
            else:
                produc_sizes = []

            ctx = {
                "order": order,
                "positions_on_order": positions_on_order,
                "products": products,
                "product_sizes": product_sizes,
                "product_size": product_size,
                "categorys": categorys,
                "category": category,
                "pizzeria": pizzeria,
            }
            return TemplateResponse(request, "product_menu.html", ctx)


@method_decorator(login_required, name="dispatch")
class SearchProductView(PermissionRequiredMixin, View):
    permission_required = "babilon_v1.view_products"

    def post(self, request):
        search = request.POST.get("search")
        cat_list = [1, 2]
        # set_code_number()
        category = Category.objects.filter(category_number__in=cat_list)
        products = Products.objects.filter(category__in=category).filter(
            is_active=True)
        products = products.filter(Q(code_number=search))

        user = request.user
        pizzeria = get_pizzeria_session(request)
        order = Orders.objects.get(pk=request.session["active_orders"])
        positions_on_order = PositionOrder.objects.filter(order_id=order.id)
        categorys = Category.objects.all()
        ctx = {
            "order": order,
            "positions_on_order": positions_on_order,
            "products": products,
            "categorys": categorys,
            "category": category,
            "pizzeria": pizzeria,
        }
        return TemplateResponse(request, "pizza_menu.html", ctx)


@method_decorator(login_required, name="dispatch")
class AddNewOrderLocalView(PermissionRequiredMixin, View):
    permission_required = "babilon_v1.add_orders"

    def get(self, request):
        year_now = datetime.now().year
        month_now = datetime.now().month
        day = datetime.now().day

        user = request.user
        pizzeria = get_pizzeria_session(request)

        order = Orders()
        order.active = True
        order.time_start = datetime.now()
        order.workplace_id = pizzeria
        order.barman_id = request.user
        order.number = new_number(pizzeria.id)
        order.type_of_order = 1
        order.time_zero = datetime.now() + timedelta(
            minutes=int(default_time_zoro_local))
        order.address = None
        order.save()
        request.session["active_orders"] = order.id
        products = Products.objects.filter(is_active=True)
        categorys = Category.objects.all()
        category_pizza = Category.objects.filter(category_name="Pizza")
        pizzas = Products.objects.filter(category__in=category_pizza).filter(
            is_active=True)
        pizza_sizes = ProductSize.objects.filter(pizza=True)
        positions_on_order = PositionOrder.objects.filter(order_id=order.id)
        # ctx={'order':order,'positions_on_order':positions_on_order,'products':products,'pizzas':pizzas,'pizza_sizes':pizza_sizes,'categorys':categorys,'pizzeria':pizzeria,}
        # return TemplateResponse(request, "main_menu.html",ctx)
        return redirect("products_category", pk=1)


@method_decorator(login_required, name="dispatch")
class AddNewOrderOutsideView(PermissionRequiredMixin, View):
    permission_required = "babilon_v1.add_orders"

    def get(self, request):
        year_now = datetime.now().year
        month_now = datetime.now().month
        day = datetime.now().day
        user = request.user
        pizzeria = get_pizzeria_session(request)
        order = Orders()
        order.active = True
        order.time_start = datetime.now()
        order.workplace_id = pizzeria
        order.barman_id = request.user
        order.number = new_number(pizzeria.id)
        order.type_of_order = 2
        order.time_zero = datetime.now() + timedelta(
            minutes=int(default_time_zoro_local))
        order.address = None
        order.save()
        request.session["active_orders"] = order.id
        products = Products.objects.filter(is_active=True)
        categorys = Category.objects.all()
        category_pizza = Category.objects.filter(category_name="Pizza")
        pizzas = Products.objects.filter(category__in=category_pizza).filter(
            is_active=True)
        pizza_sizes = ProductSize.objects.filter(pizza=True)
        positions_on_order = PositionOrder.objects.filter(order_id=order.id)
        # ctx={'order':order,'positions_on_order':positions_on_order,'products':products,'pizzas':pizzas,'pizza_sizes':pizza_sizes,'categorys':categorys,'pizzeria':pizzeria,}
        # return TemplateResponse(request, "main_menu.html",ctx)
        return redirect("products_category", pk=1)


@method_decorator(login_required, name="dispatch")
class AddNewOrderOutsideDriverView(PermissionRequiredMixin, View):
    permission_required = "babilon_v1.add_orders"

    def get(self, request):
        year_now = datetime.now().year
        month_now = datetime.now().month
        day = datetime.now().day
        user = request.user
        pizzeria = get_pizzeria_session(request)
        work_place = WorkPlace.objects.get(pk=pizzeria.id)

        order = Orders()
        order.time_start = datetime.now()
        order.type_of_order = 3
        order.active = True
        order.workplace_id = pizzeria
        order.barman_id = request.user
        order.number = new_number(pizzeria.id)
        order.time_zero = datetime.now() + timedelta(
            minutes=int(default_time_zoro_outside))
        order.save()
        request.session["active_orders"] = order.id
        products = Products.objects.filter(is_active=True)
        categorys = Category.objects.all()
        category_pizza = Category.objects.filter(category_name="Pizza")
        pizzas = Products.objects.filter(category__in=category_pizza).filter(
            is_active=True)
        pizza_sizes = ProductSize.objects.filter(pizza=True)
        positions_on_order = PositionOrder.objects.filter(order_id=order.id)

        # clients=Clients.objects.filter(work_place=work_place)
        # clients_addresses=Address.objects.all()
        ctx = {
            "order": order,
            "positions_on_order": positions_on_order,
            "products": products,
            "pizzas": pizzas,
            "pizza_sizes": pizza_sizes,
            "categorys": categorys,
            "pizzeria": pizzeria,
        }
        # return redirect('clients')
        return TemplateResponse(request, "clients.html", ctx)

    def post(self, request):
        pizzeria = get_pizzeria_session(request)
        work_place = WorkPlace.objects.get(pk=pizzeria.id)

        if "search" in request.POST:
            search = request.POST.get("search")
            order_id = request.POST.get("order_id")
            order = Orders.objects.get(pk=order_id)
            work_place = order.workplace_id
            clients = Clients.objects.filter(work_place=work_place).filter(
                Q(phone_number__icontains=search))
            clients_addresses = Address.objects.filter(client_id__in=clients)

            ctx = {
                "search": search,
                "clients": clients,
                "clients_addresses": clients_addresses,
                "order": order,
            }
            # return redirect('clients')
            return TemplateResponse(request, "clients.html", ctx)

        phone_number = request.POST.get("phone_number")
        address = request.POST.get("address")
        firstlastname = request.POST.get("firstlastname")
        order = request.POST.get("order")
        info = request.POST.get("info")
        new_address = Address()
        new_address.street = address
        new_address.save()

        new_client = Clients()
        new_client.phone_number = phone_number
        new_client.work_place = work_place
        new_client.client_name = firstlastname
        new_client.info = info
        new_client.save()

        new_address.client_id = new_client
        new_address.save()

        order = Orders.objects.get(pk=order)
        order.address = new_address
        order.save()

        # return redirect('client',pk=new_client.id)
        return redirect("products_category", pk=1)


@method_decorator(login_required, name="dispatch")
class AddClientToOrder(PermissionRequiredMixin, View):
    permission_required = "babilon_v1.add_orders"

    def get(self, request, pk):
        pizzeria = get_pizzeria_session(request)
        client_address = Address.objects.get(pk=pk)
        client_address.choice_count += 1
        client_address.save()
        user = request.user

        # order=get_order(request,pizzeria)
        order = Orders.objects.get(pk=request.session["active_orders"])
        order.type_of_order = 3
        order.time_start = datetime.now()
        order.time_zero = datetime.now() + timedelta(
            minutes=int(default_time_zoro_outside))
        order.address = client_address
        order.save()
        products = Products.objects.filter(is_active=True)
        categorys = Category.objects.all()
        category_pizza = Category.objects.filter(category_name="Pizza")
        pizzas = Products.objects.filter(category__in=category_pizza).filter(
            is_active=True)
        pizza_sizes = ProductSize.objects.filter(pizza=True)
        positions_on_order = PositionOrder.objects.filter(order_id=order.id)
        # ctx={'order':order,'positions_on_order':positions_on_order,'products':products,'pizzas':pizzas,'pizza_sizes':pizza_sizes,'categorys':categorys,'pizzeria':pizzeria,}
        # return TemplateResponse(request, "main_menu.html",ctx)
        return redirect("products_category", pk=1)


@method_decorator(login_required, name="dispatch")
class AddPizzaToOrderView(PermissionRequiredMixin, View):
    permission_required = "babilon_v1.add_orders"

    def get(self, request, order, prod):
        user = request.user
        categorys = Category.objects.all()
        order = Orders.objects.get(pk=order)
        pizza = Products.objects.get(pk=prod)
        other_size = Products.objects.filter(
            product_name=pizza.product_name).filter(is_active=True)
        cakes = (Products.objects.filter(type_of_ingredient="5").filter(
            is_active=True).order_by("product_name"))
        souse_pay = Products.objects.filter(type_of_ingredient="6").filter(
            is_active=True)
        souse_free = Products.objects.filter(type_of_ingredient="7").filter(
            is_active=True)
        positions_on_order = PositionOrder.objects.filter(order_id=order.id)

        ctx = {
            "order": order,
            "pizza": pizza,
            "other_size": other_size,
            "positions_on_order": positions_on_order,
            "categorys": categorys,
            "cakes": cakes,
            "souse_pay": souse_pay,
            "souse_free": souse_free,
        }
        return TemplateResponse(request, "add_pizza_to_order.html", ctx)

    def post(self, request, order, prod):
        user = request.user
        order = Orders.objects.get(pk=order)
        product = Products.objects.get(pk=prod)
        order = Orders.objects.get(pk=order.id)

        add = request.POST.get("add")
        quantity = request.POST.get("quantity")

        extra_price = request.POST.get("extra_price")
        info = request.POST.get("info")
        cake_change = request.POST.get("cake_change")
        add_sauces_free = request.POST.get("add_sauces_free")
        add_sauces_pay = request.POST.get("add_sauces_pay")

        productId = request.POST.get("productId")
        orderPositionId = request.POST.get("orderPosition")
        discount = request.POST.get("discount")

        price = request.POST.get("price")

        price_org = product.price

        new_position = PositionOrder()
        new_position.order_id = order
        new_position.cake_info = cake_change
        new_position.product_id = product
        new_position.size_id = product.product_size

        if price != "":
            price = float(price)
            if price < price_org and price != 0.00:

                new_position.price = price
                new_position.save()
                order.promo = True
                # order.save()
            else:
                new_position.price = product.price
                new_position.save()
        else:
            price = 0.00
            new_position.price = price
            new_position.save()
            order.promo = True
        positions_on_order = PositionOrder.objects.filter(order_id=order.id)
        if discount != "":
            if int(discount) != 0 and discount != None:
                new_position.discount = int(discount)
                new_position.save()

                # print(price_org)
                order.promo = True
                # order.save()
        else:
            new_position.discount = 0
            new_position.save()
            order.promo = True

        if quantity != None:
            if int(quantity) > 0:
                new_position.quantity = int(quantity)
                new_position.save()

        if extra_price != None:
            new_position.extra_price = float(extra_price.replace(",", "."))
            new_position.save()
        else:
            new_position.extra_price = new_position.extra_price
            new_position.save()
        if info != "":
            new_position.info = info
            new_position.save()
        if cake_change != "":
            new_position.cake_info = cake_change
            new_position.save()
        if add_sauces_free != "":
            new_position.sauces_free = add_sauces_free
            new_position.save()
        if add_sauces_pay != "":
            new_position.sauces_pay = add_sauces_pay
            new_position.save()

        changeTopps = request.POST.get("changeTopps")

        categorys = Category.objects.all()
        order.save()
        souse_pay = Products.objects.filter(type_of_ingredient="6").filter(
            is_active=True)
        souse_free = Products.objects.filter(type_of_ingredient="7").filter(
            is_active=True)
        return redirect("products_category", pk=1)


@method_decorator(login_required, name="dispatch")
class AddPizzaFreestyleToppsView(PermissionRequiredMixin, View):
    permission_required = "babilon_v1.change_positionorder"

    def get(self, request, order, prod):
        order = Orders.objects.get(pk=order)
        product = Products.objects.get(id=prod)

        vegetopps = (Products.objects.filter(type_of_ingredient="1").filter(
            is_active=True).order_by("product_name"))
        beeftopps = (Products.objects.filter(type_of_ingredient="2").filter(
            is_active=True).order_by("product_name"))
        cheesetopps = (Products.objects.filter(type_of_ingredient="3").filter(
            is_active=True).order_by("product_name"))
        extra_list = [4, 7, 8, 9, 10, 11]
        extratopps = (Products.objects.filter(
            type_of_ingredient__in=extra_list).filter(
                is_active=True).order_by("product_name"))
        cake = (Products.objects.filter(type_of_ingredient="5").filter(
            is_active=True).order_by("product_name"))

        vegecounter = 0
        beefcounter = 0
        cheesecounter = 0
        cakecounter = 0
        extracounter = 0
        extra_1_counter = 0
        extra_2_counter = 0
        extra_3_counter = 0
        extra_4_counter = 0

        addvege_pay_control = vegecounter
        beef_pay_control = beefcounter
        cheese_pay_control = cheesecounter
        cake_pay_control = cakecounter
        extra_pay_control = extracounter
        extra_1_pay_control = extra_1_counter
        extra_2_pay_control = extra_2_counter
        extra_3_pay_control = extra_3_counter
        extra_4_pay_control = extra_4_counter

        vege_pay = vegecounter
        beef_pay = beefcounter
        cheese_pay = cheesecounter
        cake_pay = cakecounter
        extra_pay = extracounter
        extra__1_pay = extra_1_counter
        extra__2_pay = extra_2_counter
        extra__3_pay = extra_3_counter
        extra__4_pay = extra_4_counter

        change_topps_vege = 0
        change_topps_beef = 0
        change_topps_cheese = 0
        change_topps_extra = 0
        change_topps_cake = 0
        change_topps_extra_1 = 0
        change_topps_extra_2 = 0
        change_topps_extra_3 = 0
        change_topps_extra_4 = 0

        ctx = {
            "order": order,
            "pizza": product,
            "toppings": toppings,
            "vegetopps": vegetopps,
            "beeftopps": beeftopps,
            "cheesetopps": cheesetopps,
            "extratopps": extratopps,
            "cake": cake,
            "vegecounter": vegecounter,
            "beefcounter": beefcounter,
            "cheesecounter": cheesecounter,
            "extracounter": extracounter,
            "cakecounter": cakecounter,
            "extra_1_counter": extra_1_counter,
            "extra_2_counter": extra_2_counter,
            "extra_3_counter": extra_3_counter,
            "extra_4_counter": extra_4_counter,
            "addvege_pay_control": addvege_pay_control,
            "beef_pay_control": beef_pay_control,
            "cheese_pay_control": cheese_pay_control,
            "extra_pay_control": extra_pay_control,
            "cake_pay_control": cake_pay_control,
            "extra_1_pay_control": extra_1_pay_control,
            "extra_2_pay_control": extra_2_pay_control,
            "extra_3_pay_control": extra_3_pay_control,
            "extra_4_pay_control": extra_4_pay_control,
            "vege_pay": vege_pay,
            "beef_pay": beef_pay,
            "cheese_pay": cheese_pay,
            "cake_pay": cake_pay,
            "extra_pay": extra_pay,
            "extra__1_pay": extra__1_pay,
            "extra__2_pay": extra__2_pay,
            "extra__3_pay": extra__3_pay,
            "extra__4_pay": extra__4_pay,
            "change_topps_vege": change_topps_vege,
            "change_topps_beef": change_topps_beef,
            "change_topps_cheese": change_topps_cheese,
            "change_topps_cake": change_topps_cake,
            "change_topps_extra": change_topps_extra,
            "change_topps_extra_1": change_topps_extra_1,
            "change_topps_extra_2": change_topps_extra_2,
            "change_topps_extra_3": change_topps_extra_3,
            "change_topps_extra_4": change_topps_extra_4,
        }
        return TemplateResponse(request, "add_pizza_freestyle.html", ctx)

    def post(self, request, order, prod):
        order = Orders.objects.get(pk=order)
        product = Products.objects.get(id=prod)
        # position_order = PositionOrder.objects.get(pk=request.POST.get('position_order'))

        input_add_topps = request.POST.get("input_add_topps")
        input_del_topps = request.POST.get("input_del_topps")
        input_add_cake = request.POST.get("input_add_cake")
        extra_price = request.POST.get("extra_price")
        extra_price = extra_price.replace(",", ".")

        new_position = PositionOrder()
        new_position.cake_info = ""
        new_position.product_id = product
        new_position.size_id = product.product_size
        new_position.price = product.price
        new_position.change_topps = ""
        new_position.save()

        if extra_price != "":
            new_position.extra_price = float(extra_price)
        else:
            new_position.extra_price = 0.00
        new_position.change_topps_info = input_del_topps + " " + input_add_topps
        new_position.cake_info = input_add_cake
        # new_position.order_id=order
        new_position.save()

        return redirect("add_pizza_freestyle_to_order",
                        order=order.id,
                        pos=new_position.id)


@method_decorator(login_required, name="dispatch")
class AddPizzaFreestyleToOrderView(PermissionRequiredMixin, View):
    permission_required = "babilon_v1.add_orders"

    def get(self, request, order, pos):
        user = request.user
        categorys = Category.objects.all()
        order = Orders.objects.get(pk=order)
        pizza = PositionOrder.objects.get(pk=pos)
        product = pizza.product_id
        other_size = Products.objects.filter(
            product_name=pizza.product_id.product_name)
        cakes = (Products.objects.filter(type_of_ingredient="5").filter(
            is_active=True).order_by("product_name"))
        souse_pay = Products.objects.filter(type_of_ingredient="6").filter(
            is_active=True)
        souse_free = Products.objects.filter(type_of_ingredient="7").filter(
            is_active=True)
        positions_on_order = PositionOrder.objects.filter(order_id=order.id)

        ctx = {
            "order": order,
            "pizza": pizza,
            "product": product,
            "other_size": other_size,
            "positions_on_order": positions_on_order,
            "categorys": categorys,
            "cakes": cakes,
            "souse_pay": souse_pay,
            "souse_free": souse_free,
        }
        return TemplateResponse(request, "add_pizza_freestyle_to_order.html",
                                ctx)

    def post(self, request, order, pos):
        user = request.user
        order = Orders.objects.get(pk=order)
        position_order = PositionOrder.objects.get(pk=pos)
        if "delete" in request.POST:
            position_order.extra_price = 0.00
            position_order.change_topps_info = ""
            position_order.sauces_free = ""
            position_order.sauces_pay = ""
            position_order.cake_info = ""
            position_order.info = ""
            position_order.discount = 0
            position_order.save()
            return redirect("add_pizza_freestyle_to_order",
                            order=order.id,
                            pos=position_order.id)

        product = Products.objects.get(pk=position_order.product_id.id)

        add = request.POST.get("add")
        quantity = request.POST.get("quantity")
        extra_price = request.POST.get("extra_price")
        info = request.POST.get("info")
        cake_change = request.POST.get("cake_change")
        add_sauces_free = request.POST.get("add_sauces_free")
        add_sauces_pay = request.POST.get("add_sauces_pay")

        orderPositionId = request.POST.get("orderPosition")
        discount = request.POST.get("discount")

        position_order.order_id = order
        position_order.save()

        productId = request.POST.get("productId")
        product = Products.objects.get(pk=productId)
        price = request.POST.get("price")
        price_org = product.price

        if price != "":
            if price != None:
                price = float(price)
                if price < price_org and price != 0:
                    position_order.price = price
                    position_order.save()
                    order.promo = True
                    # order.save()
                else:
                    position_order.price = product.price
                    position_order.save()
        else:
            position_order.price = 0
            position_order.save()
            order.promo = True
        if quantity != None:
            if int(quantity) > 0:
                position_order.quantity = int(quantity)
                position_order.save()
        if discount != "":
            if int(discount != 0) and discount != None:
                position_order.discount = int(discount)
                position_order.save()
                order.promo = True
        else:
            position_order.discount = 0
            position_order.save()
            order.promo = True
        if extra_price != None:
            position_order.extra_price = float(extra_price.replace(",", "."))
            position_order.save()
        else:
            position_order.extra_price = position_order.extra_price
            position_order.save()
        if info != "":
            position_order.info = info
            position_order.save()
        if cake_change != "":
            position_order.cake_info = cake_change
            position_order.save()
        if add_sauces_free != "":
            position_order.sauces_free = add_sauces_free
            position_order.save()
        if add_sauces_pay != "":
            position_order.sauces_pay = add_sauces_pay
            position_order.save()

        changeTopps = request.POST.get("changeTopps")

        categorys = Category.objects.all()
        order = Orders.objects.get(pk=order.id)
        souse_pay = Products.objects.filter(type_of_ingredient="6").filter(
            is_active=True)
        souse_free = Products.objects.filter(type_of_ingredient="7").filter(
            is_active=True)
        order.save()
        return redirect("products_category", pk=1)


@method_decorator(login_required, name="dispatch")
class ModyfiPizzaFreestyleToOrderView(PermissionRequiredMixin, View):
    permission_required = "babilon_v1.add_orders"

    def get(self, request, order, pos):
        order = Orders.objects.get(pk=order)
        position_order = PositionOrder.objects.get(pk=pos)
        product = position_order.product_id

        return redirect("add_pizza_freestyle_to_order",
                        order=order.id,
                        pos=position_order.id)

    def post(self, request, order, pos):
        user = request.user
        order = Orders.objects.get(pk=order)
        position_order = PositionOrder.objects.get(pk=pos)
        product = position_order.product_id

        if "delete" in request.POST:
            position_order.extra_price = 0.00
            position_order.change_topps_info = ""
            position_order.sauces_free = ""
            position_order.sauces_pay = ""
            position_order.cake_info = ""
            position_order.info = ""
            position_order.discount = 0
            position_order.save()
            return redirect("add_pizza_freestyle_to_order",
                            order=order.id,
                            pos=position_order.id)


@method_decorator(login_required, name="dispatch")
class ChangeToppsFreestyleView(PermissionRequiredMixin, View):
    permission_required = "babilon_v1.change_positionorder"

    def get(self, request, order, pos):
        order = Orders.objects.get(pk=order)
        position_order = PositionOrder.objects.get(pk=pos)
        product = position_order.product_id

        vegetopps = (Products.objects.filter(type_of_ingredient="1").filter(
            is_active=True).order_by("product_name"))
        beeftopps = (Products.objects.filter(type_of_ingredient="2").filter(
            is_active=True).order_by("product_name"))
        cheesetopps = (Products.objects.filter(type_of_ingredient="3").filter(
            is_active=True).order_by("product_name"))
        extra_list = [4, 7, 8, 9, 10, 11]
        extratopps = (Products.objects.filter(
            type_of_ingredient__in=extra_list).filter(
                is_active=True).order_by("product_name"))
        cake = (Products.objects.filter(type_of_ingredient="5").filter(
            is_active=True).order_by("product_name"))

        vegecounter = 0
        beefcounter = 0
        cheesecounter = 0
        cakecounter = 0
        extracounter = 0
        extra_1_counter = 0
        extra_2_counter = 0
        extra_3_counter = 0
        extra_4_counter = 0

        addvege_pay_control = vegecounter
        beef_pay_control = beefcounter
        cheese_pay_control = cheesecounter
        cake_pay_control = cakecounter
        extra_pay_control = extracounter
        extra_1_pay_control = extra_1_counter
        extra_2_pay_control = extra_2_counter
        extra_3_pay_control = extra_3_counter
        extra_4_pay_control = extra_4_counter

        vege_pay = vegecounter
        beef_pay = beefcounter
        cheese_pay = cheesecounter
        cake_pay = cakecounter
        extra_pay = extracounter
        extra__1_pay = extra_1_counter
        extra__2_pay = extra_2_counter
        extra__3_pay = extra_3_counter
        extra__4_pay = extra_4_counter

        change_topps_vege = 0
        change_topps_beef = 0
        change_topps_cheese = 0
        change_topps_extra = 0
        change_topps_cake = 0
        change_topps_extra_1 = 0
        change_topps_extra_2 = 0
        change_topps_extra_3 = 0
        change_topps_extra_4 = 0

        ctx = {
            "order": order,
            "pizza": product,
            "toppings": toppings,
            "vegetopps": vegetopps,
            "beeftopps": beeftopps,
            "cheesetopps": cheesetopps,
            "extratopps": extratopps,
            "cake": cake,
            "vegecounter": vegecounter,
            "beefcounter": beefcounter,
            "cheesecounter": cheesecounter,
            "extracounter": extracounter,
            "cakecounter": cakecounter,
            "extra_1_counter": extra_1_counter,
            "extra_2_counter": extra_2_counter,
            "extra_3_counter": extra_3_counter,
            "extra_4_counter": extra_4_counter,
            "addvege_pay_control": addvege_pay_control,
            "beef_pay_control": beef_pay_control,
            "cheese_pay_control": cheese_pay_control,
            "extra_pay_control": extra_pay_control,
            "cake_pay_control": cake_pay_control,
            "extra_1_pay_control": extra_1_pay_control,
            "extra_2_pay_control": extra_2_pay_control,
            "extra_3_pay_control": extra_3_pay_control,
            "extra_4_pay_control": extra_4_pay_control,
            "vege_pay": vege_pay,
            "beef_pay": beef_pay,
            "cheese_pay": cheese_pay,
            "cake_pay": cake_pay,
            "extra_pay": extra_pay,
            "extra__1_pay": extra__1_pay,
            "extra__2_pay": extra__2_pay,
            "extra__3_pay": extra__3_pay,
            "extra__4_pay": extra__4_pay,
            "change_topps_vege": change_topps_vege,
            "change_topps_beef": change_topps_beef,
            "change_topps_cheese": change_topps_cheese,
            "change_topps_cake": change_topps_cake,
            "change_topps_extra": change_topps_extra,
            "change_topps_extra_1": change_topps_extra_1,
            "change_topps_extra_2": change_topps_extra_2,
            "change_topps_extra_3": change_topps_extra_3,
            "change_topps_extra_4": change_topps_extra_4,
        }
        return TemplateResponse(request, "add_pizza_freestyle.html", ctx)

    def post(self, request, order, pos):
        order = Orders.objects.get(pk=order)
        position_order = PositionOrder.objects.get(pk=pos)
        product = position_order.product_id

        input_add_topps = request.POST.get("input_add_topps")
        input_del_topps = request.POST.get("input_del_topps")
        input_add_cake = request.POST.get("input_add_cake")
        extra_price = request.POST.get("extra_price")
        extra_price = extra_price.replace(",", ".")

        new_position = position_order
        new_position.cake_info = ""
        new_position.product_id = product
        new_position.size_id = product.product_size
        new_position.price = product.price
        new_position.change_topps = ""
        new_position.save()

        if extra_price != "":
            new_position.extra_price = float(extra_price)
        else:
            new_position.extra_price = 0.00
        new_position.change_topps_info = input_del_topps + " " + input_add_topps
        new_position.cake_info = input_add_cake
        # new_position.order_id=order
        new_position.save()

        return redirect("add_pizza_freestyle_to_order",
                        order=order.id,
                        pos=new_position.id)


@method_decorator(login_required, name="dispatch")
class ChangeToppsView(PermissionRequiredMixin, View):
    permission_required = "babilon_v1.change_positionorder"

    def get(self, request, order, prod):
        order = Orders.objects.get(pk=order)
        product = Products.objects.get(id=prod)
        new_position = PositionOrder()
        new_position.cake_info = ""
        new_position.product_id = product
        new_position.size_id = product.product_size
        new_position.price = product.price
        # new_position.extra_price=0.00
        new_position.change_topps = ""
        new_position.save()

        # for topp in product.toppings.all():
        #     new_position.toppings.add(topp)
        #     new_position.save()

        vegetopps = (Products.objects.filter(type_of_ingredient="1").filter(
            is_active=True).order_by("product_name"))
        beeftopps = (Products.objects.filter(type_of_ingredient="2").filter(
            is_active=True).order_by("product_name"))
        cheesetopps = (Products.objects.filter(type_of_ingredient="3").filter(
            is_active=True).order_by("product_name"))
        extra_list = [4, 7, 8, 9, 10, 11]
        extratopps = (Products.objects.filter(
            type_of_ingredient__in=extra_list).filter(
                is_active=True).order_by("product_name"))
        cake = (Products.objects.filter(type_of_ingredient="5").filter(
            is_active=True).order_by("product_name"))

        toppings = []
        for el in product.toppings.all():
            toppings.append(el)
        vegecounter = 0
        beefcounter = 0
        cheesecounter = 0
        cakecounter = 0
        extracounter = 0
        extra_1_counter = 0
        extra_2_counter = 0
        extra_3_counter = 0
        extra_4_counter = 0
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
            if el.type_of_ingredient == 8:
                extra_1_counter += 1
            if el.type_of_ingredient == 9:
                extra_2_counter += 1
            if el.type_of_ingredient == 10:
                extra_3_counter += 1
            if el.type_of_ingredient == 11:
                extra_4_counter += 1
        addvege_pay_control = vegecounter
        beef_pay_control = beefcounter
        cheese_pay_control = cheesecounter
        cake_pay_control = cakecounter
        extra_pay_control = extracounter
        extra_1_pay_control = extra_1_counter
        extra_2_pay_control = extra_2_counter
        extra_3_pay_control = extra_3_counter
        extra_4_pay_control = extra_4_counter

        vege_pay = vegecounter
        beef_pay = beefcounter
        cheese_pay = cheesecounter
        cake_pay = cakecounter
        extra_pay = extracounter
        extra__1_pay = extra_1_counter
        extra__2_pay = extra_2_counter
        extra__3_pay = extra_3_counter
        extra__4_pay = extra_4_counter

        change_topps_vege = 0
        change_topps_beef = 0
        change_topps_cheese = 0
        change_topps_extra = 0
        change_topps_cake = 0
        change_topps_extra_1 = 0
        change_topps_extra_2 = 0
        change_topps_extra_3 = 0
        change_topps_extra_4 = 0

        ctx = {
            "order": order,
            "pizza": product,
            "new_position": new_position,
            "toppings": toppings,
            "vegetopps": vegetopps,
            "beeftopps": beeftopps,
            "cheesetopps": cheesetopps,
            "extratopps": extratopps,
            "cake": cake,
            "vegecounter": vegecounter,
            "beefcounter": beefcounter,
            "cheesecounter": cheesecounter,
            "extracounter": extracounter,
            "cakecounter": cakecounter,
            "extra_1_counter": extra_1_counter,
            "extra_2_counter": extra_2_counter,
            "extra_3_counter": extra_3_counter,
            "extra_4_counter": extra_4_counter,
            "addvege_pay_control": addvege_pay_control,
            "beef_pay_control": beef_pay_control,
            "cheese_pay_control": cheese_pay_control,
            "extra_pay_control": extra_pay_control,
            "cake_pay_control": cake_pay_control,
            "extra_1_pay_control": extra_1_pay_control,
            "extra_2_pay_control": extra_2_pay_control,
            "extra_3_pay_control": extra_3_pay_control,
            "extra_4_pay_control": extra_4_pay_control,
            "vege_pay": vege_pay,
            "beef_pay": beef_pay,
            "cheese_pay": cheese_pay,
            "cake_pay": cake_pay,
            "extra_pay": extra_pay,
            "extra__1_pay": extra__1_pay,
            "extra__2_pay": extra__2_pay,
            "extra__3_pay": extra__3_pay,
            "extra__4_pay": extra__4_pay,
            "change_topps_vege": change_topps_vege,
            "change_topps_beef": change_topps_beef,
            "change_topps_cheese": change_topps_cheese,
            "change_topps_cake": change_topps_cake,
            "change_topps_extra": change_topps_extra,
            "change_topps_extra_1": change_topps_extra_1,
            "change_topps_extra_2": change_topps_extra_2,
            "change_topps_extra_3": change_topps_extra_3,
            "change_topps_extra_4": change_topps_extra_4,
        }
        return TemplateResponse(request, "change_topps.html", ctx)

    def post(self, request, order, prod):
        order = Orders.objects.get(pk=order)
        position_order = PositionOrder.objects.get(
            pk=request.POST.get("position_order"))

        input_add_topps = request.POST.get("input_add_topps")
        input_del_topps = request.POST.get("input_del_topps")
        input_add_cake = request.POST.get("input_add_cake")
        extra_price = request.POST.get("extra_price")
        extra_price = extra_price.replace(",", ".")
        if extra_price != "":
            position_order.extra_price = float(extra_price)
        else:
            position_order.extra_price = 0.00

        position_order.change_topps_info = input_del_topps + " " + input_add_topps
        position_order.cake_info = input_add_cake
        # position_order.order_id=order
        position_order.save()

        return redirect("add_modyfi_pizza_to_order",
                        order=order.id,
                        pos=position_order.id)


@method_decorator(login_required, name="dispatch")
class AddModyfiToOrderView(PermissionRequiredMixin, View):
    permission_required = "babilon_v1.add_orders"

    def get(self, request, order, pos):
        user = request.user
        categorys = Category.objects.all()
        order = Orders.objects.get(pk=order)
        pizza = PositionOrder.objects.get(pk=pos)
        product = pizza.product_id
        other_size = Products.objects.filter(
            product_name=pizza.product_id.product_name).filter(is_active=True)
        cakes = (Products.objects.filter(type_of_ingredient="5").filter(
            is_active=True).order_by("product_name"))
        souse_pay = Products.objects.filter(type_of_ingredient="6").filter(
            is_active=True)
        souse_free = Products.objects.filter(type_of_ingredient="7").filter(
            is_active=True)
        positions_on_order = PositionOrder.objects.filter(order_id=order.id)

        ctx = {
            "order": order,
            "pizza": pizza,
            "product": product,
            "other_size": other_size,
            "positions_on_order": positions_on_order,
            "categorys": categorys,
            "cakes": cakes,
            "souse_pay": souse_pay,
            "souse_free": souse_free,
        }
        return TemplateResponse(request, "add_modyfi_pizza_to_order.html", ctx)

    def post(self, request, order, pos):
        user = request.user
        order = Orders.objects.get(pk=order)
        new_position = PositionOrder.objects.get(pk=pos)
        product = Products.objects.get(pk=new_position.product_id.id)

        if "delete" in request.POST:
            new_position.extra_price = 0.00
            new_position.change_topps_info = ""
            new_position.sauces_free = ""
            new_position.sauces_pay = ""
            new_position.cake_info = ""
            new_position.info = ""
            new_position.discount = 0
            new_position.save()
            return redirect("add_modyfi_pizza_to_order",
                            order=order.id,
                            pos=new_position.id)

        add = request.POST.get("add")
        quantity = request.POST.get("quantity")
        extra_price = request.POST.get("extra_price")
        info = request.POST.get("info")
        cake_change = request.POST.get("cake_change")
        add_sauces_free = request.POST.get("add_sauces_free")
        add_sauces_pay = request.POST.get("add_sauces_pay")

        productId = request.POST.get("productId")
        orderPositionId = request.POST.get("orderPosition")
        discount = request.POST.get("discount")

        new_position.order_id = order
        new_position.save()
        if quantity != None:
            if int(quantity) > 0:
                new_position.quantity = int(quantity)
                new_position.save()
        if discount != "":
            if int(discount != 0) and discount != None:
                new_position.discount = int(discount)
                new_position.save()
                order.promo = True
            # order.save()
        else:
            new_position.discount = 0
            new_position.save()
            order.promo = True
        product = new_position
        price = request.POST.get("price")

        price_org = product.price
        if price != "":
            if price != None:
                price = float(price)
                if price < price_org and price != 0:
                    new_position.price = price
                    new_position.save()
                    order.promo = True
                    # order.save()
        else:
            new_position.price = 0.00
            new_position.save()
            order.promo = True
        if extra_price != None:
            new_position.extra_price = float(extra_price.replace(",", "."))
            new_position.save()
        else:
            new_position.extra_price = new_position.extra_price
            new_position.save()
        if info != "":
            new_position.info = info
            new_position.save()
        if cake_change != "":
            new_position.cake_info = cake_change
            new_position.save()
        if add_sauces_free != "":
            new_position.sauces_free = add_sauces_free
            new_position.save()
        if add_sauces_pay != "":
            new_position.sauces_pay = add_sauces_pay
            new_position.save()

        changeTopps = request.POST.get("changeTopps")

        categorys = Category.objects.all()
        # order=Orders.objects.get(pk=order.id)
        souse_pay = Products.objects.filter(type_of_ingredient="6").filter(
            is_active=True)
        souse_free = Products.objects.filter(type_of_ingredient="7").filter(
            is_active=True)
        order.save()
        return redirect("products_category", pk=1)


@method_decorator(login_required, name="dispatch")
class UpdatePizzaToOrderView(PermissionRequiredMixin, View):
    permission_required = "babilon_v1.add_orders"

    def get(self, request, order, pos):
        user = request.user
        categorys = Category.objects.all()
        order = Orders.objects.get(pk=order)
        position_order = PositionOrder.objects.get(pk=pos)
        position_order.save()
        pizza = position_order.product_id
        other_size = Products.objects.filter(product_name=pizza.product_name)
        cakes = (Products.objects.filter(type_of_ingredient="5").filter(
            is_active=True).order_by("product_name"))
        souse_pay = Products.objects.filter(type_of_ingredient="6").filter(
            is_active=True)
        souse_free = Products.objects.filter(type_of_ingredient="7").filter(
            is_active=True)
        positions_on_order = PositionOrder.objects.filter(order_id=order.id)

        position_order.save()
        pos = position_order
        ctx = {
            "order": order,
            "pos": pos,
            "pizza": pizza,
            "other_size": other_size,
            "positions_on_order": positions_on_order,
            "categorys": categorys,
            "cakes": cakes,
            "souse_pay": souse_pay,
            "souse_free": souse_free,
        }
        return TemplateResponse(request, "update_pizza_to_order.html", ctx)

    def post(self, request, order, pos):
        user = request.user
        order = Orders.objects.get(pk=order)
        position_order = PositionOrder.objects.get(pk=pos)
        pizza = position_order.product_id

        if "delete" in request.POST:
            position_order.extra_price = 0.00
            position_order.change_topps_info = ""
            position_order.sauces_free = ""
            position_order.sauces_pay = ""
            position_order.cake_info = ""
            position_order.info = ""
            position_order.discount = 0
            position_order.save()
            return redirect("update_pizza_to_order",
                            order=order.id,
                            pos=position_order.id)

        add = request.POST.get("add")
        size = request.POST.get("size")
        price = request.POST.get("price")

        quantity = request.POST.get("quantity")
        extra_price = request.POST.get("extra_price")
        info = request.POST.get("info")
        cake_change = request.POST.get("cake_change")
        add_sauces_free = request.POST.get("add_sauces_free")
        add_sauces_pay = request.POST.get("add_sauces_pay")

        orderPositionId = request.POST.get("orderPosition")
        discount = request.POST.get("discount")

        position_order.cake_info = cake_change
        position_order.save()

        productId = request.POST.get("productId")
        product = Products.objects.get(pk=productId)
        price = request.POST.get("price")

        price_org = product.price

        if price != "":
            price = float(price)
            if price != price_org and price != 0.00:

                position_order.price = price
                position_order.save()
                order.promo = True
                # order.save()
            else:
                position_order.price = product.price
                position_order.save()
        else:
            price = 0.00
            position_order.price = price
            position_order.save()
            order.promo = True
        if discount != "":
            if int(discount) != 0 and discount != None:
                position_order.discount = int(discount)
                position_order.save()

                # print(price_org)
                order.promo = True
                # order.save()
        else:
            position_order.discount = 0
            position_order.save()
            order.promo = True

        # if price!="":
        #     if price!=price_org and price!=0:
        #         position_order.price=price
        #         position_order.save()
        #         order.promo=True
        #         # order.save()
        #     else:
        #         position_order.price=product.price
        #         position_order.save()
        # else:
        #     position_order.price=0
        #     position_order.save()
        #     order.promo=True
        if size:
            size = ProductSize.objects.get(pk=size)
            position_order.size_id = size
            price = price.replace(",", ".")
            position_order.price = float(price)
            position_order.save()
        if quantity != None:
            if int(quantity) > 0:
                position_order.quantity = int(quantity)
                position_order.save()

        if int(discount != 0) and discount != None and discount != "":
            position_order.discount = int(discount)
            position_order.save()
            order.promo = True
            # order.save()
        else:
            position_order.discount = 0
            position_order.save()
            order.promo = True

        if extra_price != None:
            position_order.extra_price = float(extra_price.replace(",", "."))
            position_order.save()
        else:
            position_order.extra_price = position_order.extra_price
            position_order.save()
        if info != "":
            position_order.info = info
            position_order.save()
        else:
            position_order.info = ""
            position_order.save()
        if cake_change != "":
            position_order.cake_info = cake_change
            position_order.save()
        if add_sauces_free != "":
            position_order.sauces_free = add_sauces_free
            position_order.save()
        if add_sauces_pay != "":
            position_order.sauces_pay = add_sauces_pay
            position_order.save()

        changeTopps = request.POST.get("changeTopps")
        order.save()
        if add:
            return redirect("products_category", pk=1)
        else:
            return redirect("update_pizza_to_order",
                            order=order.id,
                            pos=position_order.id)


@method_decorator(login_required, name="dispatch")
class UpdateProductToOrderView(PermissionRequiredMixin, View):
    permission_required = "babilon_v1.add_orders"

    def get(self, request, order, pos):
        user = request.user
        categorys = Category.objects.all()
        order = Orders.objects.get(pk=order)
        position_order = PositionOrder.objects.get(pk=pos)
        position_order.save()
        product = position_order.product_id
        other_size = Products.objects.filter(product_name=product.product_name)
        cakes = (Products.objects.filter(type_of_ingredient="5").filter(
            is_active=True).order_by("product_name"))
        souse_pay = Products.objects.filter(type_of_ingredient="6").filter(
            is_active=True)
        souse_free = Products.objects.filter(type_of_ingredient="7").filter(
            is_active=True)
        positions_on_order = PositionOrder.objects.filter(order_id=order.id)

        position_order.save()
        pos = position_order
        ctx = {
            "order": order,
            "pos": pos,
            "product": product,
            "other_size": other_size,
            "positions_on_order": positions_on_order,
            "categorys": categorys,
            "cakes": cakes,
            "souse_pay": souse_pay,
            "souse_free": souse_free,
        }
        return TemplateResponse(request, "update_product_to_order.html", ctx)

    def post(self, request, order, pos):
        user = request.user
        order = Orders.objects.get(pk=order)
        position_order = PositionOrder.objects.get(pk=pos)
        product = position_order.product_id

        if "delete" in request.POST:
            position_order.extra_price = 0.00
            position_order.sauces_free = ""
            position_order.sauces_pay = ""
            position_order.cake_info = ""
            position_order.info = ""
            position_order.discount = 0
            position_order.save()
            return redirect("update_product_to_order",
                            order=order.id,
                            pos=position_order.id)

        add = request.POST.get("add")
        size = request.POST.get("size")
        price = request.POST.get("price")

        quantity = request.POST.get("quantity")
        extra_price = request.POST.get("extra_price")
        info = request.POST.get("info")
        cake_change = request.POST.get("cake_change")
        add_sauces_free = request.POST.get("add_sauces_free")
        add_sauces_pay = request.POST.get("add_sauces_pay")

        productId = request.POST.get("productId")
        orderPositionId = request.POST.get("orderPosition")
        discount = request.POST.get("discount")

        position_order.cake_info = cake_change
        position_order.save()
        if size:
            size = ProductSize.objects.get(pk=size)
            position_order.size_id = size
            price = price.replace(",", ".")
            position_order.price = float(price)
            position_order.save()
        if quantity != None:
            if int(quantity) > 0:
                position_order.quantity = int(quantity)
                position_order.save()

        product = position_order
        price = request.POST.get("price")
        price = float(price)
        price_org = product.price

        if price != "":
            price = float(price)
            if price < price_org and price != 0.00:

                position_order.price = price
                position_order.save()
                order.promo = True
                # order.save()
            else:
                position_order.price = product.price
                position_order.save()
        else:
            price = 0.00
            position_order.price = price
            position_order.save()
            order.promo = True

        if discount != "":
            if int(discount) != 0 and discount != None:
                position_order.discount = int(discount)
                position_order.save()

                # print(price_org)
                order.promo = True
                # order.save()
        else:
            position_order.discount = 0
            position_order.save()

        if extra_price != None:
            position_order.extra_price = float(extra_price.replace(",", "."))
            position_order.save()
        else:
            position_order.extra_price = position_order.extra_price
            position_order.save()
        if info != "":
            position_order.info = info
            position_order.save()
        else:
            position_order.info = ""
            position_order.save()
        if cake_change != "":
            position_order.cake_info = cake_change
            position_order.save()
        if add_sauces_free != "":
            position_order.sauces_free = add_sauces_free
            position_order.save()
        if add_sauces_pay != "":
            position_order.sauces_pay = add_sauces_pay
            position_order.save()

        changeTopps = request.POST.get("changeTopps")
        order.save()
        if add:
            return redirect("products_category", pk=1)
        else:
            return redirect("update_pizza_to_order",
                            order=order.id,
                            pos=position_order.id)


@method_decorator(login_required, name="dispatch")
class UpdateToppsView(PermissionRequiredMixin, View):
    permission_required = "babilon_v1.change_positionorder"

    def get(self, request, order, pos):
        order = Orders.objects.get(pk=order)
        new_position = PositionOrder.objects.get(pk=pos)
        product = Products.objects.get(id=new_position.product_id.id)
        new_position.cake_info = ""
        new_position.product_id = product
        new_position.size_id = product.product_size
        new_position.price = product.price
        new_position.change_topps = ""
        new_position.save()

        # for topp in product.toppings.all():
        #     new_position.toppings.add(topp)
        #     new_position.save()

        vegetopps = (Products.objects.filter(type_of_ingredient="1").filter(
            is_active=True).order_by("product_name"))
        beeftopps = (Products.objects.filter(type_of_ingredient="2").filter(
            is_active=True).order_by("product_name"))
        cheesetopps = (Products.objects.filter(type_of_ingredient="3").filter(
            is_active=True).order_by("product_name"))
        extra_list = [4, 7, 8, 9, 10, 11]
        extratopps = (Products.objects.filter(
            type_of_ingredient__in=extra_list).filter(
                is_active=True).order_by("product_name"))
        cake = (Products.objects.filter(type_of_ingredient="5").filter(
            is_active=True).order_by("product_name"))

        toppings = []
        for el in product.toppings.all():
            toppings.append(el)
        vegecounter = 0
        beefcounter = 0
        cheesecounter = 0
        cakecounter = 0
        extracounter = 0
        extra_1_counter = 0
        extra_2_counter = 0
        extra_3_counter = 0
        extra_4_counter = 0
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
            if el.type_of_ingredient == 8:
                extra_1_counter += 1
            if el.type_of_ingredient == 9:
                extra_2_counter += 1
            if el.type_of_ingredient == 10:
                extra_3_counter += 1
            if el.type_of_ingredient == 11:
                extra_4_counter += 1
        addvege_pay_control = vegecounter
        beef_pay_control = beefcounter
        cheese_pay_control = cheesecounter
        cake_pay_control = cakecounter
        extra_pay_control = extracounter
        extra_1_pay_control = extra_1_counter
        extra_2_pay_control = extra_2_counter
        extra_3_pay_control = extra_3_counter
        extra_4_pay_control = extra_4_counter

        vege_pay = vegecounter
        beef_pay = beefcounter
        cheese_pay = cheesecounter
        cake_pay = cakecounter
        extra_pay = extracounter
        extra__1_pay = extra_1_counter
        extra__2_pay = extra_2_counter
        extra__3_pay = extra_3_counter
        extra__4_pay = extra_4_counter

        change_topps_vege = 0
        change_topps_beef = 0
        change_topps_cheese = 0
        change_topps_extra = 0
        change_topps_cake = 0
        change_topps_extra_1 = 0
        change_topps_extra_2 = 0
        change_topps_extra_3 = 0
        change_topps_extra_4 = 0

        ctx = {
            "order": order,
            "pizza": product,
            "new_position": new_position,
            "toppings": toppings,
            "vegetopps": vegetopps,
            "beeftopps": beeftopps,
            "cheesetopps": cheesetopps,
            "extratopps": extratopps,
            "cake": cake,
            "vegecounter": vegecounter,
            "beefcounter": beefcounter,
            "cheesecounter": cheesecounter,
            "extracounter": extracounter,
            "cakecounter": cakecounter,
            "extra_1_counter": extra_1_counter,
            "extra_2_counter": extra_2_counter,
            "extra_3_counter": extra_3_counter,
            "extra_4_counter": extra_4_counter,
            "addvege_pay_control": addvege_pay_control,
            "beef_pay_control": beef_pay_control,
            "cheese_pay_control": cheese_pay_control,
            "extra_pay_control": extra_pay_control,
            "cake_pay_control": cake_pay_control,
            "extra_1_pay_control": extra_1_pay_control,
            "extra_2_pay_control": extra_2_pay_control,
            "extra_3_pay_control": extra_3_pay_control,
            "extra_4_pay_control": extra_4_pay_control,
            "vege_pay": vege_pay,
            "beef_pay": beef_pay,
            "cheese_pay": cheese_pay,
            "cake_pay": cake_pay,
            "extra_pay": extra_pay,
            "extra__1_pay": extra__1_pay,
            "extra__2_pay": extra__2_pay,
            "extra__3_pay": extra__3_pay,
            "extra__4_pay": extra__4_pay,
            "change_topps_vege": change_topps_vege,
            "change_topps_beef": change_topps_beef,
            "change_topps_cheese": change_topps_cheese,
            "change_topps_cake": change_topps_cake,
            "change_topps_extra": change_topps_extra,
            "change_topps_extra_1": change_topps_extra_1,
            "change_topps_extra_2": change_topps_extra_2,
            "change_topps_extra_3": change_topps_extra_3,
            "change_topps_extra_4": change_topps_extra_4,
        }
        return TemplateResponse(request, "update_topps.html", ctx)

    def post(self, request, order, pos):
        order = Orders.objects.get(pk=order)
        position_order = PositionOrder.objects.get(
            pk=request.POST.get("position_order"))

        input_add_topps = request.POST.get("input_add_topps")
        input_del_topps = request.POST.get("input_del_topps")
        input_add_cake = request.POST.get("input_add_cake")
        extra_price = request.POST.get("extra_price")
        extra_price = extra_price.replace(",", ".")
        if extra_price != "":
            position_order.extra_price = float(extra_price)
        else:
            position_order.extra_price = 0.00
        position_order.change_topps_info = input_del_topps + " " + input_add_topps
        position_order.cake_info = input_add_cake
        # position_order.order_id=order
        position_order.save()

        return redirect("add_modyfi_pizza_to_order",
                        order=order.id,
                        pos=position_order.id)


@method_decorator(login_required, name="dispatch")
class Secend_Half_Pizza_SearchView(PermissionRequiredMixin, View):
    permission_required = "babilon_v1.add_orders"

    def get(self, request, order, pk, size):
        pizza_left = Products.objects.get(id=pk)
        size = ProductSize.objects.get(pk=size)
        categorys = Category.objects.all()

        order = Orders.objects.get(pk=order)
        souse_pay = Products.objects.filter(type_of_ingredient="6").filter(
            is_active=True)
        souse_free = Products.objects.filter(type_of_ingredient="7").filter(
            is_active=True)
        cakes = (Products.objects.filter(type_of_ingredient="5").filter(
            is_active=True).order_by("product_name"))
        pizzas = (Products.objects.filter(category=1).filter(
            product_size=size).filter(is_pizza_freestyle=False).filter(
                is_active=True))
        positions_on_order = PositionOrder.objects.filter(order_id=order.id)

        ctx = {
            "order": order,
            "size": size,
            "pizzas": pizzas,
            "categorys": categorys,
            "cakes": cakes,
            "souse_pay": souse_pay,
            "souse_free": souse_free,
        }
        return TemplateResponse(request, "pizza_filter_for_secendhalf.html",
                                ctx)

    def post(self, request, order, pk, size):
        search = request.POST.get("search")
        secend_half = request.POST.get("secend_half")
        if search != "":
            pizza_left = Products.objects.get(id=pk)
            size = ProductSize.objects.get(pk=size)
            categorys = Category.objects.all()
            order = Orders.objects.get(pk=order)
            souse_pay = Products.objects.filter(type_of_ingredient="6").filter(
                is_active=True)
            souse_free = Products.objects.filter(
                type_of_ingredient="7").filter(is_active=True)
            cakes = (Products.objects.filter(type_of_ingredient="5").filter(
                is_active=True).order_by("product_name"))
            pizzas = (Products.objects.filter(product_size=size).filter(
                is_pizza_freestyle=False).filter(is_active=True))
            pizzas = pizzas.filter(Q(pizza_number=search))
            positions_on_order = PositionOrder.objects.filter(
                order_id=order.id)

            ctx = {
                "order": order,
                "size": size,
                "pizzas": pizzas,
                "categorys": categorys,
                "cakes": cakes,
                "souse_pay": souse_pay,
                "souse_free": souse_free,
            }
            return TemplateResponse(request,
                                    "pizza_filter_for_secendhalf.html", ctx)
        else:
            if secend_half != "":
                order = Orders.objects.get(pk=order)
                pizza_left = Products.objects.get(id=pk)
                size = ProductSize.objects.get(pk=size)
                pizza_rigth = Products.objects.get(id=secend_half)
                price_left = pizza_left.price
                price_right = pizza_rigth.price
                if price_left > price_right:
                    price = price_left
                elif price_left == price_right:
                    price = price_left
                else:
                    price = price_right

                pizza_half = PositionOrder()
                pizza_half.halfpizza_name = ("Lewa - " +
                                             str(pizza_left.product_name) +
                                             ", Prawa - " +
                                             str(pizza_rigth.product_name))
                pizza_half.price = price
                pizza_half.product_id = pizza_left
                pizza_half.product_id_pizza_right = pizza_rigth
                pizza_half.size_id = size
                pizza_half.pizza_half = True
                pizza_half.save()

                return redirect("left_and_right_halfpizza",
                                pizza_half=pizza_half.id,
                                order=order.id)
            else:
                pizza_left = Products.objects.get(id=pk)
                size = ProductSize.objects.get(pk=size)
                order = Orders.objects.get(pk=order)
                return redirect(
                    "add_secend_halfpizza",
                    order=order.id,
                    pk=pizza_left.id,
                    size=size.id,
                )


@method_decorator(login_required, name="dispatch")
class Left_And_Right_Half_PizzaView(PermissionRequiredMixin, View):
    permission_required = "babilon_v1.add_orders"

    def get(self, request, pizza_half, order):
        categorys = Category.objects.all()
        pizza_half = PositionOrder.objects.get(pk=pizza_half)
        user = request.user
        categorys = Category.objects.all()
        order = Orders.objects.get(pk=order)
        cakes = (Products.objects.filter(type_of_ingredient="5").filter(
            is_active=True).order_by("product_name"))
        souse_pay = Products.objects.filter(type_of_ingredient="6").filter(
            is_active=True)
        souse_free = Products.objects.filter(type_of_ingredient="7").filter(
            is_active=True)
        positions_on_order = PositionOrder.objects.filter(order_id=order.id)

        ctx = {
            "pizza_half": pizza_half,
            "order": order,
            "cakes": cakes,
            "positions_on_order": positions_on_order,
            "categorys": categorys,
            "souse_pay": souse_pay,
            "souse_free": souse_free,
        }
        return TemplateResponse(request, "add_secendhalf_to_order.html", ctx)

    def post(self, request, pizza_half, order):
        user = request.user
        pizza_half = PositionOrder.objects.get(pk=pizza_half)
        order = Orders.objects.get(pk=order)

        if "delete" in request.POST:
            pizza_half.extra_price = 0.00
            pizza_half.change_topps_info = ""
            pizza_half.change_topps_info_other_side = ""
            pizza_half.sauces_free = ""
            pizza_half.sauces_pay = ""
            pizza_half.cake_info = ""
            pizza_half.info = ""
            pizza_half.discount = 0
            pizza_half.save()
            return redirect("left_and_right_halfpizza",
                            order=order.id,
                            pizza_half=pizza_half.id)

        add = request.POST.get("add")
        quantity = request.POST.get("quantity")
        extra_price = request.POST.get("extra_price")
        info = request.POST.get("info")
        add_sauces_free = request.POST.get("add_sauces_free")
        add_sauces_pay = request.POST.get("add_sauces_pay")

        discount = request.POST.get("discount")
        price = request.POST.get("price")

        pizza_half.order_id = order
        pizza_half.save()
        positions_on_order = PositionOrder.objects.filter(order_id=order.id)
        if quantity != None:
            if int(quantity) > 0:
                pizza_half.quantity = int(quantity)
                pizza_half.save()

        if int(discount) != 0 and discount != None and discount != "":
            pizza_half.discount = int(discount)
            pizza_half.save()
            order.promo = True
            # order.save()
        else:
            pizza_half.discount = 0
            pizza_half.save()
            order.promo = True

        # productId = request.POST.get('productId')
        product = pizza_half
        price = request.POST.get("price")
        price_org = pizza_half.price

        if price != "":
            price = float(price)
            if price < price_org and price != 0.00:

                pizza_half.price = price
                pizza_half.save()
                order.promo = True
                # order.save()
            else:
                pizza_half.price = product.price
                pizza_half.save()
        else:
            price = 0.00
            pizza_half.price = price
            pizza_half.save()
            order.promo = True
        print(extra_price)
        if extra_price != None and extra_price != "":
            pizza_half.extra_price = float(extra_price.replace(",", "."))
            pizza_half.save()
        else:
            pizza_half.extra_price = 0.00
            pizza_half.save()

        if info != "":
            pizza_half.info = info
            pizza_half.save()
        if add_sauces_free != "":
            pizza_half.sauces_free = add_sauces_free
            pizza_half.save()
        if add_sauces_pay != "":
            pizza_half.sauces_pay = add_sauces_pay
            pizza_half.save()

        changeTopps = request.POST.get("changeTopps")

        categorys = Category.objects.all()
        order.save()
        if add:
            return redirect("products_category", pk=1)
        else:
            return redirect("left_and_right_halfpizza",
                            order=order.id,
                            pizza_half=pizza_half.id)


@method_decorator(login_required, name="dispatch")
class ChangeLeftToppsView(PermissionRequiredMixin, View):
    permission_required = "babilon_v1.change_positionorder"

    def get(self, request, order, pos):

        order = Orders.objects.get(pk=order)
        new_position = PositionOrder.objects.get(pk=pos)
        product = Products.objects.get(id=new_position.product_id.id)
        new_position.cake_info = ""
        new_position.product_id = product
        new_position.size_id = product.product_size
        new_position.price = product.price
        new_position.change_topps_info = ""
        new_position.change_topps_info_id = ""
        new_position.save()

        vegetopps = (Products.objects.filter(type_of_ingredient="1").filter(
            is_active=True).order_by("product_name"))
        beeftopps = (Products.objects.filter(type_of_ingredient="2").filter(
            is_active=True).order_by("product_name"))
        cheesetopps = (Products.objects.filter(type_of_ingredient="3").filter(
            is_active=True).order_by("product_name"))
        extra_list = [4, 7, 8, 9, 10, 11]
        extratopps = (Products.objects.filter(
            type_of_ingredient__in=extra_list).filter(
                is_active=True).order_by("product_name"))
        cake = (Products.objects.filter(type_of_ingredient="5").filter(
            is_active=True).order_by("product_name"))

        toppings = []
        for el in product.toppings.all():
            toppings.append(el)
        vegecounter = 0
        beefcounter = 0
        cheesecounter = 0
        cakecounter = 0
        extracounter = 0
        extra_1_counter = 0
        extra_2_counter = 0
        extra_3_counter = 0
        extra_4_counter = 0
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
            if el.type_of_ingredient == 8:
                extra_1_counter += 1
            if el.type_of_ingredient == 9:
                extra_2_counter += 1
            if el.type_of_ingredient == 10:
                extra_3_counter += 1
            if el.type_of_ingredient == 11:
                extra_4_counter += 1
        addvege_pay_control = vegecounter
        beef_pay_control = beefcounter
        cheese_pay_control = cheesecounter
        cake_pay_control = cakecounter
        extra_pay_control = extracounter
        extra_1_pay_control = extra_1_counter
        extra_2_pay_control = extra_2_counter
        extra_3_pay_control = extra_3_counter
        extra_4_pay_control = extra_4_counter

        vege_pay = vegecounter
        beef_pay = beefcounter
        cheese_pay = cheesecounter
        cake_pay = cakecounter
        extra_pay = extracounter
        extra__1_pay = extra_1_counter
        extra__2_pay = extra_2_counter
        extra__3_pay = extra_3_counter
        extra__4_pay = extra_4_counter

        change_topps_vege = 0
        change_topps_beef = 0
        change_topps_cheese = 0
        change_topps_extra = 0
        change_topps_cake = 0
        change_topps_extra_1 = 0
        change_topps_extra_2 = 0
        change_topps_extra_3 = 0
        change_topps_extra_4 = 0

        ctx = {
            "order": order,
            "pizza": product,
            "new_position": new_position,
            "toppings": toppings,
            "vegetopps": vegetopps,
            "beeftopps": beeftopps,
            "cheesetopps": cheesetopps,
            "extratopps": extratopps,
            "cake": cake,
            "vegecounter": vegecounter,
            "beefcounter": beefcounter,
            "cheesecounter": cheesecounter,
            "extracounter": extracounter,
            "cakecounter": cakecounter,
            "extra_1_counter": extra_1_counter,
            "extra_2_counter": extra_2_counter,
            "extra_3_counter": extra_3_counter,
            "extra_4_counter": extra_4_counter,
            "addvege_pay_control": addvege_pay_control,
            "beef_pay_control": beef_pay_control,
            "cheese_pay_control": cheese_pay_control,
            "extra_pay_control": extra_pay_control,
            "cake_pay_control": cake_pay_control,
            "extra_1_pay_control": extra_1_pay_control,
            "extra_2_pay_control": extra_2_pay_control,
            "extra_3_pay_control": extra_3_pay_control,
            "extra_4_pay_control": extra_4_pay_control,
            "vege_pay": vege_pay,
            "beef_pay": beef_pay,
            "cheese_pay": cheese_pay,
            "cake_pay": cake_pay,
            "extra_pay": extra_pay,
            "extra__1_pay": extra__1_pay,
            "extra__2_pay": extra__2_pay,
            "extra__3_pay": extra__3_pay,
            "extra__4_pay": extra__4_pay,
            "change_topps_vege": change_topps_vege,
            "change_topps_beef": change_topps_beef,
            "change_topps_cheese": change_topps_cheese,
            "change_topps_cake": change_topps_cake,
            "change_topps_extra": change_topps_extra,
            "change_topps_extra_1": change_topps_extra_1,
            "change_topps_extra_2": change_topps_extra_2,
            "change_topps_extra_3": change_topps_extra_3,
            "change_topps_extra_4": change_topps_extra_4,
        }
        return TemplateResponse(request, "change_topps_pizza_left.html", ctx)

    def post(self, request, order, pos):
        order = Orders.objects.get(pk=order)
        # pos=PositionOrder.objects.get(pk=pos)
        # position_order = PositionOrder.objects.get(pk=request.POST.get('position_order'))
        position_order = PositionOrder.objects.get(pk=pos)

        input_add_topps = request.POST.get("input_add_topps")
        input_del_topps = request.POST.get("input_del_topps")
        input_add_cake = request.POST.get("input_add_cake")
        extra_price = request.POST.get("extra_price")

        if extra_price != "":
            extra_price = extra_price.replace(",", ".")
            position_order.extra_price_left = float(extra_price)
        else:
            position_order.extra_price_left = 0.00
        position_order.change_topps_info = input_del_topps + " " + input_add_topps
        position_order.order_id = order
        if position_order.extra_price_right > position_order.extra_price_left:
            position_order.extra_price = position_order.extra_price_right
        else:
            position_order.extra_price = position_order.extra_price_left
        position_order.save()

        return redirect("update_halfpizza_to_order",
                        pos=position_order.id,
                        order=order.id)


@method_decorator(login_required, name="dispatch")
class ChangeRightToppsView(PermissionRequiredMixin, View):
    permission_required = "babilon_v1.change_positionorder"

    def get(self, request, order, pos):
        order = Orders.objects.get(pk=order)
        new_position = PositionOrder.objects.get(pk=pos)
        product = Products.objects.get(
            id=new_position.product_id_pizza_right.id)
        new_position.cake_info = ""
        new_position.change_topps = ""
        new_position.save()

        vegetopps = (Products.objects.filter(type_of_ingredient="1").filter(
            is_active=True).order_by("product_name"))
        beeftopps = (Products.objects.filter(type_of_ingredient="2").filter(
            is_active=True).order_by("product_name"))
        cheesetopps = (Products.objects.filter(type_of_ingredient="3").filter(
            is_active=True).order_by("product_name"))
        extra_list = [4, 7, 8, 9, 10, 11]
        extratopps = (Products.objects.filter(
            type_of_ingredient__in=extra_list).filter(
                is_active=True).order_by("product_name"))
        cake = (Products.objects.filter(type_of_ingredient="5").filter(
            is_active=True).order_by("product_name"))

        toppings = []
        for el in product.toppings.all():
            toppings.append(el)
        vegecounter = 0
        beefcounter = 0
        cheesecounter = 0
        cakecounter = 0
        extracounter = 0
        extra_1_counter = 0
        extra_2_counter = 0
        extra_3_counter = 0
        extra_4_counter = 0
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
            if el.type_of_ingredient == 8:
                extra_1_counter += 1
            if el.type_of_ingredient == 9:
                extra_2_counter += 1
            if el.type_of_ingredient == 10:
                extra_3_counter += 1
            if el.type_of_ingredient == 11:
                extra_4_counter += 1
        addvege_pay_control = vegecounter
        beef_pay_control = beefcounter
        cheese_pay_control = cheesecounter
        cake_pay_control = cakecounter
        extra_pay_control = extracounter
        extra_1_pay_control = extra_1_counter
        extra_2_pay_control = extra_2_counter
        extra_3_pay_control = extra_3_counter
        extra_4_pay_control = extra_4_counter

        vege_pay = vegecounter
        beef_pay = beefcounter
        cheese_pay = cheesecounter
        cake_pay = cakecounter
        extra_pay = extracounter
        extra__1_pay = extra_1_counter
        extra__2_pay = extra_2_counter
        extra__3_pay = extra_3_counter
        extra__4_pay = extra_4_counter

        change_topps_vege = 0
        change_topps_beef = 0
        change_topps_cheese = 0
        change_topps_extra = 0
        change_topps_cake = 0
        change_topps_extra_1 = 0
        change_topps_extra_2 = 0
        change_topps_extra_3 = 0
        change_topps_extra_4 = 0

        ctx = {
            "order": order,
            "pizza": product,
            "new_position": new_position,
            "toppings": toppings,
            "vegetopps": vegetopps,
            "beeftopps": beeftopps,
            "cheesetopps": cheesetopps,
            "extratopps": extratopps,
            "cake": cake,
            "vegecounter": vegecounter,
            "beefcounter": beefcounter,
            "cheesecounter": cheesecounter,
            "extracounter": extracounter,
            "cakecounter": cakecounter,
            "extra_1_counter": extra_1_counter,
            "extra_2_counter": extra_2_counter,
            "extra_3_counter": extra_3_counter,
            "extra_4_counter": extra_4_counter,
            "addvege_pay_control": addvege_pay_control,
            "beef_pay_control": beef_pay_control,
            "cheese_pay_control": cheese_pay_control,
            "extra_pay_control": extra_pay_control,
            "cake_pay_control": cake_pay_control,
            "extra_1_pay_control": extra_1_pay_control,
            "extra_2_pay_control": extra_2_pay_control,
            "extra_3_pay_control": extra_3_pay_control,
            "extra_4_pay_control": extra_4_pay_control,
            "vege_pay": vege_pay,
            "beef_pay": beef_pay,
            "cheese_pay": cheese_pay,
            "cake_pay": cake_pay,
            "extra_pay": extra_pay,
            "extra__1_pay": extra__1_pay,
            "extra__2_pay": extra__2_pay,
            "extra__3_pay": extra__3_pay,
            "extra__4_pay": extra__4_pay,
            "change_topps_vege": change_topps_vege,
            "change_topps_beef": change_topps_beef,
            "change_topps_cheese": change_topps_cheese,
            "change_topps_cake": change_topps_cake,
            "change_topps_extra": change_topps_extra,
            "change_topps_extra_1": change_topps_extra_1,
            "change_topps_extra_2": change_topps_extra_2,
            "change_topps_extra_3": change_topps_extra_3,
            "change_topps_extra_4": change_topps_extra_4,
        }
        return TemplateResponse(request, "change_topps_pizza_right.html", ctx)

    def post(self, request, order, pos):
        order = Orders.objects.get(pk=order)
        position_order = PositionOrder.objects.get(
            pk=request.POST.get("position_order"))

        input_add_topps = request.POST.get("input_add_topps")
        input_del_topps = request.POST.get("input_del_topps")
        input_add_cake = request.POST.get("input_add_cake")
        extra_price_right = request.POST.get("extra_price")
        extra_price_right = extra_price_right.replace(",", ".")
        position_order.extra_price_right = float(extra_price_right)
        position_order.change_topps_info_other_side = (input_del_topps + " " +
                                                       input_add_topps)
        position_order.order_id = order
        if position_order.extra_price_right > position_order.extra_price_left:
            position_order.extra_price = position_order.extra_price_right
        else:
            position_order.extra_price = position_order.extra_price_left
        position_order.save()

        return redirect("update_halfpizza_to_order",
                        pos=position_order.id,
                        order=order.id)


@method_decorator(login_required, name="dispatch")
class UpdateHalfPizzaToOrderView(PermissionRequiredMixin, View):

    permission_required = "babilon_v1.add_orders"

    def get(self, request, pos, order):
        categorys = Category.objects.all()
        pizza_half = PositionOrder.objects.get(pk=pos)
        # pizza_half.change_topps_info=""
        # pizza_half.change_topps_info_other_side=""
        # pizza_half.cake_info=""
        # pizza_half.sauces_free=""
        # pizza_half.sauces_pay=""
        # pizza_half.extra_price=0.00
        # pizza_half.save()

        user = request.user
        categorys = Category.objects.all()
        order = Orders.objects.get(pk=order)
        cakes = (Products.objects.filter(type_of_ingredient="5").filter(
            is_active=True).order_by("product_name"))
        souse_pay = Products.objects.filter(type_of_ingredient="6").filter(
            is_active=True)
        souse_free = Products.objects.filter(type_of_ingredient="7").filter(
            is_active=True)
        positions_on_order = PositionOrder.objects.filter(order_id=order.id)

        ctx = {
            "pizza_half": pizza_half,
            "order": order,
            "cakes": cakes,
            "positions_on_order": positions_on_order,
            "categorys": categorys,
            "souse_pay": souse_pay,
            "souse_free": souse_free,
        }
        return TemplateResponse(request, "update_secendhalf_to_order.html",
                                ctx)

    def post(self, request, order, pos):
        user = request.user
        order = Orders.objects.get(pk=order)
        position_order = PositionOrder.objects.get(pk=pos)
        pizza = position_order.product_id

        if "delete" in request.POST:
            extra_price = float(0)
            extra_price = round(extra_price, 2)
            position_order.extra_price = extra_price
            position_order.change_topps_info = ""
            position_order.change_topps_info_other_side = ""
            position_order.sauces_free = ""
            position_order.sauces_pay = ""
            position_order.cake_info = ""
            position_order.info = ""
            position_order.discount = 0
            position_order.save()
            return redirect("update_halfpizza_to_order",
                            order=order.id,
                            pos=position_order.id)

        add = request.POST.get("add")
        size = request.POST.get("size")
        price = request.POST.get("price")

        quantity = request.POST.get("quantity")
        extra_price = request.POST.get("extra_price")
        info = request.POST.get("info")
        cake_change = request.POST.get("cake_change")
        add_sauces_free = request.POST.get("add_sauces_free")
        add_sauces_pay = request.POST.get("add_sauces_pay")

        productId = request.POST.get("productId")
        orderPositionId = request.POST.get("orderPosition")
        discount = request.POST.get("discount")

        position_order.cake_info = cake_change
        position_order.save()

        if size:
            size = ProductSize.objects.get(pk=size)
            position_order.size_id = size
            price = price.replace(",", ".")
            position_order.price = float(price)
            position_order.save()
        if quantity != None:
            if int(quantity) > 0:
                position_order.quantity = int(quantity)
                position_order.save()

        if int(discount != 0) and discount != None and discount != "":
            position_order.discount = int(discount)
            position_order.save()
            order.promo = True
            # order.save()
        else:
            position_order.discount = 0
            position_order.save()
            order.promo = True
            # order.save()

        product = position_order
        price = request.POST.get("price")
        price_org = position_order.price

        if price != "":
            price = float(price)
            if price != price_org and price != 0.00:

                position_order.price = price
                position_order.save()
                order.promo = True
                # order.save()
            else:
                position_order.price = product.price
                position_order.save()
        else:
            price = price_org
            position_order.price = price
            position_order.save()
            order.promo = True

        if extra_price != None and extra_price != "":
            position_order.extra_price = float(extra_price.replace(",", "."))
            position_order.save()
        else:
            position_order.extra_price = 0.00
            position_order.save()
        if info != "":
            position_order.info = info
            position_order.save()
        else:
            position_order.info = ""
            position_order.save()
        if cake_change != "":
            position_order.cake_info = cake_change
            position_order.save()
        if add_sauces_free != "":
            position_order.sauces_free = add_sauces_free
            position_order.save()
        if add_sauces_pay != "":
            position_order.sauces_pay = add_sauces_pay
            position_order.save()

        changeTopps = request.POST.get("changeTopps")
        lista_id_left_topps = list(position_order.change_topps_info)
        lista_id_rigth_topps = list(
            position_order.change_topps_info_other_side)

        order.save()
        if add:
            return redirect("products_category", pk=1)
        else:
            return redirect("update_halfpizza_to_order",
                            order=order.id,
                            pos=position_order.id)


@method_decorator(login_required, name="dispatch")
class ChangeLeftSidePizzaView(PermissionRequiredMixin, View):
    permission_required = "babilon_v1.add_orders"

    def get(self, request, order, pos):
        pizza_half = PositionOrder.objects.get(id=pos)
        size = ProductSize.objects.get(pk=pizza_half.size_id.id)
        categorys = Category.objects.all()

        order = Orders.objects.get(pk=order)
        pizzas = (Products.objects.filter(category=1).filter(
            product_size=size).filter(is_pizza_freestyle=False).filter(
                is_active=True))
        positions_on_order = PositionOrder.objects.filter(order_id=order.id)

        ctx = {
            "order": order,
            "size": size,
            "pizzas": pizzas,
            "categorys": categorys,
            "positions_on_order": positions_on_order,
        }
        return TemplateResponse(request,
                                "pizza_filter_for_halfpizza_side_update.html",
                                ctx)

    def post(self, request, order, pos):
        search = request.POST.get("search")
        side_half = request.POST.get("side_half")
        if search != "":
            pizza_half = PositionOrder.objects.get(id=pos)
            size = ProductSize.objects.get(pk=pizza_half.size_id.id)
            categorys = Category.objects.all()

            order = Orders.objects.get(pk=order)
            pizzas = (Products.objects.filter(product_size=size).filter(
                is_pizza_freestyle=False).filter(is_active=True))
            pizzas = pizzas.filter(Q(pizza_number=search))
            positions_on_order = PositionOrder.objects.filter(
                order_id=order.id)

            ctx = {
                "order": order,
                "size": size,
                "pizzas": pizzas,
                "categorys": categorys,
                "positions_on_order": positions_on_order,
            }
            return TemplateResponse(
                request, "pizza_filter_for_halfpizza_side_update.html", ctx)
        else:
            if side_half != "":
                order = Orders.objects.get(pk=order)
                pizza_half = PositionOrder.objects.get(id=pos)
                # size=ProductSize.objects.get(pk=size)
                side_half = request.POST.get("side_half")
                pizza_left = Products.objects.get(id=side_half)

                # pizza_half.pr
                price_left = pizza_left.price
                price_right_price = pizza_half.product_id_pizza_right.price
                if price_left > price_right_price:
                    price = price_left
                elif price_left == price_right_price:
                    price = price_left
                else:
                    price = price_right_price

                pizza_half.halfpizza_name = (
                    "Lewa - " + str(pizza_left.product_name) + ", Prawa - " +
                    str(pizza_half.product_id_pizza_right.product_name))
                pizza_half.price = price
                pizza_half.product_id = pizza_left
                # pizza_half.product_id_pizza_right=pizza_half.product_id_pizza_right.price
                pizza_half.save()

                return redirect("update_halfpizza_to_order",
                                order=order.id,
                                pos=pizza_half.id)
            else:
                pizza_half = PositionOrder.objects.get(id=pos)
                order = Orders.objects.get(pk=order)
                return redirect("change_left_side_pizza_to_order",
                                order=order.id,
                                pos=pizza_half.id)


@method_decorator(login_required, name="dispatch")
class ChangeRightSidePizzaView(PermissionRequiredMixin, View):
    permission_required = "babilon_v1.add_orders"

    def get(self, request, order, pos):
        pizza_half = PositionOrder.objects.get(id=pos)
        size = ProductSize.objects.get(pk=pizza_half.size_id.id)
        categorys = Category.objects.all()

        order = Orders.objects.get(pk=order)
        pizzas = (Products.objects.filter(category=1).filter(
            product_size=size).filter(is_pizza_freestyle=False).filter(
                is_active=True))
        positions_on_order = PositionOrder.objects.filter(order_id=order.id)

        ctx = {
            "order": order,
            "size": size,
            "pizzas": pizzas,
            "categorys": categorys,
            "positions_on_order": positions_on_order,
        }
        return TemplateResponse(request,
                                "pizza_filter_for_halfpizza_side_update.html",
                                ctx)

    def post(self, request, order, pos):
        side_half = request.POST.get("side_half")
        search = request.POST.get("search")
        if search != "":
            pizza_half = PositionOrder.objects.get(id=pos)
            size = ProductSize.objects.get(pk=pizza_half.size_id.id)
            categorys = Category.objects.all()

            order = Orders.objects.get(pk=order)
            pizzas = (Products.objects.filter(product_size=size).filter(
                is_pizza_freestyle=False).filter(is_active=True))
            pizzas = pizzas.filter(Q(pizza_number=search))
            positions_on_order = PositionOrder.objects.filter(
                order_id=order.id)

            ctx = {
                "order": order,
                "size": size,
                "pizzas": pizzas,
                "categorys": categorys,
                "positions_on_order": positions_on_order,
            }
            return TemplateResponse(
                request, "pizza_filter_for_halfpizza_side_update.html", ctx)
        else:
            if side_half != "":
                order = Orders.objects.get(pk=order)
                pizza_half = PositionOrder.objects.get(id=pos)

                pizza_right = Products.objects.get(id=side_half)

                # pizza_half.pr
                price_right = pizza_right.price
                price_left_price = pizza_half.product_id.price
                if price_right > price_left_price:
                    price = price_right
                elif price_right == price_left_price:
                    price = price_left_price
                else:
                    price = price_left_price
                pizza_half.halfpizza_name = (
                    "Lewa - " + str(pizza_half.product_id.product_name) +
                    ", Prawa - " + str(pizza_right.product_name))
                pizza_half.price = price
                pizza_half.product_id_pizza_right = pizza_right
                # pizza_half.product_id_pizza_right=pizza_half.product_id_pizza_right.price
                pizza_half.save()
                return redirect("update_halfpizza_to_order",
                                order=order.id,
                                pos=pizza_half.id)
            else:
                pizza_half = PositionOrder.objects.get(id=pos)
                order = Orders.objects.get(pk=order)
                return redirect(
                    "change_right_side_pizza_to_order",
                    order=order.id,
                    pos=pizza_half.id,
                )


@method_decorator(login_required, name="dispatch")
class AddProductToOrderView(PermissionRequiredMixin, View):
    permission_required = "babilon_v1.add_orders"

    def get(self, request, order, prod):
        user = request.user
        product = Products.objects.get(pk=prod)
        categorys = Category.objects.all()
        order = Orders.objects.get(pk=order)
        souse_pay = Products.objects.filter(type_of_ingredient="6").filter(
            is_active=True)
        souse_free = Products.objects.filter(type_of_ingredient="7").filter(
            is_active=True)
        positions_on_order = PositionOrder.objects.filter(order_id=order.id)

        ctx = {
            "order": order,
            "positions_on_order": positions_on_order,
            "product": product,
            "categorys": categorys,
            "souse_pay": souse_pay,
            "souse_free": souse_free,
        }
        return TemplateResponse(request, "add_product_to_order.html", ctx)

    def post(self, request, order, prod):
        user = request.user
        product = Products.objects.get(pk=prod)
        order = Orders.objects.get(pk=order)

        add = request.POST.get("add")
        quantity = request.POST.get("quantity")
        extra_price = request.POST.get("sauces")
        info = request.POST.get("info")
        add_sauces_free = request.POST.get("add_sauces_free")
        add_sauces_pay = request.POST.get("add_sauces_pay")
        discount = request.POST.get("discount")

        new_position = PositionOrder()
        new_position.order_id = order
        new_position.product_id = product
        new_position.price = product.price
        new_position.save()
        positions_on_order = PositionOrder.objects.filter(order_id=order.id)
        if quantity != None:
            if int(quantity) > 0:
                new_position.quantity = int(quantity)
                new_position.save()

        if discount != "":
            if int(discount) != 0 and discount != None:
                new_position.discount = int(discount)
                new_position.save()

                # print(price_org)
                order.promo = True
                # order.save()
        else:
            new_position.discount = 0
            new_position.save()
            order.promo = True

        product = new_position
        price = request.POST.get("price")

        price_org = product.price

        if price != "":
            price = float(price)
            if price < price_org and price != 0.00:

                new_position.price = price
                new_position.save()
                order.promo = True
                # order.save()
            else:
                new_position.price = product.price
                new_position.save()
        else:
            price = 0.00
            new_position.price = price
            new_position.save()
            order.promo = True

        if discount != "":
            if int(discount) != 0 and discount != None:
                new_position.discount = int(discount)
                new_position.save()
                order.promo = True
                # order.save()
        else:
            new_position.discount = 0
            new_position.save()
        positions_on_order = PositionOrder.objects.filter(order_id=order.id)
        if discount != "":
            if int(discount) != 0 and discount != None:
                new_position.discount = int(discount)
                new_position.save()
                # print(price_org)
                order.promo = True
                # order.save()
        else:
            new_position.discount = 0
            new_position.save()
            order.promo = True

        if extra_price != None:
            new_position.extra_price = float(extra_price.replace(",", "."))
            new_position.save()
        else:
            new_position.extra_price = new_position.extra_price
            new_position.save()
        if info != "":
            new_position.info = info
            new_position.save()
        if add_sauces_free != "":
            new_position.add_sauces_free = add_sauces_free
            new_position.save()
        if add_sauces_pay != "":
            new_position.add_sauces_pay = add_sauces_pay
            new_position.save()

        changeTopps = request.POST.get("changeTopps")

        categorys = Category.objects.all()
        order.save()
        return redirect("products_category", pk=1)


@method_decorator(login_required, name="dispatch")
class ProductsView(PermissionRequiredMixin, View):
    permission_required = "babilon_v1.add_orders"

    def get(self, request):
        user = request.user
        pizzeria = get_pizzeria_session(request)
        # order=get_order(request,pizzeria)
        order = Orders.objects.get(pk=request.session["active_orders"])
        products = Products.objects.filter(is_active=True)
        categorys = Category.objects.all()
        category_pizza = Category.objects.filter(category_name="Pizza")
        positions_on_order = PositionOrder.objects.filter(order_id=order.id)
        ctx = {
            "order": order,
            "positions_on_order": positions_on_order,
            "products": products,
            "categorys": categorys,
            "pizzeria": pizzeria,
        }
        return TemplateResponse(request, "main_menu.html", ctx)


@method_decorator(login_required, name="dispatch")
class OrderCloseDeatailsView(PermissionRequiredMixin, View):

    permission_required = "babilon_v1.view_orders"

    def get(self, request, pk):

        categorys = Category.objects.all()
        time_zero_form_details = request.GET.get("time_from_details")
        time_zero_manual = request.GET.get("time_zero_manual")
        pay_delivery = request.GET.get("pay_delivery")
        client_name = request.GET.get("client_name")
        address = request.GET.get("address")
        phone = request.GET.get("phone")
        info = request.GET.get("info")
        discount = request.GET.get("discount")
        # dtime=
        order_finish = Orders.objects.get(pk=pk)
        order_finish.time_start = datetime.now()
        order_finish.active = True
        order_finish.status = 2
        order_finish.barman_id = request.user
        # order_finish.save()
        positions_on_order = (PositionOrder.objects.filter(
            order_id=pk).order_by("product_id.category").order_by("id"))

        if request.is_ajax():
            time_zero_ajax = request.GET.get("time_zero")
            driver_id = request.GET.get("driver_id")
            pay_method = request.GET.get("pay_method")
            delivery_method = request.GET.get("delivery_method")
            if time_zero_ajax:
                time_zero = time_zero_ajax
                order_finish.time_zero = order_finish.time_start
                order_finish.save()
                order_finish.time_zero = datetime.now() + timedelta(
                    minutes=int(time_zero))
                # order_finish.save()
            if pay_method:
                order_finish.pay_method = pay_method
                # order_finish.save()
            if delivery_method:
                order_finish.type_of_order = delivery_method
                # order_finish.save()
                if delivery_method != "3":
                    order_finish.time_zero = datetime.now() + timedelta(
                        minutes=int(default_time_zoro_local))
                    if delivery_method == "1":
                        order_finish.delivery_method = "1"
                        order_finish.type_of_order = "1"
                        order_finish.address=None
                    else:
                        order_finish.delivery_method = "2"
                        order_finish.type_of_order = "2"
                        order_finish.address=None
                    order_finish.status = "2"
                    # order_finish.save()
                else:
                    order_finish.time_zero = datetime.now() + timedelta(
                        minutes=int(default_time_zoro_outside))
                    order_finish.delivery_method = "3"
                    order_finish.status = "2"
                    order_finish.address=None
                    # order_finish.save()
        if time_zero_form_details:
            time_delivery = time_zero_form_details
            order_finish.time_zero = time_zero_form_details
            # order_finish.save()
        if time_zero_manual:
            order_finish.time_zero = (
                datetime.now() +
                timedelta(minutes=int(time_zero_manual))).time()
            # order_finish.save()
        order_finish.save()
        positions_on_order = PositionOrder.objects.filter(order_id=pk)
        google_key = os.environ.get("GOOGLE_MAPS")

        if order_finish.type_of_order == 3:
            ctx = google_dist(order_finish)
        else:
            paid_button = True
            ctx = {
                "google_key": google_key,
                "order": order_finish,
                "positions_on_order": positions_on_order,
                "categorys": categorys,
                "paid_button": paid_button,
            }

        return TemplateResponse(request, "order_finish_details.html", ctx)

    def post(self, request, pk):
        # order_id=request.POST.get('order_id')
        order = Orders.objects.get(pk=pk)
        year_now = datetime.now().year
        month_now = datetime.now().month
        day = datetime.now().day
        if "set_price" in request.POST:
            pos_id = request.POST.get("pos_id")
            new_price = request.POST.get("new_price")
            if new_price != "":
                new_price = float(new_price)
                new_price = round(new_price, 2)

                pos = PositionOrder.objects.get(pk=pos_id)
                pos.price = new_price - pos.extra_price
                pos.save()
                order.promo = True
                order.save()
            else:
                new_price = 0.00
                pos = PositionOrder.objects.get(pk=pos_id)
                pos.price = new_price - pos.extra_price
                pos.save()
                order.promo = True
                order.save()

            return redirect("order_details", pk=order.id)
        if "set_discount" in request.POST:
            pos_id = request.POST.get("pos_id")
            new_discount = request.POST.get("new_discount")
            if new_discount != "":
                new_discount = int(new_discount)
                pos = PositionOrder.objects.get(pk=pos_id)
                pos.discount = new_discount
                pos.save()
                order.promo = True
                order.save()
            else:
                new_discount = 0
                pos = PositionOrder.objects.get(pk=pos_id)
                pos.discount = new_discount
                pos.save()
                order.promo = True
                order.save()

            return redirect("order_details", pk=order.id)

        if "order_is_paid" in request.POST:
            order.info = "Zapłacono"
            order.save()
            return redirect("order_details", pk=order.id)

        if "phone_number" in request.POST:
            phone_number = request.POST.get("phone_number")
            new_client = Clients()
            new_client.phone_number = phone_number
            new_client.save()
            new_address = Address()
            new_address.client_id = new_client
            new_address.save()
            order.address = new_address
            order.save()
            return redirect("order_details", pk=order.id)

        info = request.POST.get("info")
        discount = request.POST.get("discount")

        order.barman_id = request.user
        if discount != "":
            order.discount = discount
        else:
            order.discount = 0
        order.info = info
        order.closed = True
        # order.save()
        # order.active=False

        if "print" in request.POST:
            order.printed = False
            order.closed = True
            # order.save()
        else:
            order.printed = True
            order.closed = True
            # order.save()
        try:
            del request.session["active_orders"]
        except:
            pass

        order.save()
        return redirect("/orders/")


@method_decorator(login_required, name="dispatch")
class OrderCloseDeatailsNotPrintView(PermissionRequiredMixin, View):

    permission_required = "babilon_v1.view_orders"

    def post(self, request, pk):
        order_id = request.POST.get("order_id")
        info = request.POST.get("info")
        order = Orders.objects.get(pk=order_id)
        order.printed = True
        order.save()
        try:
            del request.session["active_orders"]
        except:
            pass

        return redirect("/orders/")


@method_decorator(login_required, name="dispatch")
class OrdersDetailsArchivesView(PermissionRequiredMixin, View):

    permission_required = "babilon_v1.view_orders"

    def get(self, request, pk):
        order_finish = Orders.objects.get(pk=pk)
        positions_on_order = (PositionOrder.objects.filter(
            order_id=pk).order_by("product_id.category").order_by("id"))
        google_key = (os.environ.get("GOOGLE_KEY"), )
        ctx = {
            "order": order_finish,
            "positions_on_order": positions_on_order,
            "google_key": google_key,
        }
        return TemplateResponse(request, "order_details_archives.html", ctx)

    def post(self, request, pk):

        return redirect("/orders_archives/")


@method_decorator(login_required, name="dispatch")
class OrdersArchivesView(PermissionRequiredMixin, View):
    permission_required = "babilon_v1.view_orders"

    def get(self, request):
        year_now = datetime.now().year
        month_now = datetime.now().month
        day = datetime.now().day
        user = request.user
        pizzeria_active = get_pizzeria_session(request)
        date_start = request.session["date_start"]
        date_end = request.session["date_end"]
        date_start = json.loads(date_start)
        date_end = json.loads(date_end)
        orders = Orders.objects.filter(workplace_id=pizzeria_active).filter(
            date__range=[date_start, date_end])

        df_orders(orders)
        pos_counter = orders.count()

        # numpy(df)

        ctx = {
            "pos_counter": pos_counter,
            "orders": orders,
            "pizzeria_active": pizzeria_active,
            "date_start": date_start,
            "date_end": date_end,
        }
        return render(request, "orders_archives.html", ctx)


@method_decorator(login_required, name="dispatch")
class OrderChangeDeatailsView(PermissionRequiredMixin, View):
    permission_required = "babilon_v1.view_orders"

    def get(self, request, pk):
        categorys = Category.objects.all()
        time_zero_form_details = request.GET.get("time_from_details")
        time_zero_manual = request.GET.get("time_zero_manual")
        pay_delivery = request.GET.get("pay_delivery")
        client_name = request.GET.get("client_name")
        address = request.GET.get("address")
        phone = request.GET.get("phone")
        info = request.GET.get("info")
        discount = request.GET.get("discount")

        order_finish = Orders.objects.get(pk=pk)
        positions_on_order = PositionOrder.objects.filter(order_id=pk)
        request.session["active_orders"] = order_finish.id

        if request.is_ajax():
            time_zero_ajax = request.GET.get("time_zero")
            if time_zero_ajax:
                time_zero = time_zero_ajax
                order_finish.time_zero = order_finish.time_start
                order_finish.save()
                order_finish.time_zero = datetime.now() + timedelta(
                    minutes=int(time_zero))
                # order_finish.save()

            driver_id = request.GET.get("driver_id")
            pay_method = request.GET.get("pay_method")
            if pay_method:
                order_finish.pay_method = pay_method
                # order_finish.save()
            delivery_method = request.GET.get("delivery_method")
            print(delivery_method)
            if delivery_method:
                
                order_finish.type_of_order = delivery_method
                # order_finish.save()
                if delivery_method != "3":
                    order_finish.time_zero = datetime.now() + timedelta(
                        minutes=int(default_time_zoro_local))
                    if delivery_method == "1":
                        order_finish.delivery_method = "1"
                        order_finish.type_of_order = "1"
                        order_finish.address=None
                    else:
                        order_finish.delivery_method = "2"
                        order_finish.type_of_order = "2"
                        order_finish.address=None
                    order_finish.status = "2"
                    # order_finish.save()
                else:
                    order_finish.time_zero = datetime.now() + timedelta(
                        minutes=int(default_time_zoro_outside))
                    order_finish.delivery_method = "3"
                    order_finish.status = "2"
                    order_finish.address=None
                    # order_finish.save()
        order_finish.active = True
        order_finish.barman_id = request.user

        # order_finish.save()

        if time_zero_form_details:

            time_delivery = time_zero_form_details
            # order_finish.time_zero=time_zero_form_details
            order_finish.time_zero = datetime.now() + timedelta(
                minutes=int(time_zero))
            order_finish.barman_id = request.user
            # order_finish.save()
        if time_zero_manual:

            order_finish.time_zero = datetime.now() + timedelta(
                minutes=int(time_zero_manual))
            order_finish.barman_id = request.user
            # order_finish.save()
        order_finish.save()
        google_key = os.environ.get("GOOGLE_MAPS")
        if order_finish.type_of_order == 3:
            ctx = google_dist(order_finish)
        else:
            ctx = {
                "order": order_finish,
                "positions_on_order": positions_on_order,
                "categorys": categorys,
                "google_key": google_key,
            }

        return TemplateResponse(request, "order_finish_details.html", ctx)

    def post(self, request, pk):
        order_id = request.POST.get("order_id")
        order = Orders.objects.get(pk=order_id)
        if "set_price" in request.POST:
            pos_id = request.POST.get("pos_id")
            new_price = request.POST.get("new_price")
            if new_price != "":
                new_price = float(new_price)
                new_price = round(new_price, 2)

            else:
                new_price = 0.00
            pos = PositionOrder.objects.get(pk=pos_id)
            pos.price = new_price - pos.extra_price
            pos.save()
            order.promo = True
            order.save()
            return redirect("order_change_details", pk=order.id)
        if "set_discount" in request.POST:
            pos_id = request.POST.get("pos_id")
            new_discount = request.POST.get("new_discount")
            if new_discount != "":
                new_discount = int(new_discount)
                pos = PositionOrder.objects.get(pk=pos_id)
                pos.discount = new_discount
                pos.save()
                order.promo = True
                order.save()
            else:
                new_discount = 0
                pos = PositionOrder.objects.get(pk=pos_id)
                pos.discount = new_discount
                pos.save()
                order.promo = True
                order.save()
            return redirect("order_change_details", pk=order.id)
        if "phone_number" in request.POST:
            phone_number = request.POST.get("phone_number")
            new_client = Clients()
            new_client.phone_number = phone_number
            new_client.save()
            new_address = Address()
            new_address.client_id = new_client
            new_address.save()
            order.address = new_address
            order.save()
            return redirect("order_change_details", pk=order.id)

        info = request.POST.get("info")
        discount = request.POST.get("discount")

        # order=Orders.objects.get(pk=order_id)
        order.barman_id = request.user
        order.info = info
        order.discount = discount
        if "print" in request.POST:
            order.printed = False
            order.closed = True
            # order.save()
        else:
            order.printed = True
            order.closed = True
            # order.save()
        order.save()

        del request.session["active_orders"]
        order.save()
        return redirect("/orders/")


@method_decorator(login_required, name="dispatch")
class OrdersView(PermissionRequiredMixin, View):
    permission_required = "babilon_v1.view_orders"

    def get(self, request):
        pizzeria_id = request.session["pizzeria"]
        year_now = datetime.now().year
        month_now = datetime.now().month
        day = datetime.now().day

        orders = (Orders.objects.filter(date__day=day).filter(
            date__month=month).filter(date__year=year).filter(
                workplace_id=pizzeria_id))
        # for el in orders:
        #     el.active=False
        #     el.save()
        orders_closed_outside = (Orders.objects.filter(
            workplace_id=pizzeria_id).filter(status=3).filter(
                type_of_order=3).filter(date__day=day).filter(
                    date__month=month).filter(date__year=year))
        len_orders_close = len(orders_closed_outside)
        pay_methods = PAY_METHOD
        drivers = (MyUser.objects.filter(profession=4).filter(
            work_place=pizzeria_id).filter(active=True))
        day_time = datetime.now().date()
        driver_active_order = (Orders.objects.filter(type_of_order="3").filter(
            status="3").filter(date=day_time).filter(workplace_id=pizzeria_id))
        # print(driver_active_order)
        for driver in drivers:
            for order in driver_active_order:
                print(order.driver_id)
                print(driver.id)
                if order.driver_id == driver.id:
                    driver.counter_active_orders_in_car_count(
                        driver, day_time, day_time, pizzeria_id)
                    driver.save()
                else:
                    driver.counter_active_orders_in_car_count = 0
                    driver.save()

        ctx = {
            "pay_methods": pay_methods,
            "len_orders_close": len_orders_close,
            "orders": orders,
            "drivers": drivers,
            "workplace": pizzeria_id,
        }
        return TemplateResponse(request, "orders.html", ctx)

    def post(self, request):
        time_zero = 0
        year = datetime.now().year
        month = datetime.now().month
        day = datetime.now().day
        pizzeria_id = request.session["pizzeria"]
        if "unlock" in request.POST:
            order_id = request.POST.get("order_id")
            order = Orders.objects.get(pk=order_id)
            order.closed = False
            order.save()
            return redirect("/orders/")
        if "pay_mathod" in request.POST:
            order_id = request.POST.get("order_id")
            pay_method = request.POST.get("pay_mathod")

            order = Orders.objects.get(pk=order_id)
            order.pay_method = pay_method
            order.save()
            return redirect("/orders/")
        if "set_driver" in request.POST:
            order_id = request.POST.get("order_id")
            driver_id = request.POST.get("set_driver")

            driver = MyUser.objects.get(pk=driver_id)
            order = Orders.objects.get(pk=order_id)
            order.driver_id = driver
            order.status = 3
            order.start_delivery_time = datetime.now().time()
            order.save()
            return redirect("/orders/")

        if request.is_ajax():
            try:
                order_cancell_id = request.POST.get("order_cancell_id")
                if order_cancell_id:
                    order = Orders.objects.get(pk=order_cancell_id)
                    order.active = False
                    order.status = 5
                    order.closed = True
                    work_place_id = request.session["pizzeria"]
                    order_last = Orders.objects.filter(
                        workplace_id=work_place_id).first()
                    if order_last.id == order.id:
                        try:
                            session = request.session["active_orders"]
                            if session:
                                del request.session["active_orders"]

                        except:
                            pass
                    serialized_obj = serializers.serialize("json", [
                        order,
                    ])
                    response_data = {"order": serialized_obj}
                    order.save()
                    return JsonResponse(response_data)

                order_send_sms = request.POST.get("order_send_sms")
                if order_send_sms:
                    order = Orders.objects.get(pk=order_send_sms)
                    order.start_delivery_time = datetime.now().time()
                    message = request.POST.get("message")
                    message = message.replace("  ", "")
                    message = message.replace("ó", "o")
                    message = message.replace("ł", "l")
                    message = message.replace("ż", "z")
                    phone_number = request.POST.get("phone_number")
                    send_sms(phone_number, message)
                    order.sms_send = True
                    order.sms_time = datetime.now().time()
                    # order.status=3
                    order.save()
                    serialized_obj = serializers.serialize("json", [
                        order,
                    ])
                    response_data = {"order": serialized_obj}
                    return JsonResponse(response_data)

                order_close = request.POST.get("order_close")
                if order_close:
                    order = Orders.objects.get(pk=order_close)
                    order.active = False
                    order.status = 4
                    order.closed = True
                    now = datetime.now()
                    order.time_delivery_in = datetime(
                        year=now.year,
                        month=now.month,
                        day=now.day,
                        hour=now.hour,
                        minute=now.minute,
                    )
                    order.save()
                    work_place_id = request.session["pizzeria"]
                    order_last = Orders.objects.filter(
                        workplace_id=work_place_id).first()
                    if order_last.id == order.id:
                        try:
                            session = request.session["active_orders"]
                            if session:
                                del request.session["active_orders"]
                        except:
                            pass
                    serialized_obj = serializers.serialize("json", [
                        order,
                    ])
                    response_data = {"order": serialized_obj}
                    return JsonResponse(response_data)

                order_id = request.POST.get("order_id")
                driver_id = request.POST.get("driver_id")
                order = Orders.objects.get(pk=order_id)

            except ObjectDoesNotExist:
                pass
        orders_closed_outside = (Orders.objects.filter(
            workplace_id=pizzeria_id).filter(status=3).filter(
                type_of_order=3).filter(date__day=day).filter(
                    date__month=month).filter(date__year=year))
        len_orders_close = len(orders_closed_outside)
        orders = Orders.objects.filter(date__day=day)
        drivers = MyUser.objects.filter(profession=4)
        pay_methods = PAY_METHOD
        ctx = {
            "pay_methods": pay_methods,
            "len_orders_close": len_orders_close,
            "orders": orders,
            "drivers": drivers,
            "workplace": pizzeria_id,
        }
        return TemplateResponse(request, "orders.html", ctx)


@method_decorator(login_required, name="dispatch")
class OrdersFilterView(PermissionRequiredMixin, View):
    permission_required = "babilon_v1.view_orders"

    def get(self, request):
        pizzeria_id = request.session["pizzeria"]
        year_now = datetime.now().year
        month_now = datetime.now().month
        day = datetime.now().day
        lista = [1, 2, 3]
        orders_lokal_type = (Orders.objects.filter(date__day=day).filter(
            date__month=month).filter(date__year=year).filter(
                workplace_id=pizzeria_id).filter(type_of_order="1").filter(
                    status__in=lista).count())
        orders_outside_type = (Orders.objects.filter(date__day=day).filter(
            date__month=month).filter(date__year=year).filter(
                workplace_id=pizzeria_id).filter(type_of_order="2").filter(
                    status__in=lista).count())
        orders_driver_type = (Orders.objects.filter(date__day=day).filter(
            date__month=month).filter(date__year=year).filter(
                workplace_id=pizzeria_id).filter(type_of_order="3").filter(
                    status__in=lista).count())

        orders = (Orders.objects.filter(date__day=day).filter(
            date__month=month).filter(date__year=year).filter(
                workplace_id=pizzeria_id).filter(active=True).filter(
                    status__in=lista))
        orders_closed_outside = (Orders.objects.filter(
            workplace_id=pizzeria_id).filter(status=3).filter(
                type_of_order=3).filter(date__day=day).filter(
                    date__month=month).filter(date__year=year))
        orders_active = (Orders.objects.filter(date__day=day).filter(
            date__month=month).filter(date__year=year).filter(
                workplace_id=pizzeria_id).filter(status__in=[1, 2, 3]).filter(
                    active=True).count())
        orders_prepare = (Orders.objects.filter(date__day=day).filter(
            date__month=month).filter(date__year=year).filter(
                workplace_id=pizzeria_id).filter(status="2").count())
        orders_driver = (Orders.objects.filter(date__day=day).filter(
            date__month=month).filter(date__year=year).filter(
                workplace_id=pizzeria_id).filter(status="3").count())
        orders_cancelled = (Orders.objects.filter(date__day=day).filter(
            date__month=month).filter(date__year=year).filter(
                workplace_id=pizzeria_id).filter(status="5").count())
        orders_closed = (Orders.objects.filter(date__day=day).filter(
            date__month=month).filter(date__year=year).filter(
                workplace_id=pizzeria_id).filter(status="4").count())

        in_progress = True
        len_orders_close = len(orders_closed_outside)
        drivers = (MyUser.objects.filter(profession=4).filter(
            work_place=pizzeria_id).filter(active=True))
        pay_methods = PAY_METHOD
        ctx = {
            "pay_methods": pay_methods,
            "len_orders_close": len_orders_close,
            "orders": orders,
            "orders_active": orders_active,
            "orders_closed": orders_closed,
            "orders_prepare": orders_prepare,
            "orders_driver": orders_driver,
            "orders_cancelled": orders_cancelled,
            "orders_lokal_type": orders_lokal_type,
            "orders_outside_type": orders_outside_type,
            "orders_driver_type": orders_driver_type,
            "drivers": drivers,
            "in_progress": in_progress,
            "workplace": pizzeria_id,
        }
        return TemplateResponse(request, "orders_filter.html", ctx)

    def post(self, request):
        time_zero = 0
        year = datetime.now().year
        month = datetime.now().month
        day = datetime.now().day
        pizzeria_id = request.session["pizzeria"]
        if "pay_mathod" in request.POST:
            order_id = request.POST.get("order_id")
            pay_method = request.POST.get("pay_mathod")

            order = Orders.objects.get(pk=order_id)
            order.pay_method = pay_method
            order.save()
            return redirect("/orders/filter/")
        if "set_driver" in request.POST:
            order_id = request.POST.get("order_id")
            driver_id = request.POST.get("set_driver")

            driver = MyUser.objects.get(pk=driver_id)
            order = Orders.objects.get(pk=order_id)
            order.driver_id = driver
            order.status = 3
            order.start_delivery_time = datetime.now().time()
            order.save()
            return redirect("/orders/filter/")

        if request.is_ajax():
            try:
                order_cancell_id = request.POST.get("order_cancell_id")
                if order_cancell_id:
                    order = Orders.objects.get(pk=order_cancell_id)
                    order.active = False
                    order.status = 5
                    order.save()
                    work_place_id = request.session["pizzeria"]
                    order_last = Orders.objects.filter(
                        workplace_id=work_place_id).first()
                    if order_last.id == order.id:
                        try:
                            session = request.session["active_orders"]
                            if session:
                                del request.session["active_orders"]

                        except:
                            pass
                    serialized_obj = serializers.serialize("json", [
                        order,
                    ])
                    response_data = {"order": serialized_obj}
                    return JsonResponse(response_data)

                order_send_sms = request.POST.get("order_send_sms")
                if order_send_sms:
                    order = Orders.objects.get(pk=order_send_sms)
                    order.start_delivery_time = datetime.now().time()
                    message = request.POST.get("message")
                    message = message.replace("  ", "")
                    message = message.replace("ó", "o")
                    message = message.replace("ł", "l")
                    message = message.replace("ż", "z")
                    phone_number = request.POST.get("phone_number")
                    send_sms(phone_number, message)
                    order.sms_send = True
                    order.sms_time = datetime.now().time()
                    # order.status=3
                    order.save()
                    serialized_obj = serializers.serialize("json", [
                        order,
                    ])
                    response_data = {"order": serialized_obj}
                    return JsonResponse(response_data)

                order_close = request.POST.get("order_close")
                if order_close:
                    order = Orders.objects.get(pk=order_close)
                    order.active = False
                    order.status = 4
                    now = datetime.now()
                    order.time_delivery_in = datetime(
                        year=now.year,
                        month=now.month,
                        day=now.day,
                        hour=now.hour,
                        minute=now.minute,
                    )
                    order.save()
                    work_place_id = request.session["pizzeria"]
                    order_last = Orders.objects.filter(
                        workplace_id=work_place_id).first()
                    if order_last.id == order.id:
                        try:
                            session = request.session["active_orders"]
                            if session:
                                del request.session["active_orders"]
                        except:
                            pass
                    serialized_obj = serializers.serialize("json", [
                        order,
                    ])
                    response_data = {"order": serialized_obj}
                    return JsonResponse(response_data)

                order_id = request.POST.get("order_id")
                driver_id = request.POST.get("driver_id")
                order = Orders.objects.get(pk=order_id)

                # if driver_id:
                #     driver=MyUser.objects.get(pk=driver_id)
                #     order.driver_id=driver
                #     order.status=3
                #     order.save()
                #     save_driver=order.driver_id

                #     serialized_obj = serializers.serialize('json',[save_driver,])
                #     response_data = {'save_driver':serialized_obj}
                #     return JsonResponse(response_data)

            except ObjectDoesNotExist:
                pass
        orders_closed_outside = (Orders.objects.filter(
            workplace_id=pizzeria_id).filter(status=3).filter(
                type_of_order=3).filter(date__day=day).filter(
                    date__month=month).filter(date__year=year))
        len_orders_close = len(orders_closed_outside)
        orders = (Orders.objects.filter(date__day=day).filter(
            date__month=month).filter(date__year=year))
        drivers = MyUser.objects.filter(profession=4)
        pay_methods = PAY_METHOD
        ctx = {
            "pay_methods": pay_methods,
            "len_orders_close": len_orders_close,
            "orders": orders,
            "drivers": drivers,
            "workplace": pizzeria_id,
        }
        return TemplateResponse(request, "orders_filter.html", ctx)


@method_decorator(login_required, name="dispatch")
class UpdateOrderView(PermissionRequiredMixin, UpdateView):
    permission_required = "babilon_v1.view_orders"
    model = Orders
    fields = [
        "discount_finish",
        "info",
    ]
    template_name_suffix = "_update_form"
    success_url = "/"

    def get_success_url(self):
        return f"/order_details/{self.object.order_id.id}"


@method_decorator(login_required, name="dispatch")
class UpdatePositionOrderView(PermissionRequiredMixin, UpdateView):
    permission_required = "miktel.change_positionorder"
    model = PositionOrder
    fields = [
        "order_id",
        "quantity",
        "cake_info",
        "change_topps_info",
        "change_topps_info_other_side",
        "sauces_free",
        "sauces_pay",
        "extra_price",
        "price",
        "info",
        "discount",
    ]
    template_name_suffix = "_update_form"
    success_url = "/"

    def get_success_url(self):
        return f"/order_details/{self.object.order_id.id}"


@method_decorator(login_required, name="dispatch")
class DeletePositionOrderView(PermissionRequiredMixin, DeleteView):
    permission_required = "miktel.del_positionorder"
    model = PositionOrder
    fields = "__all__"
    template_name_suffix = "_confirm_delete"
    success_url = "/"

    def get_success_url(self):
        return f"/order_details/{self.object.order_id.id}"


@method_decorator(login_required, name="dispatch")
class UpdateOrderView(PermissionRequiredMixin, UpdateView):
    permission_required = "miktel.change_positionorder"
    model = Orders
    fields = ["pizzeria", "number", "delivery", "paymethod"]
    template_name_suffix = "_update_form"
    success_url = "/"


@method_decorator(login_required, name="dispatch")
class DelDriverFromOrderView(PermissionRequiredMixin, View):

    permission_required = "babilon_v1.view_orders"

    def get(self, request, pk):
        order = Orders.objects.get(pk=pk)
        order.status = 2
        order.driver_id = None
        order.save()

        return redirect("orders")


# PDF Create
@method_decorator(login_required, name="dispatch")
class WSView(PermissionRequiredMixin, View):
    permission_required = "babilon_v1.view_orders"

    def get(self, request):
        async def hello(websocket, path):
            name = await websocket.recv()

            greeting = f"Hello fajfusie {name}!"

            await websocket.send(greeting)

            return redirect("orders")


# from rest_framework import generics
# from rest_framework import renderers
# from rest_framework.response import Response

# class SnippetHighlight(generics.GenericAPIView):
#     queryset = Orders.objects.all()
#     renderer_classes = [renderers.StaticHTMLRenderer]

#     def get(self, request, *args, **kwargs):
#         snippet = self.get_object()
#         return Response(snippet.highlighted)


@method_decorator(login_required, name="dispatch")
class CreatePDFOrderView(PermissionRequiredMixin, View):
    permission_required = "babilon_v1.view_orders"

    def get(self, request, pk):
        pass
        # order=Orders.objects.get(pk=pk)
        # # order.printed=False
        # # order.save()
        # # return redirect('orders')
        # positions_order=PositionOrder.objects.filter(order_id=order.id)
        # context = {
        #     'order': order,'positions_order':positions_order
        # }
        # html_string = render_to_string('order_pdf.html', context)

        # html = HTML(string=html_string)
        # html.write_pdf(target='/tmp/order_pdf.pdf')

        # fs = FileSystemStorage('/tmp')
        # with fs.open('/tmp/order_pdf.pdf') as pdf:
        #     response = HttpResponse(pdf, content_type='application/pdf')
        #     response[
        #         'Content-Disposition'] = 'attachment; filename="order_pdf.pdf"'
        # return response


# Klienci


@method_decorator(login_required, name="dispatch")
class AddNewClientView(PermissionRequiredMixin, View):
    permission_required = "babilon_v1.add_clients"

    def get(self, request):

        form = ClientForm()
        ctx = {"form": form}
        return TemplateResponse(request, "add_new_client.html", ctx)

    def post(self, request):
        form = ClientForm(request.POST)
        if form.is_valid():
            phone_number = form.cleaned_data["phone_number"]
            firstlastname = form.cleaned_data["firstlastname"]
            info = form.cleaned_data["info"]
            adres_1 = form.cleaned_data["adres_1"]
            status = form.cleaned_data["status"]
            work_place = get_pizzeria_session(request).address

            new_address = Address()
            new_address.street = adres_1
            new_address.save()

            new_client = Clients()
            new_client.phone_number = phone_number
            new_client.work_place = work_place
            new_client.client_name = firstlastname
            new_client.status = status
            new_client.info = info
            new_client.save()

            new_address.client_id = new_client
            new_address.save()

            return redirect("client", pk=new_client.id)


@method_decorator(login_required, name="dispatch")
class ClientsView(PermissionRequiredMixin, View):
    permission_required = "babilon_v1.view_clients"

    def get(self, request):
        pizzeria = get_pizzeria_session(request)
        order = Orders.objects.get(pk=request.session["active_orders"])
        # clients = Clients.objects.filter(work_place=pizzeria.id)
        # clients_addresses = Address.objects.all()
        form = ClientForm()
        ctx = {
            "order": order,
            # "clients": clients,
            # "clients_addresses": clients_addresses,
            "form": form,
        }
        return TemplateResponse(request, "clients.html", ctx)

    def post(self, request):
        pizzeria = get_pizzeria_session(request)
        # order = Orders.objects.get(pk=request.session["active_orders"])
        if "search" in request.POST:
            search = request.POST.get("search")
            order_id = request.POST.get("order_id")
            order = Orders.objects.get(pk=order_id)
            work_place = order.workplace_id
            clients = Clients.objects.filter(work_place=work_place).filter(
                Q(phone_number__icontains=search))
            clients_addresses = Address.objects.filter(client_id__in=clients)

            ctx = {
                "search": search,
                "clients": clients,
                "clients_addresses": clients_addresses,
                "order": order,
            }
            # return redirect('clients')
            return TemplateResponse(request, "clients.html", ctx)

        phone_number = request.POST.get("phone_number")
        address = request.POST.get("address")
        firstlastname = request.POST.get("firstlastname")
        order = request.POST.get("order")
        info = request.POST.get("info")
        work_place = get_pizzeria_session(request)
        new_address = Address()
        new_address.street = address
        new_address.save()

        new_client = Clients()
        new_client.phone_number = phone_number
        new_client.work_place = work_place
        new_client.client_name = firstlastname
        new_client.info = info
        new_client.save()

        new_address.client_id = new_client
        new_address.save()

        order = Orders.objects.get(pk=order)
        order.address = new_address
        order.save()

        # return redirect('client',pk=new_client.id)
        return redirect("products_category", pk=1)


@method_decorator(login_required, name="dispatch")
class ClientView(PermissionRequiredMixin, View):
    permission_required = "babilon_v1.view_clients"

    def get(self, request, pk):

        client = Clients.objects.get(pk=pk)
        client_addresses = Address.objects.filter(client_id=client)
        ctx = {"client": client, "client_addresses": client_addresses}
        return TemplateResponse(request, "client.html", ctx)


@method_decorator(login_required, name="dispatch")
class AddClientNewAddressView(PermissionRequiredMixin, View):
    permission_required = "babilon_v1.view_clients"

    def get(self, request, pk):

        form = CleintNewAddressForm()
        ctx = {"form": form}
        return TemplateResponse(request, "add_client_new_address.html", ctx)

    def post(self, request, pk):
        form = CleintNewAddressForm(request.POST)
        if form.is_valid():
            client = Clients.objects.get(pk=pk)

            street = form.cleaned_data["new_address"]

            new_address = Address()
            new_address.street = street
            new_address.client_id = client
            new_address.save()

            return redirect("client", pk=client.id)


@method_decorator(login_required, name="dispatch")
class EditAddressView(UpdateView):
    permission_required = "babilon_v1.change_address"
    model = Address
    fields = [
        "street",
    ]
    template_name_suffix = "_update_form"
    success_url = "/clients/"

    def get_success_url(self):
        # return f'/client/{self.object.Adresy_klienta.all()[0].id}'
        return f"/client/{self.object.client_id.id}"


@method_decorator(login_required, name="dispatch")
class EditClientView(UpdateView):
    permission_required = "babilon_v1.change_address"
    model = Clients
    fields = "__all__"
    template_name_suffix = "_update_form"
    success_url = "/clients/"

    def get_success_url(self):
        # return f'/client/{self.object.Adresy_klienta.all()[0].id}'
        return f"/client/{self.object.id}"


@method_decorator(login_required, name="dispatch")
class DelAddressView(PermissionRequiredMixin, DeleteView):
    permission_required = "babilon_v1.delete_address"
    model = Address
    fields = "__all__"
    template_name_suffix = "_confirm_delete"
    success_url = "/clients/"


@method_decorator(login_required, name="dispatch")
class DelClientView(PermissionRequiredMixin, DeleteView):
    permission_required = "babilon_v1.delete_clients"
    model = Clients
    fields = "__all__"
    template_name_suffix = "_confirm_delete"
    success_url = "/clients/"
