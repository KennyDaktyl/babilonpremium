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
        orders = Orders.objects.all()
        ctx = {'orders': orders}
        return TemplateResponse(request, "zamowienia.html", ctx)

class LocalStatusView(View):
    def get(self, request):
        clients=Clients.objects.all()
        ctx={'clients':clients}
        return TemplateResponse(request, "mainview.html",ctx)

# class AddClientView(CreateView):
#     model = Clients
#     fields = '__all__'
#     success_url = reverse_lazy("main_view")

class AddNewOrderLocalCashView(View):
    def get(self, request):
        try:
            newOrder_LocalCash=Orders.objects.get(active=True)
        
            pizzeria_id=1
            pizzeria=Pizzeria.objects.get(pk=pizzeria_id)
            # newOrder_LocalCash.number=new_number(pizzeria_id)
            newOrder_LocalCash.delivery=1
            newOrder_LocalCash.pizzeria=pizzeria
            newOrder_LocalCash.save()
        except ObjectDoesNotExist:
            newOrder_LocalCash=Orders()
            pizzeria_id=1
            pizzeria=Pizzeria.objects.get(pk=pizzeria_id)
            newOrder_LocalCash.number=new_number(pizzeria_id)
            newOrder_LocalCash.delivery=1
            newOrder_LocalCash.pizzeria=pizzeria
            newOrder_LocalCash.active=True
            newOrder_LocalCash.save()
        
        return redirect('products')


class ProductsView(View):
    def get(self, request):
        products=Products.objects.all()

        ctx={'products':products}
        return TemplateResponse(request, "pizza_menu.html",ctx)

class AddNewOrderOutsideView(View):
    def get(self, request):
        try:
            newOrder_Outside=Orders.objects.get(active=True)   

            pizzeria_id=1
            pizzeria=Pizzeria.objects.get(pk=pizzeria_id)
            newOrder_Outside.delivery=2
            newOrder_Outside.pizzeria=pizzeria
            newOrder_Outside.save()
        except ObjectDoesNotExist:
            newOrder_Outside=Orders()
            pizzeria_id=1
            pizzeria=Pizzeria.objects.get(pk=pizzeria_id)
            newOrder_Outside.number=new_number(pizzeria_id)
            newOrder_Outside.delivery=2
            newOrder_Outside.pizzeria=pizzeria
            newOrder_Outside.active=True
            newOrder_Outside.save()
        return redirect('clients')

class AddNewOrderOutsideDriverView(View):
    def get(self, request):
        try:
            newOrder_Driver=Orders.objects.get(active=True)  
            pizzeria_id=1
            pizzeria=Pizzeria.objects.get(pk=pizzeria_id)
            newOrder_Driver.delivery=3
            newOrder_Driver.pizzeria=pizzeria
            newOrder_Driver.save() 

        except ObjectDoesNotExist: 
            newOrder_Driver=Orders()
            pizzeria_id=1
            pizzeria=Pizzeria.objects.get(pk=pizzeria_id)
            newOrder_Driver.number=new_number(pizzeria_id)
            newOrder_Driver.delivery=3
            newOrder_Driver.pizzeria=pizzeria
            newOrder_Driver.active=True
            newOrder_Driver.save() 
        return redirect('clients')
        
class EditAddressView(UpdateView):   
    model = Address
    fields = ['address',]
    template_name_suffix = ('_update_form')
    success_url = ('/clients/' ) 

    

class ClientsView(View):
    def get(self, request):
        
        clients=Clients.objects.all()
        ctx={'clients':clients}
        return TemplateResponse(request, "clients.html",ctx)

class ClientView(View):
    def get(self, request,pk):
        
        client=Clients.objects.get(pk=pk)
        ctx={'client':client}
        return TemplateResponse(request, "client.html",ctx)

