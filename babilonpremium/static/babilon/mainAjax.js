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
// cake.each(function (index) {
//     $(this).on("click", function () {
//         caketopps.removeClass("btn-success");
//         caketopps.addClass("btn-warning");
//         $(this).removeClass("btn-warning");
//         $(this).addClass("btn-success");
//         change_cake.text(i_cake);
//         cake_topp_price = ($(this).data('cakeprice'));
//         cake_topp = cake_topp_price.replace(',', ".");
//         price_cake = parseFloat(cake_topp);
//         extra_price_text = extra_price_text.text((price_vege + price_beef + price_cheese + price_extra + price_cake).toFixed(2));
//         text_add_cake = $(this).text();
//         // ul_add.append('<li>' + text_add + '</li>');
//         input_add_cake = text_add_cake
//         input_add_cake_text.attr('value', input_add_cake);
//         input_value.attr('value', (price_vege + price_beef + price_cheese + price_extra + price_cake).toFixed(2));
//     })

// })

// var beeftopps = $('button.beeftopps');
// var cheesetopps = $('button.cheesetopps');
// var extratopps = $('button.extratopps');

// var caketopps = $('button.caketopps');
// var change_cake = $('#change_cake');

// var i_vege = $('#change_vege');
// var i_beef = $('#change_beef');
// var i_cheese = $('#change_cheese');
// var i_extra = $('#change_extra');
// var i_cake = $('#change_cake');






// topps.each(function (el) {
//     if (($(this).attr("class").split((/\s+/))[0]) == 1) {
//         vege_toops_array.push(1);
//         $(this).on("click", function () {
//             if ($(this).hasClass("btn-danger")) {
//                 $(this).removeClass("btn-danger");
//                 $(this).addClass("btn-secondary");
//                 ctr_vege_array.push(-1);
//                 sum_ctr_vege_array = eval(ctr_vege_array.join("+"));
//                 sum_ctr_vege_array = parseInt(sum_ctr_vege_array);
//                 i_vege.text(sum_ctr_vege_array);
//                 text_del = "-" + $(this).text() + ", ";
//                 ul_del.append('<li>' + text_del + '</li>');
//                 input_del_text += text_del
//                 input_del_topps.attr('value', input_del_text);
//                 if ((sum_ctr_beef_array > 0) && (sum_ctr_extra_array < 0) && (sum_ctr_beef_array + sum_ctr_extra_array) == 0) {
//                     price_vege = sum_ctr_vege_array * price_vege_toops;
//                     if ((price_vege) < 0) {
//                         price_vege = 0;
//                     }
//                     extra_price_text = extra_price_text.text((price_vege + price_beef + price_cheese + price_extra + price_cake).toFixed(2));
//                 }
//                 if ((sum_ctr_beef_array > 0) && (sum_ctr_extra_array > 0) && (sum_ctr_beef_array + sum_ctr_extra_array) == 0) {
//                     price_vege = sum_ctr_vege_array * price_vege_toops;
//                     if ((price_vege) < 0) {
//                         price_vege = 0;
//                     }
//                     extra_price_text = extra_price_text.text((price_vege + price_beef + price_cheese + price_extra + price_cake).toFixed(2));
//                 }

//                 if ((sum_ctr_beef_array < 0) && (sum_ctr_extra_array < 0)) {
//                     price_vege = (sum_ctr_vege_array + (sum_ctr_beef_array + sum_ctr_extra_array)) * price_vege_toops;
//                     if ((price_vege) < 0) {
//                         price_vege = 0;
//                     }
//                     extra_price_text = extra_price_text.text((price_vege + price_beef + price_cheese + price_extra + price_cake).toFixed(2));
//                 }
//                 if ((sum_ctr_beef_array == 0) && (sum_ctr_extra_array < 0)) {
//                     price_vege = (sum_ctr_vege_array + (sum_ctr_extra_array)) * price_vege_toops;
//                     if ((price_vege) < 0) {
//                         price_vege = 0;
//                     }
//                     extra_price_text = extra_price_text.text((price_vege + price_beef + price_cheese + price_extra + price_cake).toFixed(2));
//                 }
//                 if ((sum_ctr_beef_array > 0) && (sum_ctr_extra_array == 0)) {
//                     price_vege = (sum_ctr_vege_array * price_vege_toops);
//                     if ((price_vege) < 0) {
//                         price_vege = 0;
//                     }
//                     extra_price_text = extra_price_text.text((price_vege + price_beef + price_cheese + price_extra + price_cake).toFixed(2));
//                 }

//                 if ((sum_ctr_beef_array < 0) && (sum_ctr_extra_array == 0)) {
//                     price_vege = ((sum_ctr_vege_array + sum_ctr_beef_array) * price_vege_toops);
//                     if ((price_vege) < 0) {
//                         price_vege = 0;
//                     }
//                     extra_price_text = extra_price_text.text((price_vege + price_beef + price_cheese + price_extra + price_cake).toFixed(2));
//                 }
//                 if ((sum_ctr_beef_array > 0) && (sum_ctr_extra_array > 0)) {
//                     price_vege = (sum_ctr_vege_array * price_vege_toops);
//                     if ((price_vege) < 0) {
//                         price_vege = 0;
//                     }
//                     extra_price_text = extra_price_text.text((price_vege + price_beef + price_cheese + price_extra + price_cake).toFixed(2));
//                 }
//                 if ((sum_ctr_beef_array == 0) && (sum_ctr_extra_array == 0)) {
//                     price_vege = sum_ctr_vege_array * price_vege_toops;
//                     if ((price_vege) < 0) {
//                         price_vege = 0;
//                     }
//                     extra_price_text = extra_price_text.text((price_vege + price_beef + price_cheese + price_extra + price_cake).toFixed(2));
//                 }
//                 if ((sum_ctr_beef_array == 0) && (sum_ctr_extra_array > 0)) {
//                     price_vege = sum_ctr_vege_array * price_vege_toops;
//                     if ((price_vege) < 0) {
//                         price_vege = 0;
//                     }
//                     extra_price_text = extra_price_text.text((price_vege + price_beef + price_cheese + price_extra + price_cake).toFixed(2));
//                 }



//                 if (sum_ctr_extra_array < 0) {
//                     price_beef = (sum_ctr_beef_array + sum_ctr_extra_array) * price_beef_toops;
//                     if ((price_beef) < 0) {
//                         price_beef = 0;
//                     }

//                     extra_price_text = extra_price_text.text((price_vege + price_beef + price_cheese + price_extra + price_cake).toFixed(2));
//                 }
//                 if (sum_ctr_extra_array == 0) {
//                     price_beef = sum_ctr_beef_array * price_beef_toops;
//                     if ((price_beef) < 0) {
//                         price_beef = 0;
//                     }
//                     extra_price_text = extra_price_text.text((price_vege + price_beef + price_cheese + price_extra + price_cake).toFixed(2));
//                 }
//                 if (sum_ctr_extra_array > 0) {
//                     price_beef = sum_ctr_beef_array * price_beef_toops;
//                     if ((price_beef) < 0) {
//                         price_beef = 0;
//                     }
//                     extra_price_text = extra_price_text.text((price_vege + price_beef + price_cheese + price_extra + price_cake).toFixed(2));
//                 }
//                 if (sum_ctr_extra_array > 0) {
//                     price_extra = sum_ctr_extra_array * price_extra_toops;

//                     extra_price_text = extra_price_text.text((price_vege + price_beef + price_cheese + price_extra + price_cake).toFixed(2));
//                 }

//                 if (sum_ctr_extra_array == 0) {
//                     price_extra = 0;

//                     extra_price_text = extra_price_text.text((price_vege + price_beef + price_cheese + price_extra + price_cake).toFixed(2));
//                 }
//                 input_value.attr('value', (price_vege + price_beef + price_cheese + price_extra + price_cake).toFixed(2));

//             } else {
//                 $(this).removeClass("btn-secondary");
//                 $(this).addClass("btn-danger");
//                 ctr_vege_array.push(1);
//                 sum_ctr_vege_array = eval(ctr_vege_array.join("+"));
//                 sum_ctr_vege_array = parseInt(sum_ctr_vege_array);
//                 i_vege.text(sum_ctr_vege_array);
//                 $('#text_change_topps_del li:contains(' + $(this).text() + ')').remove();
//                 text_del = "-" + $(this).text() + ", ";
//                 input_del_text = input_del_text.replace(text_del, "");
//                 input_del_topps.attr('value', input_del_text);
//                 if ((sum_ctr_beef_array > 0) && (sum_ctr_extra_array < 0) && (sum_ctr_beef_array + sum_ctr_extra_array) == 0) {
//                     price_vege = sum_ctr_vege_array * price_vege_toops;
//                     if ((price_vege) < 0) {
//                         price_vege = 0;
//                     }
//                     extra_price_text = extra_price_text.text((price_vege + price_beef + price_cheese + price_extra + price_cake).toFixed(2));
//                 }
//                 if ((sum_ctr_beef_array > 0) && (sum_ctr_extra_array > 0) && (sum_ctr_beef_array + sum_ctr_extra_array) == 0) {
//                     price_vege = sum_ctr_vege_array * price_vege_toops;
//                     if ((price_vege) < 0) {
//                         price_vege = 0;
//                     }
//                     extra_price_text = extra_price_text.text((price_vege + price_beef + price_cheese + price_extra + price_cake).toFixed(2));
//                 }
//                 if ((sum_ctr_beef_array < 0) && (sum_ctr_extra_array < 0)) {
//                     price_vege = (sum_ctr_vege_array + (sum_ctr_beef_array + sum_ctr_extra_array)) * price_vege_toops;
//                     if ((price_vege) < 0) {
//                         price_vege = 0;
//                     }
//                     extra_price_text = extra_price_text.text((price_vege + price_beef + price_cheese + price_extra + price_cake).toFixed(2));
//                 }
//                 if ((sum_ctr_beef_array == 0) && (sum_ctr_extra_array < 0)) {
//                     price_vege = (sum_ctr_vege_array + (sum_ctr_extra_array)) * price_vege_toops;
//                     if ((price_vege) < 0) {
//                         price_vege = 0;
//                     }
//                     extra_price_text = extra_price_text.text((price_vege + price_beef + price_cheese + price_extra + price_cake).toFixed(2));
//                 }
//                 if ((sum_ctr_beef_array > 0) && (sum_ctr_extra_array == 0)) {
//                     price_vege = (sum_ctr_vege_array * price_vege_toops);
//                     if ((price_vege) < 0) {
//                         price_vege = 0;
//                     }
//                     extra_price_text = extra_price_text.text((price_vege + price_beef + price_cheese + price_extra + price_cake).toFixed(2));
//                 }

