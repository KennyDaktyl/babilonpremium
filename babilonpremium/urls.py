from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from babilon.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', MainView.as_view(), name="main_view"),
    path('add_to_order/<int:pk>',
         AddToOrdersView.as_view(),
         name="add_to_order"),
    path('add_modyfi_to_order/<int:pk>/<int:modyfi>/',
         AddModyfiProduct.as_view(),
         name="add_modyfi_to_order"),
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