class AddClientView(View):
    def get(self, request):
        
        form=CleintForm()
        ctx={'form':form}
        return TemplateResponse(request, "addclient.html",ctx)
    
    def post(self, request):
        form = CleintForm(request.POST)
        if form.is_valid():
            phone_number= form.cleaned_data['phone_number']
            adres_1= form.cleaned_data['adres_1']
            
            new_address=Address()
            new_address.address=adres_1
            new_address.save()
            
            new_client=Clients()
            new_client.phone_number=phone_number
            new_client.save()

            new_client.adrress.add(new_address)
            new_client.save()
            
            return redirect('client',pk=new_client.id)

class AddClientNewAddressView(View):
    def get(self, request,pk):
        
        form=CleintNewAddressForm()
        ctx={'form':form}
        return TemplateResponse(request, "addclientnewaddress.html",ctx)
    
    def post(self, request,pk):
        form = CleintNewAddressForm(request.POST)
        if form.is_valid():
            client=Clients.objects.get(pk=pk)

            new_address_form= form.cleaned_data['new_address']
            
            new_address=Address()
            new_address.address=new_address_form
            new_address.save()
            
            client.adrress.add(new_address)
            client.save()

            
            return redirect('client', pk=client.id)

class DelAddressView(DeleteView):
    model = Address
    fields = '__all__'
    template_name_suffix = ('_confirm_delete')
    success_url = ('/clients/')




class AddClientToOrder(View):
    def get(self, request,pk, address):

        order=Orders.objects.get(active=True)
        client=Clients.objects.get(pk=pk)
        address=Address.objects.get(pk=address)
        print(address)

        order.client=client
        order.address=address
        order.save()

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
        # print(quantity)
        print("jestemTuatj")
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
            # print(discount)
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
            return redirect('products')
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
        extra_price = request.GET.get('extra_price')
        if extra_price != "":
            orderPosition.extra_price = float(extra_price)
            orderPosition.save()
        else:
            orderPosition.extra_price = 0
            orderPosition.save()
        changes = changes.replace("  ", '')
        orderPosition.change_topps = cake + changes
        orderPosition.save()
        vege_components = Products.objects.filter(component="1")
        beef_components = Products.objects.filter(component="2")
        sizes = ProductSize.objects.filter(pizza=True)
        products = Products.objects.all()
        souse_pay = Products.objects.filter(component="6")
        souse_free = Products.objects.filter(component="7")
        # print(quantity)
        print("jestemTuatj")
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
            return redirect('products')
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
        changeToppsAdd = request.GET.get('input_add_topps')
        changeToppsDel = request.GET.get('input_del_topps')
        input_add_cake = request.GET.get('input_add_cake')
        changeTopps = changeToppsDel + changeToppsAdd
        otherSize = Products.objects.filter(
            name=product_add.name).order_by('size')

        orderPosition = PositionOrder.objects.get(pk=modyfi)
        orderPosition.cake_info = input_add_cake
        orderPosition.save()
        if len(changeTopps) < 512:
            orderPosition.change_topps = changeTopps
            orderPosition.save()
            print(len(changeTopps))
        extra_price = request.GET.get('extra_price')
        if extra_price != "":
            orderPosition.extra_price = float(extra_price)
            orderPosition.save()
        else:
            orderPosition.extra_price = 0
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
            # print(discount)
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
            return redirect('products')
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


class AddToppsFreeStyleView(View):
    def get(self, request, pk):
        product_add = Products.objects.get(id=pk)
        otherSize = Products.objects.filter(
            name=product_add.name).order_by('size')

        vegetopps = Products.objects.filter(component="1")
        beeftopps = Products.objects.filter(component="2")
        cheesetopps = Products.objects.filter(component="3")
        extratopps = Products.objects.filter(component="4")
        cake = Products.objects.filter(component="5")
        sizes = ProductSize.objects.filter(pizza=True)
        products = Products.objects.all()
        souse_pay = Products.objects.filter(component="6")
        souse_free = Products.objects.filter(component="7")
        change_topps_vege = 0
        change_topps_beef = 0
        change_topps_cheese = 0
        change_topps_extra = 0
        change_topps_cake = 0
        ctx = {
            # 'orderPosition': orderPosition,
            'product_add': product_add,
            'otherSize': otherSize,
            'vegetopps': vegetopps,
            'beeftopps': beeftopps,
            'cheesetopps': cheesetopps,
            'extratopps': extratopps,
            'cake': cake,
            'sizes': sizes,
            'products': products,
            'souse_pay': souse_pay,
            'souse_free': souse_free,
            'change_topps_vege': change_topps_vege,
            'change_topps_beef': change_topps_beef,
            'change_topps_cheese': change_topps_cheese,
            'change_topps_extra': change_topps_extra,
            'change_topps_cake': change_topps_cake,
        }
        return TemplateResponse(request, "add_freestyle_topps.html", ctx)


