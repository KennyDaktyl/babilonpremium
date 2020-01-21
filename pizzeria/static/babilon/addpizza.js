$(document).ready(function () {

    //Widok dodaj pizze ilość plus i minus jeden
    var qplus = $("#quantity_plus");
    var qminus = $("#quantity_minus");
    var quantity = $("#quantity");

    //widok dodaj pizze bez zmian (edycja sosów,info,rabatu i ilości)
    // var sauce_free = $('button.sauce_free');
    // var sauce_pay = $('button.sauce_pay');
    // var sauce_free_text = $('#sauce_free_text');
    // var sauce_pay_text = $('#sauce_pay_text');
    // var text_sauce_free = "";
    // var text_sauce_pay = "";
    // var extra_price_edit = $('#extra_price_edit');
    // var sauces_form = $('#sauces_form');
    // var add_sauces_free = $('#add_sauces_free');
    // var add_sauces_pay = $('#add_sauces_pay');

    var sauce_free = $('button.sauce_free');
    var sauce_pay = $('button.sauce_pay');
    var sauce_free_text = $('#sauce_free_text');
    var sauce_pay_text = $('#sauce_pay_text');
    var text_sauce_free = "";
    var text_sauce_pay = "";
    var extra_price_edit = $('#extra_price_edit');
    var caketopps = $('button.caketopps');
    var input_add_cake_text = $('#input_add_cake');
    var extra_price = $('#extra_price');
    var price_cake = 0.00;
    // extra_price_edit = extra_price_edit.data('price');
    // extra_price_edit = extra_price_edit.replace(',', ".");
    // extra_price_edit = parseFloat(extra_price_edit)
    // extra_price_edit = extra_price_edit.toFixed(2)
    // console.log(typeof (extra_price_edit));


    var sauces_form = $('#sauces_form');
    var add_sauces_free = $('#add_sauces_free');
    var add_sauces_pay = $('#add_sauces_pay');

    var size_button = $('.Pizza');
    var pizza_button = $('.product button');

    array_extra_price = [0, ];
    array_extra_sauce = [0, ];


    var refresh = $('#refresh');

    refresh.click(function () {
        location.reload();
    });

    // $(document).keyup(function (event) {
    //     if (event.keyCode === 13) {
    //         $('#enter').click();
    //     }
    // });

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
            if (len_sauces_free < 200) {
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

            if (len_sauces_pay < 400) {
                text_sauce_pay += " +" + $(this).text() + ", ";
                sauce_pay_text.text(text_sauce_pay);
                var sauce_price = $(this).data('price');
                sauce_price = sauce_price.replace(',', ".");
                sauce_price = parseFloat(sauce_price);

                sauce_price = sauce_price.toFixed(2);
                array_extra_sauce.push(sauce_price);
                var tab = eval(array_extra_sauce.join("+"))
                tab = parseFloat(tab) + parseFloat(price_cake);

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
    caketopps.each(function (index) {
        $(this).on("click", function () {
            caketopps.removeClass("btn-success");
            caketopps.addClass("btn-warning");
            $(this).removeClass("btn-warning");
            $(this).addClass("btn-success");

            cake_topp_price = ($(this).data('price'));
            cake_topp = cake_topp_price.replace(',', ".");
            price_cake = parseFloat(cake_topp);


            price_sauce_edit = extra_price_edit.data('price');
            price_sauce_edit = price_sauce_edit.replace(',', ".");
            price_sauce_edit = parseFloat(price_sauce_edit);



            price_cake = price_cake.toFixed(2);

            var tab = eval(array_extra_sauce.join("+"))
            tab = parseFloat(tab);


            extra_price_edit.html("<b>" + ((parseFloat(tab) + parseFloat(price_sauce_edit) + parseFloat(price_cake))).toFixed(2) + "</b>");
            price_sauce_edit = ((parseFloat(tab) + parseFloat(price_sauce_edit) + parseFloat(price_cake))).toFixed(2);


            input_add_cake = $(this).text();
            input_add_cake_text.attr('value', input_add_cake);
            sauces_form.attr('value', price_sauce_edit);

        });
    });
});