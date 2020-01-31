from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from babilon_v1.views import *
from django.conf import settings
from django.conf.urls.static import static

from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets, generics
from babilon_v1.rest_class import *


urlpatterns = [
    url(r"^ws/", include(router.urls)),
    url(r"^api-auth/", include("rest_framework.urls")),
    path("pos/<int:pk>", PositionOrderViewSet.as_view(), name="PositionOrder"),
    path(
        "orders_for_drivers/<int:pk>",
        OrdersForDriversView.as_view(),
        name="orders_for_drivers",
    ),
    path(
        "orders_set_drivers/<int:pk>",
        OrdersSetDriversView.as_view(),
        name="orders_set_drivers",
    ),
    path(
        "driver_closed_order/<int:pk>",
        DriverClosedOrderView.as_view(),
        name="driver_close_order",
    ),
    path("admin/", admin.site.urls),
    path("", UserLoginView.as_view(), name="login"),
    path("logout/", User_Logout, name="logout"),
    path("local_status/", LocalStatusView.as_view(), name="local_status"),
    # Dodawanie produktów
    path("add_topp/", AddToppView.as_view(), name="add_topp"),
    path(
        "set_topp_price_by_size/",
        SetToppPriceBySize.as_view(),
        name="set_topp_price_by_size",
    ),
    path(
        "set_topps_price_by_size/<int:pk>",
        SetToppsPriceBySize.as_view(),
        name="set_topps_price_by_size",
    ),
    path("add_sauce/", AddSauceView.as_view(), name="add_sauce"),
    path("add_pizza/", AddPizzaView.as_view(), name="add_pizza"),
    path("add_pizza_premium/", AddPizzaPremiumView.as_view(), name="add_pizza_premium"),
    path("add_dish/", AddDishView.as_view(), name="add_dish"),
    path("add_topp_dish/", AddToppForDishView.as_view(), name="add_topp_for_dish"),
    path("add_category/", AddCategoryView.as_view(), name="add_category"),
    path("products_list/", ProductsListView.as_view(), name="products_list"),
    path("edit_product/<int:pk>", EditProductProView.as_view(), name="edit_product"),
    path("change_product/<int:pk>", ChangeProductView.as_view(), name="update_product"),
    path("del_product/<int:pk>", DelProductView.as_view(), name="del_product"),
    # Kasowanie ustawień sesji
    path(
        "set_session_pizzeria/",
        DelSessionPizzeriaView.as_view(),
        name="set_session_pizzeria",
    ),
    path("set_session_date/", SetSessionDateView.as_view(), name="set_session_date"),
    path(
        "set_session_today_date/",
        SetTodayDateView.as_view(),
        name="set_session_today_date",
    ),
    path(
        "set_session_month_date/",
        SetMonthDateView.as_view(),
        name="set_session_month_date",
    ),
    path(
        "set_session_period_date/",
        SetPeriodDateView.as_view(),
        name="set_session_period_date",
    ),
    # Kierdowcy, pracownicy
    path(
        "driver_mobile_view/<int:pk>",
        DriverMobileView.as_view(),
        name="driver_mobile_view",
    ),
    path(
        "order_outside_details/<int:pk>",
        DriverMobileOrderView.as_view(),
        name="driver_mobile_order_view",
    ),
    path("drivers/", DriversView.as_view(), name="drivers"),
    path(
        "set_driver_active/<int:pk>",
        SetDriversActiveView.as_view(),
        name="set_driver_active",
    ),
    path("del_worker/<int:pk>", DelDriverView.as_view(), name="del_driver"),
    path("menagers/", MenagersView.as_view(), name="menagers"),
    path("barmans/", BarmansView.as_view(), name="del_barman"),
    # Wydatki i koszty
    path("purchases/", PurchaseView.as_view(), name="purchases"),
    path("purchases/<int:pk>", PurchaseCategoryView.as_view(), name="purchases_cat"),
    path("edit_purchase/<int:pk>", EditPurchaseView.as_view(), name="edit_purchases"),
    path("del_purchase/<int:pk>", DelPurchaseView.as_view(), name="del_purchases"),
    path("statistics/", StatisticsView.as_view(), name="statistics"),
    # Zamówienia
    path("products/", ProductsView.as_view(), name="products"),
    path(
        "add_new_order_local/",
        AddNewOrderLocalView.as_view(),
        name="add_new_order_local",
    ),
    path(
        "add_new_order_outside/",
        AddNewOrderOutsideView.as_view(),
        name="add_new_order_outside",
    ),
    path(
        "add_new_order_driver/",
        AddNewOrderOutsideDriverView.as_view(),
        name="add_new_order_driver",
    ),
    path(
        "add_client_to_order/<int:pk>",
        AddClientToOrder.as_view(),
        name="add_client_to_order",
    ),
    path(
        "add_pizza_to_order/<int:order>/<int:prod>",
        AddPizzaToOrderView.as_view(),
        name="add_pizza_to_order",
    ),
    path(
        "add_pizza_freestyle_topps/<int:order>/<int:prod>",
        AddPizzaFreestyleToppsView.as_view(),
        name="add_pizza_freestyle_topps",
    ),
    path(
        "add_pizza_freestyle_to_order/<int:order>/<int:pos>",
        AddPizzaFreestyleToOrderView.as_view(),
        name="add_pizza_freestyle_to_order",
    ),
    path(
        "modyfi_pizza_freestyle_to_order/<int:order>/<int:pos>",
        ModyfiPizzaFreestyleToOrderView.as_view(),
        name="modyfi_pizza_freestyle_to_order",
    ),
    path(
        "change_topps_freestyle/<int:order>/<int:pos>",
        ChangeToppsFreestyleView.as_view(),
        name="change_topps_freestyle",
    ),
    path(
        "change_topps/<int:order>/<int:prod>",
        ChangeToppsView.as_view(),
        name="change_topps",
    ),
    path(
        "add_modyfi_pizza_to_order/<int:order>/<int:pos>",
        AddModyfiToOrderView.as_view(),
        name="add_modyfi_pizza_to_order",
    ),
    path(
        "update_pizza_to_order/<int:order>/<int:pos>",
        UpdatePizzaToOrderView.as_view(),
        name="update_pizza_to_order",
    ),
    path(
        "update_product_to_order/<int:order>/<int:pos>",
        UpdateProductToOrderView.as_view(),
        name="update_product_to_order",
    ),
    path(
        "update_topps/<int:order>/<int:pos>",
        UpdateToppsView.as_view(),
        name="update_topps",
    ),
    path(
        "half_pizza/<int:order>/<int:pk>/<int:size>/",
        Secend_Half_Pizza_SearchView.as_view(),
        name="add_secend_halfpizza",
    ),
    path(
        "left_and_right_halfpizza/<int:pizza_half>/<int:order>",
        Left_And_Right_Half_PizzaView.as_view(),
        name="left_and_right_halfpizza",
    ),
    path(
        "update_halfpizza_to_order/<int:order>/<int:pos>",
        UpdateHalfPizzaToOrderView.as_view(),
        name="update_halfpizza_to_order",
    ),
    path(
        "change_left_side/<int:order>/<int:pos>",
        ChangeLeftSidePizzaView.as_view(),
        name="change_left_side_pizza_to_order",
    ),
    path(
        "change_right_side/<int:order>/<int:pos>",
        ChangeRightSidePizzaView.as_view(),
        name="change_right_side_pizza_to_order",
    ),
    path(
        "change_topps_pizza_left/<int:order>/<int:pos>",
        ChangeLeftToppsView.as_view(),
        name="change_topps_pizza_left",
    ),
    path(
        "change_topps_pizza_right/<int:order>/<int:pos>",
        ChangeRightToppsView.as_view(),
        name="change_topps_pizza_right",
    ),
    path(
        "add_product_to_order/<int:order>/<int:prod>",
        AddProductToOrderView.as_view(),
        name="add_product_to_order",
    ),
    path(
        "products_category/<int:pk>",
        CategoryProductsView.as_view(),
        name="products_category",
    ),
    path("search_product/", SearchProductView.as_view(), name="search_product",),
    path("orders_archives/", OrdersArchivesView.as_view(), name="orders_archives"),
    path(
        "order_details_archives/<int:pk>",
        OrdersDetailsArchivesView.as_view(),
        name="orders_details_archives",
    ),
    path("orders/", OrdersView.as_view(), name="orders"),
    path("orders/filter/", OrdersFilterView.as_view(), name="orders_in_progress"),
    path(
        "order_details/<int:pk>", OrderCloseDeatailsView.as_view(), name="order_details"
    ),
    # path(
    #     "order_details_not_print/<int:pk>", OrderCloseDeatailsNotPrintView.as_view(), name="order_details_not_print"
    # ),
    path(
        "order_change_details/<int:pk>",
        OrderChangeDeatailsView.as_view(),
        name="order_change_details",
    ),
    path(
        "delete_position_order/<int:pk>",
        DeletePositionOrderView.as_view(),
        name="delete_position_order",
    ),
    path(
        "update_position_order/<int:pk>",
        UpdatePositionOrderView.as_view(),
        name="update_position_order",
    ),
    # PDF
    # path("ws/", include("rest_framework.urls")),
    path(
        "create_pdf_order/<int:pk>",
        CreatePDFOrderView.as_view(),
        name="create_pdf_order",
    ),
    # Kierowcy
    path("driver_courses/<int:pk>", DriverCoursesView.as_view(), name="driver_courses"),
    path(
        "del_driver_from_order/<int:pk>",
        DelDriverFromOrderView.as_view(),
        name="del_driver_from_order",
    ),
    # Klienci
    path("clients/", ClientsView.as_view(), name="clients"),
    path("client/<int:pk>", ClientView.as_view(), name="client"),
    path("edit_client/<int:pk>", EditClientView.as_view(), name="edit_client"),
    path("add_new_client/", AddNewClientView.as_view(), name="add_new_client"),
    path(
        "add_client_new_address/<int:pk>",
        AddClientNewAddressView.as_view(),
        name="add_client_new_address",
    ),
    path("edit_address/<int:pk>", EditAddressView.as_view(), name="edit_address"),
    path("del_address/<int:pk>", DelAddressView.as_view(), name="del_client_address"),
] + static(settings.STATIC_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
