from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from babilon.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', MainView.as_view(), name="main_view"),
    #     path('product/<int:id>', ProductView.as_view(), name="main_view_id"),
    path('add_to_order/<int:pk>',
         AddToOrdersView.as_view(),
         name="add_to_order"),
    path('add_modyfi_to_order/<int:pk>/<int:modyfi>/',
         AddModyfiProductWithOut.as_view(),
         name="add_modyfi_to_order_without"),
    path(
        'add_modyfi_to_order/<int:pk>/<int:modyfi>/<str:extra_price>/<str:cake>/<str:changes>/',
        AddModyfiProduct.as_view(),
        name="add_modyfi_to_order"),
    path('add_position_to_order/',
         AddPositionToOrder.as_view(),
         name="add_position_to_order"),
    path('update_order/<int:pk>',
         UpdateOrderView.as_view(),
         name="update_order"),
    path('delete_position_order/<int:pk>',
         DeletePositionOrderView.as_view(),
         name="delete_position_order"),
    path('update_position_order/<int:pk>',
         UpdatePositionOrderView.as_view(),
         name="update_position_order"),
    path('category_list/<int:pk>',
         CategoryListView.as_view(),
         name="category_list"),
    path('change_topps/<int:pk>/<int:modyfi>/',
         ChangeToppsView.as_view(),
         name="change_topps"),
    #     path('change_topps/', ChangeToppView.as_view(), name="change_topp"),
    path('close_order/<int:pk>', CloseOrderView.as_view(), name="close_order"),
    # path('check_add_product/',
    #      CheckAddProductView.as_view(),
    #      name="check_add_product"),
    path('zamowienia/', OrdersView.as_view(), name="orders"),
    path('lista_produktow/', ProductsView.as_view(), name="products"),
    path('lista_klientow/', ClientsView.as_view(), name="clients"),
    path('lista_pracownikow/', EmployesView.as_view(), name="employes"),
    path('stan_magazynu/', StanMagazynuView.as_view(), name="stock"),
    path('dodaj_zamowienie_wywoz/',
         AddOrderOutsideView.as_view(),
         name="dodajzamowiewywoz"),
    path('delete_from_pizza/', PizzaMixView.as_view(), name="pizza_mix"),
    path('add_pizza/', AddPizzaView.as_view(), name="add_pizza"),
    path('pizza_edit/', PizzaEdit.as_view(), name="pizza_edit")
] + static(settings.STATIC_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:  # new
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
