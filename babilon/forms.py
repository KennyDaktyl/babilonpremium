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

    price = forms.DecimalField(label="Cena pizzy",
                               max_digits=19,
                               decimal_places=2)


class CleintForm(forms.Form):
    phone_number = forms.CharField(label="Numer telefonu",
                                   max_length=9,
                                   help_text="*, 9-cyfr (500111222333)")
    firstlastname = forms.CharField(label="Dane klienta",
                                    max_length=128,
                                    required=False)

    adres_1 = forms.CharField(label="Adres 1",
                              max_length=128,
                              help_text="* , minimum 1 adres")
    adres_2 = forms.CharField(label="Adres 2", max_length=128, required=False)
    adres_3 = forms.CharField(label="Adres 3", max_length=128, required=False)
    adres_4 = forms.CharField(label="Adres 4", max_length=128, required=False)
    adres_5 = forms.CharField(label="Adres 5", max_length=128, required=False)
    status = forms.ChoiceField(choices=STATUS_KLIENTA,
                               label="Status",
                               initial='1',
                               widget=forms.Select(),
                               required=True,
                               help_text='*')
    info = forms.CharField(label="Info",
                           widget=forms.Textarea,
                           max_length=200,
                           required=False)


class CleintNewAddressForm(forms.Form):

    new_address = forms.CharField(label="Nowy adres",
                                  max_length=128,
                                  help_text="*")
