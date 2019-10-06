from babilon.models import MainMenu, ProductSize, Products, Orders


def menu(request):
    menu = MainMenu.objects.all()
    ctx = {
        "menu": menu,
        "version": "1.0",
    }
    return ctx


def products(request):
    products = Products.objects.all()
    ctx = {
        "products": products,
        "version": "1.0",
    }
    return ctx


def order(request):
    order = Orders.objects.filter(active=True)
    ctx = {
        "order": order,
        "version": "1.0",
    }
    return ctx


def pizza_sizes(request):
    sizes = ProductSize.objects.filter(pizza=True)
    ctx = {
        "pizza_sizes": sizes,
        "version": "1.0",
    }
    return ctx


# def pracownicy(request):
#     pracownicy = MyUser.objects.all().order_by("username")
#     ctx = {
#         "pracownicy": pracownicy,
#         "version": "1.0",
#     }
#     return ctx
