JOB_STATUS = (
    (0, "Właściciel"),
    (1, "Menager"),
    (2, "Barman"),
    (3, "Pizzer"),
    (4, "Kierowca"),
)

CONTRACT_TYPE = (
    (0, "Umowa o prace"),
    (1, "Umowa zlecenie"),
    (2, "Brak danych"),
    (3, "Licznik wyjazdów"),
)
INGREDIENT_TYPE = (
    (1, "Warzywny"),
    (2, "Mięsny"),
    (3, "Serowy"),
    (4, "Dodatki extra"),
    (5, "Rodzaj ciasta"),
    (6, "Sosy płatne"),
    (7, "Sosy darmowe"),
    (8, "Dodatki extra_1"),
    (9, "Dodatki extra_2"),
    (10, "Dodatki extra_3"),
    (11, "Dodatki extra_4"),
)

INGREDIENT_TYPE_FORM = (
    (1, "Warzywny"),
    (2, "Mięsny"),
    (3, "Serowy"),
    (4, "Dodatki extra"),
    (8, "Dodatki extra_1"),
    (9, "Dodatki extra_2"),
    (10, "Dodatki extra_3"),
    (11, "Dodatki extra_4"),
)

SAUCES_TYPE = ((6, "Sosy płatne"), (7, "Sosy darmowe"))

CLIENT_STATUS = ((0, "Vip"), (1, "Normal"), (2, "Podejrzany"))

ORDER_STATUS = (
    (1, "Otwarte"),
    (2, "W przygotowaniu"),
    (3, "W dostawie"),
    (4, "Zrealizowane"),
    (5, "Anulowane"),
)

DELIVERY_TYPE = (
    (1, "Lokal"),
    (2, "Wynos"),
    (3, "Dostawa"),
)

DRIVER_STATUS = (
    (1, "Wolny"),
    (2, "W dostawie"),
    (3, "Powrót"),
)

PAY_METHOD = (
    (1, "Gotówka"),
    (2, "Karta"),
    (3, "Online_1"),
    (4, "Online_2"),
    (5, "Online_3"),
    (6, "Online_4"),
    (7, "Online_5"),
)

PAY_METHOD_2 = (
    (1, "Gotówka"),
    (2, "Karta"),
    (3, "Przelew"),
)

TYPE_OF_PURCHASE = (
    (0, "Zakup towarów"),
    (1, "Wypłata pracownikom"),
    (2, "Podatki/ZUS"),
    (3, "Koszta stałe"),
    (4, "Inne wydatki"),
)

CONTRACTOR_NAME = (
    (0, "Biedronka"),
    (1, "Makro"),
    (2, "Szubryt"),
    (3, "Pepsi"),
    (4, "Clock Food"),
    (5, "Kartony"),
    (6, "Inne"),
)

TAX_TYPE = (
    (0, "VAT-7"),
    (1, "PIT-5"),
    (2, "PIT-4"),
    (3, "ZUS"),
    (4, "L-4"),
    (5, "Inne"),
)

TYPE_OF_FIXED_COST = (
    (0, "Czynsz"),
    (1, "Internet"),
    (2, "Prąd"),
    (3, "Ulotki/kolportarz"),
    (4, "Prowizje pizza_portal"),
    (5, "Prowizje pyszne.pl"),
    (6, "Prowizje terminal"),
    (7, "Leasing"),
    (8, "Usługi księgowe"),
    (9, "Straty"),
    (10, "Inne"),
)