//                 if ((sum_ctr_beef_array < 0) && (sum_ctr_extra_array == 0)) {
//                     price_vege = ((sum_ctr_vege_array + sum_ctr_beef_array) * price_vege_toops);
//                     if ((price_vege) < 0) {
//                         price_vege = 0;
//                     }
//                     extra_price_text = extra_price_text.text((price_vege + price_beef + price_cheese + price_extra + price_cake).toFixed(2));
//                 }
//                 if ((sum_ctr_beef_array > 0) && (sum_ctr_extra_array > 0)) {
//                     price_vege = (sum_ctr_vege_array * price_vege_toops);
//                     if ((price_vege) < 0) {
//                         price_vege = 0;
//                     }
//                     extra_price_text = extra_price_text.text((price_vege + price_beef + price_cheese + price_extra + price_cake).toFixed(2));
//                 }
//                 if ((sum_ctr_beef_array == 0) && (sum_ctr_extra_array == 0)) {
//                     price_vege = sum_ctr_vege_array * price_vege_toops;
//                     if ((price_vege) < 0) {
//                         price_vege = 0;
//                     }
//                     extra_price_text = extra_price_text.text((price_vege + price_beef + price_cheese + price_extra + price_cake).toFixed(2));
//                 }
//                 if ((sum_ctr_beef_array == 0) && (sum_ctr_extra_array > 0)) {
//                     price_vege = sum_ctr_vege_array * price_vege_toops;
//                     if ((price_vege) < 0) {
//                         price_vege = 0;
//                     }
//                     extra_price_text = extra_price_text.text((price_vege + price_beef + price_cheese + price_extra + price_cake).toFixed(2));
//                 }



//                 if (sum_ctr_extra_array < 0) {
//                     price_beef = (sum_ctr_beef_array + sum_ctr_extra_array) * price_beef_toops;
//                     if ((price_beef) < 0) {
//                         price_beef = 0;
//                     }

//                     extra_price_text = extra_price_text.text((price_vege + price_beef + price_cheese + price_extra + price_cake).toFixed(2));
//                 }
//                 if (sum_ctr_extra_array == 0) {
//                     price_beef = sum_ctr_beef_array * price_beef_toops;
//                     if ((price_beef) < 0) {
//                         price_beef = 0;
//                     }
//                     extra_price_text = extra_price_text.text((price_vege + price_beef + price_cheese + price_extra + price_cake).toFixed(2));
//                 }
//                 if (sum_ctr_extra_array > 0) {
//                     price_beef = sum_ctr_beef_array * price_beef_toops;
//                     if ((price_beef) < 0) {
//                         price_beef = 0;
//                     }
//                     extra_price_text = extra_price_text.text((price_vege + price_beef + price_cheese + price_extra + price_cake).toFixed(2));
//                 }
//                 if (sum_ctr_extra_array > 0) {
//                     price_extra = sum_ctr_extra_array * price_extra_toops;

//                     extra_price_text = extra_price_text.text((price_vege + price_beef + price_cheese + price_extra + price_cake).toFixed(2));
//                 }
//                 if (sum_ctr_extra_array == 0) {
//                     price_extra = 0;

//                     extra_price_text = extra_price_text.text((price_vege + price_beef + price_cheese + price_extra + price_cake).toFixed(2));
//                 }
//                 input_value.attr('value', (price_vege + price_beef + price_cheese + price_extra + price_cake).toFixed(2));

//             }
//         });
//     }
//     if (($(this).attr("class").split((/\s+/))[0]) == 2) {
//         beef_toops_array.push(1);
//         $(this).on("click", function () {
//             if ($(this).hasClass("btn-danger")) {
//                 changes -= 1;
//                 $(this).removeClass("btn-danger");
//                 $(this).addClass("btn-secondary");
//                 ctr_beef_array.push(-1);
//                 sum_ctr_beef_array = eval(ctr_beef_array.join("+"));
//                 sum_ctr_beef_array = parseInt(sum_ctr_beef_array);
//                 i_beef.text(sum_ctr_beef_array);
//                 text_del = "-" + $(this).text() + ", ";
//                 ul_del.append('<li>' + text_del + '</li>');
//                 input_del_text += text_del
//                 input_del_topps.attr('value', input_del_text);
//                 if ((sum_ctr_beef_array > 0) && (sum_ctr_extra_array < 0) && (sum_ctr_beef_array + sum_ctr_extra_array) == 0) {
//                     price_vege = sum_ctr_vege_array * price_vege_toops;
//                     if ((price_vege) < 0) {
//                         price_vege = 0;
//                     }
//                     extra_price_text = extra_price_text.text((price_vege + price_beef + price_cheese + price_extra + price_cake).toFixed(2));
//                 }
//                 if ((sum_ctr_beef_array > 0) && (sum_ctr_extra_array > 0) && (sum_ctr_beef_array + sum_ctr_extra_array) == 0) {
//                     price_vege = sum_ctr_vege_array * price_vege_toops;
//                     if ((price_vege) < 0) {
//                         price_vege = 0;
//                     }
//                     extra_price_text = extra_price_text.text((price_vege + price_beef + price_cheese + price_extra + price_cake).toFixed(2));
//                 }
//                 if ((sum_ctr_beef_array < 0) && (sum_ctr_extra_array < 0)) {
//                     price_vege = (sum_ctr_vege_array + (sum_ctr_beef_array + sum_ctr_extra_array)) * price_vege_toops;
//                     if ((price_vege) < 0) {
//                         price_vege = 0;
//                     }
//                     extra_price_text = extra_price_text.text((price_vege + price_beef + price_cheese + price_extra + price_cake).toFixed(2));
//                 }
//                 if ((sum_ctr_beef_array == 0) && (sum_ctr_extra_array < 0)) {
//                     price_vege = (sum_ctr_vege_array + (sum_ctr_extra_array)) * price_vege_toops;
//                     if ((price_vege) < 0) {
//                         price_vege = 0;
//                     }
//                     extra_price_text = extra_price_text.text((price_vege + price_beef + price_cheese + price_extra + price_cake).toFixed(2));
//                 }
//                 if ((sum_ctr_beef_array > 0) && (sum_ctr_extra_array == 0)) {
//                     price_vege = (sum_ctr_vege_array * price_vege_toops);
//                     if ((price_vege) < 0) {
//                         price_vege = 0;
//                     }
//                     extra_price_text = extra_price_text.text((price_vege + price_beef + price_cheese + price_extra + price_cake).toFixed(2));
//                 }

//                 if ((sum_ctr_beef_array < 0) && (sum_ctr_extra_array == 0)) {
//                     price_vege = ((sum_ctr_vege_array + sum_ctr_beef_array) * price_vege_toops);
//                     if ((price_vege) < 0) {
//                         price_vege = 0;
//                     }
//                     extra_price_text = extra_price_text.text((price_vege + price_beef + price_cheese + price_extra + price_cake).toFixed(2));
//                 }
//                 if ((sum_ctr_beef_array > 0) && (sum_ctr_extra_array > 0)) {
//                     price_vege = (sum_ctr_vege_array * price_vege_toops);
//                     if ((price_vege) < 0) {
//                         price_vege = 0;
//                     }
//                     extra_price_text = extra_price_text.text((price_vege + price_beef + price_cheese + price_extra + price_cake).toFixed(2));
//                 }
//                 if ((sum_ctr_beef_array == 0) && (sum_ctr_extra_array == 0)) {
//                     price_vege = sum_ctr_vege_array * price_vege_toops;
//                     if ((price_vege) < 0) {
//                         price_vege = 0;
//                     }
//                     extra_price_text = extra_price_text.text((price_vege + price_beef + price_cheese + price_extra + price_cake).toFixed(2));
//                 }
//                 if ((sum_ctr_beef_array == 0) && (sum_ctr_extra_array > 0)) {
//                     price_vege = sum_ctr_vege_array * price_vege_toops;
//                     if ((price_vege) < 0) {
//                         price_vege = 0;
//                     }
//                     extra_price_text = extra_price_text.text((price_vege + price_beef + price_cheese + price_extra + price_cake).toFixed(2));
//                 }



//                 if (sum_ctr_extra_array < 0) {
//                     price_beef = (sum_ctr_beef_array + sum_ctr_extra_array) * price_beef_toops;
//                     if ((price_beef) < 0) {
//                         price_beef = 0;
//                     }

