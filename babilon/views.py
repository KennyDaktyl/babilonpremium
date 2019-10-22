from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.template.response import TemplateResponse
from django.shortcuts import render, redirect

from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.core.exceptions import ObjectDoesNotExist

# Generici i szablony
from django.views import View
from django.views.generic.edit \
    import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from django.core.files.storage import FileSystemStorage
from django.template.loader import render_to_string
from weasyprint import HTML

from django.db.models import Q
from django.db.models import Count

from googlevoice import Voice
from googlevoice.util import input
# from smsapi.client import SmsApiPlClient

from django.core.paginator import Paginator

from babilon.models import *
from babilon.forms import *
from babilon.function import *
# from miktel.hasla import *

# import json
# from babilon.serializers import *
# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import status
# from django.http import Http404

from datetime import datetime
rok = datetime.now().year
miesiac = datetime.now().month


class MainView(View):
    def get(self, request):

        return TemplateResponse(request, "product_list.html")


# serializer = ProductSerializer()
# data = Products.objects.get(id=1)

# json = json.loads(data)
# print(json)

# class MainView(APIView):
#     def get(self, request, format=None):
#         product = Products.objects.all()
#         serializer = ProductSerializer(product,
#                                        many=True,
#                                        context={"request": request})
#         return Response(serializer.data)

#     def post(self, request, format=None):
#         serializer = ProductSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# class ProductView(APIView):
#     def get_object(self, pk):
#         try:
#             return Products.objects.get(pk=pk)
#         except Products.DoesNotExist:
#             raise Http404

#     def get(self, request, id, format=None):
#         Product = self.get_object(id)
#         serializer = ProductSerializer(Product, context={"request": request})
#         return Response(serializer.data)

#     def delete(self, request, id, format=None):
#         product = self.get_object(id)
#         product.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

#     def put(self, request, id, format=None):
#         product = self.get_object(id)
#         serializer = ProductSerializer(product, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def post(self, request, id, format=None):
#         pass


class AddToOrdersView(View):
    def get(self, request, pk):
        product_add = Products.objects.get(id=pk)
        otherSize = Products.objects.filter(
            name=product_add.name).order_by('size')

        orderPosition = add_position_to_order(product_add)

        vege_components = Products.objects.filter(component="1")
        beef_components = Products.objects.filter(component="2")
        sizes = ProductSize.objects.filter(pizza=True)
        products = Products.objects.all()
        souse_pay = Products.objects.filter(component="6")
        souse_free = Products.objects.filter(component="7")
        ctx = {
            'orderPosition': orderPosition,
            'product_add': product_add,
            'otherSize': otherSize,
            'vege_components': vege_components,
            'beef_components': beef_components,
            'sizes': sizes,
            'products': products,
            'souse_pay': souse_pay,
            'souse_free': souse_free
        }
        return TemplateResponse(request, "add_product_to_order.html", ctx)

    def post(self, request, pk):
        add = request.POST.get('add')
        quantity = request.POST.get('quantity')
        sauces = request.POST.get('sauces')
        info = request.POST.get('info')
        add_sauces_free = request.POST.get('add_sauces_free')
        add_sauces_pay = request.POST.get('add_sauces_pay')

        productId = request.POST.get('productId')
        orderPositionId = request.POST.get('orderPosition')
        orderPosition = PositionOrder.objects.get(pk=orderPositionId)
        discount = request.POST.get('discount')
        if quantity != None:
            if int(quantity) > 0:
                orderPosition.quantity = int(quantity)
                orderPosition.save()

        if discount != 0:
            print(discount)
            orderPosition.discount = int(discount)
            orderPosition.save()
        if sauces != None:
            orderPosition.extra_price = float(sauces.replace(",", "."))
            orderPosition.save()
        else:
            orderPosition.extra_price = orderPosition.extra_price
            orderPosition.save()
        if info != "":
            orderPosition.info = info
            orderPosition.save()
        if add_sauces_free != "":
            orderPosition.add_sauces_free = add_sauces_free
            orderPosition.save()
        if add_sauces_pay != "":
            orderPosition.add_sauces_pay = add_sauces_pay
            orderPosition.save()
        product_add = Products.objects.get(id=pk)
        changeTopps = request.POST.get('changeTopps')
        otherSize = Products.objects.filter(
            name=product_add.name).order_by('size')
        vege_components = Products.objects.filter(component="1")
        beef_components = Products.objects.filter(component="2")
        sizes = ProductSize.objects.filter(pizza=True)
        souse_pay = Products.objects.filter(component="6")
        souse_free = Products.objects.filter(component="7")
        if add != None:
            new_positionOrder(orderPosition)
            return redirect('main_view')
        ctx = {
            'orderPosition': orderPosition,
            'product_add': product_add,
            'otherSize': otherSize,
            'vege_components': vege_components,
            'beef_components': beef_components,
            'sizes': sizes,
            'products': product_add,
            'souse_pay': souse_pay,
            'souse_free': souse_free
        }

        return TemplateResponse(request, "add_product_to_order.html", ctx)


