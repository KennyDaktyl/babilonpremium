from django import forms
from django.forms import ModelForm
from django.core.exceptions import ValidationError
from django.contrib.admin import widgets
from django.utils.dates import MONTHS
from babilon_v1.models import *
from babilon_v1.choice_field import *
from django.contrib.auth.models import Group

year_range = (
    "2019",
    "2020",
    "2021",
    "2022",
    "2023",
    "2024",
    "2025",
    "2026",
    "2027",
)


class SetPassowrdForm(ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = MyUser
        fields = ["password"]


class LoginForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={"class": "form-control col-10 col-lg-4 mx-auto h1 text-center"}
        )
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control col-10 col-lg-4 mx-auto h1 display-1 text-center"
            }
        )
    )


class AddToppForm(forms.Form):
    type_of_ingredient = forms.ChoiceField(
        choices=INGREDIENT_TYPE_FORM,
        label="Rodzaj składnika",
        widget=forms.Select(),
        required=True,
        help_text="*",
    )
    topp_name = forms.CharField(label="Nazwa dodatku", min_length=3, max_length=128)


class AddSauceForm(forms.Form):
    sauce_type = forms.ChoiceField(
        choices=SAUCES_TYPE,
        label="Rodzaj sosu",
        widget=forms.Select(),
        required=True,
        help_text="*",
    )
    sauce_name = forms.CharField(label="Nazwa dodatku", min_length=3, max_length=128)
    price = forms.FloatField(label="Cena sosu", help_text="", required=False)


class AddDrink(forms.Form):
    lista = [4, 5]
    category_drink = forms.ModelChoiceField(
        label="Categoria napoju",
        queryset=Category.objects.filter(category_number__in=lista),
    )
    size_drink = forms.ModelChoiceField(
        label="Rozmiar napoju", queryset=ProductSize.objects.filter(bottle=True)
    )
    drink_name = forms.CharField(label="Nazwa napoju", min_length=0, max_length=64)
    price = forms.FloatField(label="Cena napoju", help_text="*")


class AddPizzaForm(forms.Form):
    pizza_number = forms.IntegerField(label="Numer pizzy",)
    pizza_name = forms.CharField(label="Nazwa Pizzy", min_length=3, max_length=64)
    toppings = forms.ModelMultipleChoiceField(
        required=False,
        label="Składniki pizzy",
        widget=forms.CheckboxSelectMultiple,
        queryset=Products.objects.filter(pizza_topp=True),
    )
    price_1 = forms.FloatField(label="Cena pizzy 30", help_text="*")
    price_2 = forms.FloatField(label="Cena pizzy 40", help_text="*")
    price_3 = forms.FloatField(label="Cena pizzy 50", help_text="*")
    pizza_freestyle = forms.BooleanField(
        label="Pizza freestyle", initial=False, required=False
    )


class AddDishForm(forms.Form):
    category = forms.ModelChoiceField(
        queryset=Category.objects.all(),
        label="Kategoria w menu",
        widget=forms.Select(),
        required=True,
        help_text="*",
    )
    dish_name = forms.CharField(label="Nazwa dania", min_length=3, max_length=64)
    toppings = forms.ModelMultipleChoiceField(
        required=False,
        label="Składniki dana",
        widget=forms.CheckboxSelectMultiple,
        queryset=Products.objects.filter(dish_topp=True),
    )

    price = forms.FloatField(label="Cena dania", help_text="*")


class AddToppForDishForm(forms.Form):
    topp_name = forms.CharField(
        label="Nazwa dodatku", min_length=3, max_length=128, help_text="*"
    )
    price = forms.FloatField(label="Cena dodatku",)


class AddCategoryForm(forms.Form):
    category_number = forms.IntegerField(
        label="Numer wyświetlania kategorii", help_text="wpisz cyfrę"
    )
    category_name = forms.CharField(
        label="Nazwa kategorii", min_length=3, max_length=128, help_text="*"
    )


class SetLocalStatsForm(forms.Form):
    pizzeria = forms.ModelChoiceField(
        label="Wybierz lokal", queryset=WorkPlace.objects.all()
    )