//                     extra_price_text = extra_price_text.text((price_vege + price_beef + price_cheese + price_extra + price_cake).toFixed(2));
//                 }
//                 if (sum_ctr_extra_array == 0) {
//                     price_beef = sum_ctr_beef_array * price_beef_toops;
//                     if ((price_beef) < 0) {
//                         price_beef = 0;
//                     }
//                     extra_price_text = extra_price_text.text((price_vege + price_beef + price_cheese + price_extra + price_cake).toFixed(2));
//                 }
//                 if (sum_ctr_extra_array > 0) {
//                     price_beef = sum_ctr_beef_array * price_beef_toops;
//                     if ((price_beef) < 0) {
//                         price_beef = 0;
//                     }
//                     extra_price_text = extra_price_text.text((price_vege + price_beef + price_cheese + price_extra + price_cake).toFixed(2));
//                 }
//                 if (sum_ctr_extra_array > 0) {
//                     price_extra = sum_ctr_extra_array * price_extra_toops;

//                     extra_price_text = extra_price_text.text((price_vege + price_beef + price_cheese + price_extra + price_cake).toFixed(2));
//                 }
//                 if (sum_ctr_extra_array == 0) {
//                     price_extra = 0;

//                     extra_price_text = extra_price_text.text((price_vege + price_beef + price_cheese + price_extra + price_cake).toFixed(2));
//                 }
//                 input_value.attr('value', (price_vege + price_beef + price_cheese + price_extra + price_cake).toFixed(2));

//             } else {
//                 changes += 1;
//                 $(this).removeClass("btn-secondary");
//                 $(this).addClass("btn-danger");
//                 ctr_beef_array.push(1);
//                 sum_ctr_beef_array = eval(ctr_beef_array.join("+"));
//                 sum_ctr_beef_array = parseInt(sum_ctr_beef_array);
//                 i_beef.text(sum_ctr_beef_array);
//                 $('#text_change_topps_del li:contains(' + $(this).text() + ')').remove();
//                 text_del = "-" + $(this).text() + ", ";
//                 input_del_text = input_del_text.replace(text_del, "");
//                 input_del_topps.attr('value', input_del_text);
//                 if ((sum_ctr_beef_array > 0) && (sum_ctr_extra_array < 0) && (sum_ctr_beef_array + sum_ctr_extra_array) == 0) {
//                     price_vege = sum_ctr_vege_array * price_vege_toops;
//                     if ((price_vege) < 0) {
//                         price_vege = 0;
//                     }
//                     extra_price_text = extra_price_text.text((price_vege + price_beef + price_cheese + price_extra + price_cake).toFixed(2));
//                 }
//                 if ((sum_ctr_beef_array > 0) && (sum_ctr_extra_array > 0) && (sum_ctr_beef_array + sum_ctr_extra_array) == 0) {
//                     price_vege = sum_ctr_vege_array * price_vege_toops;
//                     if ((price_vege) < 0) {
//                         price_vege = 0;
//                     }
//                     extra_price_text = extra_price_text.text((price_vege + price_beef + price_cheese + price_extra + price_cake).toFixed(2));
//                 }
//                 if ((sum_ctr_beef_array < 0) && (sum_ctr_extra_array < 0)) {
//                     price_vege = (sum_ctr_vege_array + (sum_ctr_beef_array + sum_ctr_extra_array)) * price_vege_toops;
//                     if ((price_vege) < 0) {
//                         price_vege = 0;
//                     }
//                     extra_price_text = extra_price_text.text((price_vege + price_beef + price_cheese + price_extra + price_cake).toFixed(2));
//                 }
//                 if ((sum_ctr_beef_array == 0) && (sum_ctr_extra_array < 0)) {
//                     price_vege = (sum_ctr_vege_array + (sum_ctr_extra_array)) * price_vege_toops;
//                     if ((price_vege) < 0) {
//                         price_vege = 0;
//                     }
//                     extra_price_text = extra_price_text.text((price_vege + price_beef + price_cheese + price_extra + price_cake).toFixed(2));
//                 }
//                 if ((sum_ctr_beef_array > 0) && (sum_ctr_extra_array == 0)) {
//                     price_vege = (sum_ctr_vege_array * price_vege_toops);
//                     if ((price_vege) < 0) {
//                         price_vege = 0;
//                     }
//                     extra_price_text = extra_price_text.text((price_vege + price_beef + price_cheese + price_extra + price_cake).toFixed(2));
//                 }

//                 if ((sum_ctr_beef_array < 0) && (sum_ctr_extra_array == 0)) {
//                     price_vege = ((sum_ctr_vege_array + sum_ctr_beef_array) * price_vege_toops);
//                     if ((price_vege) < 0) {
//                         price_vege = 0;
//                     }
//                     extra_price_text = extra_price_text.text((price_vege + price_beef + price_cheese + price_extra + price_cake).toFixed(2));
//                 }
//                 if ((sum_ctr_beef_array > 0) && (sum_ctr_extra_array > 0)) {
//                     price_vege = (sum_ctr_vege_array * price_vege_toops);
//                     if ((price_vege) < 0) {
//                         price_vege = 0;
//                     }
//                     extra_price_text = extra_price_text.text((price_vege + price_beef + price_cheese + price_extra + price_cake).toFixed(2));
//                 }
//                 if ((sum_ctr_beef_array == 0) && (sum_ctr_extra_array == 0)) {
//                     price_vege = sum_ctr_vege_array * price_vege_toops;
//                     if ((price_vege) < 0) {
//                         price_vege = 0;
//                     }
//                     extra_price_text = extra_price_text.text((price_vege + price_beef + price_cheese + price_extra + price_cake).toFixed(2));
//                 }
//                 if ((sum_ctr_beef_array == 0) && (sum_ctr_extra_array > 0)) {
//                     price_vege = sum_ctr_vege_array * price_vege_toops;
//                     if ((price_vege) < 0) {
//                         price_vege = 0;
//                     }
//                     extra_price_text = extra_price_text.text((price_vege + price_beef + price_cheese + price_extra + price_cake).toFixed(2));
//                 }



//                 if (sum_ctr_extra_array < 0) {
//                     price_beef = (sum_ctr_beef_array + sum_ctr_extra_array) * price_beef_toops;
//                     if ((price_beef) < 0) {
//                         price_beef = 0;
//                     }

//                     extra_price_text = extra_price_text.text((price_vege + price_beef + price_cheese + price_extra + price_cake).toFixed(2));
//                 }
//                 if (sum_ctr_extra_array == 0) {
//                     price_beef = sum_ctr_beef_array * price_beef_toops;
//                     if ((price_beef) < 0) {
//                         price_beef = 0;
//                     }
//                     extra_price_text = extra_price_text.text((price_vege + price_beef + price_cheese + price_extra + price_cake).toFixed(2));
//                 }
//                 if (sum_ctr_extra_array > 0) {
//                     price_beef = sum_ctr_beef_array * price_beef_toops;
//                     if ((price_beef) < 0) {
//                         price_beef = 0;
//                     }
//                     extra_price_text = extra_price_text.text((price_vege + price_beef + price_cheese + price_extra + price_cake).toFixed(2));
//                 }
//                 if (sum_ctr_extra_array > 0) {
//                     price_extra = sum_ctr_extra_array * price_extra_toops;

//                     extra_price_text = extra_price_text.text((price_vege + price_beef + price_cheese + price_extra + price_cake).toFixed(2));
//                 }
//                 if (sum_ctr_extra_array == 0) {
//                     price_extra = 0;

//                     extra_price_text = extra_price_text.text((price_vege + price_beef + price_cheese + price_extra + price_cake).toFixed(2));
//                 }
//                 input_value.attr('value', (price_vege + price_beef + price_cheese + price_extra + price_cake).toFixed(2));
//             }
//         });
//     }
//     if (($(this).attr("class").split((/\s+/))[0]) == 3) {
//         cheese_toops_array.push(1);
//         $(this).on("click", function () {
//             if ($(this).hasClass("btn-danger")) {
//                 changes -= 1;
//                 $(this).removeClass("btn-danger");
//                 $(this).addClass("btn-secondary");
//                 ctr_cheese_array.push(-1);
//                 sum_ctr_cheese_array = eval(ctr_cheese_array.join("+"));
//                 sum_ctr_cheese_array = parseInt(sum_ctr_cheese_array);
//                 i_cheese.text(sum_ctr_cheese_array);
//                 price_cheese = sum_ctr_cheese_array * price_cheese_toops;
//                 text_del = "-" + $(this).text() + ", ";
//                 ul_del.append('<li>' + text_del + '</li>');
//                 input_del_text += text_del
//                 input_del_topps.attr('value', input_del_text);
//                 if (price_cheese < 0) {
//                     price_cheese = 0;
//                 }
//                 extra_price_text = extra_price_text.text((price_vege + price_beef + price_cheese + price_extra + price_cake).toFixed(2));
//                 input_value.attr('value', (price_vege + price_beef + price_cheese + price_extra + price_cake).toFixed(2));
//             } else {
//                 changes += 1;
//                 $(this).removeClass("btn-secondary");
//                 $(this).addClass("btn-danger");
//                 ctr_cheese_array.push(1);
//                 sum_ctr_cheese_array = eval(ctr_cheese_array.join("+"));
//                 sum_ctr_cheese_array = parseInt(sum_ctr_cheese_array);
//                 i_cheese.text(sum_ctr_cheese_array);
//                 price_cheese = sum_ctr_cheese_array * price_cheese_toops;
//                 $('#text_change_topps_del li:contains(' + $(this).text() + ')').remove();
//                 text_del = "-" + $(this).text() + ", ";
//                 input_del_text = input_del_text.replace(text_del, "");
//                 input_del_topps.attr('value', input_del_text);
//                 if (price_cheese < 0) {
//                     price_cheese = 0;
//                 }
//                 extra_price_text = extra_price_text.text((price_vege + price_beef + price_cheese + price_extra + price_cake).toFixed(2));
//                 input_value.attr('value', (price_vege + price_beef + price_cheese + price_extra + price_cake).toFixed(2));
//             }
//         })
//     }