class AddModyfiProduct(View):
    def get(self, request, pk, modyfi, extra_price, cake, changes):
        product_add = Products.objects.get(id=pk)
        otherSize = Products.objects.filter(
            name=product_add.name).order_by('size')

        orderPosition = PositionOrder.objects.get(pk=modyfi)
        orderPosition.extra_price = float(extra_price)
        changes = changes.replace("  ", '')

        orderPosition.change_topps = cake + changes
        orderPosition.save()
        vege_components = Products.objects.filter(component="1")
        beef_components = Products.objects.filter(component="2")
        sizes = ProductSize.objects.filter(pizza=True)
        products = Products.objects.all()
        souse_pay = Products.objects.filter(component="6")
        souse_free = Products.objects.filter(component="7")
        ctx = {
            'orderPosition': orderPosition,
            'product_add': product_add,
            'otherSize': otherSize,
            'vege_components': vege_components,
            'beef_components': beef_components,
            'sizes': sizes,
            'products': products,
            'souse_pay': souse_pay,
            'souse_free': souse_free
        }
        return TemplateResponse(request, "add_product_to_order.html", ctx)

    def post(self, request, pk, modyfi, extra_price, cake, changes):
        productId = request.POST.get('productId')
        add = request.POST.get('add')
        quantity = request.POST.get('quantity')
        sauces = request.POST.get('sauces')
        info = request.POST.get('info')
        add_sauces_free = request.POST.get('add_sauces_free')
        add_sauces_pay = request.POST.get('add_sauces_pay')
        orderPosition = PositionOrder.objects.get(pk=modyfi)
        discount = request.POST.get('discount')
        if quantity != None:
            if int(quantity) > 0:
                orderPosition.quantity = int(quantity)
                orderPosition.save()

        if discount != 0:
            orderPosition.discount = int(discount)
            orderPosition.save()
        orderPosition.extra_price = float(sauces.replace(",", "."))
        print(orderPosition.extra_price)
        orderPosition.save()
        if info != "":
            orderPosition.info = info
            orderPosition.save()
        if add_sauces_free != "":
            orderPosition.add_sauces_free = add_sauces_free
            orderPosition.save()
        if add_sauces_pay != "":
            orderPosition.add_sauces_pay = add_sauces_pay
            orderPosition.save()
        product_add = Products.objects.get(id=pk)
        changeTopps = request.POST.get('changeTopps')
        otherSize = Products.objects.filter(
            name=product_add.name).order_by('size')
        vege_components = Products.objects.filter(component="1")
        beef_components = Products.objects.filter(component="2")
        sizes = ProductSize.objects.filter(pizza=True)
        souse_pay = Products.objects.filter(component="6")
        souse_free = Products.objects.filter(component="7")
        if add != None:
            new_positionOrder(orderPosition)
            return redirect('main_view')
        ctx = {
            'orderPosition': orderPosition,
            'product_add': product_add,
            'otherSize': otherSize,
            'vege_components': vege_components,
            'beef_components': beef_components,
            'sizes': sizes,
            'products': product_add,
            'souse_pay': souse_pay,
            'souse_free': souse_free
        }

        return TemplateResponse(request, "add_product_to_order.html", ctx)


