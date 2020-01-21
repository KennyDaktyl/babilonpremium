$(document).ready(function () {


    var vegetopps = $('button.vegetopps');
    var change_vege = $('#change_vege');
    var vege_price = $('#price_size_vege').data('price');
    vege_price = vege_price.replace(",", ".");
    vege_price = parseFloat(vege_price).toFixed(2);
    var i_vege = parseInt(change_vege.text());

    var beeftopps = $('button.beeftopps');
    var beef_price = $('#price_size_beef').data('price');;
    beef_price = beef_price.replace(",", ".");
    beef_price = parseFloat(beef_price).toFixed(2);
    var change_beef = $('#change_beef');
    var i_beef = parseInt(change_beef.text());

    var cheesetopps = $('button.cheesetopps');
    var change_cheese = $('#change_cheese');
    var cheese_price = $('#price_size_cheese').data('price');;
    cheese_price = cheese_price.replace(",", ".");
    cheese_price = parseFloat(cheese_price).toFixed(2);
    var i_cheese = parseInt(change_cheese.text());

    var extratopps = $('button.extratopps');
    var change_extra = $('#change_extra');
    var extra_price = $('#price_size_extra').data('price');;;
    extra_price = extra_price.replace(",", ".");
    extra_price = parseFloat(extra_price).toFixed(2);
    var i_extra = parseInt(change_extra.text());
    var cake = $('button.caketopps');
    var text_add = "";
    var text_add_topps = $('#topps_add');
    var text_add_pay = "";
    var text_add_topps_pay = $('#topps_add_pay');


    var extra_price_text = $('#extra_price');
    var add_topps_price = 0;
    var topps_free_array = [];
    var topps_pay_array = [0, ];
    var sum_topps_pay_array = eval(topps_pay_array.join("+"));

    var caketopps = $('button.caketopps');
    var change_cake = $('#change_cake');
    var price_cake = 0.00;

    var input_extra_price = $('#input_extra_price');
    var input_topps_free = $('#input_topps_free');
    var input_topps_pay = $('#input_topps_pay');

    var input_add_cake = "";
    var input_add_cake_text = $('#input_cake_info');
    // var topps_text = "";

    var url_adress = window.location.href;
    vegetopps.each(function (index) {
        $(this).on("click", function () {
            if (((topps_free_array.length) == 6) && ($(this).hasClass("btn-success"))) {
                $(this).removeClass("btn-success");
                $(this).addClass("btn-warning");
                i_vege -= 1;
                change_vege.html("<b>" + i_vege + "</b>");
                topps_free_array.pop();
                extra_price_text = extra_price_text.text((parseFloat(add_topps_price) + parseFloat(price_cake)).toFixed(2));
                text_add = text_add.replace(($(this).text() + ", "), "");
                text_add_topps = text_add_topps.text(text_add);
                input_topps_free.attr('value', text_add);
                input_extra_price.attr('value', ((parseFloat(add_topps_price) + parseFloat(price_cake))).toFixed(2));

            } else if (((topps_free_array.length) < 6) && ($(this).hasClass("btn-success"))) {
                $(this).removeClass("btn-success");
                $(this).addClass("btn-warning");
                i_vege -= 1;
                change_vege.html("<b>" + i_vege + "</b>");
                topps_free_array.pop();
                extra_price_text = extra_price_text.text((parseFloat(add_topps_price) + parseFloat(price_cake)).toFixed(2));
                text_add = text_add.replace(($(this).text() + ", "), "");
                text_add_topps = text_add_topps.text(text_add);
                text_add_topps = text_add_topps.text(text_add);
                input_topps_free = input_topps_free.attr('value', text_add);
                input_extra_price.attr('value', ((parseFloat(add_topps_price) + parseFloat(price_cake))).toFixed(2));
            } else if (((topps_free_array.length) >= 6) && ($(this).hasClass('btn-warning'))) {
                $(this).removeClass("btn-warning");
                $(this).addClass("btn-danger");
                i_vege += 1;
                change_vege.html("<b>" + i_vege + "</b>");
                topps_pay_array.push(vege_price);
                sum_topps_pay_array = eval(topps_pay_array.join("+"));
                add_topps_price = sum_topps_pay_array.toFixed(2);
                extra_price_text = extra_price_text.text((parseFloat(add_topps_price) + parseFloat(price_cake)).toFixed(2));
                text_add_pay += $(this).text() + ", ";
                text_add_topps_pay = text_add_topps_pay.text(text_add_pay);
                text_add_topps = text_add_topps.text(text_add);
                input_topps_pay.attr('value', text_add_pay);
                input_extra_price.attr('value', ((parseFloat(add_topps_price) + parseFloat(price_cake))).toFixed(2));
            } else if ($(this).hasClass('btn-danger')) {
                $(this).removeClass("btn-danger");
                $(this).addClass("btn-warning");
                i_vege -= 1;
                change_vege.html("<b>" + i_vege + "</b>");
                topps_pay_array.push((vege_price * (-1)));
                sum_topps_pay_array = eval(topps_pay_array.join("+"));
                add_topps_price = sum_topps_pay_array.toFixed(2);
                extra_price_text = extra_price_text.text((parseFloat(add_topps_price) + parseFloat(price_cake)).toFixed(2));
                text_add_pay = text_add_pay.replace(($(this).text() + ", "), "");
                text_add_topps_pay = text_add_topps_pay.text(text_add_pay);
                input_topps_pay.attr('value', text_add_pay);
                input_extra_price.attr('value', ((parseFloat(add_topps_price) + parseFloat(price_cake))).toFixed(2));
            } else if ((topps_free_array.length) < 6) {
                topps_free_array.push(1);
                console.log(topps_free_array);
                $(this).removeClass("btn-warning");
                $(this).addClass("btn-success");
                i_vege += 1;
                change_vege.html("<b>" + i_vege + "</b>");
                sum_topps_pay_array = eval(topps_pay_array.join("+"));
                add_topps_price = sum_topps_pay_array.toFixed(2);
                extra_price_text = extra_price_text.text((parseFloat(add_topps_price) + parseFloat(price_cake)).toFixed(2));
                text_add += $(this).text() + ", ";
                text_add_topps = text_add_topps.text(text_add);
                input_topps_free = input_topps_free.attr('value', text_add);
                input_extra_price.attr('value', ((parseFloat(add_topps_price) + parseFloat(price_cake))).toFixed(2));
            }
        })
    })
    beeftopps.each(function (index) {
        $(this).on("click", function () {
            if (((topps_free_array.length) == 6) && ($(this).hasClass("btn-success"))) {
                $(this).removeClass("btn-success");
                $(this).addClass("btn-warning");
                i_beef -= 1;
                change_beef.html("<b>" + i_beef + "</b>");
                topps_free_array.pop();
                extra_price_text = extra_price_text.text((parseFloat(add_topps_price) + parseFloat(price_cake)).toFixed(2));
                text_add = text_add.replace(($(this).text() + ", "), "");
                text_add_topps = text_add_topps.text(text_add);
                input_topps_free = input_topps_free.attr('value', text_add);
                input_extra_price.attr('value', ((parseFloat(add_topps_price) + parseFloat(price_cake))).toFixed(2));
            } else if (((topps_free_array.length) < 6) && ($(this).hasClass("btn-success"))) {
                $(this).removeClass("btn-success");
                $(this).addClass("btn-warning");
                i_beef -= 1;
                change_beef.html("<b>" + i_beef + "</b>");
                topps_free_array.pop();
                extra_price_text = extra_price_text.text((parseFloat(add_topps_price) + parseFloat(price_cake)).toFixed(2));
                text_add = text_add.replace(($(this).text() + ", "), "");
                text_add_topps = text_add_topps.text(text_add);
                input_topps_free = input_topps_free.attr('value', text_add);
                input_extra_price.attr('value', ((parseFloat(add_topps_price) + parseFloat(price_cake))).toFixed(2));
            } else if (((topps_free_array.length) >= 6) && ($(this).hasClass('btn-warning'))) {
                $(this).removeClass("btn-warning");
                $(this).addClass("btn-danger");
                i_beef += 1;
                change_beef.html("<b>" + i_beef + "</b>");
                topps_pay_array.push(beef_price);
                sum_topps_pay_array = eval(topps_pay_array.join("+"));
                add_topps_price = sum_topps_pay_array.toFixed(2);
                extra_price_text = extra_price_text.text((parseFloat(add_topps_price) + parseFloat(price_cake)).toFixed(2));
                text_add_pay += $(this).text() + ", ";
                text_add_topps_pay = text_add_topps_pay.text(text_add_pay);
                input_topps_pay = input_topps_pay.attr('value', text_add_pay);
                input_extra_price.attr('value', ((parseFloat(add_topps_price) + parseFloat(price_cake))).toFixed(2));
            } else if ($(this).hasClass('btn-danger')) {
                $(this).removeClass("btn-danger");
                $(this).addClass("btn-warning");
                i_beef -= 1;
                change_beef.html("<b>" + i_beef + "</b>");
                topps_pay_array.push((beef_price * (-1)));
                sum_topps_pay_array = eval(topps_pay_array.join("+"));
                add_topps_price = sum_topps_pay_array.toFixed(2);
                extra_price_text = extra_price_text.text((parseFloat(add_topps_price) + parseFloat(price_cake)).toFixed(2));
                text_add_pay = text_add_pay.replace(($(this).text() + ", "), "");
                text_add_topps_pay = text_add_topps_pay.text(text_add_pay);
                input_topps_pay = input_topps_pay.attr('value', text_add_pay);
                input_extra_price.attr('value', ((parseFloat(add_topps_price) + parseFloat(price_cake))).toFixed(2));
            } else if ((topps_free_array.length) < 6) {
                topps_free_array.push(1);
                console.log(topps_free_array);
                $(this).removeClass("btn-warning");
                $(this).addClass("btn-success");
                i_beef += 1;
                change_beef.html("<b>" + i_beef + "</b>");
                sum_topps_pay_array = eval(topps_pay_array.join("+"));
                add_topps_price = sum_topps_pay_array.toFixed(2);
                extra_price_text = extra_price_text.text((parseFloat(add_topps_price) + parseFloat(price_cake)).toFixed(2));
                text_add += $(this).text() + ", ";
                text_add_topps = text_add_topps.text(text_add);
                input_topps = input_topps_free.attr('value', text_add);
                input_extra_price.attr('value', ((parseFloat(add_topps_price) + parseFloat(price_cake))).toFixed(2));
            }
        })
    })
    cheesetopps.each(function (index) {
        $(this).on("click", function () {
            if (((topps_free_array.length) == 6) && ($(this).hasClass("btn-success"))) {
                $(this).removeClass("btn-success");
                $(this).addClass("btn-warning");
                i_cheese -= 1;
                change_cheese.html("<b>" + i_cheese + "</b>");
                topps_free_array.pop();
                extra_price_text = extra_price_text.text((parseFloat(add_topps_price) + parseFloat(price_cake)).toFixed(2));
                text_add = text_add.replace(($(this).text() + ", "), "");
                text_add_topps = text_add_topps.text(text_add);
                input_topps_free = input_topps_free.attr('value', text_add);
                input_extra_price.attr('value', ((parseFloat(add_topps_price) + parseFloat(price_cake))).toFixed(2));
            } else if (((topps_free_array.length) < 6) && ($(this).hasClass("btn-success"))) {
                $(this).removeClass("btn-success");
                $(this).addClass("btn-warning");
                i_cheese -= 1;
                change_cheese.html("<b>" + i_cheese + "</b>");
                topps_free_array.pop();
                extra_price_text = extra_price_text.text((parseFloat(add_topps_price) + parseFloat(price_cake)).toFixed(2));
                text_add = text_add.replace(($(this).text() + ", "), "");
                text_add_topps = text_add_topps.text(text_add);
                input_topps_free = input_topps_free.attr('value', text_add);
                input_extra_price.attr('value', ((parseFloat(add_topps_price) + parseFloat(price_cake))).toFixed(2));
            } else if (((topps_free_array.length) >= 6) && ($(this).hasClass('btn-warning'))) {
                $(this).removeClass("btn-warning");
                $(this).addClass("btn-danger");
                i_cheese += 1;
                change_cheese.html("<b>" + i_cheese + "</b>");
                topps_pay_array.push(cheese_price);
                sum_topps_pay_array = eval(topps_pay_array.join("+"));
                add_topps_price = sum_topps_pay_array.toFixed(2);
                extra_price_text = extra_price_text.text((parseFloat(add_topps_price) + parseFloat(price_cake)).toFixed(2));
                text_add_pay += $(this).text() + ", ";
                text_add_topps_pay = text_add_topps_pay.text(text_add_pay);
                input_topps_pay.attr('value', text_add_pay);
                input_extra_price.attr('value', ((parseFloat(add_topps_price) + parseFloat(price_cake))).toFixed(2));
            } else if ($(this).hasClass('btn-danger')) {
                $(this).removeClass("btn-danger");
                $(this).addClass("btn-warning");
                i_cheese -= 1;
                change_cheese.html("<b>" + i_cheese + "</b>");
                topps_pay_array.push((cheese_price * (-1)));
                sum_topps_pay_array = eval(topps_pay_array.join("+"));
                add_topps_price = sum_topps_pay_array.toFixed(2);
                extra_price_text = extra_price_text.text((parseFloat(add_topps_price) + parseFloat(price_cake)).toFixed(2));
                text_add_pay = text_add_pay.replace(($(this).text() + ", "), "");
                text_add_topps_pay = text_add_topps_pay.text(text_add_pay);
                input_topps_pay.attr('value', text_add_pay);
                input_extra_price.attr('value', ((parseFloat(add_topps_price) + parseFloat(price_cake))).toFixed(2));
            } else if ((topps_free_array.length) < 6) {
                topps_free_array.push(1);
                console.log(topps_free_array);
                $(this).removeClass("btn-warning");
                $(this).addClass("btn-success");
                i_cheese += 1;
                change_cheese.html("<b>" + i_cheese + "</b>");
                sum_topps_pay_array = eval(topps_pay_array.join("+"));
                add_topps_price = sum_topps_pay_array.toFixed(2);
                extra_price_text = extra_price_text.text((parseFloat(add_topps_price) + parseFloat(price_cake)).toFixed(2));
                text_add += $(this).text() + ", ";
                text_add_topps = text_add_topps.text(text_add);
                input_topps_free = input_topps_free.attr('value', text_add);
                input_extra_price.attr('value', ((parseFloat(add_topps_price) + parseFloat(price_cake))).toFixed(2));
            }
        })
    })
    extratopps.each(function (index) {
        $(this).on("click", function () {
            if (((topps_free_array.length) == 6) && ($(this).hasClass("btn-success"))) {
                $(this).removeClass("btn-success");
                $(this).addClass("btn-warning");
                i_extra -= 1;
                change_extra.html("<b>" + i_extra + "</b>");
                topps_free_array.pop();
                extra_price_text = extra_price_text.text((parseFloat(add_topps_price) + parseFloat(price_cake)).toFixed(2));
                text_add = text_add.replace(($(this).text() + ", "), "");
                text_add_topps = text_add_topps.text(text_add);
                input_topps_free = input_topps_free.attr('value', text_add);
                input_extra_price.attr('value', ((parseFloat(add_topps_price) + parseFloat(price_cake))).toFixed(2));
            } else if (((topps_free_array.length) < 6) && ($(this).hasClass("btn-success"))) {
                $(this).removeClass("btn-success");
                $(this).addClass("btn-warning");
                i_extra -= 1;
                change_extra.html("<b>" + i_extra + "</b>");
                topps_free_array.pop();
                extra_price_text = extra_price_text.text((parseFloat(add_topps_price) + parseFloat(price_cake)).toFixed(2));
                text_add = text_add.replace(($(this).text() + ", "), "");
                text_add_topps = text_add_topps.text(text_add);
                input_topps_free = input_topps_free.attr('value', text_add);
                input_extra_price.attr('value', ((parseFloat(add_topps_price) + parseFloat(price_cake))).toFixed(2));
            } else if (((topps_free_array.length) >= 6) && ($(this).hasClass('btn-warning'))) {
                $(this).removeClass("btn-warning");
                $(this).addClass("btn-danger");
                i_extra += 1;
                change_extra.html("<b>" + i_extra + "</b>");
                topps_pay_array.push(extra_price);
                sum_topps_pay_array = eval(topps_pay_array.join("+"));
                add_topps_price = sum_topps_pay_array.toFixed(2);
                extra_price_text = extra_price_text.text((parseFloat(add_topps_price) + parseFloat(price_cake)).toFixed(2));
                text_add_pay += $(this).text() + ", ";
                text_add_topps_pay = text_add_topps_pay.text(text_add_pay);
                input_topps_pay.attr('value', text_add_pay);
                input_extra_price.attr('value', ((parseFloat(add_topps_price) + parseFloat(price_cake))).toFixed(2));
            } else if ($(this).hasClass('btn-danger')) {
                $(this).removeClass("btn-danger");
                $(this).addClass("btn-warning");
                i_extra -= 1;
                change_extra.html("<b>" + i_extra + "</b>");
                topps_pay_array.push((extra_price * (-1)));
                sum_topps_pay_array = eval(topps_pay_array.join("+"));
                add_topps_price = sum_topps_pay_array.toFixed(2);
                extra_price_text = extra_price_text.text((parseFloat(add_topps_price) + parseFloat(price_cake)).toFixed(2));
                text_add_pay = text_add_pay.replace(($(this).text() + ", "), "");
                text_add_topps_pay = text_add_topps_pay.text(text_add_pay);
                input_topps_free = input_topps_free.attr('value', text_add);
                input_extra_price.attr('value', ((parseFloat(add_topps_price) + parseFloat(price_cake))).toFixed(2));
            } else if ((topps_free_array.length) < 6) {
                topps_free_array.push(1);
                console.log(topps_free_array);
                $(this).removeClass("btn-warning");
                $(this).addClass("btn-success");
                i_extra += 1;
                change_extra.html("<b>" + i_extra + "</b>");
                sum_topps_pay_array = eval(topps_pay_array.join("+"));
                add_topps_price = sum_topps_pay_array.toFixed(2);
                extra_price_text = extra_price_text.text((parseFloat(add_topps_price) + parseFloat(price_cake)).toFixed(2));
                text_add += $(this).text() + ", ";
                text_add_topps = text_add_topps.text(text_add);
                input_topps_free = input_topps_free.attr('value', text_add);
                input_extra_price.attr('value', ((parseFloat(add_topps_price) + parseFloat(price_cake))).toFixed(2));
            }
        })
    })

    caketopps.each(function (index) {
        $(this).on("click", function () {
            caketopps.removeClass("btn-success");
            caketopps.addClass("btn-warning");
            $(this).removeClass("btn-warning");
            $(this).addClass("btn-success");
            // change_cake.text(i_cake);
            cake_topp_price = ($(this).data('price'));
            cake_topp = cake_topp_price.replace(',', ".");
            price_cake = parseFloat(cake_topp);

            extra_price_text = extra_price_text.text((parseFloat(add_topps_price) + parseFloat(price_cake)).toFixed(2));

            input_add_cake = $(this).text();
            input_add_cake_text.attr('value', input_add_cake);

            input_extra_price.attr('value', ((parseFloat(add_topps_price) + parseFloat(price_cake))).toFixed(2));
            input_topps_free = input_topps_free.attr('value', text_add);
            input_extra_price.attr('value', ((parseFloat(add_topps_price) + parseFloat(price_cake))).toFixed(2));
            console.log(input_add_cake_text.attr('value'));
        });
    });
})