//     if (($(this).attr("class").split((/\s+/))[0]) == 4) {
//         extra_toops_array.push(1);
//         $(this).on("click", function () {
//             if ($(this).hasClass("btn-danger")) {
//                 changes -= 1;
//                 $(this).removeClass("btn-danger");
//                 $(this).addClass("btn-secondary");
//                 ctr_extra_array.push(-1);
//                 sum_ctr_extra_array = eval(ctr_extra_array.join("+"));
//                 sum_ctr_extra_array = parseInt(sum_ctr_extra_array);
//                 i_extra.text(sum_ctr_extra_array);
//                 text_del = "-" + $(this).text() + ", ";
//                 ul_del.append('<li>' + text_del + '</li>');
//                 input_del_text += text_del
//                 input_del_topps.attr('value', input_del_text);
//                 if ((sum_ctr_beef_array > 0) && (sum_ctr_extra_array < 0) && (sum_ctr_beef_array + sum_ctr_extra_array) == 0) {
//                     price_vege = sum_ctr_vege_array * price_vege_toops;
//                     if ((price_vege) < 0) {
//                         price_vege = 0;
//                     }
//                     extra_price_text = extra_price_text.text((price_vege + price_beef + price_cheese + price_extra + price_cake).toFixed(2));
//                 }
//                 if ((sum_ctr_beef_array > 0) && (sum_ctr_extra_array > 0) && (sum_ctr_beef_array + sum_ctr_extra_array) == 0) {
//                     price_vege = sum_ctr_vege_array * price_vege_toops;
//                     if ((price_vege) < 0) {
//                         price_vege = 0;
//                     }
//                     extra_price_text = extra_price_text.text((price_vege + price_beef + price_cheese + price_extra + price_cake).toFixed(2));
//                 }
//                 if ((sum_ctr_beef_array < 0) && (sum_ctr_extra_array < 0)) {
//                     price_vege = (sum_ctr_vege_array + (sum_ctr_beef_array + sum_ctr_extra_array)) * price_vege_toops;
//                     if ((price_vege) < 0) {
//                         price_vege = 0;
//                     }
//                     extra_price_text = extra_price_text.text((price_vege + price_beef + price_cheese + price_extra + price_cake).toFixed(2));
//                 }
//                 if ((sum_ctr_beef_array == 0) && (sum_ctr_extra_array < 0)) {
//                     price_vege = (sum_ctr_vege_array + (sum_ctr_extra_array)) * price_vege_toops;
//                     if ((price_vege) < 0) {
//                         price_vege = 0;
//                     }
//                     extra_price_text = extra_price_text.text((price_vege + price_beef + price_cheese + price_extra + price_cake).toFixed(2));
//                 }
//                 if ((sum_ctr_beef_array > 0) && (sum_ctr_extra_array == 0)) {
//                     price_vege = (sum_ctr_vege_array * price_vege_toops);
//                     if ((price_vege) < 0) {
//                         price_vege = 0;
//                     }
//                     extra_price_text = extra_price_text.text((price_vege + price_beef + price_cheese + price_extra + price_cake).toFixed(2));
//                 }

//                 if ((sum_ctr_beef_array < 0) && (sum_ctr_extra_array == 0)) {
//                     price_vege = ((sum_ctr_vege_array + sum_ctr_beef_array) * price_vege_toops);
//                     if ((price_vege) < 0) {
//                         price_vege = 0;
//                     }
//                     extra_price_text = extra_price_text.text((price_vege + price_beef + price_cheese + price_extra + price_cake).toFixed(2));
//                 }
//                 if ((sum_ctr_beef_array > 0) && (sum_ctr_extra_array > 0)) {
//                     price_vege = (sum_ctr_vege_array * price_vege_toops);
//                     if ((price_vege) < 0) {
//                         price_vege = 0;
//                     }
//                     extra_price_text = extra_price_text.text((price_vege + price_beef + price_cheese + price_extra + price_cake).toFixed(2));
//                 }
//                 if ((sum_ctr_beef_array == 0) && (sum_ctr_extra_array == 0)) {
//                     price_vege = sum_ctr_vege_array * price_vege_toops;
//                     if ((price_vege) < 0) {
//                         price_vege = 0;
//                     }
//                     extra_price_text = extra_price_text.text((price_vege + price_beef + price_cheese + price_extra + price_cake).toFixed(2));
//                 }
//                 if ((sum_ctr_beef_array == 0) && (sum_ctr_extra_array > 0)) {
//                     price_vege = sum_ctr_vege_array * price_vege_toops;
//                     if ((price_vege) < 0) {
//                         price_vege = 0;
//                     }
//                     extra_price_text = extra_price_text.text((price_vege + price_beef + price_cheese + price_extra + price_cake).toFixed(2));
//                 }



//                 if (sum_ctr_extra_array < 0) {
//                     price_beef = (sum_ctr_beef_array + sum_ctr_extra_array) * price_beef_toops;
//                     if ((price_beef) < 0) {
//                         price_beef = 0;
//                     }

//                     extra_price_text = extra_price_text.text((price_vege + price_beef + price_cheese + price_extra + price_cake).toFixed(2));
//                 }
//                 if (sum_ctr_extra_array == 0) {
//                     price_beef = sum_ctr_beef_array * price_beef_toops;
//                     if ((price_beef) < 0) {
//                         price_beef = 0;
//                     }
//                     extra_price_text = extra_price_text.text((price_vege + price_beef + price_cheese + price_extra + price_cake).toFixed(2));
//                 }
//                 if (sum_ctr_extra_array > 0) {
//                     price_beef = sum_ctr_beef_array * price_beef_toops;
//                     if ((price_beef) < 0) {
//                         price_beef = 0;
//                     }
//                     extra_price_text = extra_price_text.text((price_vege + price_beef + price_cheese + price_extra + price_cake).toFixed(2));
//                 }
//                 if (sum_ctr_extra_array > 0) {
//                     price_extra = sum_ctr_extra_array * price_extra_toops;

//                     extra_price_text = extra_price_text.text((price_vege + price_beef + price_cheese + price_extra + price_cake).toFixed(2));
//                 }
//                 if (sum_ctr_extra_array == 0) {
//                     price_extra = 0;

//                     extra_price_text = extra_price_text.text((price_vege + price_beef + price_cheese + price_extra + price_cake).toFixed(2));
//                 }
//                 input_value.attr('value', (price_vege + price_beef + price_cheese + price_extra + price_cake).toFixed(2));

//             } else {
//                 changes += 1;
//                 $(this).removeClass("btn-secondary");
//                 $(this).addClass("btn-danger");
//                 ctr_extra_array.push(1);
//                 sum_ctr_extra_array = eval(ctr_extra_array.join("+"));
//                 sum_ctr_extra_array = parseInt(sum_ctr_extra_array);
//                 i_extra.text(sum_ctr_extra_array);
//                 $('#text_change_topps_del li:contains(' + $(this).text() + ')').remove();
//                 text_del = "-" + $(this).text() + ", ";
//                 input_del_text = input_del_text.replace(text_del, "");
//                 input_del_topps.attr('value', input_del_text);
//                 if ((sum_ctr_beef_array > 0) && (sum_ctr_extra_array < 0) && (sum_ctr_beef_array + sum_ctr_extra_array) == 0) {
//                     price_vege = sum_ctr_vege_array * price_vege_toops;
//                     if ((price_vege) < 0) {
//                         price_vege = 0;
//                     }
//                     extra_price_text = extra_price_text.text((price_vege + price_beef + price_cheese + price_extra + price_cake).toFixed(2));
//                 }
//                 if ((sum_ctr_beef_array > 0) && (sum_ctr_extra_array > 0) && (sum_ctr_beef_array + sum_ctr_extra_array) == 0) {
//                     price_vege = sum_ctr_vege_array * price_vege_toops;
//                     if ((price_vege) < 0) {
//                         price_vege = 0;
//                     }
//                     extra_price_text = extra_price_text.text((price_vege + price_beef + price_cheese + price_extra + price_cake).toFixed(2));
//                 }
//                 if ((sum_ctr_beef_array < 0) && (sum_ctr_extra_array < 0)) {
//                     price_vege = (sum_ctr_vege_array + (sum_ctr_beef_array + sum_ctr_extra_array)) * price_vege_toops;
//                     if ((price_vege) < 0) {
//                         price_vege = 0;
//                     }
//                     extra_price_text = extra_price_text.text((price_vege + price_beef + price_cheese + price_extra + price_cake).toFixed(2));
//                 }
//                 if ((sum_ctr_beef_array == 0) && (sum_ctr_extra_array < 0)) {
//                     price_vege = (sum_ctr_vege_array + (sum_ctr_extra_array)) * price_vege_toops;
//                     if ((price_vege) < 0) {
//                         price_vege = 0;
//                     }
//                     extra_price_text = extra_price_text.text((price_vege + price_beef + price_cheese + price_extra + price_cake).toFixed(2));
//                 }
//                 if ((sum_ctr_beef_array > 0) && (sum_ctr_extra_array == 0)) {
//                     price_vege = (sum_ctr_vege_array * price_vege_toops);
//                     if ((price_vege) < 0) {
//                         price_vege = 0;
//                     }
//                     eextra_price_text = extra_price_text.text((price_vege + price_beef + price_cheese + price_extra + price_cake).toFixed(2));
//                 }