class AddModyfiProductWithOut(View):
    def get(self, request, pk, modyfi):
        product_add = Products.objects.get(id=pk)
        otherSize = Products.objects.filter(
            name=product_add.name).order_by('size')

        orderPosition = PositionOrder.objects.get(pk=modyfi)
        orderPosition.extra_price = 0
        orderPosition.change_topps = ""
        orderPosition.save()
        vege_components = Products.objects.filter(component="1")
        beef_components = Products.objects.filter(component="2")
        sizes = ProductSize.objects.filter(pizza=True)
        products = Products.objects.all()
        souse_pay = Products.objects.filter(component="6")
        souse_free = Products.objects.filter(component="7")
        ctx = {
            'orderPosition': orderPosition,
            'product_add': product_add,
            'otherSize': otherSize,
            'vege_components': vege_components,
            'beef_components': beef_components,
            'sizes': sizes,
            'products': products,
            'souse_pay': souse_pay,
            'souse_free': souse_free
        }
        return TemplateResponse(request, "add_product_to_order.html", ctx)

    def post(self, request, pk, modyfi):
        add = request.POST.get('add')
        productId = request.POST.get('productId')
        # orderPositionId = request.POST.get('orderPosition')
        orderPosition = PositionOrder.objects.get(pk=modyfi)
        product_add = Products.objects.get(id=pk)
        changeTopps = request.POST.get('changeTopps')
        product_add = Products.objects.get(id=pk)
        # new_positionOrder(orderPositionAdd)
        otherSize = Products.objects.filter(
            name=product_add.name).order_by('size')
        vege_components = Products.objects.filter(component="1")
        beef_components = Products.objects.filter(component="2")
        sizes = ProductSize.objects.filter(pizza=True)
        souse_pay = Products.objects.filter(component="6")
        souse_free = Products.objects.filter(component="7")

        if add != None:
            new_positionOrder(orderPosition)
            return redirect('main_view')
        ctx = {
            'orderPosition': orderPosition,
            'product_add': product_add,
            'otherSize': otherSize,
            'vege_components': vege_components,
            'beef_components': beef_components,
            'sizes': sizes,
            'products': product_add,
            'souse_pay': souse_pay,
            'souse_free': souse_free
        }

        return TemplateResponse(request, "add_product_to_order.html", ctx)


class AddPositionToOrder(View):
    def post(self, request):
        productId = request.POST.get('productId')
        orderPositionId = request.POST.get('orderPosition')
        orderPosition = PositionOrder.objects.get(pk=orderPositionId)
        product_add = Products.objects.get(id=productId)

        new_positionOrder(orderPosition)
        otherSize = Products.objects.filter(
            name=product_add.name).order_by('size')
        vege_components = Products.objects.filter(component="1")
        beef_components = Products.objects.filter(component="2")
        sizes = ProductSize.objects.filter(pizza=True)
        souse_pay = Products.objects.filter(component="6")
        souse_free = Products.objects.filter(component="7")
        ctx = {
            'orderPosition': orderPosition,
            'product_add': product_add,
            'otherSize': otherSize,
            'vege_components': vege_components,
            'beef_components': beef_components,
            'sizes': sizes,
            'products': product_add,
            'souse_pay': souse_pay,
            'souse_free': souse_free
        }

        return redirect('/add_to_order/', product_add.id)