class SetDataStatsForm(forms.Form):
    date_start = forms.DateField(
        initial=datetime.now().date,
        label="Od",
        widget=forms.SelectDateWidget(years=year_range),
    )
    date_end = forms.DateField(
        initial=datetime.now().date,
        label="Do",
        widget=forms.SelectDateWidget(years=year_range),
    )


class SetTodayStatsForm(forms.Form):
    cur_year = datetime.today().year
    today_show = forms.DateField(
        initial=datetime.now().date, widget=forms.SelectDateWidget(years=year_range),
    )


month_choices = MONTHS.items()


class SetMonthStatsForm(forms.Form):
    month = forms.ChoiceField(
        choices=month_choices,
        label="Miesiąc",
        widget=forms.Select(),
        required=True,
        help_text="*",
    )


class DriverForm(forms.Form):
    username = forms.CharField(label="UserName", max_length=32, help_text="*")
    password = forms.CharField(widget=forms.PasswordInput())
    group = forms.ModelChoiceField(
        label="Grupa praw dostępu", queryset=Group.objects.all(), help_text="*"
    )
    first_name = forms.CharField(label="Imię", max_length=32, required=False)
    last_name = forms.CharField(label="Nazwisko", max_length=32, help_text="*")
    rate = forms.FloatField(
        label="Stawka za kurs", min_value=0, max_value=100, help_text="*"
    )
    phone_number = forms.CharField(
        label="Numer telefonu",
        min_length=9,
        max_length=9,
        help_text="9-cyfr (500111222)",
    )
    street = forms.CharField(
        label="ulica zamieszkania",
        max_length=64,
        required=False,
        help_text="Nie musi być",
    )
    city = forms.CharField(
        label="Miasto", max_length=64, required=False, help_text="Nie musi być"
    )

    info = forms.CharField(
        label="Info", widget=forms.Textarea, max_length=200, required=False
    )

    class Meta:
        model = MyUser


class MenagerForm(forms.Form):
    username = forms.CharField(label="UserName", max_length=32, help_text="*")
    password = forms.CharField(widget=forms.PasswordInput())
    group = forms.ModelChoiceField(
        label="Grupa praw dostępu", queryset=Group.objects.all(), help_text="*"
    )
    first_name = forms.CharField(label="Imię", max_length=32, required=False)
    last_name = forms.CharField(label="Nazwisko", max_length=32, help_text="*")
    work_places = forms.ModelMultipleChoiceField(
        label="Wybierz lokal", queryset=WorkPlace.objects.all()
    )
    phone_number = forms.CharField(
        label="Numer telefonu",
        min_length=9,
        max_length=9,
        help_text="9-cyfr (500111222)",
    )
    street = forms.CharField(
        label="ulica zamieszkania",
        max_length=64,
        required=False,
        help_text="Nie musi być",
    )
    city = forms.CharField(
        label="Miasto", max_length=64, required=False, help_text="Nie musi być"
    )

    info = forms.CharField(
        label="Info", widget=forms.Textarea, max_length=200, required=False
    )

    class Meta:
        model = MyUser


class BarmanForm(forms.Form):
    username = forms.CharField(label="UserName", max_length=32, help_text="*")
    password = forms.CharField(widget=forms.PasswordInput())
    group = forms.ModelChoiceField(
        label="Grupa praw dostępu", queryset=Group.objects.all(), help_text="*"
    )
    first_name = forms.CharField(label="Imię", max_length=32, required=False)
    last_name = forms.CharField(label="Nazwisko", max_length=32, help_text="*")
    work_place = forms.ModelChoiceField(
        label="Wybierz lokal", queryset=WorkPlace.objects.all()
    )
    phone_number = forms.CharField(
        label="Numer telefonu",
        min_length=9,
        max_length=9,
        help_text="9-cyfr (500111222)",
    )
    street = forms.CharField(
        label="ulica zamieszkania",
        max_length=64,
        required=False,
        help_text="Nie musi być",
    )
    city = forms.CharField(
        label="Miasto", max_length=64, required=False, help_text="Nie musi być"
    )

    info = forms.CharField(
        label="Info", widget=forms.Textarea, max_length=200, required=False
    )

    class Meta:
        model = MyUser


