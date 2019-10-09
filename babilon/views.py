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

from datetime import datetime
rok = datetime.now().year
miesiac = datetime.now().month


class MainView(View):
    def get(self, request):
        return TemplateResponse(request, "product_list.html")


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

        productId = request.POST.get('productId')
        orderPositionId = request.POST.get('orderPosition')
        print(orderPositionId)

        orderPositionAdd = PositionOrder.objects.get(pk=orderPositionId)
        product_add = Products.objects.get(id=pk)
        changeTopps = request.POST.get('changeTopps')
        product_add = Products.objects.get(id=pk)

        new_positionOrder(orderPositionAdd)

        return TemplateResponse(request, "product_list.html")


class AddModyfiProduct(View):
    def get(self, request, pk, modyfi):
        product_add = Products.objects.get(id=pk)
        otherSize = Products.objects.filter(
            name=product_add.name).order_by('size')

        orderPosition = PositionOrder.objects.get(pk=modyfi)

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

        productId = request.POST.get('productId')
        orderPositionId = request.POST.get('orderPosition')
        orderPositionAdd = PositionOrder.objects.get(pk=orderPositionId)
        product_add = Products.objects.get(id=pk)
        changeTopps = request.POST.get('changeTopps')
        product_add = Products.objects.get(id=pk)
        new_positionOrder(orderPositionAdd)

        return TemplateResponse(request, "product_list.html")


class ChangeToppsView(View):
    def get(self, request, pk, modyfi):
        product = Products.objects.get(id=pk)
        orderPosition = PositionOrder.objects.get(pk=modyfi)
        vegetopps = Products.objects.filter(component="1")
        beeftopps = Products.objects.filter(component="2")
        cheesetopps = Products.objects.filter(component="3")

        toppings = []
        for el in orderPosition.toppings.all():
            toppings.append(el)
        #
        vegecounter = 0
        beefcounter = 0
        cheesecounter = 0
        for el in toppings:
            if el.component == 1:
                vegecounter += 1

            if el.component == 2:
                beefcounter += 1
            if el.component == 3:
                cheesecounter += 1
        # ilosc = 1
        # product_modyfi = PositionOrder()
        # product_modyfi.position = "{}x {} Rozmiar:{}, Cena{}".format(
        #     ilosc, product.name, product.size, product.price)
        # product_modyfi.price = product.price
        # # print(product_modyfi.price)
        # product_modyfi.save()
        # product_modyfi.extra_price = product.extra_price
        # product_modyfi.quantity = ilosc
        # product_modyfi.save()
        # for el in toppings:
        #     product_modyfi.toppings.add(el)
        #     product_modyfi.save()

        ctx = {
            'product': product,
            'product_modyfi': orderPosition,
            'cheesetopps': cheesetopps,
            'toppings': toppings,
            'vegetopps': vegetopps,
            'beeftopps': beeftopps,
            'vegecounter': vegecounter,
            'beefcounter': beefcounter,
            'cheesecounter': cheesecounter
        }
        return TemplateResponse(request, "change_topps.html", ctx)

    def post(self, request, pk, modyfi):
        product = Products.objects.get(pk=pk)
        product_modyfi = PositionOrder.objects.get(pk=modyfi)

        deltopps = request.POST.get('deltopps')
        vegetopps = request.POST.get('vegetopps')
        beeftopps = request.POST.get('beeftopps')
        cheesetopps = request.POST.get('cheesetopps')

        if deltopps != None:
            deltop = Products.objects.get(pk=deltopps)
            product_modyfi.change_topps += "- {}, ".format(deltop.name)
            # product_modyfi.toppings.add(deltop)
            # product_modyfi.save()
            for el in product_modyfi.toppings.all():
                if deltop.id == el.id:
                    product_modyfi.toppings.remove(el)
                    product_modyfi.save()
        if vegetopps != None:
            vegetopp = Products.objects.get(pk=vegetopps)
            print(vegetopps)
            product_modyfi.change_topps += "+ {}, ".format(vegetopp.name)
            product_modyfi.toppings.add(vegetopp)
            product_modyfi.save()
        if beeftopps != None:
            beeftopp = Products.objects.get(pk=beeftopps)
            product_modyfi.change_topps += "+ {}, ".format(beeftopp.name)
            product_modyfi.toppings.add(beeftopp)
            product_modyfi.save()
        if cheesetopps != None:
            cheesetopp = Products.objects.get(pk=beeftopps)
            product_modyfi.change_topps += "+ {}, ".format(cheesetopp.name)
            product_modyfi.toppings.add(cheesetopp)
            product_modyfi.save()

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

        deltopps = request.POST.get('deltopps')
        vegetopps = request.POST.get('vegetopps')
        beeftopps = request.POST.get('beeftopps')

        # try:
        #     order = Orders.objects.get(active=True)
        #     order.save()
        #     order.position.add(product_modyfi)
        #     order.save()
        # except ObjectDoesNotExist:
        #     order = Orders()
        #     order.active = True
        #     orderId = order.id
        #     order.save()
        #     order.position.add(product_modyfi)
        #     order.save()

        vegetopps = Products.objects.filter(component="1")
        beeftopps = Products.objects.filter(component="2")
        cheesetopps = Products.objects.filter(component="3")
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
            'product_modyfi.change_info': product_modyfi.change_topps
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


# class AddToOrdersView(View):
#     def post(self, request):
#         product_id = request.POST.get('addProduct')
#         product_add = Products.objects.get(id=product_id)

#         orderId = request.POST.get('orderId')
#         if orderId != None:
#             order = Orders.objects.get(pk=orderId)
#         else:
#             order = Orders()
#             order.save()

#         order.product.add(product_add)
#         order.save()
#         vege_components = Products.objects.filter(component="1")
#         beef_components = Products.objects.filter(component="2")
#         ctx = {
#             'orderId': orderId,
#             'product_add': product_add,
#             'vege_components': vege_components,
#             'beef_components': beef_components,
#         }
#         return TemplateResponse(request, "add_order.html", ctx)


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
        pizzas = Pizza.objects.all()

        ctx = {'product': products}
        return TemplateResponse(request, "pizza_menu.html", ctx)
