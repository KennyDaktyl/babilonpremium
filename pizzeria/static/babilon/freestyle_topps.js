$(document).ready(function () {
    //Button ze składnikami pizzy stworzonymi przez autora

    var url_adress = window.location.href;
    var vege_ctr = $('#change_vege').data('vegectrl');
    vege_ctr = parseInt(vege_ctr);

    var beef_ctr = $('#change_beef').data('beefctrl');
    beef_ctr = parseInt(beef_ctr);

    var cheese_ctr = $('#change_cheese').data('cheesectrl');
    cheese_ctr = parseInt(cheese_ctr);

    var extra_ctr = $('#change_extra').data('extractrl');
    extra_ctr = parseInt(extra_ctr);

    var extra_1_ctr = $('#change_extra_1').data('extra_1_ctrl');
    extra_1_ctr = parseInt(extra_1_ctr);
    var extra_2_ctr = $('#change_extra_2').data('extra_2_ctrl');
    extra_2_ctr = parseInt(extra_2_ctr);
    var extra_3_ctr = $('#change_extra_3').data('extra_3_ctrl');
    extra_3_ctr = parseInt(extra_3_ctr);
    var extra_4_ctr = $('#change_extra_4').data('extra_4_ctrl');
    extra_4_ctr = parseInt(extra_4_ctr);

    // console.log(vege_ctr, beef_ctr, extra_ctr);

    var topps = $('button.in');
    if (topps.length > 6) {
        console.log(topps[0].data('price'));
    }


    var add_topps = $('#add_topps');
    var changes = 0;
    var ul_del = $('#text_change_topps_del');
    var ul_add = $('#text_change_topps_add');
    var input_del_text = "";
    var input_add_text = "";
    var input_add_cake = "";
    var input_value = $('#input_value');
    var input_add_topps = $('#input_add_topps');
    var input_del_topps = $('#input_del_topps');
    var input_add_cake_text = $('#input_add_cake');
    var add_topps_buttons = $("#add_topps > button");



    var change_vege = $('#change_vege').data('vege_plus');
    var vege_toops_array = [];
    var ctr_vege_array = [];
    var sum_ctr_vege_array = 0;
    var price_vege_toops = ($('#price_size_vege').data('price'));
    price_vege_toops = price_vege_toops.replace(',', ".");
    price_vege_toops = parseFloat(price_vege_toops).toFixed(2);

    var change_beef = $('#change_beef').data('beef_plus');
    var beef_toops_array = [];
    var ctr_beef_array = [];
    var sum_ctr_beef_array = 0;
    var price_beef_toops = ($('#price_size_beef').data('price'));
    price_beef_toops = price_beef_toops.replace(',', ".");
    price_beef_toops = parseFloat(price_beef_toops).toFixed(2);

    var change_cheese = $('#change_cheese').data('cheese_plus');
    var cheese_toops_array = [];
    var ctr_cheese_array = [];
    var sum_ctr_cheese_array = 0;
    var price_cheese_toops = ($('#price_size_cheese').data('price'));
    price_cheese_toops = price_cheese_toops.replace(',', ".");
    price_cheese_toops = parseFloat(price_cheese_toops).toFixed(2);

    var price_extra_toops = ($('#price_size_extra').data('price'));
    price_extra_toops = price_extra_toops.replace(',', ".");
    price_extra_toops = parseFloat(price_extra_toops).toFixed(2);

    var price_extra_1_toops = ($('#price_size_extra_1').data('price'));
    price_extra_1_toops = price_extra_1_toops.replace(',', ".");
    price_extra_1_toops = parseFloat(price_extra_1_toops).toFixed(2);

    var price_extra_2_toops = ($('#price_size_extra_2').data('price'));
    price_extra_2_toops = price_extra_2_toops.replace(',', ".");
    price_extra_2_toops = parseFloat(price_extra_2_toops).toFixed(2);
    var price_extra_3_toops = ($('#price_size_extra_3').data('price'));
    price_extra_3_toops = price_extra_3_toops.replace(',', ".");
    price_extra_3_toops = parseFloat(price_extra_3_toops).toFixed(2);
    var price_extra_4_toops = ($('#price_size_extra_4').data('price'));
    price_extra_4_toops = price_extra_4_toops.replace(',', ".");
    price_extra_4_toops = parseFloat(price_extra_4_toops).toFixed(2);

    var change_extra = $('#change_extra').data('extra_plus');
    var cheese_toops_array = [];
    var ctr_cheese_array = [];
    var sum_ctr_cheese_array = 0;
    var extra_toops_array = [];
    var ctr_extra_array = [];
    var sum_ctr_extra_array = 0;
    var ctr_extra_1_array = [];
    var sum_ctr_extra_1_array = 0;
    var ctr_extra_2_array = [];
    var sum_ctr_extra_2_array = 0;
    var ctr_extra_3_array = [];
    var sum_ctr_extra_3_array = 0;
    var ctr_extra_4_array = [];
    var sum_ctr_extra_4_array = 0;

    var price_extra_toops = ($('#price_size_extra').data('price'));
    price_extra_toops = price_extra_toops.replace(',', ".");
    price_extra_toops = parseFloat(price_extra_toops).toFixed(2);
    var price_vege = 0;
    var price_beef = 0;
    var price_cheese = 0;
    var price_extra = 0;
    var price_cake = 0;
    var price_extra_1 = 0;
    var price_extra_2 = 0;
    var price_extra_3 = 0;
    var price_extra_4 = 0;


    var cheese_toops_array = [];
    var extra_toops_array = [];

    var extra_price_text = $('#extra_price');

    var text_changes = $('#text_change_topps');
    var text = " ";

    var vegetopps = $('button.vegetopps');
    var beeftopps = $('button.beeftopps');
    var cheesetopps = $('button.cheesetopps');
    var extratopps = $('button.extratopps');
    var extra_1_topps = $('button.extra_1_topps');
    var extra_2_topps = $('button.extra_2_topps');
    var extra_3_topps = $('button.extra_3_topps');
    var extra_4_topps = $('button.extra_4_topps');

    var caketopps = $('button.caketopps');
    var change_cake = $('#change_cake');

    var i_vege = $('#change_vege');
    var i_beef = $('#change_beef');
    var i_cheese = $('#change_cheese');
    var i_extra = $('#change_extra');
    var i_cake = $('#change_cake');
    var i_extra_1 = $('#change_extra_1');
    var i_extra_2 = $('#change_extra_2');
    var i_extra_3 = $('#change_extra_3');
    var i_extra_4 = $('#change_extra_4');

    var price_vege_org_array = [];
    var price_beef_org_array = [];
    var price_cheese_org_array = [];
    var price_extra_org_array = [];
    var price_extra_1_org_array = [];
    var price_extra_2_org_array = [];
    var price_extra_3_org_array = [];
    var price_extra_4_org_array = [];
    var price_vege_org_sum = 0;
    var price_this_vege = 0;

    var price_this_cheese_array = [];
    var price_this_cheese_sum = 0;
    var price_this_cheese = 0;

    var price_this_extra_array = [];
    var price_this_extra_sum = 0;
    var price_this_extra = 0;

    var price_this_extra_1_sum = 0;
    var price_this_extra_1 = 0;
    var price_this_extra_2_array = [];
    var price_this_extra_2_sum = 0;
    var price_this_extra_3 = 0;
    var price_this_extra_3_array = [];
    var price_this_extra_4_sum = 0;
    var price_this_extra_4 = 0;
    var price_this_extra_4_array = [];



    var price_this_extra_array = [];
    var price_this_extra_1_array = [];
    var price_this_extra_sum = 0;
    var price_this_extra = 0;
    var price_this_extra_1 = 0;
    var price_this_extra_2 = 0;
    var price_this_extra_3 = 0;
    var price_this_extra_4 = 0;
    var id_this_extra = "";
    var id_this_extra_array = [];


    var topps_in;
    var new_price_topps;

    var sum_free_topps_price = 0;
    var sum_pay_topps_price = 0;
    var price_topp = 0;
    input_value.attr('value', (0.00));
    var sum_free_topps_array = [];
    var sum_pay_topps_array = [];

    function input() {
        var topps_add = $('button.add');
        var text_add_topps123 = "";
        topps_add.each(function (index) {
            text_add_topps123 += "+" + $(this).text() + ", ";
        });
        // console.log(text_add_topps123);
        input_add_topps.attr('value', text_add_topps123);
    }

    function calc_free_topps() {
        topps_free = $('button.in');
        sum_free_topps_array = [];
        if (topps_free.length > 6) {
            topps_free = topps_in.slice(0, 6);
            topps_free.each(function (el) {
                price_topp = $(this).data('price');
                price_topp = parseFloat(price_topp);
                price_topp = price_topp.toFixed(2);
                sum_free_topps_array.push(price_topp);
                sum_free_topps_price = eval(sum_free_topps_array.join("+"));
                sum_free_topps_price = parseFloat(sum_free_topps_price);
                sum_free_topps_price = sum_free_topps_price.toFixed(2);
                console.log(sum_free_topps_price);
            });
        }
        return sum_free_topps_price;
    }


    function calc_topps() {
        topps_in = $('button.in');
        sum_free_topps_array = [];
        sum_pay_topps_array = [];
        input_value.attr('value', (0.00));
        if (topps_in.length < 7) {
            topps_in.each(function (el) {
                $(this).removeClass('btn-danger');
                $(this).addClass('btn-warning');
                price_topp = $(this).data('price');
                price_topp = parseFloat(price_topp);
                price_topp = price_topp.toFixed(2);
                sum_free_topps_array.push(price_topp);
                sum_free_topps_price = eval(sum_free_topps_array.join("+"));
                sum_free_topps_price = parseFloat(sum_free_topps_price);
                sum_free_topps_price = sum_free_topps_price.toFixed(2);
                input_value.attr('value', (0.00));
                extra_price_text = extra_price_text.text(0.00);
                // console.log(sum_free_topps_array);
            });
        }
        if (topps_in.length > 6) {
            topps_in.each(function (el) {
                $(this).removeClass('btn-warning');
                $(this).addClass('btn-warning');
                price_topp = $(this).data('price');
                price_topp = parseFloat(price_topp);
                price_topp = price_topp.toFixed(2);
                // console.log(price_topp);
                sum_pay_topps_array.push(price_topp);
                sum_pay_topps_price = eval(sum_pay_topps_array.join("+"));
                sum_pay_topps_price = parseFloat(sum_pay_topps_price);
                sum_pay_topps_price = sum_pay_topps_price.toFixed(2);

                sum_free_topps_price = calc_free_topps();
                var new_extra_price = sum_pay_topps_price - sum_free_topps_price;
                input_value.attr('value', (new_extra_price));
                extra_price_text = extra_price_text.text(new_extra_price);
            });
        }

        var i = 0;
        topps_in.each(function (el) {
            if (i > 5) {
                $(this).removeClass('btn-warning');
                $(this).addClass('btn-danger');
            } else {
                $(this).removeClass('btn-danger');
                $(this).addClass('btn-warning');
            }
            i++;
        });


        function class_topps() {
            topps_in.each(function (el) {
                $(this).removeClass('btn-danger');
                $(this).addClass('btn-warning');
            });
        }
    }




    vegetopps.each(function (index) {
        $(this).on("click", function () {
            ctr_vege_array.push(1);
            sum_ctr_vege_array = eval(ctr_vege_array.join("+"));
            sum_ctr_vege_array = parseInt(sum_ctr_vege_array);
            i_vege.text(sum_ctr_vege_array);
            var text = $(this).text();
            new_button = $('<button/>', {
                text: text,
                class: 'btn-warning 1 in add m-1',
                'data-price': price_vege_toops,
                click: function () {
                    $(this).remove();
                    calc_topps();
                    $('#text_change_topps_add li:contains(' + $(this).text() + ')').first().remove();
                    ctr_vege_array.push(-1);
                    sum_ctr_vege_array = eval(ctr_vege_array.join("+"));
                    sum_ctr_vege_array = parseInt(sum_ctr_vege_array);
                    i_vege.text(sum_ctr_vege_array);
                    input()
                },
            })
            new_button.appendTo(add_topps);
            calc_topps();
            text_add = "+" + $(this).text() + ", ";
            ul_add.append('<li class="align-top">' + text_add + '</li>');
            input_add_text += text_add
            // input_add_topps.attr('value', input_add_text);
            input()
            calc_free_topps()


        });
    });

    beeftopps.each(function (index) {
        $(this).on("click", function () {

            ctr_beef_array.push(1);
            sum_ctr_beef_array = eval(ctr_beef_array.join("+"));
            sum_ctr_beef_array = parseInt(sum_ctr_beef_array);
            i_beef.text(sum_ctr_beef_array);
            var text = $(this).text();
            new_button = $('<button/>', {
                text: text,
                class: 'btn-warning 2 in add m-1',
                'data-price': price_beef_toops,
                click: function () {
                    $(this).remove();
                    calc_topps();
                    $('#text_change_topps_add li:contains(' + $(this).text() + ')').first().remove();
                    ctr_beef_array.push(-1);
                    sum_ctr_beef_array = eval(ctr_beef_array.join("+"));
                    sum_ctr_beef_array = parseInt(sum_ctr_beef_array);
                    i_beef.text(sum_ctr_beef_array);
                    input();
                },
            })
            new_button.appendTo(add_topps);
            calc_topps();
            text_add = "+" + $(this).text() + ", ";
            ul_add.append('<li>' + text_add + '</li>');
            input_add_text += text_add
            // input_add_topps.attr('value', input_add_text);
            input();
        })
    });
    cheesetopps.each(function (index) {
        $(this).on("click", function () {

            ctr_cheese_array.push(1);
            sum_ctr_cheese_array = eval(ctr_cheese_array.join("+"));
            sum_ctr_cheese_array = parseInt(sum_ctr_cheese_array);
            i_cheese.text(sum_ctr_cheese_array);
            var text = $(this).text();
            new_button = $('<button/>', {
                text: text,
                class: 'btn-warning 3 in add m-1',
                'data-price': price_cheese_toops,
                click: function () {
                    $(this).remove();
                    calc_topps();
                    $('#text_change_topps_add li:contains(' + $(this).text() + ')').first().remove();
                    ctr_cheese_array.push(-1);
                    sum_ctr_cheese_array = eval(ctr_cheese_array.join("+"));
                    sum_ctr_cheese_array = parseInt(sum_ctr_cheese_array);
                    i_cheese.text(sum_ctr_cheese_array);
                    input();
                },
            })
            new_button.appendTo(add_topps);
            calc_topps();
            text_add = "+" + $(this).text() + ", ";
            ul_add.append('<li>' + text_add + '</li>');
            input_add_text += text_add
            // input_add_topps.attr('value', input_add_text);
            input();
        });
    });



    // var url_adress = window.location.href;
    // caketopps.each(function (index) {
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
    //     });
    // });

    extratopps.each(function (index) {
        $(this).on("click", function () {
            price_this_extra = $(this).data('price');
            price_this_extra = price_this_extra.replace(',', ".");
            price_this_extra = parseFloat(price_this_extra).toFixed(2);
            price_this_extra_array.push(price_this_extra);
            price_this_extra_sum = eval(price_this_extra_array.join("+"));
            price_this_extra_sum = parseInt(price_this_extra_sum);
            // console.log(price_this_extra_sum);

            ctr_extra_array.push(1);
            sum_ctr_extra_array = eval(ctr_extra_array.join("+"));
            sum_ctr_extra_array = parseInt(sum_ctr_extra_array);
            i_extra.text(sum_ctr_extra_array);
            var text = $(this).text();
            new_button = $('<button/>', {
                text: text,
                class: 'btn-warning 4 in add m-1',
                'data-price': price_extra_toops,
                click: function () {
                    $(this).remove();
                    calc_topps();
                    $('#text_change_topps_add li:contains(' + $(this).text() + ')').first().remove();
                    ctr_extra_array.push(-1);
                    sum_ctr_extra_array = eval(ctr_extra_array.join("+"));
                    sum_ctr_extra_array = parseInt(sum_ctr_extra_array);
                    i_extra.text(sum_ctr_extra_array);
                    input();
                },
            })
            new_button.appendTo(add_topps);
            calc_topps();
            text_add = "+" + $(this).text() + ", ";
            ul_add.append('<li>' + text_add + '</li>');
            input_add_text += text_add
            input_add_topps.attr('value', input_add_text);
            input();
        })
    });

    extra_1_topps.each(function (index) {
        $(this).on("click", function () {
            price_this_extra_1 = $(this).data('price');
            price_this_extra_1 = price_this_extra_1.replace(',', ".");
            price_this_extra_1 = parseFloat(price_this_extra_1).toFixed(2);
            price_this_extra_1_array.push(price_this_extra_1);
            price_this_extra_1_sum = eval(price_this_extra_1_array.join("+"));
            price_this_extra_1_sum = parseInt(price_this_extra_1_sum);
            // console.log(price_this_extra_sum);

            ctr_extra_1_array.push(1);
            sum_ctr_extra_1_array = eval(ctr_extra_1_array.join("+"));
            sum_ctr_extra_1_array = parseInt(sum_ctr_extra_1_array);
            i_extra_1.text(sum_ctr_extra_1_array);
            var text = $(this).text();
            new_button = $('<button/>', {
                text: text,
                class: 'btn-warning 8 in add m-1',
                'data-price': price_extra_1_toops,
                click: function () {
                    $(this).remove();
                    calc_topps();
                    $('#text_change_topps_add li:contains(' + $(this).text() + ')').first().remove();
                    ctr_extra_1_array.push(-1);
                    sum_ctr_extra_1_array = eval(ctr_extra_1_array.join("+"));
                    sum_ctr_extra_1_array = parseInt(sum_ctr_extra_1_array);
                    i_extra_1.text(sum_ctr_extra_1_array);
                    input();
                },
            })
            new_button.appendTo(add_topps);
            calc_topps();
            text_add = "+" + $(this).text() + ", ";
            ul_add.append('<li>' + text_add + '</li>');
            input_add_text += text_add
            // input_add_topps.attr('value', input_add_text);
            input();
        })
    });
    extra_2_topps.each(function (index) {
        $(this).on("click", function () {
            price_this_extra_2 = $(this).data('price');
            price_this_extra_2 = price_this_extra_2.replace(',', ".");
            price_this_extra_2 = parseFloat(price_this_extra_2).toFixed(2);
            price_this_extra_2_array.push(price_this_extra_2);
            price_this_extra_2_sum = eval(price_this_extra_2_array.join("+"));
            price_this_extra_2_sum = parseInt(price_this_extra_2_sum);
            // console.log(price_this_extra_sum);

            ctr_extra_2_array.push(1);
            sum_ctr_extra_2_array = eval(ctr_extra_2_array.join("+"));
            sum_ctr_extra_2_array = parseInt(sum_ctr_extra_2_array);
            i_extra_2.text(sum_ctr_extra_2_array);
            var text = $(this).text();
            new_button = $('<button/>', {
                text: text,
                class: 'btn-warning 9 in add m-1',
                'data-price': price_extra_2_toops,
                click: function () {
                    $(this).remove();
                    calc_topps();
                    $('#text_change_topps_add li:contains(' + $(this).text() + ')').first().remove();
                    ctr_extra_2_array.push(-1);
                    sum_ctr_extra_2_array = eval(ctr_extra_2_array.join("+"));
                    sum_ctr_extra_2_array = parseInt(sum_ctr_extra_2_array);
                    i_extra_2.text(sum_ctr_extra_2_array);
                    input();
                },
            })
            new_button.appendTo(add_topps);
            calc_topps();
            text_add = "+" + $(this).text() + ", ";
            ul_add.append('<li>' + text_add + '</li>');
            input_add_text += text_add
            // input_add_topps.attr('value', input_add_text);
            input();
        })
    });

    extra_3_topps.each(function (index) {
        $(this).on("click", function () {
            price_this_extra_3 = $(this).data('price');
            price_this_extra_3 = price_this_extra_3.replace(',', ".");
            price_this_extra_3 = parseFloat(price_this_extra_3).toFixed(2);
            price_this_extra_3_array.push(price_this_extra_3);
            price_this_extra_3_sum = eval(price_this_extra_3_array.join("+"));
            price_this_extra_3_sum = parseInt(price_this_extra_3_sum);
            // console.log(price_this_extra_sum);

            ctr_extra_3_array.push(1);
            sum_ctr_extra_3_array = eval(ctr_extra_3_array.join("+"));
            sum_ctr_extra_3_array = parseInt(sum_ctr_extra_3_array);
            i_extra_3.text(sum_ctr_extra_3_array);
            var text = $(this).text();
            new_button = $('<button/>', {
                text: text,
                class: 'btn-warning 10 in add m-1',
                'data-price': price_extra_3_toops,
                click: function () {
                    $(this).remove();
                    calc_topps();
                    $('#text_change_topps_add li:contains(' + $(this).text() + ')').first().remove();
                    ctr_extra_3_array.push(-1);
                    sum_ctr_extra_3_array = eval(ctr_extra_3_array.join("+"));
                    sum_ctr_extra_3_array = parseInt(sum_ctr_extra_3_array);
                    i_extra_3.text(sum_ctr_extra_3_array);
                    input();
                },
            })
            new_button.appendTo(add_topps);
            calc_topps();
            text_add = "+" + $(this).text() + ", ";
            ul_add.append('<li>' + text_add + '</li>');
            input_add_text += text_add
            // input_add_topps.attr('value', input_add_text);
            input();
        })
    });

    extra_4_topps.each(function (index) {
        $(this).on("click", function () {
            price_this_extra_4 = $(this).data('price');
            price_this_extra_4 = price_this_extra_4.replace(',', ".");
            price_this_extra_4 = parseFloat(price_this_extra_4).toFixed(2);
            price_this_extra_4_array.push(price_this_extra_4);
            price_this_extra_4_sum = eval(price_this_extra_4_array.join("+"));
            price_this_extra_4_sum = parseInt(price_this_extra_4_sum);
            // console.log(price_this_extra_sum);

            ctr_extra_4_array.push(1);
            sum_ctr_extra_4_array = eval(ctr_extra_4_array.join("+"));
            sum_ctr_extra_4_array = parseInt(sum_ctr_extra_4_array);
            i_extra_4.text(sum_ctr_extra_4_array);
            var text = $(this).text();
            new_button = $('<button/>', {
                text: text,
                class: 'btn-warning 11 in add m-1',
                'data-price': price_extra_4_toops,
                click: function () {
                    $(this).remove();
                    calc_topps();
                    $('#text_change_topps_add li:contains(' + $(this).text() + ')').first().remove();
                    ctr_extra_4_array.push(-1);
                    sum_ctr_extra_4_array = eval(ctr_extra_4_array.join("+"));
                    sum_ctr_extra_4_array = parseInt(sum_ctr_extra_4_array);
                    i_extra_4.text(sum_ctr_extra_4_array);
                    input();
                },
            })
            new_button.appendTo(add_topps);
            calc_topps();
            console.log('zwrot funkcji' + calc_topps());
            text_add = "+" + $(this).text() + ", ";
            ul_add.append('<li>' + text_add + '</li>');
            input_add_text += text_add
            // input_add_topps.attr('value', input_add_text);
            input();

        })
    });

})