class AddToOrderFreeStyleView(View):
    def get(self, request, pk):
        product_add = Products.objects.get(id=pk)
        orderPosition = add_position_to_order(product_add)
        add = request.GET.get('add')
        topps = request.GET.get('topps')
        input_topps_free = request.GET.get('input_topps_free')
        input_topps_pay = request.GET.get('input_topps_pay')
        extra_price = request.GET.get('extra_price')
        input_cake_info = request.GET.get('input_cake_info')
        print(input_cake_info)
        set_topps = input_topps_free + input_topps_pay
        orderPosition.change_topps = set_topps
        orderPosition.cake_info = input_cake_info
        orderPosition.save()
        if extra_price != "":
            orderPosition.extra_price = extra_price
            orderPosition.save()

        otherSize = Products.objects.filter(
            name=product_add.name).order_by('size')

        vegetopps = Products.objects.filter(component="1")
        beeftopps = Products.objects.filter(component="2")
        cheesetopps = Products.objects.filter(component="3")
        extratopps = Products.objects.filter(component="4")
        cake = Products.objects.filter(component="5")
        sizes = ProductSize.objects.filter(pizza=True)
        products = Products.objects.all()
        souse_pay = Products.objects.filter(component="6")
        souse_free = Products.objects.filter(component="7")

        ctx = {
            'orderPosition': orderPosition,
            'product_add': product_add,
            'otherSize': otherSize,
            'vegetopps': vegetopps,
            'beeftopps': beeftopps,
            'cheesetopps': cheesetopps,
            'extratopps': extratopps,
            'cake': cake,
            'sizes': sizes,
            'products': products,
            'souse_pay': souse_pay,
            'souse_free': souse_free
        }

        return TemplateResponse(request, "add_freestyle_to_order.html", ctx)

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
            # print(discount)
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
            return redirect('products')
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

        return TemplateResponse(request, "add_freestyle_topps.html", ctx)


class Secend_Half_Pizza_SearchView(View):
    def get(self, request, pk, modyfi):
        product = Products.objects.get(id=pk)
        orderPosition = PositionOrder.objects.get(pk=modyfi)
        size_search = product.size.id

        pizza_search = Products.objects.filter(size=size_search).filter(
            pizza_freestyle=False).filter(menu_category=1)
        ctx = {
            'products_search_secendhalf': pizza_search,
            'orderPosition': orderPosition.id,
            
        }
        return TemplateResponse(request, "pizza_filter_for_secendhalf.html",
                                ctx)
    def post(self, request, pk, modyfi):
        orderPosition_1_2 = PositionOrder.objects.get(pk=modyfi)
        id_secend_part_halfpizza = request.POST.get('secend_part_halfpizza')
        product = Products.objects.get(id=id_secend_part_halfpizza)
        orderPosition_2_2 = add_position_to_order(product)

        return redirect('first_and_secend_halfpizza',first_part=orderPosition_1_2.id,secend_part=orderPosition_2_2.id)
        