class ChangeToppsView(View):
    def get(self, request, pk, modyfi):
        product = Products.objects.get(id=pk)
        orderPosition = PositionOrder.objects.get(pk=modyfi)
        orderPosition.change_topps = ""

        vegetopps = Products.objects.filter(component="1")
        beeftopps = Products.objects.filter(component="2")
        cheesetopps = Products.objects.filter(component="3")
        extratopps = Products.objects.filter(component="4")
        cake = Products.objects.filter(component="5")

        toppings = []
        for el in product.toppings.all():
            toppings.append(el)
        vegecounter = 0
        beefcounter = 0
        cheesecounter = 0
        extracounter = 0
        cakecounter = 0
        for el in toppings:
            if el.component == 1:
                vegecounter += 1

            if el.component == 2:
                beefcounter += 1
            if el.component == 3:
                cheesecounter += 1
            if el.component == 4:
                cheesecounter += 1
            if el.component == 5:
                cheesecounter += 1
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
        change_topps_vege = 0
        change_topps_beef = 0
        change_topps_cheese = 0
        change_topps_extra = 0
        change_topps_cake = 0

        ctx = {
            'product': product,
            'product_modyfi': orderPosition,
            'toppings': toppings,
            'vegetopps': vegetopps,
            'beeftopps': beeftopps,
            'cheesetopps': cheesetopps,
            'extratopps': extratopps,
            'cake': cake,
            'vegecounter': vegecounter,
            'beefcounter': beefcounter,
            'cheesecounter': cheesecounter,
            'extracounter': extracounter,
            'cakecounter': cakecounter,
            'addvege_pay_control': addvege_pay_control,
            'beef_pay_control': beef_pay_control,
            'cheese_pay_control': cheese_pay_control,
            'extra_pay_control': extra_pay_control,
            'cake_pay_control': cake_pay_control,
            'vege_pay': vege_pay,
            'beef_pay': beef_pay,
            'cheese_pay': cheese_pay,
            'extra_pay': extra_pay,
            'cake_pay': cake_pay,
            'change_topps_vege': change_topps_vege,
            'change_topps_beef': change_topps_beef,
            'change_topps_cheese': change_topps_cheese,
            'change_topps_extra': change_topps_extra,
            'change_topps_cake': change_topps_cake,
        }
        return TemplateResponse(request, "change_topps.html", ctx)

    def post(self, request, pk, modyfi):
        product = Products.objects.get(pk=pk)
        product_modyfi = PositionOrder.objects.get(pk=modyfi)

        deltopps = request.POST.get('deltopps')
        vegetopps = request.POST.get('vegetopps')
        beeftopps = request.POST.get('beeftopps')
        cheesetopps = request.POST.get('cheesetopps')

        change_topps_vege = int(request.POST.get('change_topps_vege'))
        change_topps_beef = int(request.POST.get('change_topps_beef'))
        change_topps_cheese = int(request.POST.get('change_topps_cheese'))

        addvege_pay_control = int(request.POST.get('addvege_pay_control'))
        beef_pay_control = int(request.POST.get('beef_pay_control'))
        cheese_pay_control = int(request.POST.get('cheese_pay_control'))

        vege_pay = int(request.POST.get('vege_pay'))
        beef_pay = int(request.POST.get('beef_pay'))
        cheese_pay = int(request.POST.get('cheese_pay'))

        toppings = []
        for el in product_modyfi.toppings.all():
            toppings.append(el)

        if deltopps != None:
            deltop = Products.objects.get(pk=deltopps)
            product_modyfi.change_topps += "- {}, ".format(deltop.name)
            for el in product_modyfi.toppings.all():
                if deltop.id == el.id:
                    product_modyfi.toppings.remove(el)
                    product_modyfi.save()
                    vege_pay -= 1

                    if deltop.component == 1:
                        change_topps_vege -= 1
                    if deltop.component == 2:
                        change_topps_beef -= 1
                    if deltop.component == 3:
                        change_topps_cheese -= 1

            product_modyfi.save()
            # addvege_pay_control += 1

        if vegetopps != None:
            vegetopp = Products.objects.get(pk=vegetopps)
            product_modyfi.change_topps += "+ {}, ".format(vegetopp.name)
            product_modyfi.toppings.add(vegetopp)
            product_modyfi.save()
            vege_pay += 1
            change_topps_vege += 1
            if change_topps_vege > 0:
                i = vege_pay - addvege_pay_control
                price_copy = product_modyfi.extra_price
                product_modyfi.extra_price += product.size.vege_topps_price
                product_modyfi.save()
                # addvege_pay_control += 1

        if beeftopps != None:
            beeftopp = Products.objects.get(pk=beeftopps)
            product_modyfi.change_topps += "+ {}, ".format(beeftopp.name)
            product_modyfi.toppings.add(beeftopp)
            product_modyfi.save()
            beef_pay += 1
            change_topps_beef += 1
            if change_topps_beef > 0:
                i = beef_pay - beef_pay_control
                price_copy = product_modyfi.extra_price
                product_modyfi.extra_price += product.size.beef_topps_price
                product_modyfi.save()
        if cheesetopps != None:
            cheesetopp = Products.objects.get(pk=cheesetopps)
            product_modyfi.change_topps += "+ {}, ".format(cheesetopp.name)
            product_modyfi.toppings.add(cheesetopp)
            product_modyfi.save()
            cheese_pay += 1
            change_topps_cheese += 1

        vegecounter = 0
        beefcounter = 0
        cheesecounter = 0
        toppings = []
        for el in product_modyfi.toppings.all():
            toppings.append(el)
        for el in toppings:
            if el.component == 1:
                vegecounter += 1
            if el.component == 2:
                beefcounter += 1
            if el.component == 3:
                cheesecounter += 1
        vegetopps = Products.objects.filter(component="1")
        beeftopps = Products.objects.filter(component="2")
        cheesetopps = Products.objects.filter(component="3")

        if change_topps_vege == 0 and change_topps_beef == 0 and change_topps_cheese == 0:
            product_modyfi.extra_price = 0
        else:

            if change_topps_cheese > 0:
                product_modyfi.extra_price += product.size.cheese_topps_price
                product_modyfi.save()

        product_modyfi.save()

        ctx = {
            'product': product,
            'product_modyfi': product_modyfi,
            'toppings': toppings,
            'vegetopps': vegetopps,
            'beeftopps': beeftopps,
            'cheesetopps': cheesetopps,
            'vegecounter': vegecounter,
            'beefcounter': beefcounter,
            'cheesecounter': cheesecounter,
            'product_modyfi.change_info': product_modyfi.change_topps,
            'addvege_pay_control': addvege_pay_control,
            'beef_pay_control': beef_pay_control,
            'cheese_pay_control': cheese_pay_control,
            'vege_pay': vege_pay,
            'beef_pay': beef_pay,
            'cheese_pay': cheese_pay,
            'change_topps_vege': change_topps_vege,
            'change_topps_beef': change_topps_beef,
            'change_topps_cheese': change_topps_cheese
        }

        return TemplateResponse(request, "change_topps.html", ctx)


