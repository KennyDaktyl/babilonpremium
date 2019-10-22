$(document).ready(function () {
    //Button ze składnikami pizzy stworzonymi przez autora
    var topps = $('button.topps')
    //Link w buttonie Zapisz dzieki któremu przekazuje w url teks GETem do widoku dodaj pizze
    var link = $('#link').attr('href');

    var price_size_vege = $('#price_size_vege').data('vege_price');
    // price_size_vege = price_size_vege.replace(",", ".");
    // price_size_vege = parseFloat(price_size_vege);
    // price_size_vege = price_size_vege.toFixed(2);


    var price_size_beef = $('#price_size_beef').data('beef_price');
    // price_size_beef = price_size_beef.replace(",", ".");
    // price_size_beef = parseFloat(price_size_beef);
    // price_size_beef = price_size_beef.toFixed(2);
    var ctr_gr_vege = 0;
    var ctr_gr_beef = 0;
    // var sum_ctr_gr_beef = eval(ctr_gr_beef.join("+"))
    // sum_ctr_gr_beef = parseInt(sum_ctr_gr_beef);
    var ctr_gr_extra = 0;
    // var sum_ctr_gr_extra = eval(ctr_gr_extra.join("+"));
    // sum_ctr_gr_extra = parseInt(sum_ctr_gr_extra);


    //Widok dodaj pizze ilość plus i minus jeden
    var qplus = $("#quantity_plus");
    var qminus = $("#quantity_minus");
    var quantity = $("#quantity");

    //Dodatki vege, beef i cheese
    var vegetopps = $('button.vegetopps')
    //Zmiana na czerowno ilość dodatków ponad orginalny skład pizzy podzielone ne kategorie
    var change_vege = $('#change_vege')
    var beeftopps = $('button.beeftopps');
    var change_beef = $('#change_beef');
    var change_cake = $('#change_cake');

    var cheesetopps = $('button.cheesetopps');
    var change_cheese = $('#change_cheese');

    var extratopps = $('button.extratopps');
    var change_extra = $('#change_extra');

    var caketopps = $('button.caketopps');
    var change_cake = $('#change_cake');


    //dodatki wybrane pierwszy element
    var add_topps = $('span.nobody');
    var suma_vege = 0;
    var suma_beef = 0;
    var suma_cheese = 0;
    var suma_extra = 0;
    var suma_cake = 0;
    var suma_sauce = 0;

    var cake_price = 0;
    array_extra_price = [0, ];
    array_extra_sauce = [0, ];

    //liczniki składników wykorzystuwane do funkcji i=i+1 oraz i=i-1
    var i_vege = $('#change_vege').data('vege_plus');
    var i_beef = $('#change_beef').data('beef_plus');
    var i_cheese = $('#change_cheese').data('cheese_plus');
    var i_extra = $('#change_extra').data('extra_plus');
    var i_cake = $('#change_cake').data('cake_plus');

    //span z liczbą cena za składniki wspólna dla wszystkich (pamietaj ustawione na if extra_price<1.00)
    var extra_price = $('#extra_price');
    var cake_topp_price = 0;
    //tekst wysyłane GETem do widoku dodaj pizze
    var text_changes_del = $('#text_change_topps_del');
    var text_changes_add = $('#text_change_topps_add');
    var cake_text_changes = $('#text_change_cake');
    var caketext = " ";
    var text_add = " ";
    var text_minus = " ";




    //var span_vege = $('#price_add_vege_topp');


    //var span_beef = $('#price_add_beef_topp');
    beef_adds = $('#price_add_beef_topp').data('price');

    //var span_cheese = $('#price_add_cheese_topp');
    cheese_adds = $('#price_add_cheese_topp').data('price');

    extra_adds = $('span.price_add_extra_topp').data('price');
    cake_adds = $('#price_add_cake_topp').data('price');

    //widok dodaj pizze bez zmian (edycja sosów,info,rabatu i ilości)
    var sauce_free = $('button.sauce_free');
    var sauce_pay = $('button.sauce_pay');
    var sauce_free_text = $('#sauce_free_text');
    var sauce_pay_text = $('#sauce_pay_text');
    var text_sauce_free = "";
    var text_sauce_pay = "";
    var extra_price_edit = $('#extra_price_edit');
    var sauces_form = $('#sauces_form');
    var add_sauces_free = $('#add_sauces_free');
    var add_sauces_pay = $('#add_sauces_pay');

    var size_button = $('.Pizza');
    var pizza_button = $('.product button');


    //Składniki stworzone przez autora pizze zmienają klasę oraz mają wpływ na licznik składników
    topps.each(function (index) {

        $(this).on("click", function () {
            //typ składnika (vege 1, beef 2, cheese 3)
            var type = $(this).data('type');
            if (type == 1) {
                //jesli ma klasę danger jest na pizzy
                if ($(this).hasClass("btn-danger")) {
                    //kliknięcie na niego odejmuje licznik składników w kategorii
                    i_vege -= 1;
                    ctr_gr_vege -= 1;
                    //edycja tekstu dla pizzera o zmianie
                    text_minus = text_minus.replace("b_z", "");
                    text_minus = "-" + $(this).html() + ", " + text_minus;
                    text_changes_del.append('<li>jdjdjd</li>');
                    // text = text.html("<br>");
                    //zapis do zmiennej
                    //jeśli licznik jest większy od 0 liczy extra_price
                    var tab = eval(array_extra_price.join("+")).toFixed(2);


                    var newlink = link + tab + "/";
                    $('#link').attr("href", newlink + caketext + "/" + text_minus + text_add + "");


                    if (i_vege >= 0) {
                        //pobierz dane o cenie składnika z butttona i jedo attr data-price
                        var vege_topp = price_size_vege.data('price');
                        //zamien , na . (inaczej nie liczy) pamietaj w modelu zrób float!
                        vege_adds = vege_topp.replace(',', ".");
                        //skoro odejmujemy cenę to przed dodaniem do tabicy SUMA skłądników obracamy na liczbę ujemną
                        p = price_size_vege * -1;
                        //dodajemy do teblicy suma za extra_prcie
                        array_extra_price.push(p);
                        //liczymy sumę elementów w tablicy z 2 liczbami po przecinku
                        var tab = eval(array_extra_price.join("+")).toFixed(2);
                        //wklejamu tekst do spana pokazującego cena za extra składniki dla pizzy
                        extra_price.text(tab);
                        //warunkiem klienta jeśli róznica skłądników mniejsza od jeden to nie ustaw na 0



                        if (tab < 1.0) {
                            extra_price.text(0);
                        }
                    }
                    //aktualizujemy nasz licznik składników
                    change_vege.text(i_vege);
                    //podmieniamy klasy buttona jako odklikniety
                    $(this).removeClass("btn-danger")
                    $(this).addClass("btn-secondary")
                    //teraz mamy odznaczony składnik a więć jeśli ko znowu klikniemy

                } else {
                    alert("Skasuj");

                    //     //wjeżdza znomu na pizze i dodaje nam licznik skladników
                    //     i_vege += 1;
                    //     ctr_gr_vege += 1;
                    //     //znajduje tekst o odjęciu składnika i podmienia/usówa go!
                    //     text = text.replace(("-" + $(this).text() + ", "), "");

                    //     //aktualizuje go w zmiennej
                    //     text_changes.text(text);

                    //     if (text.length == 1) {
                    //         text = "b_z";
                    //     }

                    //     var tab = eval(array_extra_price.join("+")).toFixed(2);
                    //     var newlink = link + tab + "/";
                    //     $('#link').attr("href", newlink + caketext + "/" + text + "");
                    //     //aktualizuje licznik składników
                    //     change_vege.text(i_vege);
                    //     //podmienia klasy buttona poznieważ znowu jest jednak na pizzy
                    //     $(this).removeClass("btn-secendary");
                    //     $(this).addClass("btn-danger");
                    //     //jeśli licznik jest ponad 0 to licz cena za skłądniki
                    //     if (i_vege > 0) {
                    //         //pobiera attr price z kliknietego butttona ze skłądnikiem
                    //         var vege_topp = ($(this).data('price'));
                    //         vege_adds = vege_topp.replace(',', ".");
                    //         p = vege_adds * -1;
                    //         array_extra_price.push(vege_adds);
                    //         var tab = eval(array_extra_price.join("+")).toFixed(2);
                    //         extra_price.text(tab);
                    //         if (tab < 1) {
                    //             extra_price.text(0);
                    //         }
                    //     }
                }

            }
            //tutaj jest to samo tylko kategoria 2 czyli dodatki mięsne
            if (type == 2) {
                if ($(this).hasClass("btn-danger")) {
                    i_beef -= 1;
                    ctr_gr_beef -= 1;
                    text_minus = text_minus.replace("b_z", "");
                    text_minus = "-" + $(this).html() + " " + text_minus;
                    text_changes_del.text(text_minus);
                    text_changes_add.append('<li>jdjdjd</li>');

                    var tab = eval(array_extra_price.join("+")).toFixed(2);
                    var newlink = link + tab + "/";
                    $('#link').attr("href", newlink + caketext + "/" + text_minus + text_add + "");
                    if (i_beef >= 0) {
                        var beef_topp = ($(this).data('price'));
                        beef_adds = beef_topp.replace(',', ".");
                        p = beef_adds * -1;
                        array_extra_price.push(p);
                        var tab = eval(array_extra_price.join("+")).toFixed(2);
                        extra_price.text(tab);
                        if (tab < 1.0) {
                            extra_price.text(0);
                        }
                    }
                    change_beef.text(i_beef);
                    $(this).removeClass("btn-danger")
                    $(this).addClass("btn-secondary")
                } else {
                    alert("Skasuj !!!")
                    //     i_beef += 1;
                    //     text = text.replace(("-" + $(this).text() + ", "), "");
                    //     text_changes.text(text);
                    //     change_beef.text(i_beef);

                    //     if (text.length == 1) {
                    //         text = "b_z";
                    //     }

                    //     var tab = eval(array_extra_price.join("+")).toFixed(2);
                    //     var newlink = link + tab + "/";
                    //     $('#link').attr("href", newlink + caketext + "/" + text + "");
                    //     $(this).removeClass("btn-secendary");
                    //     $(this).addClass("btn-danger");
                    //     if (i_beef > 0) {
                    //         var beef_topp = ($(this).data('price'));
                    //         beef_adds = beef_topp.replace(',', ".");
                    //         p = beef_adds * -1;
                    //         array_extra_price.push(beef_adds);
                    //         var tab = eval(array_extra_price.join("+")).toFixed(2);
                    //         extra_price.text(tab);
                    //         if (tab < 1) {
                    //             extra_price.text(0);
                    //         }
                    //     }
                }
            }
            //tutaj jest to samo tylko kategoria 2 czyli dodatki mięsne
            if (type == 3) {
                if ($(this).hasClass("btn-danger")) {
                    i_cheese -= 1;
                    text_minus = text_minus.replace("b_z", "");
                    text_minus = "-" + $(this).html() + " " + text_minus;
                    text_changes_del.text(text_minus);

                    var tab = eval(array_extra_price.join("+")).toFixed(2);
                    var newlink = link + tab + "/";
                    $('#link').attr("href", newlink + caketext + "/" + text_minus + text_add + "");
                    if (i_cheese >= 0) {
                        var cheese_topp = ($(this).data('price'));
                        cheese_adds = cheese_topp.replace(',', ".");
                        p = cheese_adds * -1;
                        array_extra_price.push(p);
                        var tab = eval(array_extra_price.join("+")).toFixed(2);
                        extra_price.text(tab);
                        if (tab < 1.0) {
                            extra_price.text(0);
                        }
                    }
                    change_cheese.text(i_cheese);
                    $(this).removeClass("btn-danger")
                    $(this).addClass("btn-secondary")
                } else {
                    // alert("Skasuj !!!")
                    i_cheese += 1;
                    text_add = text_add.replace(("-" + $(this).text() + ", "), "");
                    text_changes_add.text(text_add);

                    change_cheese.text(i_cheese);

                    if (text.length == 1) {
                        text = "b_z";
                    }

                    var tab = eval(array_extra_price.join("+")).toFixed(2);
                    var newlink = link + tab + "/";
                    $('#link').attr("href", newlink + caketext + "/" + text_minus + text_add + "");

                    $(this).removeClass("btn-secendary");
                    $(this).addClass("btn-danger");
                    if (i_cheese > 0) {
                        var cheese_topp = ($(this).data('price'));
                        cheese_adds = cheese_topp.replace(',', ".");
                        p = cheese_adds * -1;
                        array_extra_price.push(cheese_adds);
                        var tab = eval(array_extra_price.join("+")).toFixed(2);
                        extra_price.text(tab);
                        if (tab < 1) {
                            extra_price.text(0);
                        }
                    }
                }

            }
            if (type == 4) {
                //jesli ma klasę danger jest na pizzy
                if ($(this).hasClass("btn-danger")) {
                    //kliknięcie na niego odejmuje licznik składników w kategorii
                    i_extra -= 1;
                    ctr_gr_extra -= 1;


                    text_minus = text_minus.replace("b_z", "");
                    text_minus = "-" + $(this).html() + " " + text_minus;
                    text_changes_del.text(text_minus);
                    //jeśli licznik jest większy od 0 liczy extra_price
                    if (i_extra >= 0) {
                        //pobierz dane o cenie składnika z butttona i jedo attr data-price
                        var extra_topp = ($(this).data('price'));
                        //zamien , na . (inaczej nie liczy) pamietaj w modelu zrób float!
                        extra_adds = extra_topp.replace(',', ".");
                        //skoro odejmujemy cenę to przed dodaniem do tabicy SUMA skłądników obracamy na liczbę ujemną
                        p = extra_adds * -1;
                        //dodajemy do teblicy suma za extra_prcie
                        array_extra_price.push(p);
                        //liczymy sumę elementów w tablicy z 2 liczbami po przecinku
                        var tab = eval(array_extra_price.join("+")).toFixed(2);
                        //wklejamu tekst do spana pokazującego cena za extra składniki dla pizzy
                        extra_price.text(tab);
                        //waruken klienta jeśli róznica skłądników mniejsza od jeden to nie ustaw na 0
                        if (tab < 1.0) {
                            extra_price.text(0);
                        }
                    }
                    //aktualizujemy nasz licznik składników
                    change_extra.text(i_extra);
                    //podmieniamy klasy buttona jako odklikniety
                    $(this).removeClass("btn-danger")
                    $(this).addClass("btn-secondary")
                    //teraz mamy odznaczony składnik a więć jeśli ko znowu klikniemy
                } else {
                    alert("Skasuj !!!");
                    // ctr_gr_extra += 1;


                    // text = text.replace("b_z", "");
                    // //wjeżdza znomu na pizze i dodaje nam licznik skladników
                    // i_extra += 1;
                    // //znajduje tekst o odjęciu składnika i podmienia/usówa go!
                    // text = text.replace(("-" + $(this).text() + ", "), "");
                    // //aktualizuje go w zmiennej
                    // text_changes.text(text);
                    // //aktualizuje licznik składników
                    // change_extra.text(i_extra);

                    // var tab = eval(array_extra_price.join("+")).toFixed(2);
                    // var newlink = link + tab + "/";
                    // $('#link').attr("href", newlink + caketext + "/" + text + "");
                    // //podmienia klasy buttona poznieważ znowu jest jednak na pizzy
                    // $(this).removeClass("btn-secendary");
                    // $(this).addClass("btn-danger");
                    // //jeśli licznik jest ponad 0 to licz cena za skłądniki
                    // if (i_extra > 0) {
                    //     //pobiera attr price z kliknietego butttona ze skłądnikiem
                    //     var extra_topp = ($(this).data('price'));
                    //     extra_adds = extra_topp.replace(',', ".");
                    //     p = extra_adds * -1;
                    //     array_extra_price.push(extra_adds);
                    //     var tab = eval(array_extra_price.join("+")).toFixed(2);
                    //     extra_price.text(tab);
                    //     if (tab < 1) {
                    //         extra_price.text(0);
                    //     }
                    // }
                }

            }
            if (type == 5) {
                //jesli ma klasę danger jest na pizzy
                if ($(this).hasClass("btn-danger")) {
                    //kliknięcie na niego odejmuje licznik składników w kategorii
                    i_cake -= 1;
                    text_minus = text_minus.replace("b_z", "");
                    //edycja tekstu dla pizzera o zmianie
                    text_minus = "-" + $(this).text() + ", " + text_minus + text_add;
                    //zapis do zmiennej
                    text_changes_del.text(text_minus);
                    //jeśli licznik jest większy od 0 liczy extra_price
                    if (i_cake >= 0) {
                        //pobierz dane o cenie składnika z butttona i jedo attr data-price
                        var cake_topp = ($(this).data('price'));
                        //zamien , na . (inaczej nie liczy) pamietaj w modelu zrób float!
                        cake_adds = cake_topp.replace(',', ".");
                        //skoro odejmujemy cenę to przed dodaniem do tabicy SUMA skłądników obracamy na liczbę ujemną
                        p = cake_adds * -1;
                        //dodajemy do teblicy suma za extra_prcie
                        array_extra_price.push(p);
                        //liczymy sumę elementów w tablicy z 2 liczbami po przecinku
                        var tab = eval(array_extra_price.join("+")).toFixed(2);
                        //wklejamu tekst do spana pokazującego cena za extra składniki dla pizzy
                        extra_price.text(tab);
                        //waruken klienta jeśli róznica skłądników mniejsza od jeden to nie ustaw na 0
                        if (tab < 1.0) {
                            cake_price.text(0);
                        }
                    }
                    //aktualizujemy nasz licznik składników
                    change_cake.text(i_cake);
                    //podmieniamy klasy buttona jako odklikniety
                    $(this).removeClass("btn-danger")
                    $(this).addClass("btn-secondary")
                    //teraz mamy odznaczony składnik a więć jeśli ko znowu klikniemy
                } else {
                    //wjeżdza znomu na pizze i dodaje nam licznik skladników
                    i_cake += 1;
                    //znajduje tekst o odjęciu składnika i podmienia/usówa go!
                    text = text.replace(("-" + $(this).text() + ", "), "");
                    //aktualizuje go w zmiennej
                    text_changes_add.text(text);
                    //aktualizuje licznik składników
                    change_cake.text(i_cake);

                    var tab = eval(array_extra_price.join("+")).toFixed(2);
                    var newlink = link + tab + "/";
                    $('#link').attr("href", newlink + caketext + "/" + text + "");
                    //podmienia klasy buttona poznieważ znowu jest jednak na pizzy
                    $(this).removeClass("btn-secendary");
                    $(this).addClass("btn-danger");
                    //jeśli licznik jest ponad 0 to licz cena za skłądniki
                    if (i_cake > 0) {
                        //pobiera attr price z kliknietego butttona ze skłądnikiem
                        var cake_topp = ($(this).data('price'));
                        cake_adds = cake_topp.replace(',', ".");
                        p = cake_adds * -1;
                        array_extra_price.push(cake_adds);
                        var tab = eval(array_extra_price.join("+")).toFixed(2);
                        extra_price.text(tab);
                        if (tab < 1) {
                            extra_price.text(0);
                        }
                    }
                }

            }


        });
    });


    //lista z bazy wszystkich dodatków mięsnych, vege itd
    vegetopps.each(function (index) {

        $(this).on("click", function () {
            //sprawdzam długóść tekst ze zmianą skłądników
            var len = text_changes_add.text().length;
            if (i_extra < 0) {
                i_vege -= 1;
                i_extra += 1;
            }
            if (i_beef < 0) {
                i_vege -= 1;
                i_beef += 1;
            }
            if (len < 240) {
                //dodanie skłądnika z list dodaje nam licznik skłądników plus 1
                i_vege += 1;

                //edycja zmiennej licznika
                change_vege.text(i_vege)
                //przed dodaniem buttona na listę dodanych skłądników Klonujemy go
                new_button = $(this).clone();
                //dodajemu do ADD_TOPPS miejsce na dodane skłądniki
                new_button.appendTo(add_topps);
                //pobieramy cenę skłądnika z attr data-price
                var vege_topp = ($(this).data('vegeprice'));
                vege_topp = vege_topp.replace(',', ".");
                //do zmiennej suma VEGE dodajemy jego cenę sparsowaną na float
                suma_vege += parseFloat(vege_topp);
                //edytujemy tekst dla pizzera
                text_add += "+" + $(this).text() + ", ";
                text_changes_add.text(text_add);
                // if (sum_ctr_gr_extra < 0) {
                //     if ((sum_ctr_gr_extra + i_vege) == 0) {

                //         extra_price.text(0);
                //     }
                // }
                if (i_vege > 0) {

                    var p = parseFloat(vege_topp);
                    array_extra_price.push(p);
                    var tab = eval(array_extra_price.join("+"))
                    tab += cake_price;
                    extra_price.text(tab.toFixed(2));

                    //tutaj jest ciekawie!! edytuję attr href w linku a
                    //w jego href przekazuję cenę za dodatki oraz tekst o zmienach składników
                    //dlatego że w widoku dodaj pizze POSTy wykorzystuję do czego innego
                    //więć do tego widoku musi wjechac GETem
                    var newlink = link + tab + "/";
                    $('#link').attr("href", newlink + caketext + "/" + text_minus + text_add + "");

                }

            } else {
                //powyzej 240 znaków blokada edytowania skłądników
                alert("Za dużo zmian");
                suma_vege = parseFloat(vege_topp);
                text_changes_add.text(text_add);
            }

            // var a = ($('#change_vege').data('vege_plus') + i_vege);

            //jeśli licznik składników ponad jeden to licz cenę

        });


    });
    beeftopps.each(function (index) {

        $(this).on("click", function () {
            var len = text_changes_add.text().length;
            if (i_extra < 0) {
                i_beef -= 1;
                i_extra += 1;
            }

            if (len < 240) {
                i_beef += 1;
                change_beef.text(i_beef)
                new_button = $(this).clone();
                new_button.appendTo(add_topps);
                var beef_topp = ($(this).data('beefprice'));
                beef_topp = beef_topp.replace(',', ".");
                suma_beef += parseFloat(beef_topp);
                var b = ($('#change_beef').data('beef_plus') + i_beef);
                text_add += "+" + $(this).text() + ", ";
                text_changes_add.text(text_add);
                if (i_beef > 0) {
                    var p = parseFloat(beef_topp);
                    array_extra_price.push(p);
                    var tab = eval(array_extra_price.join("+"))
                    tab += cake_price;
                    tab = tab.toFixed(2)
                    extra_price.text(tab);
                    var newlink = link + tab + "/";
                    $('#link').attr("href", newlink + caketext + "/" + text_minus + text_add + "");
                }
            } else {
                alert("Za dużo zmian");
                var beef_topp = ($(this).data('beefprice'));
                beef_topp = beef_topp.replace(',', ".");
                suma_beef = parseFloat(beef_topp);
                text_changes.text(text);
            }
        });
    });
    cheesetopps.each(function (index) {

        $(this).on("click", function () {
            var len = text_changes_add.text().length;
            if (len < 120) {
                i_cheese += 1;
                change_cheese.text(i_cheese)
                new_button = $(this).clone();
                new_button.appendTo(add_topps);
                var cheese_topp = ($(this).data('cheeseprice'));
                cheese_topp = cheese_topp.replace(',', ".");
                suma_cheese += parseFloat(cheese_topp);
                var c = ($('#change_cheese').data('cheese_plus') + i_cheese);
                text_add += "+" + $(this).text() + ", ";
                text_changes_add.text(text_add);
                if (i_cheese > 0) {
                    cheese_adds = cheese_topp.replace(',', ".");
                    var p = parseFloat(cheese_adds);
                    array_extra_price.push(p);
                    var tab = eval(array_extra_price.join("+"))
                    tab += cake_price;
                    extra_price.text(tab.toFixed(2));
                    var newlink = link + tab + "/";
                    $('#link').attr("href", newlink + caketext + "/" + text_minus + text_add + "");
                }
            } else {
                alert("Za dużo zmian");
                text_changes.text(text);
            }
        });
    });

    extratopps.each(function (index) {

        $(this).on("click", function () {
            var len = text_changes_add.text().length;
            if (len < 120) {
                i_extra += 1;
                change_extra.text(i_extra)
                new_button = $(this).clone();
                new_button.appendTo(add_topps);
                var extra_topp = ($(this).data('extraprice'));
                extra_topp = extra_topp.replace(',', ".");
                suma_extra += parseFloat(extra_topp);
                var c = ($('#change_extra').data('extra_plus') + i_extra);
                text_add += "+" + $(this).text() + ", ";
                text_changes_add.text(text_add);
                if (i_extra > 0) {
                    extra_adds = extra_topp.replace(',', ".");
                    var p = parseFloat(extra_adds);
                    array_extra_price.push(p);
                    var tab = eval(array_extra_price.join("+"))
                    tab += cake_price;
                    extra_price.text(tab.toFixed(2));
                    var newlink = link + tab + "/";
                    $('#link').attr("href", newlink + caketext + "/" + text_minus + text_add + "");
                }
            } else {
                alert("Za dużo zmian");
                text_changes.text(text);
            }

        });
    });

    caketopps.each(function (index) {
        $(this).on("click", function () {
            i_cake += 1;
            caketopps.removeClass("btn-success");
            caketopps.addClass("btn-warning");
            $(this).removeClass("btn-warning");
            $(this).addClass("btn-success");
            change_cake.text(i_cake);
            // new_button = $(this).clone();
            // new_button.appendTo(add_topps);

            // var c = ($('#change_cake').data('cake_plus') + i_cake);
            caketext = " +" + $(this).text() + ", ";
            cake_text_changes.text(caketext);
            cake_topp_price = ($(this).data('cakeprice'));
            cake_topp = cake_topp_price.replace(',', ".");
            cake_price = parseFloat(cake_topp);
            // array_extra_price.push(cake_price);
            var tab = eval(array_extra_price.join("+"))
            tab += cake_price;
            extra_price.text(tab.toFixed(2));
            var newlink = link + tab + "/";
            $('#link').attr("href", newlink + caketext + "/" + text_minus + text_add + "/");

        });
    });





    qplus.each(function (index) {

        $(this).on("click", function () {
            var q = parseInt(quantity.val());
            q += 1;
            quantity.val(q);
        });
    });
    qminus.each(function (index) {

        $(this).on("click", function () {
            var q = parseInt(quantity.val());
            if (q > 1) {
                q -= 1;
                quantity.val(q);
            }
        });
    });

    sauce_free.each(function (index) {
        $(this).on("click", function () {

            var len_sauces_free = sauce_free_text.text().length;
            if (len_sauces_free < 120) {
                text_sauce_free += " +" + $(this).text() + ", ";
                sauce_free_text.text(text_sauce_free);
                add_sauces_free = add_sauces_free.attr('value', text_sauce_free);

            } else {
                alert("Za dużo zmian");
            }
        });
    });

    sauce_pay.each(function (index) {

        $(this).on("click", function () {
            var len_sauces_pay = sauce_pay_text.text().length;

            if (len_sauces_pay < 120) {
                text_sauce_pay += " +" + $(this).text() + ", ";
                sauce_pay_text.text(text_sauce_pay);
                var sauce_price = $(this).data('price');
                sauce_price = sauce_price.replace(',', ".");
                sauce_price = parseFloat(sauce_price);
                // suma_sauce += sauce_price;
                sauce_price = sauce_price.toFixed(2);
                array_extra_sauce.push(sauce_price);
                var tab = eval(array_extra_sauce.join("+"))

                price_sauce_edit = extra_price_edit.data('price');
                price_sauce_edit = price_sauce_edit.replace(',', ".");
                price_sauce_edit = parseFloat(price_sauce_edit);

                price_sauce_edit += tab;
                price_sauce_edit = price_sauce_edit.toFixed(2);

                extra_price_edit.html("<b>" + price_sauce_edit + "</b>");
                sauces_form.attr('value', price_sauce_edit);
                sauce_pay_text.text(text_sauce_pay);
                add_sauces_pay = add_sauces_pay.attr('value', text_sauce_pay);

            } else {
                alert("Za dużo zmian");
                sauces_text.attr('value', text_sauce_pay);
            }

        });
    });
    size_button.each(function (index) {
        $(this).on("click", function () {
            var size_class = ($(this).attr("class").split((/\s+/))[0]);
            // pizza_button.hide();
            pizza_button.each(function (el) {
                if (($(this).hasClass(size_class))) {
                    $(this).show();
                } else {
                    $(this).hide();
                };
            });

        });

    })


})