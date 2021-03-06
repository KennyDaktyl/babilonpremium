from .models import *
from rest_framework import routers, serializers, viewsets, generics
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.http import JsonResponse

# from babilon_v1.views import today, month, year
import json
from django.http import JsonResponse

from rest_framework.views import APIView
from rest_framework import permissions
import json


# Serializers define the API representation.
class OrdersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Orders
        depth = 2
        fields = (
            "id",
            "order_total_price2",
            "printed",
            "info",
            "discount",
            "sms_send",
            "time_delivery_in",
            "start_delivery_time",
            "pay_method",
            "address",
            "type_of_order",
            "driver_id",
            "barman_id",
            "workplace_id",
            "time_zero",
            "time_start",
            "date",
            "status",
            "number",
            "active",
            "promo",
        )
        ordering_fields = "__all__"
        ordering = ("name", )


class WorkPlaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkPlace
        depth = 2
        fields = ("id", "workplace_name")
        ordering_fields = "__all__"
        ordering = ("id", )


class PostionOrderSerializer(serializers.ModelSerializer):
    freestyle_toppings = serializers.StringRelatedField(many=True)

    class Meta:
        model = PositionOrder
        depth = 2
        fields = (
            "id",
            "order_id",
            "quantity",
            "product_id",
            "product_id_pizza_right",
            "size_id",
            "halfpizza_name",
            "pizza_half",
            "change_topps_info",
            "change_topps_info_id",
            "change_topps_info_other_side",
            "freestyle_toppings",
            "change_topps_info_right_id",
            "cake_info",
            "sauces_free",
            "sauces_pay",
            "extra_price",
            "info",
            "price",
            "discount",
            "total_price",
        )
        ordering_fields = "__all__"
        ordering = ("id", )


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = "__all__"
        ordering_fields = "__all__"
        ordering = ("id", )


# ViewSets define the view behavior.


class OrdersViewSet(viewsets.ModelViewSet):
    # Login authorisiation for client
    permission_classes = [permissions.DjangoModelPermissions]

    queryset = Orders.objects.filter(printed=False)
    serializer_class = OrdersSerializer


class WorkPlaceViewSet(viewsets.ModelViewSet):
    # Login authorisiation for client
    permission_classes = [permissions.DjangoModelPermissions]
    queryset = WorkPlace.objects.filter(is_active=True)
    serializer_class = WorkPlaceSerializer


# @method_decorator(login_required, name="dispatch")
class PositionOrderViewSet(generics.ListAPIView):
    # Login authorisiation for client
    permission_classes = [permissions.DjangoModelPermissions]
    serializer_class = PostionOrderSerializer

    def get_queryset(self):
        """
        This view should return a list of all the purchases for
        the user as determined by the username portion of the URL.
        """
        order_id = self.kwargs["pk"]
        order = Orders.objects.get(pk=order_id)
        order.printed = True
        order.save()
        return PositionOrder.objects.filter(
            order_id=order_id).order_by("product_id")


# @method_decorator(login_required, name="dispatch")
class OrdersForWorkplaceView(generics.ListAPIView):
    permission_classes = [permissions.DjangoModelPermissions]
    serializer_class = OrdersSerializer

    def get_queryset(self):
        pk = self.kwargs["pk"]
        year = datetime.now().year
        month = datetime.now().month
        day = datetime.now().day
        orders = (Orders.objects.filter(workplace_id=pk).filter(
            printed=False).filter(date__day=day).filter(
                date__month=month).filter(date__year=year))
        return orders


# @method_decorator(login_required, name="dispatch")
class OrdersForDriversView(generics.ListAPIView):
    serializer_class = OrdersSerializer

    def get_queryset(self):
        pk = self.kwargs["pk"]
        year = datetime.now().year
        month = datetime.now().month
        day = datetime.now().day
        orders = (Orders.objects.filter(workplace_id=pk).filter(
            status=2).filter(driver_id=None).filter(date__day=day).filter(
                date__month=month).filter(date__year=year).exclude(
                    address=None))
        return orders


router = routers.DefaultRouter()
router.register(r"order", OrdersViewSet, basename="order")
router.register(r"workplaces", WorkPlaceViewSet, basename="work_places")