//                 if ((sum_ctr_beef_array < 0) && (sum_ctr_extra_array == 0)) {
//                     price_vege = ((sum_ctr_vege_array + sum_ctr_beef_array) * price_vege_toops);
//                     if ((price_vege) < 0) {
//                         price_vege = 0;
//                     }
//                     extra_price_text = extra_price_text.text((price_vege + price_beef + price_cheese + price_extra + price_cake).toFixed(2));
//                 }
//                 if ((sum_ctr_beef_array > 0) && (sum_ctr_extra_array > 0)) {
//                     price_vege = (sum_ctr_vege_array * price_vege_toops);
//                     if ((price_vege) < 0) {
//                         price_vege = 0;
//                     }
//                     extra_price_text = extra_price_text.text((price_vege + price_beef + price_cheese + price_extra + price_cake).toFixed(2));
//                 }
//                 if ((sum_ctr_beef_array == 0) && (sum_ctr_extra_array == 0)) {
//                     price_vege = sum_ctr_vege_array * price_vege_toops;
//                     if ((price_vege) < 0) {
//                         price_vege = 0;
//                     }
//                     extra_price_text = extra_price_text.text((price_vege + price_beef + price_cheese + price_extra + price_cake).toFixed(2));
//                 }
//                 if ((sum_ctr_beef_array == 0) && (sum_ctr_extra_array > 0)) {
//                     price_vege = sum_ctr_vege_array * price_vege_toops;
//                     if ((price_vege) < 0) {
//                         price_vege = 0;
//                     }
//                     extra_price_text = extra_price_text.text((price_vege + price_beef + price_cheese + price_extra + price_cake).toFixed(2));
//                 }



//                 if (sum_ctr_extra_array < 0) {
//                     price_beef = (sum_ctr_beef_array + sum_ctr_extra_array) * price_beef_toops;
//                     if ((price_beef) < 0) {
//                         price_beef = 0;
//                     }

//                     extra_price_text = extra_price_text.text((price_vege + price_beef + price_cheese + price_extra + price_cake).toFixed(2));
//                 }
//                 if (sum_ctr_extra_array == 0) {
//                     price_beef = sum_ctr_beef_array * price_beef_toops;
//                     if ((price_beef) < 0) {
//                         price_beef = 0;
//                     }
//                     extra_price_text = extra_price_text.text((price_vege + price_beef + price_cheese + price_extra + price_cake).toFixed(2));
//                 }
//                 if (sum_ctr_extra_array > 0) {
//                     price_beef = sum_ctr_beef_array * price_beef_toops;
//                     if ((price_beef) < 0) {
//                         price_beef = 0;
//                     }
//                     extra_price_text = extra_price_text.text((price_vege + price_beef + price_cheese + price_extra + price_cake).toFixed(2));
//                 }
//                 if (sum_ctr_extra_array > 0) {
//                     price_extra = sum_ctr_extra_array * price_extra_toops;

//                     extra_price_text = extra_price_text.text((price_vege + price_beef + price_cheese + price_extra + price_cake).toFixed(2));
//                 }
//                 if (sum_ctr_extra_array == 0) {
//                     price_extra = 0;

//                     extra_price_text = extra_price_text.text((price_vege + price_beef + price_cheese + price_extra + price_cake).toFixed(2));
//                 }
//                 input_value.attr('value', (price_vege + price_beef + price_cheese + price_extra + price_cake).toFixed(2));

//             }
//         });
//     }

// });

// vegetopps.each(function (index) {
//     $(this).on("click", function () {
//         ctr_vege_array.push(1);
//         sum_ctr_vege_array = eval(ctr_vege_array.join("+"));
//         sum_ctr_vege_array = parseInt(sum_ctr_vege_array);
//         i_vege.text(sum_ctr_vege_array);
//         new_button = $(this).clone();
//         new_button.appendTo(add_topps);
//         text_add = "+" + $(this).text() + ", ";
//         ul_add.append('<li class="align-top">' + text_add + '</li>');
//         input_add_text += text_add
//         input_add_topps.attr('value', input_add_text);

//         // var add_topps_buttons = $("#add_topps > button");

//         // add_topps_buttons.each(function (index) {
//         //     $(this).on("click", function () {
//         //         $(this).text();
//         //     });
//         // })

//         if ((sum_ctr_beef_array > 0) && (sum_ctr_extra_array < 0) && (sum_ctr_beef_array + sum_ctr_extra_array) == 0) {
//             price_vege = sum_ctr_vege_array * price_vege_toops;
//             if ((price_vege) < 0) {
//                 price_vege = 0;
//             }
//             extra_price_text = extra_price_text.text((price_vege + price_beef + price_cheese + price_extra + price_cake).toFixed(2));
//         }
//         if ((sum_ctr_beef_array > 0) && (sum_ctr_extra_array > 0) && (sum_ctr_beef_array + sum_ctr_extra_array) == 0) {
//             price_vege = sum_ctr_vege_array * price_vege_toops;
//             if ((price_vege) < 0) {
//                 price_vege = 0;
//             }
//             extra_price_text = extra_price_text.text((price_vege + price_beef + price_cheese + price_extra + price_cake).toFixed(2));
//         }
//         if ((sum_ctr_beef_array < 0) && (sum_ctr_extra_array < 0)) {
//             price_vege = (sum_ctr_vege_array + (sum_ctr_beef_array + sum_ctr_extra_array)) * price_vege_toops;
//             if ((price_vege) < 0) {
//                 price_vege = 0;
//             }
//             extra_price_text = extra_price_text.text((price_vege + price_beef + price_cheese + price_extra + price_cake).toFixed(2));
//         }
//         if ((sum_ctr_beef_array == 0) && (sum_ctr_extra_array < 0)) {
//             price_vege = (sum_ctr_vege_array + (sum_ctr_extra_array)) * price_vege_toops;
//             if ((price_vege) < 0) {
//                 price_vege = 0;
//             }
//             extra_price_text = extra_price_text.text((price_vege + price_beef + price_cheese + price_extra + price_cake).toFixed(2));
//         }
//         if ((sum_ctr_beef_array > 0) && (sum_ctr_extra_array == 0)) {
//             price_vege = (sum_ctr_vege_array * price_vege_toops);
//             if ((price_vege) < 0) {
//                 price_vege = 0;
//             }
//             extra_price_text = extra_price_text.text((price_vege + price_beef + price_cheese + price_extra + price_cake).toFixed(2));
//         }

//         if ((sum_ctr_beef_array < 0) && (sum_ctr_extra_array == 0)) {
//             price_vege = ((sum_ctr_vege_array + sum_ctr_beef_array) * price_vege_toops);
//             if ((price_vege) < 0) {
//                 price_vege = 0;
//             }
//             extra_price_text = extra_price_text.text((price_vege + price_beef + price_cheese + price_extra + price_cake).toFixed(2));
//         }
//         if ((sum_ctr_beef_array > 0) && (sum_ctr_extra_array > 0)) {
//             price_vege = (sum_ctr_vege_array * price_vege_toops);
//             if ((price_vege) < 0) {
//                 price_vege = 0;
//             }
//             extra_price_text = extra_price_text.text((price_vege + price_beef + price_cheese + price_extra + price_cake).toFixed(2));
//         }
//         if ((sum_ctr_beef_array == 0) && (sum_ctr_extra_array == 0)) {
//             price_vege = sum_ctr_vege_array * price_vege_toops;
//             if ((price_vege) < 0) {
//                 price_vege = 0;
//             }
//             extra_price_text = extra_price_text.text((price_vege + price_beef + price_cheese + price_extra + price_cake).toFixed(2));
//         }
//         if ((sum_ctr_beef_array == 0) && (sum_ctr_extra_array > 0)) {
//             price_vege = sum_ctr_vege_array * price_vege_toops;
//             if ((price_vege) < 0) {
//                 price_vege = 0;
//             }
//             extra_price_text = extra_price_text.text((price_vege + price_beef + price_cheese + price_extra + price_cake).toFixed(2));
//         }



//         if (sum_ctr_extra_array < 0) {
//             price_beef = (sum_ctr_beef_array + sum_ctr_extra_array) * price_beef_toops;
//             if ((price_beef) < 0) {
//                 price_beef = 0;
//             }

//             extra_price_text = extra_price_text.text((price_vege + price_beef + price_cheese + price_extra + price_cake).toFixed(2));
//         }
//         if (sum_ctr_extra_array == 0) {
//             price_beef = sum_ctr_beef_array * price_beef_toops;
//             if ((price_beef) < 0) {
//                 price_beef = 0;
//             }
//             extra_price_text = extra_price_text.text((price_vege + price_beef + price_cheese + price_extra + price_cake).toFixed(2));
//         }
//         if (sum_ctr_extra_array > 0) {
//             price_beef = sum_ctr_beef_array * price_beef_toops;
//             if ((price_beef) < 0) {
//                 price_beef = 0;
//             }
//             extra_price_text = extra_price_text.text((price_vege + price_beef + price_cheese + price_extra + price_cake).toFixed(2));
//         }
//         if (sum_ctr_extra_array > 0) {
//             price_extra = sum_ctr_extra_array * price_extra_toops;

//             extra_price_text = extra_price_text.text((price_vege + price_beef + price_cheese + price_extra + price_cake).toFixed(2));
//         }
//         if (sum_ctr_extra_array == 0) {
//             price_extra = 0;

//             extra_price_text = extra_price_text.text((price_vege + price_beef + price_cheese + price_extra + price_cake).toFixed(2));
//         }
//         input_value.attr('value', (price_vege + price_beef + price_cheese + price_extra + price_cake).toFixed(2));
//     });
// });

// beeftopps.each(function (index) {
//     $(this).on("click", function () {