class CloseOrderView(View):
    def get(self, request, pk):
        order = Orders.objects.get(pk=pk)
        order.active = False
        order.status = "2"
        order.save()
        product = Products.objects.all()
        for el in product:
            el.quantity = 1
            el.change_info = ""
            el.save()
        return TemplateResponse(request, "product_list.html")


class OrdersView(View):
    def get(self, request):
        orders = Orders.objects.all()
        ctx = {'orders': orders}
        return TemplateResponse(request, "zamowienia.html", ctx)


class ProductsView(View):
    def get(self, request):
        return TemplateResponse(request, "produkty.html")


class ClientsView(View):
    def get(self, request):
        return TemplateResponse(request, "klienci.html")


class EmployesView(View):
    def get(self, request):
        return TemplateResponse(request, "pracownicy.html")


class StanMagazynuView(View):
    def get(self, request):
        return TemplateResponse(request, "stan_magazynu.html")


class AddOrderOutsideView(View):
    def get(self, request):
        client = Clients.objects.all()
        product = Products.objects.all()
        for el in product:
            el.quantity = 1
            el.save()
        pizza_size = ProductSize.objects.filter(pizza=True)
        size = ProductSize.objects.filter(pizza=True)
        menu = MainMenu.objects.all()
        orderList = Orders.objects.create()
        orderId = orderList.id
        ctx = {
            'client': client,
            'pizza_size': pizza_size,
            'menu': menu,
            'products': product,
            'orderId': orderId
        }
        return TemplateResponse(request, "dodaj_zam_wywoz.html", ctx)

    def post(self, request):
        orderId = request.POST.get('orderId')
        addList = request.POST.get('addList')
        product_add = Products.objects.get(id=addList)

        orderList = Orders.objects.get(pk=orderId)
        if product_add in orderList.product.all():
            product_add.quantity = product_add.quantity + 1
            product_add.save()
        else:
            orderList.product.add(product_add)
        orderList.save()
        print(orderList.status)
        for el in orderList.product.all():
            print(el.name)
        client = Clients.objects.all()
        product = Products.objects.all()
        pizza_size = ProductSize.objects.filter(pizza=True)
        size = ProductSize.objects.filter(pizza=True)
        menu = MainMenu.objects.all()
        order = Orders.objects.get(pk=orderId)
        ctx = {
            'client': client,
            'pizza_size': pizza_size,
            'menu': menu,
            'products': product,
            'orderList': orderList,
            'orderId': orderId,
            'order': order
        }
        return TemplateResponse(request, "dodaj_zam_wywoz.html", ctx)