class Firts_And_Secend_Half_PizzaView(View):
    def get(self, request, first_part, secend_part):
        orderPosition_1_2 = PositionOrder.objects.get(pk=first_part)
        orderPosition_2_2 = PositionOrder.objects.get(pk=secend_part)
        product_id=orderPosition_1_2.position.id
        pizza_oryg=Products.objects.get(pk=product_id)
      
        
        cake = Products.objects.filter(component="5").order_by('name')
        souse_pay = Products.objects.filter(component="6")
        souse_free = Products.objects.filter(component="7")
        if orderPosition_1_2.price <= orderPosition_2_2.price:
            halfpizza_price=orderPosition_2_2.price
        else:
            halfpizza_price=orderPosition_1_2.price
        
        add_topps_part1=[]
        add_topps_part2=[]
        for el in orderPosition_1_2.toppings.all():
            add_topps_part1.append(el.id)
        for el in orderPosition_2_2.toppings.all():
            add_topps_part2.append(el.id)
        common_topps=list(set(add_topps_part1).intersection(add_topps_part2))
        
        common_price=0

        for el in common_topps:
            comm_topp=Products.objects.get(pk=el)
            if comm_topp.component==1:
                price_comm_topp=pizza_oryg.size.vege_topps_price
            if comm_topp.component==2:
                price_comm_topp=pizza_oryg.size.beef_topps_price
            if comm_topp.component==3:
                price_comm_topp=pizza_oryg.size.cheese_topps_price
            if comm_topp.component==4:
                price_comm_topp=pizza_oryg.size.extra_topps_price 
            common_price+=price_comm_topp
      
        if orderPosition_1_2.extra_price>=orderPosition_2_2.extra_price:    
            extra_price=(orderPosition_1_2.extra_price+orderPosition_2_2.extra_price)-common_price
        else:
            extra_price=(orderPosition_2_2.extra_price+orderPosition_1_2.extra_price)-common_price
        if len(add_topps_part1)==0 :
            extra_price=orderPosition_2_2.extra_price
        if len(add_topps_part2)==0 :
                extra_price=orderPosition_1_2.extra_price
        if len(common_topps)==0:
            extra_price=orderPosition_1_2.extra_price+orderPosition_2_2.extra_price
        extra_price=round(extra_price,2)
       
        ctx = {
            'orderPosition_1_2': orderPosition_1_2,
            'orderPosition_2_2': orderPosition_2_2,
            'souse_free': souse_free,
            'souse_pay': souse_pay,
            'cake':cake,
            'halfpizza_price':halfpizza_price,
            'extra_price':extra_price
        }
        return TemplateResponse(request, "add_secendhalf_to_order.html", ctx)
    def post(self, request, first_part, secend_part):
        orderPosition_1_2 = PositionOrder.objects.get(pk=first_part)
        orderPosition_2_2 = PositionOrder.objects.get(pk=secend_part)
        product_id=orderPosition_1_2.position.id
        pizza_oryg=Products.objects.get(pk=product_id)
        productId = request.POST.get('productId')
        add = request.POST.get('add')
        quantity = request.POST.get('quantity')
        halfpizza_price=request.POST.get('halfpizza_price')
        sauces = request.POST.get('sauces')
        info = request.POST.get('info')
        add_sauces_free = request.POST.get('add_sauces_free')
        add_sauces_pay = request.POST.get('add_sauces_pay')
        discount = request.POST.get('discount')
        input_add_cake = request.POST.get('input_add_cake')
        sauces=sauces.replace(",",".")

        print(input_add_cake)

        newOrderPosition_pizzahals=PositionOrder()
        newOrderPosition_pizzahals.halfpizza_name="Lewa:" +orderPosition_1_2.position.name+","+" Prawa:" +orderPosition_2_2.position.name
        
        if orderPosition_1_2.price >= orderPosition_2_2.price:
            newOrderPosition_pizzahals.price=float(orderPosition_1_2.price)
        else:
            newOrderPosition_pizzahals.price=float(orderPosition_2_2.price)
        
        newOrderPosition_pizzahals.extra_price=float(sauces)
        newOrderPosition_pizzahals.change_topps=orderPosition_1_2.change_topps
        newOrderPosition_pizzahals.change_topps_on_right=orderPosition_2_2.change_topps
        newOrderPosition_pizzahals.add_sauces_free=add_sauces_free
        newOrderPosition_pizzahals.add_sauces_pay=add_sauces_pay
        newOrderPosition_pizzahals.cake_info=input_add_cake
        newOrderPosition_pizzahals.discount=discount
        newOrderPosition_pizzahals.pizza_half=True
        newOrderPosition_pizzahals.save()

       
        if quantity != None:
            if int(quantity) > 0:
                newOrderPosition_pizzahals.quantity = int(quantity)
                newOrderPosition_pizzahals.save()
               
        if discount != 0:
            newOrderPosition_pizzahals.discount = int(discount)
            newOrderPosition_pizzahals.save()
            
        if info != "":
            newOrderPosition_pizzahals.info = info
            newOrderPosition_pizzahals.save()
            
        if add_sauces_free != "":
            
            newOrderPosition_pizzahals.add_sauces_free = add_sauces_free
            newOrderPosition_pizzahals.save()
        if add_sauces_pay != "":
            
            newOrderPosition_pizzahals.add_sauces_pay = add_sauces_pay
            newOrderPosition_pizzahals.save()
        new_positionOrder(newOrderPosition_pizzahals)
            
        return redirect('products')
       

