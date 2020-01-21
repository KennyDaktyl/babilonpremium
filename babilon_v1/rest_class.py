from .models import *
from rest_framework import routers, serializers, viewsets, generics
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.http import JsonResponse

from babilon_v1.views import today, month, year
import json
from django.http import JsonResponse


# Serializers define the API representation.
class OrdersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Orders
        depth = 1
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
        ordering = ("name",)


class PostionOrderSerializer(serializers.ModelSerializer):
    freestyle_toppings = serializers.StringRelatedField(many=True)

    class Meta:
        model = PositionOrder
        depth = 1
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
        ordering = ("id",)


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = "__all__"
        ordering_fields = "__all__"
        ordering = ("id",)


# ViewSets define the view behavior.
@method_decorator(login_required, name="dispatch")
class OrdersViewSet(viewsets.ModelViewSet):
    queryset = Orders.objects.filter(printed=False)
    # queryset = Orders.objects.values("workplace_id").distinct()
    serializer_class = OrdersSerializer


@method_decorator(login_required, name="dispatch")
class PositionOrderViewSet(generics.ListAPIView):
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
        return PositionOrder.objects.filter(order_id=order_id).order_by("product_id")


@method_decorator(login_required, name="dispatch")
class OrdersForDriversView(generics.ListAPIView):
    serializer_class = OrdersSerializer

    def get_queryset(self):
        """
        This view should return a list of all the purchases for
        the user as determined by the username portion of the URL.
        """
        pk = self.kwargs["pk"]
        orders = (
            Orders.objects.filter(workplace_id=pk)
            .filter(status=2)
            .filter(driver_id=None)
            .filter(date__day=today)
            .filter(date__month=month)
            .filter(date__year=year)
        )
        # orders = json.dumps({"data": self.get_queryset()})
        # orders = json.dumps(list(orders.values()))
        # print(orders)
        return orders


@method_decorator(login_required, name="dispatch")
class OrdersSetDriversView(generics.ListAPIView):
    serializer_class = OrdersSerializer

    def get_queryset(self, *args, **kwargs):
        """
        This view should return a list of all the purchases for
        the user as determined by the username portion of the URL.
        """
        pk = self.kwargs["pk"]
        # order_id = self.kwargs["order_id"]

        orders = (
            Orders.objects.filter(workplace_id=pk)
            .filter(status=3)
            .filter(date__day=today)
            .filter(date__month=month)
            .filter(date__year=year)
        )
        print(orders)

        return orders


@method_decorator(login_required, name="dispatch")
class DriverClosedOrderView(generics.ListAPIView):
    serializer_class = OrdersSerializer

    def get_queryset(self, *args, **kwargs):
        """
        This view should return a list of all the purchases for
        the user as determined by the username portion of the URL.
        """
        pk = self.kwargs["pk"]
        # order_id = self.kwargs["order_id"]

        orders = (
            Orders.objects.filter(workplace_id=pk)
            .filter(status=4)
            .filter(date__day=today)
            .filter(date__month=month)
            .filter(date__year=year)
        )
        print(orders)

        return orders


router = routers.DefaultRouter()
router.register(r"order", OrdersViewSet, basename="order")