class PizzaMixView(View):
    def post(self, request):
        orderId = request.POST.get('orderId')
        pizza_id = request.POST.get('pizza_id')
        del_comp = request.POST.get('del_comp')
        add_comp = request.POST.get('add_comp')
        pizza = Products.objects.get(pk=pizza_id)

        if del_comp != None:
            component = Products.objects.get(pk=del_comp)
            component.quantity = 1
            component.save()
            pizzamix = pizza
            pizzamix.price = pizza.price
            pizzamix.pizza_componets.remove(component)
            pizzamix.save()
        if add_comp != None:

            component = Products.objects.get(pk=add_comp)
            pizzamix = pizza
            if component in pizzamix.pizza_componets.all():
                print("Jest")
                component.quantity += 1
                pizzamix.price = pizzamix.price + (1 * component.price)
                component.save()
            else:
                pizzamix.pizza_componets.add(component)
                pizzamix.price = pizza.total_price_pizzamix
                pizzamix.save()

        vege_components = Products.objects.filter(component="1")
        beef_components = Products.objects.filter(component="2")
        ctx = {
            'orderId': orderId,
            'product_add': pizzamix,
            'vege_components': vege_components,
            'beef_components': beef_components,
        }
        return TemplateResponse(request, "add_to_orders.html", ctx)


class PizzaListView(View):
    def get(self, request):
        pizzas = Products.objects.filter(pizza=True)
        pizzeria = Pizzeria.objects.all()
        size = ProductSize.objects.filter(pizza=True)
        ctx = {'pizzeria': [pizzeria], 'pizzas': pizzas, 'sizes': size}
        return TemplateResponse(request, "pizza_list.html", ctx)


class PizzaEdit(UpdateView):
    model = Products
    fields = [
        'name',
    ]
    template_name_suffix = ('_update_form')
    success_url = ('/lista_czesci/')


class AddPizzaView(View):
    def get(self, request):
        form = AddPizzaForm()
        ctx = {'form': form}
        return TemplateResponse(request, "add_pizza.html", ctx)

    def post(self, request):
        form = AddPizzaForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            size = form.cleaned_data['size']
            vegetopps = form.cleaned_data['vegetopps']
            beeftopps = form.cleaned_data['beeftopps']
            price = form.cleaned_data['price']

            product = Products()
            product.pizza = True
            product.size = size
            product.name = name
            product.price = price
            product.save()

            for el in vegetopps:
                product.pizza_componets.add(el)
                product.save()
            for el in beeftopps:
                product.pizza_componets.add(el)
                product.save()

            return TemplateResponse(request, "product_list.html")


class CategoryListView(View):
    def get(self, request, pk):
        products = Products.objects.filter(menu_category=pk)
        if pk == 1:
            otherSize = ProductSize.objects.filter(menu=1)
            ctx = {'product': products, 'otherSize': otherSize}
        else:
            ctx = {'product': products}
        return TemplateResponse(request, "pizza_menu.html", ctx)


class UpdatePositionOrderView(UpdateView):
    # permission_required='miktel.delete_usluga'
    model = PositionOrder
    fields = [
        'quantity', 'change_topps', 'add_sauces_free', 'add_sauces_pay',
        'extra_price', 'price', 'info', 'discount'
    ]
    template_name_suffix = ('_update_form')
    success_url = ('/')


class DeletePositionOrderView(DeleteView):
    # permission_required='miktel.delete_usluga'
    model = PositionOrder
    fields = '__all__'
    template_name_suffix = ('_confirm_delete')
    success_url = ('/')


class UpdateOrderView(UpdateView):
    # permission_required='miktel.delete_usluga'
    model = Orders
    fields = ['pizzeria', 'number', 'delivery', 'paymethod']
    template_name_suffix = ('_update_form')
    success_url = ('/')