//         ctr_beef_array.push(1);
//         sum_ctr_beef_array = eval(ctr_beef_array.join("+"));
//         sum_ctr_beef_array = parseInt(sum_ctr_beef_array);
//         i_beef.text(sum_ctr_beef_array);
//         new_button = $(this).clone();
//         new_button.appendTo(add_topps);
//         text_add = "+" + $(this).text() + ", ";
//         ul_add.append('<li>' + text_add + '</li>');
//         input_add_text += text_add
//         input_add_topps.attr('value', input_add_text);
//         if ((sum_ctr_beef_array > 0) && (sum_ctr_extra_array < 0) && (sum_ctr_beef_array + sum_ctr_extra_array) == 0) {
//             price_vege = sum_ctr_vege_array * price_vege_toops;
//             if ((price_vege) < 0) {
//                 price_vege = 0;
//             }
//             extra_price_text = extra_price_text.text((price_vege + price_beef + price_cheese + price_extra + price_cake).toFixed(2));
//         }
//         if ((sum_ctr_beef_array > 0) && (sum_ctr_extra_array > 0) && (sum_ctr_beef_array + sum_ctr_extra_array) == 0) {
//             price_vege = sum_ctr_vege_array * price_vege_toops;
//             if ((price_vege) < 0) {
//                 price_vege = 0;
//             }
//             extra_price_text = extra_price_text.text((price_vege + price_beef + price_cheese + price_extra + price_cake).toFixed(2));
//         }
//         if ((sum_ctr_beef_array < 0) && (sum_ctr_extra_array < 0)) {
//             price_vege = (sum_ctr_vege_array + (sum_ctr_beef_array + sum_ctr_extra_array)) * price_vege_toops;
//             if ((price_vege) < 0) {
//                 price_vege = 0;
//             }
//             extra_price_text = extra_price_text.text((price_vege + price_beef + price_cheese + price_extra + price_cake).toFixed(2));
//         }
//         if ((sum_ctr_beef_array == 0) && (sum_ctr_extra_array < 0)) {
//             price_vege = (sum_ctr_vege_array + (sum_ctr_extra_array)) * price_vege_toops;
//             if ((price_vege) < 0) {
//                 price_vege = 0;
//             }
//             eextra_price_text = extra_price_text.text((price_vege + price_beef + price_cheese + price_extra + price_cake).toFixed(2));
//         }
//         if ((sum_ctr_beef_array > 0) && (sum_ctr_extra_array == 0)) {
//             price_vege = (sum_ctr_vege_array * price_vege_toops);
//             if ((price_vege) < 0) {
//                 price_vege = 0;
//             }
//             extra_price_text = extra_price_text.text((price_vege + price_beef + price_cheese + price_extra + price_cake).toFixed(2));
//         }

//         if ((sum_ctr_beef_array < 0) && (sum_ctr_extra_array == 0)) {
//             price_vege = ((sum_ctr_vege_array + sum_ctr_beef_array) * price_vege_toops);
//             if ((price_vege) < 0) {
//                 price_vege = 0;
//             }
//             extra_price_text = extra_price_text.text((price_vege + price_beef + price_cheese + price_extra + price_cake).toFixed(2));
//         }
//         if ((sum_ctr_beef_array > 0) && (sum_ctr_extra_array > 0)) {
//             price_vege = (sum_ctr_vege_array * price_vege_toops);
//             if ((price_vege) < 0) {
//                 price_vege = 0;
//             }
//             extra_price_text = extra_price_text.text((price_vege + price_beef + price_cheese + price_extra + price_cake).toFixed(2));
//         }
//         if ((sum_ctr_beef_array == 0) && (sum_ctr_extra_array == 0)) {
//             price_vege = sum_ctr_vege_array * price_vege_toops;
//             if ((price_vege) < 0) {
//                 price_vege = 0;
//             }
//             extra_price_text = extra_price_text.text((price_vege + price_beef + price_cheese + price_extra + price_cake).toFixed(2));
//         }
//         if ((sum_ctr_beef_array == 0) && (sum_ctr_extra_array > 0)) {
//             price_vege = sum_ctr_vege_array * price_vege_toops;
//             if ((price_vege) < 0) {
//                 price_vege = 0;
//             }
//             extra_price_text = extra_price_text.text((price_vege + price_beef + price_cheese + price_extra + price_cake).toFixed(2));
//         }



//         if (sum_ctr_extra_array < 0) {
//             price_beef = (sum_ctr_beef_array + sum_ctr_extra_array) * price_beef_toops;
//             if ((price_beef) < 0) {
//                 price_beef = 0;
//             }

//             extra_price_text = extra_price_text.text((price_vege + price_beef + price_cheese + price_extra + price_cake).toFixed(2));
//         }
//         if (sum_ctr_extra_array == 0) {
//             price_beef = sum_ctr_beef_array * price_beef_toops;
//             if ((price_beef) < 0) {
//                 price_beef = 0;
//             }
//             extra_price_text = extra_price_text.text((price_vege + price_beef + price_cheese + price_extra + price_cake).toFixed(2));
//         }
//         if (sum_ctr_extra_array > 0) {
//             price_beef = sum_ctr_beef_array * price_beef_toops;
//             if ((price_beef) < 0) {
//                 price_beef = 0;
//             }
//             extra_price_text = extra_price_text.text((price_vege + price_beef + price_cheese + price_extra + price_cake).toFixed(2));
//         }
//         if (sum_ctr_extra_array > 0) {
//             price_extra = sum_ctr_extra_array * price_extra_toops;

//             extra_price_text = extra_price_text.text((price_vege + price_beef + price_cheese + price_extra + price_cake).toFixed(2));
//         }
//         if (sum_ctr_extra_array == 0) {
//             price_extra = 0;

//             extra_price_text = extra_price_text.text((price_vege + price_beef + price_cheese + price_extra + price_cake).toFixed(2));
//         }
//         input_value.attr('value', (price_vege + price_beef + price_cheese + price_extra + price_cake).toFixed(2));

//     })
// });
// cheesetopps.each(function (index) {
//     $(this).on("click", function () {
//         ctr_cheese_array.push(1);
//         sum_ctr_cheese_array = eval(ctr_cheese_array.join("+"));
//         sum_ctr_cheese_array = parseInt(sum_ctr_cheese_array);
//         i_cheese.text(sum_ctr_cheese_array);
//         new_button = $(this).clone();
//         new_button.appendTo(add_topps);
//         text_add = "+" + $(this).text() + ", ";
//         ul_add.append('<li>' + text_add + '</li>');
//         input_add_text += text_add
//         input_add_topps.attr('value', input_add_text);
//         price_cheese = sum_ctr_cheese_array * price_cheese_toops;

//         if (price_cheese < 0) {
//             price_cheese = 0;
//         }
//         extra_price_text = extra_price_text.text((price_vege + price_beef + price_cheese + price_extra + price_cake).toFixed(2));
//         input_value.attr('value', (price_vege + price_beef + price_cheese + price_extra + price_cake).toFixed(2));
//     });
// });


// extratopps.each(function (index) {
//     $(this).on("click", function () {
//         ctr_extra_array.push(1);
//         sum_ctr_extra_array = eval(ctr_extra_array.join("+"));
//         sum_ctr_extra_array = parseInt(sum_ctr_extra_array);
//         i_extra.text(sum_ctr_extra_array);
//         new_button = $(this).clone();
//         new_button.appendTo(add_topps);
//         text_add = "+" + $(this).text() + ", ";
//         ul_add.append('<li>' + text_add + '</li>');
//         input_add_text += text_add
//         input_add_topps.attr('value', input_add_text);
//         if ((sum_ctr_beef_array > 0) && (sum_ctr_extra_array < 0) && (sum_ctr_beef_array + sum_ctr_extra_array) == 0) {
//             price_vege = sum_ctr_vege_array * price_vege_toops;
//             if ((price_vege) < 0) {
//                 price_vege = 0;
//             }
//             extra_price_text = extra_price_text.text((price_vege + price_beef + price_cheese + price_extra + price_cake).toFixed(2));
//         }
//         if ((sum_ctr_beef_array > 0) && (sum_ctr_extra_array > 0) && (sum_ctr_beef_array + sum_ctr_extra_array) == 0) {
//             price_vege = sum_ctr_vege_array * price_vege_toops;
//             if ((price_vege) < 0) {
//                 price_vege = 0;
//             }
//             extra_price_text = extra_price_text.text((price_vege + price_beef + price_cheese + price_extra + price_cake).toFixed(2));
//         }
//         if ((sum_ctr_beef_array < 0) && (sum_ctr_extra_array < 0)) {
//             price_vege = (sum_ctr_vege_array + (sum_ctr_beef_array + sum_ctr_extra_array)) * price_vege_toops;
//             if ((price_vege) < 0) {
//                 price_vege = 0;
//             }
//             extra_price_text = extra_price_text.text((price_vege + price_beef + price_cheese + price_extra + price_cake).toFixed(2));
//         }
//         if ((sum_ctr_beef_array == 0) && (sum_ctr_extra_array < 0)) {
//             price_vege = (sum_ctr_vege_array + (sum_ctr_extra_array)) * price_vege_toops;
//             if ((price_vege) < 0) {
//                 price_vege = 0;
//             }
//             extra_price_text = extra_price_text.text((price_vege + price_beef + price_cheese + price_extra + price_cake).toFixed(2));
//         }
//         if ((sum_ctr_beef_array > 0) && (sum_ctr_extra_array == 0)) {
//             price_vege = (sum_ctr_vege_array * price_vege_toops);
//             if ((price_vege) < 0) {
//                 price_vege = 0;
//             }
//             extra_price_text = extra_price_text.text((price_vege + price_beef + price_cheese + price_extra + price_cake).toFixed(2));
//         }