class AddShoppingForm(forms.Form):
    shopping_name = forms.ChoiceField(
        choices=CONTRACTOR_NAME,
        label="Nazwa sklepu",
        widget=forms.Select(),
        required=True,
        help_text="*",
    )

    pay_method = forms.ChoiceField(
        choices=PAY_METHOD_2,
        label="Rodzaj płatności",
        widget=forms.Select(),
        required=True,
        help_text="*",
    )
    price = forms.FloatField(label="Kwota", help_text="*", min_value=0)
    info = forms.CharField(label="Info", max_length=256, required=False)


class AddTaxForm(forms.Form):
    tax_name = forms.ChoiceField(
        choices=TAX_TYPE,
        label="Nazwa podatku",
        widget=forms.Select(),
        required=True,
        help_text="*",
    )

    pay_method = forms.ChoiceField(
        choices=PAY_METHOD_2,
        label="Rodzaj płatności",
        widget=forms.Select(),
        required=True,
        help_text="*",
    )
    price = forms.FloatField(label="Kwota", help_text="*", min_value=0)
    info = forms.CharField(label="Info", max_length=256, required=False)


class AddRewardForm(forms.Form):
    worker = forms.ModelChoiceField(
        label="Wybierz pracownika", queryset=MyUser.objects.all()
    )

    pay_method = forms.ChoiceField(
        choices=PAY_METHOD_2,
        label="Rodzaj płatności",
        widget=forms.Select(),
        required=True,
        help_text="*",
    )
    price = forms.FloatField(label="Kwota", help_text="*", min_value=0)
    info = forms.CharField(label="Info", max_length=256, required=False)


class AddConstForm(forms.Form):
    const_name = forms.ChoiceField(
        choices=TYPE_OF_FIXED_COST,
        label="Nazwa kosztu stałego",
        widget=forms.Select(),
        required=True,
        help_text="*",
    )

    pay_method = forms.ChoiceField(
        choices=PAY_METHOD_2,
        label="Rodzaj płatności",
        widget=forms.Select(),
        required=True,
        help_text="*",
    )
    price = forms.FloatField(label="Kwota", help_text="*", min_value=0)

    info = forms.CharField(label="Info", max_length=256, required=False)


class AddOtherForm(forms.Form):
    other_name = forms.CharField(
        label="Nazwa wydatku", max_length=256, required="False"
    )

    pay_method = forms.ChoiceField(
        choices=PAY_METHOD_2,
        label="Rodzaj płatności",
        widget=forms.Select(),
        required=True,
        help_text="*",
    )
    price = forms.FloatField(label="Kwota", help_text="*", min_value=0)

    info = forms.CharField(label="Info", max_length=256, required=False)


class ClientForm(forms.Form):
    phone_number = forms.CharField(
        label="Numer telefonu", max_length=15, help_text="*, 15-cyfr (500111222333)"
    )
    firstlastname = forms.CharField(
        label="Dane klienta", max_length=128, required=False
    )

    adres_1 = forms.CharField(
        label="Adres 1", max_length=128, help_text="* , minimum 1 adres"
    )
    # adres_2 = forms.CharField(label="Adres 2", max_length=128, required=False)
    # adres_3 = forms.CharField(label="Adres 3", max_length=128, required=False)
    # adres_4 = forms.CharField(label="Adres 4", max_length=128, required=False)
    # adres_5 = forms.CharField(label="Adres 5", max_length=128, required=False)
    status = forms.ChoiceField(
        choices=CLIENT_STATUS,
        label="Status",
        initial="1",
        widget=forms.Select(),
        required=True,
        help_text="*",
    )
    info = forms.CharField(
        label="Info", widget=forms.Textarea, max_length=200, required=False
    )


class CleintNewAddressForm(forms.Form):

    new_address = forms.CharField(label="Nowy adres", max_length=128, help_text="*")

    # def clean(self, pk):
    #     ilosc = self
    #     quantity = Czesc.objects.get(pk=pk)
    #     if (quantity.ilosc < ilosc):
    #         raise ValidationError("Insufficient inventory")