class ChangeToppsHalfPizzaView(View):
    def get(self, request,part):
        orderPosition = PositionOrder.objects.get(pk=part)

        orderPosition.toppings.clear()
        orderPosition.change_toppings=""
        orderPosition.extra_price=0
        orderPosition.save()

        vegetopps = Products.objects.filter(component="1").order_by('name')
        beeftopps = Products.objects.filter(component="2").order_by('name')
        cheesetopps = Products.objects.filter(component="3").order_by('name')
        extratopps = Products.objects.filter(component="4").order_by('name')
        cake = Products.objects.filter(component="5").order_by('name')

        toppings = []
        for el in orderPosition.position.toppings.all():
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
                extracounter += 1
            if el.component == 5:
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
        change_topps_vege = 0
        change_topps_beef = 0
        change_topps_cheese = 0
        change_topps_extra = 0
        change_topps_cake = 0

        ctx = {
            'product': orderPosition.position,
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
        return TemplateResponse(request, "change_topps_half_pizza.html", ctx)

    def post(self, request,part):
        
        
        orderPosition = PositionOrder.objects.get(pk=part)
        product =orderPosition.position 

        if request.is_ajax():
            add_topps = request.POST.get('add_topps')
            add_topp=Products.objects.get(pk=add_topps)
            orderPosition.toppings.add(add_topp)
            orderPosition.save()

             # return redirect('first_and_secend_halfpizza',first_part=int(orderPosition.id)-1,secend_part=orderPosition.id,)
            vegetopps = Products.objects.filter(component="1").order_by('name')
            beeftopps = Products.objects.filter(component="2").order_by('name')
            cheesetopps = Products.objects.filter(component="3").order_by('name')
            extratopps = Products.objects.filter(component="4").order_by('name')
            cake = Products.objects.filter(component="5").order_by('name')

            toppings = []
            for el in orderPosition.position.toppings.all():
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
                    extracounter += 1
                if el.component == 5:
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
            change_topps_vege = 0
            change_topps_beef = 0
            change_topps_cheese = 0
            change_topps_extra = 0
            change_topps_cake = 0

            ctx = {
                'product': orderPosition.position,
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
            return TemplateResponse(request, "change_topps_half_pizza.html", ctx)
        
        
        
        
        
        
        else:
            extra_price = request.POST.get('extra_price')
            input_add_topps = request.POST.get('input_add_topps')
            input_del_topps = request.POST.get('input_del_topps')
            cake = request.POST.get('input_add_cake')
            

            changes=input_del_topps+input_add_topps

            if extra_price != "":
                orderPosition.extra_price = float(extra_price)
                orderPosition.save()
            else:
                orderPosition.extra_price = 0
                orderPosition.save()
            changes = changes.replace("  ", '')
            orderPosition.change_topps = cake + changes
            if extra_price!="":
                orderPosition.extra_price=extra_price
            else:
                orderPosition.extra_price=0.00
            orderPosition.save()

            return redirect('first_and_secend_halfpizza',first_part=orderPosition.id,secend_part=int(orderPosition.id)+1)
      



class ChangeToppsHalfPizza_Part2View(View):
    def get(self, request,part):
        orderPosition = PositionOrder.objects.get(pk=part)

        orderPosition.toppings.clear()
        orderPosition.change_toppings=""
        orderPosition.extra_price=0
        orderPosition.save()


        vegetopps = Products.objects.filter(component="1").order_by('name')
        beeftopps = Products.objects.filter(component="2").order_by('name')
        cheesetopps = Products.objects.filter(component="3").order_by('name')
        extratopps = Products.objects.filter(component="4").order_by('name')
        cake = Products.objects.filter(component="5").order_by('name')

        toppings = []
        for el in orderPosition.position.toppings.all():
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
                extracounter += 1
            if el.component == 5:
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
        change_topps_vege = 0
        change_topps_beef = 0
        change_topps_cheese = 0
        change_topps_extra = 0
        change_topps_cake = 0

        ctx = {
            'product': orderPosition.position,
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
        return TemplateResponse(request, "change_topps_half_pizza_right.html", ctx)

    def post(self, request,part):
        
        
        orderPosition = PositionOrder.objects.get(pk=part)
        product =orderPosition.position 

        if request.is_ajax():
            add_topps = request.POST.get('add_topps')
            add_topp=Products.objects.get(pk=add_topps)
            orderPosition.toppings.add(add_topp)
            orderPosition.save()

            vegetopps = Products.objects.filter(component="1").order_by('name')
            beeftopps = Products.objects.filter(component="2").order_by('name')
            cheesetopps = Products.objects.filter(component="3").order_by('name')
            extratopps = Products.objects.filter(component="4").order_by('name')
            cake = Products.objects.filter(component="5").order_by('name')

            toppings = []
            for el in orderPosition.position.toppings.all():
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
                    extracounter += 1
                if el.component == 5:
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
            change_topps_vege = 0
            change_topps_beef = 0
            change_topps_cheese = 0
            change_topps_extra = 0
            change_topps_cake = 0

            ctx = {
                'product': orderPosition.position,
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
            return TemplateResponse(request, "change_topps_half_pizza_right.html", ctx)
            




           
        else:
            extra_price = request.POST.get('extra_price')
            input_add_topps = request.POST.get('input_add_topps')
            input_del_topps = request.POST.get('input_del_topps')
            cake = request.POST.get('input_add_cake')
            

            changes=input_del_topps+input_add_topps

            if extra_price != "":
                orderPosition.extra_price = float(extra_price)
                orderPosition.save()
            else:
                orderPosition.extra_price = 0
                orderPosition.save()
            changes = changes.replace("  ", '')
            orderPosition.change_topps = cake + changes
            orderPosition.save()

            return redirect('first_and_secend_halfpizza',first_part=int(orderPosition.id)-1,secend_part=int(orderPosition.id))
      

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

        vegetopps = Products.objects.filter(component="1").order_by('name')
        beeftopps = Products.objects.filter(component="2").order_by('name')
        cheesetopps = Products.objects.filter(component="3").order_by('name')
        extratopps = Products.objects.filter(component="4").order_by('name')
        cake = Products.objects.filter(component="5").order_by('name')

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
                extracounter += 1
            if el.component == 5:
                cakecounter += 1
        addvege_pay_control = vegecounter
        beef_pay_control = beefcounter
        cheese_pay_control = cheesecounter
        extra_pay_control = extracounter
        cake_pay_control = cakecounter
        print(cheese_pay_control)
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
        vegetopps = Products.objects.filter(component="1").order_by('name')
        beeftopps = Products.objects.filter(component="2").order_by('name')
        cheesetopps = Products.objects.filter(component="3").order_by('name')

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
        
        return redirect('/')

class CloseOrderNoneView(View):
    def get(self, request):
        
        return TemplateResponse(request, "product_list.html")


class OrdersView(View):
    pass








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
            ctx = {'products': products, 'otherSize': otherSize}
        else:
            ctx = {'products': products}
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