//         if ((sum_ctr_beef_array < 0) && (sum_ctr_extra_array == 0)) {
//             price_vege = ((sum_ctr_vege_array + sum_ctr_beef_array) * price_vege_toops);
//             if ((price_vege) < 0) {
//                 price_vege = 0;
//             }
//             extra_price_text = extra_price_text.text((price_vege + price_beef + price_cheese + price_extra + price_cake).toFixed(2));
//         }
//         if ((sum_ctr_beef_array > 0) && (sum_ctr_extra_array > 0)) {
//             price_vege = (sum_ctr_vege_array * price_vege_toops);
//             if ((price_vege) < 0) {
//                 price_vege = 0;
//             }
//             extra_price_text = extra_price_text.text((price_vege + price_beef + price_cheese + price_extra + price_cake).toFixed(2));
//         }
//         if ((sum_ctr_beef_array == 0) && (sum_ctr_extra_array == 0)) {
//             price_vege = sum_ctr_vege_array * price_vege_toops;
//             if ((price_vege) < 0) {
//                 price_vege = 0;
//             }
//             extra_price_text = extra_price_text.text((price_vege + price_beef + price_cheese + price_extra + price_cake).toFixed(2));
//         }
//         if ((sum_ctr_beef_array == 0) && (sum_ctr_extra_array > 0)) {
//             price_vege = sum_ctr_vege_array * price_vege_toops;
//             if ((price_vege) < 0) {
//                 price_vege = 0;
//             }
//             extra_price_text = extra_price_text.text((price_vege + price_beef + price_cheese + price_extra + price_cake).toFixed(2));
//         }



//         if (sum_ctr_extra_array < 0) {
//             price_beef = (sum_ctr_beef_array + sum_ctr_extra_array) * price_beef_toops;
//             if ((price_beef) < 0) {
//                 price_beef = 0;
//             }
//             extra_price_text = extra_price_text.text((price_vege + price_beef + price_cheese + price_extra + price_cake).toFixed(2));
//         }
//         if (sum_ctr_extra_array == 0) {
//             price_beef = sum_ctr_beef_array * price_beef_toops;
//             if ((price_beef) < 0) {
//                 price_beef = 0;
//             }
//             extra_price_text = extra_price_text.text((price_vege + price_beef + price_cheese + price_extra + price_cake).toFixed(2));
//         }
//         if (sum_ctr_extra_array > 0) {
//             price_beef = sum_ctr_beef_array * price_beef_toops;
//             if ((price_beef) < 0) {
//                 price_beef = 0;
//             }
//             extra_price_text = extra_price_text.text((price_vege + price_beef + price_cheese + price_extra + price_cake).toFixed(2));
//         }
//         if (sum_ctr_extra_array > 0) {
//             price_extra = sum_ctr_extra_array * price_extra_toops;

//             extra_price_text = extra_price_text.text((price_vege + price_beef + price_cheese + price_extra + price_cake).toFixed(2));
//         }
//         if (sum_ctr_extra_array == 0) {
//             price_extra = 0;

//             extra_price_text = extra_price_text.text((price_vege + price_beef + price_cheese + price_extra + price_cake).toFixed(2));
//         }
//         input_value.attr('value', (price_vege + price_beef + price_cheese + price_extra + price_cake).toFixed(2));

//     })
// });
// caketopps.each(function (index) {
//     $(this).on("click", function () {
//         i_cake += 1;
//         caketopps.removeClass("btn-success");
//         caketopps.addClass("btn-warning");
//         $(this).removeClass("btn-warning");
//         $(this).addClass("btn-success");
//         change_cake.text(i_cake);
//         cake_topp_price = ($(this).data('cakeprice'));
//         cake_topp = cake_topp_price.replace(',', ".");
//         price_cake = parseFloat(cake_topp);
//         extra_price_text = extra_price_text.text((price_vege + price_beef + price_cheese + price_extra + price_cake).toFixed(2));
//         text_add = "+" + $(this).text() + ", ";
//         ul_add.append('<li>' + text_add + '</li>');
//         input_add_text += text_add
//         input_add_topps.attr('value', input_add_text);
//         input_value.attr('value', (price_vege + price_beef + price_cheese + price_extra + price_cake).toFixed(2));

//     });
// });



// $(document).on('click', "#add_topps > button", function () {
//     var topps = $('button.topps');
//     var add_topps = $('#add_topps');
//     var changes = 0;
//     var ul_del = $('#text_change_topps_del');
//     var ul_add = $('#text_change_topps_add');
//     var input_del_text = "";
//     var input_add_text = "";
//     var input_value = $('#input_value');
//     var input_add_topps = $('#input_add_topps');
//     var input_del_topps = $('#input_del_topps');
//     var add_topps_buttons = $("#add_topps > button");



//     var change_vege = $('#change_vege').data('vege_plus');
//     var vege_toops_array = [];
//     var ctr_vege_array = [];
//     var sum_ctr_vege_array = 0;
//     var price_vege_toops = ($('#price_size_vege').data('price'));
//     price_vege_toops = price_vege_toops.replace(',', ".");
//     price_vege_toops = parseFloat(price_vege_toops).toFixed(2);

//     var change_beef = $('#change_beef').data('beef_plus');
//     var beef_toops_array = [];
//     var ctr_beef_array = [];
//     var sum_ctr_beef_array = 0;
//     var price_beef_toops = ($('#price_size_beef').data('price'));
//     price_beef_toops = price_beef_toops.replace(',', ".");
//     price_beef_toops = parseFloat(price_beef_toops).toFixed(2);

//     var change_cheese = $('#change_cheese').data('cheese_plus');
//     var cheese_toops_array = [];
//     var ctr_cheese_array = [];
//     var sum_ctr_cheese_array = 0;
//     var price_cheese_toops = ($('#price_size_cheese').data('price'));
//     price_cheese_toops = price_cheese_toops.replace(',', ".");
//     price_cheese_toops = parseFloat(price_cheese_toops).toFixed(2);

//     var change_extra = $('#change_extra').data('extra_plus');
//     var extra_toops_array = [];
//     var ctr_extra_array = [];
//     var sum_ctr_extra_array = 0;
//     var price_extra_toops = ($('#price_size_extra').data('price'));
//     price_extra_toops = price_extra_toops.replace(',', ".");
//     price_extra_toops = parseFloat(price_extra_toops).toFixed(2);
//     var price_vege = 0;
//     var price_beef = 0;
//     var price_cheese = 0;
//     var price_extra = 0;
//     var price_cake = 0;
//     var price = 0;


//     var cheese_toops_array = [];
//     var extra_toops_array = [];

//     var extra_price_text = $('#extra_price');

//     var text_changes = $('#text_change_topps');
//     var text = " ";

//     var vegetopps = $('button.vegetopps');
//     var beeftopps = $('button.beeftopps');
//     var cheesetopps = $('button.cheesetopps');
//     var extratopps = $('button.extratopps');

//     var caketopps = $('button.caketopps');
//     var change_cake = $('#change_cake');

//     var i_vege = $('#change_vege');
//     var i_beef = $('#change_beef');
//     var i_cheese = $('#change_cheese');
//     var i_extra = $('#change_extra');
//     var i_cake = $('#change_cake');



//     if (($(this).attr("class").split((/\s+/))[0]) == "vegetopps") {
//         $(this).hide();
//         ctr_vege_array.push(-1);
//         sum_ctr_vege_array = eval(ctr_vege_array.join("+"));
//         sum_ctr_vege_array = parseInt(sum_ctr_vege_array);
//         i_vege.text(sum_ctr_vege_array);
//         text_del = "-" + $(this).text() + ", ";
//         ul_del.append('<li>' + text_del + '</li>');
//         input_del_text += text_del
//         input_del_topps.attr('value', input_del_text);
//         if ((sum_ctr_beef_array > 0) && (sum_ctr_extra_array < 0) && (sum_ctr_beef_array + sum_ctr_extra_array) == 0) {
//             price_vege = sum_ctr_vege_array * price_vege_toops;
//             if ((price_vege) < 0) {
//                 price_vege = 0;
//             }
//             extra_price_text = extra_price_text.text((price_vege + price_beef + price_cheese + price_extra + price_cake).toFixed(2));
//         }
//         if ((sum_ctr_beef_array > 0) && (sum_ctr_extra_array > 0) && (sum_ctr_beef_array + sum_ctr_extra_array) == 0) {
//             price_vege = sum_ctr_vege_array * price_vege_toops;
//             if ((price_vege) < 0) {
//                 price_vege = 0;
//             }
//             extra_price_text = extra_price_text.text((price_vege + price_beef + price_cheese + price_extra + price_cake).toFixed(2));
//         }

//         if ((sum_ctr_beef_array < 0) && (sum_ctr_extra_array < 0)) {
//             price_vege = (sum_ctr_vege_array + (sum_ctr_beef_array + sum_ctr_extra_array)) * price_vege_toops;
//             if ((price_vege) < 0) {
//                 price_vege = 0;
//             }
//             extra_price_text = extra_price_text.text((price_vege + price_beef + price_cheese + price_extra + price_cake).toFixed(2));
//         }
//         if ((sum_ctr_beef_array == 0) && (sum_ctr_extra_array < 0)) {
//             price_vege = (sum_ctr_vege_array + (sum_ctr_extra_array)) * price_vege_toops;
//             if ((price_vege) < 0) {
//                 price_vege = 0;
//             }
//             extra_price_text = extra_price_text.text((price_vege + price_beef + price_cheese + price_extra + price_cake).toFixed(2));
//         }
//         if ((sum_ctr_beef_array > 0) && (sum_ctr_extra_array == 0)) {
//             price_vege = (sum_ctr_vege_array * price_vege_toops);
//             if ((price_vege) < 0) {
//                 price_vege = 0;
//             }
//             extra_price_text = extra_price_text.text((price_vege + price_beef + price_cheese + price_extra + price_cake).toFixed(2));
//         }

