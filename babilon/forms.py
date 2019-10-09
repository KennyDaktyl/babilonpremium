from django import forms
from django.forms import ModelForm
from django.core.exceptions import ValidationError
from babilon.models import *
from babilon.choices_field import *


class OrderForm(forms.Form):
    Clients = forms.ModelChoiceField(label="Numer telefonu",
                                     queryset=Clients.objects.all())
    Procuct = forms.ModelChoiceField(label="Pizza",
                                     queryset=Products.objects.all())
    Size = forms.ModelChoiceField(label="Rozmiar",
                                  queryset=ProductSize.objects.all())


class AddPizzaForm(forms.Form):
    name = forms.CharField(label="Nazwa pizzy rozmiar 30",
                           min_length=3,
                           max_length=128)
    size = forms.ModelChoiceField(
        label="Rozmiar", queryset=ProductSize.objects.filter(pizza=True))
    # vegetopps = forms.ModelMultipleChoiceField(
    #     label="Dodaj składniki warzywne",
    #     queryset=Products.objects.filter(topping__id=1),
    #     required=False)
    # beeftopps = forms.ModelMultipleChoiceField(
    #     label="Dodaj składniki mięsne",
    #     queryset=Products.objects.filter(topping__id=4),
    #     required=False)
    price = forms.DecimalField(label="Cena pizzy",
                               max_digits=19,
                               decimal_places=2)
