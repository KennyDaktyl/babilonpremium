from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from django.forms import Textarea
from django.db.models.fields import TextField

from babilon.models import *

# Register your models here.

admin.site.register(MyUser)
admin.site.register(Products)
admin.site.register(ProductSize)
admin.site.register(Adress)
admin.site.register(Pizzeria)
admin.site.register(EmployeePosition)
admin.site.register(Clients)
admin.site.register(Vat)
admin.site.register(Orders)
admin.site.register(MainMenu)
admin.site.register(ToppingCategory)
admin.site.register(Toppings)
admin.site.register(PositionOrder)
admin.site.register(PizzaSize)


class ToppingsInline(admin.TabularInline):
    model = Toppings
    # exclude=['']
    extra = 3
    max_num = 6


class PizzaSizeInline(admin.TabularInline):
    model = PizzaSize
    fields = [
        'size',
    ]
    # extra = 3
    # max_num = 6


@admin.register(Pizza)
class PizzaAdmin(admin.ModelAdmin):
    exclude = ('change_info', )
    inlines = [ToppingsInline]
    search_fields = ['name']
    list_per_page = 10
    formfield_overrides = {
        TextField: {
            'widget': Textarea(attrs={
                'rows': 2,
                'cols': 100
            })
        },
    }

    # def save_model(self, request, obj, form, change):
    #     if not change:
    #         obj.autor = request.user
    #     obj.save()