//         if ((sum_ctr_beef_array < 0) && (sum_ctr_extra_array == 0)) {
//             price_vege = ((sum_ctr_vege_array + sum_ctr_beef_array) * price_vege_toops);
//             if ((price_vege) < 0) {
//                 price_vege = 0;
//             }
//             extra_price_text = extra_price_text.text((price_vege + price_beef + price_cheese + price_extra + price_cake).toFixed(2));
//         }
//         if ((sum_ctr_beef_array > 0) && (sum_ctr_extra_array > 0)) {
//             price_vege = (sum_ctr_vege_array * price_vege_toops);
//             if ((price_vege) < 0) {
//                 price_vege = 0;
//             }
//             extra_price_text = extra_price_text.text((price_vege + price_beef + price_cheese + price_extra + price_cake).toFixed(2));
//         }
//         if ((sum_ctr_beef_array == 0) && (sum_ctr_extra_array == 0)) {
//             price_vege = sum_ctr_vege_array * price_vege_toops;
//             if ((price_vege) < 0) {
//                 price_vege = 0;
//             }
//             extra_price_text = extra_price_text.text((price_vege + price_beef + price_cheese + price_extra + price_cake).toFixed(2));
//         }
//         if ((sum_ctr_beef_array == 0) && (sum_ctr_extra_array > 0)) {
//             price_vege = sum_ctr_vege_array * price_vege_toops;
//             if ((price_vege) < 0) {
//                 price_vege = 0;
//             }
//             extra_price_text = extra_price_text.text((price_vege + price_beef + price_cheese + price_extra + price_cake).toFixed(2));
//         }



//         if (sum_ctr_extra_array < 0) {
//             price_beef = (sum_ctr_beef_array + sum_ctr_extra_array) * price_beef_toops;
//             if ((price_beef) < 0) {
//                 price_beef = 0;
//             }

//             extra_price_text = extra_price_text.text((price_vege + price_beef + price_cheese + price_extra + price_cake).toFixed(2));
//         }
//         if (sum_ctr_extra_array == 0) {
//             price_beef = sum_ctr_beef_array * price_beef_toops;
//             if ((price_beef) < 0) {
//                 price_beef = 0;
//             }
//             extra_price_text = extra_price_text.text((price_vege + price_beef + price_cheese + price_extra + price_cake).toFixed(2));
//         }
//         if (sum_ctr_extra_array > 0) {
//             price_beef = sum_ctr_beef_array * price_beef_toops;
//             if ((price_beef) < 0) {
//                 price_beef = 0;
//             }
//             extra_price_text = extra_price_text.text((price_vege + price_beef + price_cheese + price_extra + price_cake).toFixed(2));
//         }
//         if (sum_ctr_extra_array > 0) {
//             price_extra = sum_ctr_extra_array * price_extra_toops;

//             extra_price_text = extra_price_text.text((price_vege + price_beef + price_cheese + price_extra + price_cake).toFixed(2));
//         }

//         if (sum_ctr_extra_array == 0) {
//             price_extra = 0;

//             extra_price_text = extra_price_text.text((price_vege + price_beef + price_cheese + price_extra + price_cake).toFixed(2));
//         }
//         input_value.attr('value', (price_vege + price_beef + price_cheese + price_extra + price_cake).toFixed(2));
//     }
//     if (($(this).attr("class").split((/\s+/))[0]) == "beeftopps") {
//         alert("beef");
//     }
//     if (($(this).attr("class").split((/\s+/))[0]) == "cheesetopps") {
//         alert("cheese");
//     }
//     if (($(this).attr("class").split((/\s+/))[0]) == "extratopps") {
//         alert("extra");
//     }
// })

// $(document).on('click', "#add_topps > button", function () {
//     $(this).each(function (el) {
//         $(this).on("click", function () {
//             $(this).hide();

//         });
//     })
// })


// // /**
// //  * Created by Jacek on 2016-01-12.
// //  */
// // // document.addEventListener('DOMContentLoaded', function () {
// // var active_forms = document.querySelectorAll('div.show');
// // var zakup = document.querySelectorAll('#zakup');

// // var select = document.querySelector('#rodzaj');

// // // $(document).ready(function () {
// // //     $("div.show").click(function () {
// // //         $("div").hide();
// // //     });
// // // });


// // //Wyłącz wszystkei img
// // active_forms.forEach((el) => {
// //     el.style.display = 'None'
// // });

// // //Włącz pierwszy img dla option domyślnej
// // active_forms[0].style.display = 'block'

// // //zmiana img dla option selected
// // select.addEventListener("change", function () {
// //     var currentOpt = select.options[select.selectedIndex];
// //     value = currentOpt.innerHTML

// //     if (value == 'Telefon zakup') {
// //         zakup.style.display = 'block'
// //     } else {
// //         zakup.style.display = 'none'
// //     };
// // });
// // $("#usluga").show();
// // $("#sprzedaz").hide();
// // $("#zakup").hide();

// // $(function () {
// //     $("#rodzaj").change(function () {
// //         var val = $(this).val();
// //         if (val == 7) {
// //             $("#zakup").show();
// //             $("#usluga").hide();
// //             $("#sprzedaz").hide();
// //         } else if (val == 9) {
// //             $("#sprzedaz").show();
// //             $("#zakup").hide();
// //             $("#usluga").hide();
// //         } else {
// //             $("#usluga").show();
// //             $("#sprzedaz").hide();
// //             $("#zakup").hide();
// //         }
// //     });
// // });

// // });

// $(document).ready(function () {

//     $('#search').keyup(function () {
//         //pole szukaj
//         var text = $(this).val();


//         //na dziendobry ukryj wszystko po nacisnieciu klawisza
//         $('.lista').hide();

//         //lecz nastepnie pokaż pasujące frary
//         $('.lista:contains("' + text + '")').show();

//     });
// });

// $(document).ready(function () {
//     $('#search2').change(function () {
//         //pole szukaj
//         var text = $(this).val();

//         //na dziendobry ukryj wszystko po nacisnieciu klawisza
//         $('.lista').hide();

//         //lecz nastepnie pokaż pasujące frary
//         $('.lista:contains("' + text + '")').show();

//     });

//     var skladniki = $(".skladniki").hide()
//     $('#wielosklad').click(function () {
//         //pole szukaj
//         $('#wielosklad').hide();
//         select = $(".skladniki").show();
//     });

//     $("#zapisz").click(function () {

//         select = $(".skladniki").hide();
//         $('#wielosklad').show();
//     });
// });




// $(document).ready(function () {

//     var wybierz = $('#wybierz').css({
//         "color": "red"
//     });
//     var button = $('#ready_button').hide();

//     $('#wybierz_serwis').change(function () {

//         if ($(this).val() != "") {
//             wybierz.html("OK").css({
//                 "color": "green"
//             });
//             button.show();

//         } else {
//             wybierz.html("Nie wybrano").css({
//                 "color": "red"
//             });
//             button.hide();
//         };
//     });
// });


// $(document).ready(function () {

//     var ilosc = $('#ilosc').css({
//         "color": "red"
//     });
//     var plus = $('#plus');
//     var minus = $('#minus');
//     var i = 0;

//     plus.click(function () {
//         ilosc.val(i);
//         i++;
//     });
//     minus.click(function () {
//         ilosc.val(i);
//         i--;

//     });
// });

// $(function () {
//     $('select').selectpicker();
// });


// $(document).ready(function () {
//     var products = $('button.pizzamenu')
//     var size = $('div.Pizza').hide()
//     var cena = $('span.cena')

//     var menu = $('.menu').click(function () {
//         show_menu = ($(this).attr('class').split(/\s+/))[1];
//         products = $('button.pizzamenu').hide()
//         size = $('div.Pizza').hide()
//         products = ($(this).attr('class').split(/\s+/))[1];
//         $('.' + show_menu).show();
//     });

//     // size.click(function () {
//     //     size = ($(this).attr('class').split(/\s+/))[0];
//     //     $(this).children().removeClass('btn-primary');
//     //     $(this).children().addClass('btn-warning');
//     //     products = $('div.pizzamenu').hide()
//     //     $('.' + size).show();
//     // });
//     var listaMenu = $('.orders')

//     $('button.pizzamenu').each(function () {

//         $(this).on("click", function () {
//             $('button.pizzamenu').removeClass('btn-warning');
//             $(this).addClass('btn-warning');
//             $("#zamowienie ul li:last").append("<li>Hello</li>");
//         });
//     });
//     size.each(function (index) {

//         $(this).on("click", function () {
//             $('div.Pizza').children().removeClass('btn-warning');
//             $(this).children().addClass('btn-warning');
//             console.log(this)
//             size = ($(this).attr('class').split(/\s+/))[0];
//             products = $('button.pizzamenu').hide()
//             $('.' + size).show();
//         });
//     });

// });

// $(document).ready(function () {
//     var topps = $('button.topps')
//     var vegetopps = $('button.vegetopps')
//     var beeftopps = $('button.beeftopps')
//     var cheesetopps = $('button.cheesetopps')
//     var changes = $('span.change')
//     topps.each(function (index) {

//         $(this).on("click", function () {
//             $(this).hide()
//             text = $(this).text()
//             changes = "- " + changes.text(text)
//         });
//     });

//     vegetopps.each(function (index) {

//         $(this).on("click", function () {
//             $(this).hide()
//             text = $(this).text()
//             changes = changes.text(text)
//         });
//     });
//     beeftopps.each(function (index) {

//         $(this).on("click", function () {
//             $(this).hide()
//         });
//     });
//     cheesetopps.each(function (index) {

//         $(this).on("click", function () {
//             $(this).hide()
//         });
//     });
// });