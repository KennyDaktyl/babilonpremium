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

    function calc_topps() {
        topps_in = $('button.in');
        var len_vege_topps = 0;
        var len_beef_topps = 0;
        var len_cheese_topps = 0;
        var len_extra_topps = 0;
        var len_extra_1_topps = 0;
        var len_extra_2_topps = 0;
        var len_extra_3_topps = 0;
        var len_extra_4_topps = 0;
        price_vege_org_array = [];
        price_beef_org_array = [];
        price_cheese_org_array = [];
        price_extra_org_array = [];
        price_extra_1_org_array = [];
        price_extra_2_org_array = [];
        price_extra_3_org_array = [];
        price_extra_4_org_array = [];

        topps_in.each(function (el) {
            if ($(this).hasClass('1') && $(this).hasClass('in')) {
                var price_vege_toops = $(this).data('vege_price');
                price_vege_toops = price_vege_toops.replace(',', ".");
                price_vege_toops = parseFloat(price_vege_toops).toFixed(2);

                price_vege_org_array.push(price_vege_toops);
                price_vege_org_sum = eval(price_vege_org_array.join("+"));
                price_vege_org_sum = parseInt(price_vege_org_sum);

                len_vege_topps = (price_vege_org_array.length);

            }
            if ($(this).hasClass('2') && $(this).hasClass('in')) {
                var price_beef_toops = $(this).data('beef_price');
                price_beef_toops = price_beef_toops.replace(',', ".");
                price_beef_toops = parseFloat(price_beef_toops).toFixed(2);

                price_beef_org_array.push(price_beef_toops);
                price_beef_org_sum = eval(price_beef_org_array.join("+"));
                price_beef_org_sum = parseInt(price_beef_org_sum);

                len_beef_topps = (price_beef_org_array.length);

            }
            if ($(this).hasClass('3') && $(this).hasClass('in')) {
                var price_cheese_toops = $(this).data('cheese_price');
                price_cheese_toops = price_cheese_toops.replace(',', ".");
                price_cheese_toops = parseFloat(price_cheese_toops).toFixed(2);

                price_cheese_org_array.push(price_cheese_toops);
                price_cheese_org_sum = eval(price_cheese_org_array.join("+"));
                price_cheese_org_sum = parseInt(price_cheese_org_sum);

                len_cheese_topps = (price_cheese_org_array.length);

            }
            if ($(this).hasClass('4') && $(this).hasClass('in')) {
                var price_extra_toops = $(this).data('extra_price');
                price_extra_toops = price_extra_toops.replace(',', ".");
                price_extra_toops = parseFloat(price_extra_toops).toFixed(2);

                price_extra_org_array.push(price_extra_toops);
                price_extra_org_sum = eval(price_extra_org_array.join("+"));
                price_extra_org_sum = parseInt(price_extra_org_sum);

                len_extra_topps = (price_extra_org_array.length);

            }
            if ($(this).hasClass('8') && $(this).hasClass('in')) {
                var price_extra_1_toops = $(this).data('extra_1_price');
                price_extra_1_toops = price_extra_1_toops.replace(',', ".");
                price_extra_1_toops = parseFloat(price_extra_1_toops).toFixed(2);
                console.log('to jest cena ' + price_extra_1_toops);
                price_extra_1_org_array.push(price_extra_1_toops);
                price_extra_1_org_sum = eval(price_extra_1_org_array.join("+"));
                price_extra_1_org_sum = parseInt(price_extra_1_org_sum);

                len_extra_1_topps = (price_extra_1_org_array.length);

            }
            if ($(this).hasClass('9') && $(this).hasClass('in')) {
                var price_extra_2_toops = $(this).data('extra_2_price');
                price_extra_2_toops = price_extra_2_toops.replace(',', ".");
                price_extra_2_toops = parseFloat(price_extra_2_toops).toFixed(2);

                price_extra_2_org_array.push(price_extra_2_toops);
                price_extra_2_org_sum = eval(price_extra_2_org_array.join("+"));
                price_extra_2_org_sum = parseInt(price_extra_2_org_sum);

                len_extra_2_topps = (price_extra_2_org_array.length);

            }
            if ($(this).hasClass('10') && $(this).hasClass('in')) {
                var price_extra_3_toops = $(this).data('extra_3_price');
                price_extra_3_toops = price_extra_3_toops.replace(',', ".");
                price_extra_3_toops = parseFloat(price_extra_3_toops).toFixed(2);

                price_extra_3_org_array.push(price_extra_3_toops);
                price_extra_3_org_sum = eval(price_extra_3_org_array.join("+"));
                price_extra_3_org_sum = parseInt(price_extra_3_org_sum);

                len_extra_3_topps = (price_extra_3_org_array.length);

            }
            if ($(this).hasClass('11') && $(this).hasClass('in')) {
                var price_extra_4_toops = $(this).data('extra_4_price');
                price_extra_4_toops = price_extra_4_toops.replace(',', ".");
                price_extra_toops = parseFloat(price_extra_toops).toFixed(2);

                price_extra_4_org_array.push(price_extra_4_toops);
                price_extra_4_org_sum = eval(price_extra_4_org_array.join("+"));
                price_extra_4_org_sum = parseInt(price_extra_4_org_sum);

                len_extra_4_topps = (price_extra_4_org_array.length);

            }
            return (len_vege_topps, len_beef_topps, len_extra_topps, len_extra_1_topps, len_extra_2_topps, len_extra_3_topps, len_extra_4_topps)
        });
        var counter_change_v = len_vege_topps - vege_ctr;
        var counter_change_b = len_beef_topps - beef_ctr;
        var counter_change_ch = len_cheese_topps - cheese_ctr;
        console.log('len_cheese_topps: ' + len_cheese_topps);
        console.log('cheese_ctr: ' + cheese_ctr);
        var counter_change_ex = len_extra_topps - extra_ctr;
        var counter_change_ex1 = len_extra_1_topps - extra_1_ctr;
        var counter_change_ex2 = len_extra_2_topps - extra_2_ctr;
        var counter_change_ex3 = len_extra_3_topps - extra_3_ctr;
        var counter_change_ex4 = len_extra_4_topps - extra_4_ctr;
        console.log(counter_change_v);
        console.log(counter_change_b);
        console.log(counter_change_ch);
        console.log(counter_change_ex);
        console.log(counter_change_ex1);
        console.log(counter_change_ex2);
        console.log(counter_change_ex3);
        console.log(counter_change_ex4);
        console.log(price_extra_1_toops);
        price_vege = ((len_vege_topps - vege_ctr) * price_vege_toops);
        price_beef = ((len_beef_topps - beef_ctr) * price_beef_toops);
        price_cheese = ((len_cheese_topps - cheese_ctr) * price_cheese_toops);
        price_extra = ((len_extra_topps - extra_ctr) * price_extra_toops);
        price_extra_1 = ((len_extra_1_topps - extra_1_ctr) * price_extra_1_toops);
        price_extra_2 = ((len_extra_2_topps - extra_2_ctr) * price_extra_2_toops);
        price_extra_3 = ((len_extra_3_topps - extra_3_ctr) * price_extra_3_toops);
        price_extra_4 = ((len_extra_4_topps - extra_4_ctr) * price_extra_4_toops);
        if (price_vege < 0) {
            price_vege = 0;
        }
        if (price_beef < 0) {
            price_beef = 0;
        }
        if (price_cheese < 0) {
            price_cheese = 0;
        }
        if (price_extra < 0) {
            price_extra = 0;
        }
        if (price_extra_1 < 0) {
            price_extra_1 = 0;
        }
        if (price_extra_2 < 0) {
            price_extra_2 = 0;
        }
        if (price_extra_3 < 0) {
            price_extra_3 = 0;
        }
        if (price_extra_4 < 0) {
            price_extra_4 = 0;
        }


        function counter_v() {
            var count = 0;
            if (counter_change_ex4 < 0) {
                count += counter_change_ex4;
            } else {
                count += counter_change_ex4;
            }

            if (counter_change_ex3 < 0) {
                count += counter_change_ex3;
            } else {
                count += counter_change_ex3;
            }

            if (counter_change_ex2 < 0) {
                count += counter_change_ex2;
            } else {
                count += counter_change_ex2;
            }

            if (counter_change_ex1 < 0) {
                count += counter_change_ex1;
            } else {
                count += counter_change_ex1;
            }

            if (counter_change_ex < 0) {
                count += counter_change_ex;
            } else {
                count += counter_change_ex;
            }
            if (counter_change_ch < 0) {
                count += counter_change_ch;
            } else {
                count += counter_change_ch;
            }

            if (counter_change_b < 0) {
                count += counter_change_b;
            } else {
                count += counter_change_b;
            }


            return count;
        }

        function counter_b() {
            var count = 0;
            if (counter_change_ex4 < 0) {
                count += counter_change_ex4;
            } else {
                count += counter_change_ex4;
            }

            if (counter_change_ex3 < 0) {
                count += counter_change_ex3;
            } else {
                count += counter_change_ex3;
            }

            if (counter_change_ex2 < 0) {
                count += counter_change_ex2;
            } else {
                count += counter_change_ex2;
            }

            if (counter_change_ex1 < 0) {
                count += counter_change_ex1;
            } else {
                count += counter_change_ex1;
            }

            if (counter_change_ex < 0) {
                count += counter_change_ex;
            } else {
                count += counter_change_ex;
            }

            if (counter_change_ch < 0) {
                count += counter_change_ch;
            } else {
                count += counter_change_ch;
            }
            return count;
        }

        function counter_ch() {
            var count = 0;
            if (counter_change_ex4 < 0) {
                count += counter_change_ex4;
            } else {
                count += counter_change_ex4;
            }

            if (counter_change_ex3 < 0) {
                count += counter_change_ex3;
            } else {
                count += counter_change_ex3;
            }

            if (counter_change_ex2 < 0) {
                count += counter_change_ex2;
            } else {
                count += counter_change_ex2;
            }

            if (counter_change_ex1 < 0) {
                count += counter_change_ex1;
            } else {
                count += counter_change_ex1;
            }

            if (counter_change_ex < 0) {
                count += counter_change_ex;
            } else {
                count += counter_change_ex;
            }
            return count;
        }

        function counter_ex() {
            var count = 0;
            if (counter_change_ex4 < 0) {
                count += counter_change_ex4;
            } else {
                count += counter_change_ex4;
            }

            if (counter_change_ex3 < 0) {
                count += counter_change_ex3;
            } else {
                count += counter_change_ex3;
            }

            if (counter_change_ex2 < 0) {
                count += counter_change_ex2;
            } else {
                count += counter_change_ex2;
            }

            if (counter_change_ex1 < 0) {
                count += counter_change_ex1;
            } else {
                count += counter_change_ex1;
            }
            return count;
        }



        function counter_ex1() {
            var count = 0;
            if (counter_change_ex4 < 0) {
                count += counter_change_ex4;
            } else {
                count += counter_change_ex4;
            }

            if (counter_change_ex3 < 0) {
                count += counter_change_ex3;
            } else {
                count += counter_change_ex3;
            }

            if (counter_change_ex2 < 0) {
                count += counter_change_ex2;
            } else {
                count += counter_change_ex2;
            }

            return count;
        }

        function counter_ex2() {
            var count = 0;
            if (counter_change_ex4 < 0) {
                count += counter_change_ex4;
            } else {
                count += counter_change_ex4;
            }

            if (counter_change_ex3 < 0) {
                count += counter_change_ex3;
            } else {
                count += counter_change_ex3;
            }
            return count;
        }

        function counter_ex3() {
            var count = 0;
            if (counter_change_ex4 < 0) {
                count += counter_change_ex4;
            } else {
                count += counter_change_ex4;
            }
            return count;
        }


        count_ex3 = counter_ex3();
        if (count_ex3 < 0) {
            price_extra_3 = ((counter_change_ex3 + count_ex3) * price_extra_3_toops);
        }

        console.log('cena extra_3 = ' + price_extra_3);

        count_ex2 = counter_ex2();
        if (count_ex2 < 0) {
            price_extra_2 = ((counter_change_ex2 + count_ex2) * price_extra_2_toops);
        }
        console.log('cena extra_2 = ' + price_extra_2);

        count_ex1 = counter_ex1();
        if (count_ex1 < 0) {
            price_extra_1 = ((counter_change_ex1 + count_ex1) * price_extra_1_toops);
        }

        console.log('cena extra_1 = ' + price_extra_1);


        count_ex = counter_ex();
        if (count_ex < 0) {
            price_extra = ((counter_change_ex + count_ex) * price_extra_toops);
        }

        console.log('cena extra = ' + price_extra);

        count_ch = counter_ch();
        if (count_ch < 0) {
            price_cheese = ((counter_change_ch + count_ch) * price_cheese_toops);
        }

        console.log('cena cheese = ' + price_cheese);


        count_b = counter_b();
        if (count_b < 0) {
            price_beef = ((counter_change_b + count_b) * price_beef_toops);
        }

        console.log('cena beef = ' + price_beef);


        count_v = counter_v();
        if (count_v < 0) {

            price_vege = ((counter_change_v + count_v) * price_vege_toops);

        }
        console.log('cena vege = ' + price_vege);


        if (price_vege < 0) {
            price_vege = 0;
        }
        if (price_beef < 0) {
            price_beef = 0;
        }
        if (price_cheese < 0) {
            price_cheese = 0;
        }
        if (price_extra < 0) {
            price_extra = 0;
        }
        if (price_extra_1 < 0) {
            price_extra_1 = 0;
        }
        if (price_extra_2 < 0) {
            price_extra_2 = 0;
        }
        if (price_extra_3 < 0) {
            price_extra_3 = 0;
        }
        if (price_extra_4 < 0) {
            price_extra_4 = 0;
        }
        var new_price_topps = (price_vege + price_beef + price_cheese + price_extra + price_extra_1 + price_extra_2 + price_extra_3 + price_extra_4);
        extra_price_text = extra_price_text.text(new_price_topps);
        input_value.attr('value', (new_price_topps).toFixed(2));
        console.log("Cena extra dodatków: " + (price_vege + price_beef + price_cheese + price_extra + price_extra_1 + price_extra_2 + price_extra_3 + price_extra_4));
    }




    topps.each(function (el) {
        if (($(this).attr("class").split((/\s+/))[0]) == 1) {



            vege_toops_array.push(1);
            $(this).on("click", function () {

                if ($(this).hasClass("btn-danger")) {
                    $(this).removeClass("btn-danger");
                    $(this).addClass("btn-secondary");
                    $(this).removeClass("in");
                    calc_topps();

                    ctr_vege_array.push(-1);
                    sum_ctr_vege_array = eval(ctr_vege_array.join("+"));
                    sum_ctr_vege_array = parseInt(sum_ctr_vege_array);
                    i_vege.text(sum_ctr_vege_array);
                    text_del = "-" + $(this).text() + ", ";
                    ul_del.append('<li>' + text_del + '</li>');
                    input_del_text += text_del
                    input_del_topps.attr('value', input_del_text);
                    // extra_price_function(sum_ctr_beef_array, sum_ctr_extra_array, sum_ctr_beef_array, sum_ctr_extra_array, price_vege, sum_ctr_vege_array, price_vege_toops, input_value);

                } else {
                    $(this).addClass("in");
                    calc_topps();
                    $(this).removeClass("btn-secondary");
                    $(this).addClass("btn-danger");
                    ctr_vege_array.push(1);
                    sum_ctr_vege_array = eval(ctr_vege_array.join("+"));
                    sum_ctr_vege_array = parseInt(sum_ctr_vege_array);
                    i_vege.text(sum_ctr_vege_array);
                    $('#text_change_topps_del li:contains(' + $(this).text() + ')').remove();
                    text_del = "-" + $(this).text() + ", ";
                    input_del_text = input_del_text.replace(text_del, "");
                    input_del_topps.attr('value', input_del_text);
                    // extra_price_function(sum_ctr_beef_array, sum_ctr_extra_array, sum_ctr_beef_array, sum_ctr_extra_array, price_vege, sum_ctr_vege_array, price_vege_toops, input_value)
                }
            });
        }

        if (($(this).attr("class").split((/\s+/))[0]) == 2) {
            beef_toops_array.push(1);
            $(this).on("click", function () {
                if ($(this).hasClass("btn-danger")) {
                    $(this).removeClass("in");
                    calc_topps();


                    changes -= 1;
                    $(this).removeClass("btn-danger");
                    $(this).addClass("btn-secondary");
                    ctr_beef_array.push(-1);
                    sum_ctr_beef_array = eval(ctr_beef_array.join("+"));
                    sum_ctr_beef_array = parseInt(sum_ctr_beef_array);
                    i_beef.text(sum_ctr_beef_array);
                    text_del = "-" + $(this).text() + ", ";
                    ul_del.append('<li>' + text_del + '</li>');
                    input_del_text += text_del
                    input_del_topps.attr('value', input_del_text);
                    // extra_price_function(sum_ctr_beef_array, sum_ctr_extra_array, sum_ctr_beef_array, sum_ctr_extra_array, price_vege, sum_ctr_vege_array, price_vege_toops, input_value)

                } else {
                    $(this).addClass("in");
                    calc_topps();
                    changes += 1;
                    $(this).removeClass("btn-secondary");
                    $(this).addClass("btn-danger");
                    ctr_beef_array.push(1);
                    sum_ctr_beef_array = eval(ctr_beef_array.join("+"));
                    sum_ctr_beef_array = parseInt(sum_ctr_beef_array);
                    i_beef.text(sum_ctr_beef_array);
                    $('#text_change_topps_del li:contains(' + $(this).text() + ')').remove();
                    text_del = "-" + $(this).text() + ", ";
                    input_del_text = input_del_text.replace(text_del, "");
                    input_del_topps.attr('value', input_del_text);
                    // extra_price_function(sum_ctr_beef_array, sum_ctr_extra_array, sum_ctr_beef_array, sum_ctr_extra_array, price_vege, sum_ctr_vege_array, price_vege_toops, input_value)
                }
            });
        }
        if (($(this).attr("class").split((/\s+/))[0]) == 3) {
            cheese_toops_array.push(1);
            $(this).on("click", function () {

                if ($(this).hasClass("btn-danger")) {
                    $(this).removeClass("in");
                    calc_topps();

                    changes -= 1;
                    $(this).removeClass("btn-danger");
                    $(this).addClass("btn-secondary");
                    ctr_cheese_array.push(-1);
                    sum_ctr_cheese_array = eval(ctr_cheese_array.join("+"));
                    sum_ctr_cheese_array = parseInt(sum_ctr_cheese_array);
                    i_cheese.text(sum_ctr_cheese_array);
                    // price_cheese = sum_ctr_cheese_array * price_cheese_toops;
                    text_del = "-" + $(this).text() + ", ";
                    ul_del.append('<li>' + text_del + '</li>');
                    input_del_text += text_del
                    input_del_topps.attr('value', input_del_text);
                } else {
                    $(this).addClass("in");
                    calc_topps();

                    changes += 1;
                    $(this).removeClass("btn-secondary");
                    $(this).addClass("btn-danger");
                    ctr_cheese_array.push(1);
                    // price_cheese = sum_ctr_cheese_array * price_cheese_toops;
                    $('#text_change_topps_del li:contains(' + $(this).text() + ')').remove();
                    text_del = "-" + $(this).text() + ", ";
                    input_del_text = input_del_text.replace(text_del, "");
                    input_del_topps.attr('value', input_del_text);
                }
            })
        }

        if (($(this).attr("class").split((/\s+/))[0]) == 4) {
            extra_toops_array.push(1);
            $(this).on("click", function () {
                if ($(this).hasClass("btn-danger")) {
                    $(this).removeClass("in");
                    calc_topps();


                    price_this_extra = $(this).data('extra_price');
                    price_this_extra = price_this_extra.replace(',', ".");
                    price_this_extra = parseFloat(price_this_extra).toFixed(2);
                    price_this_extra_array.push(-price_this_extra);
                    price_this_extra_sum = eval(price_this_extra_array.join("+"));
                    price_this_extra_sum = parseInt(price_this_extra_sum);
                    id_this_extra = $(this).data('id');
                    id_this_extra_array.push(id_this_extra);
                    changes -= 1;
                    $(this).removeClass("btn-danger");
                    $(this).addClass("btn-secondary");
                    ctr_extra_array.push(-1);
                    sum_ctr_extra_array = eval(ctr_extra_array.join("+"));
                    sum_ctr_extra_array = parseInt(sum_ctr_extra_array);
                    i_extra.text(sum_ctr_extra_array);
                    text_del = "-" + $(this).text() + ", ";
                    ul_del.append('<li>' + text_del + '</li>');
                    input_del_text += text_del
                    input_del_topps.attr('value', input_del_text);
                } else {
                    $(this).addClass("in");
                    calc_topps();

                    changes += 1;
                    $(this).removeClass("btn-secondary");
                    $(this).addClass("btn-danger");
                    ctr_extra_array.push(1);
                    sum_ctr_extra_array = eval(ctr_extra_array.join("+"));
                    sum_ctr_extra_array = parseInt(sum_ctr_extra_array);
                    i_extra.text(sum_ctr_extra_array);
                    $('#text_change_topps_del li:contains(' + $(this).text() + ')').remove();
                    text_del = "-" + $(this).text() + ", ";
                    input_del_text = input_del_text.replace(text_del, "");
                    input_del_topps.attr('value', input_del_text);
                }
            });
        }
        if (($(this).attr("class").split((/\s+/))[0]) == 8) {
            $(this).on("click", function () {
                if ($(this).hasClass("btn-danger")) {
                    $(this).removeClass("in");
                    calc_topps();
                    $(this).removeClass("btn-danger");
                    $(this).addClass("btn-secondary");
                    text_del = "-" + $(this).text() + ", ";
                    ul_del.append('<li>' + text_del + '</li>');
                    input_del_text += text_del
                    input_del_topps.attr('value', input_del_text);
                    ctr_extra_1_array.push(-1);
                    sum_ctr_extra_1_array = eval(ctr_extra_1_array.join("+"));
                    sum_ctr_extra_1_array = parseInt(sum_ctr_extra_1_array);
                    i_extra_1.text(sum_ctr_extra_1_array);

                } else {
                    $(this).addClass("in");
                    calc_topps();
                    $(this).removeClass("btn-secondary");
                    $(this).addClass("btn-danger");
                    $('#text_change_topps_del li:contains(' + $(this).text() + ')').remove();
                    text_del = "-" + $(this).text() + ", ";
                    input_del_text = input_del_text.replace(text_del, "");
                    input_del_topps.attr('value', input_del_text);
                    ctr_extra_1_array.push(1);
                    sum_ctr_extra_1_array = eval(ctr_extra_1_array.join("+"));
                    sum_ctr_extra_1_array = parseInt(sum_ctr_extra_1_array);
                    i_extra_1.text(sum_ctr_extra_1_array);
                }
            });
        }
        if (($(this).attr("class").split((/\s+/))[0]) == 9) {
            $(this).on("click", function () {
                if ($(this).hasClass("btn-danger")) {
                    $(this).removeClass("in");
                    calc_topps();
                    $(this).removeClass("btn-danger");
                    $(this).addClass("btn-secondary");
                    text_del = "-" + $(this).text() + ", ";
                    ul_del.append('<li>' + text_del + '</li>');
                    input_del_text += text_del
                    input_del_topps.attr('value', input_del_text);
                    ctr_extra_2_array.push(-1);
                    sum_ctr_extra_2_array = eval(ctr_extra_2_array.join("+"));
                    sum_ctr_extra_2_array = parseInt(sum_ctr_extra_2_array);
                    i_extra_2.text(sum_ctr_extra_2_array);

                } else {
                    $(this).addClass("in");
                    calc_topps();
                    $(this).removeClass("btn-secondary");
                    $(this).addClass("btn-danger");
                    $('#text_change_topps_del li:contains(' + $(this).text() + ')').remove();
                    text_del = "-" + $(this).text() + ", ";
                    input_del_text = input_del_text.replace(text_del, "");
                    input_del_topps.attr('value', input_del_text);
                    ctr_extra_2_array.push(1);
                    sum_ctr_extra_2_array = eval(ctr_extra_2_array.join("+"));
                    sum_ctr_extra_2_array = parseInt(sum_ctr_extra_2_array);
                    i_extra_2.text(sum_ctr_extra_2_array);
                }
            });
        }
        if (($(this).attr("class").split((/\s+/))[0]) == 10) {
            $(this).on("click", function () {
                if ($(this).hasClass("btn-danger")) {
                    $(this).removeClass("in");
                    calc_topps();
                    $(this).removeClass("btn-danger");
                    $(this).addClass("btn-secondary");
                    text_del = "-" + $(this).text() + ", ";
                    ul_del.append('<li>' + text_del + '</li>');
                    input_del_text += text_del
                    input_del_topps.attr('value', input_del_text);
                    ctr_extra_3_array.push(-1);
                    sum_ctr_extra_3_array = eval(ctr_extra_3_array.join("+"));
                    sum_ctr_extra_3_array = parseInt(sum_ctr_extra_3_array);
                    i_extra_3.text(sum_ctr_extra_3_array);

                } else {
                    $(this).addClass("in");
                    calc_topps();
                    $(this).removeClass("btn-secondary");
                    $(this).addClass("btn-danger");
                    $('#text_change_topps_del li:contains(' + $(this).text() + ')').remove();
                    text_del = "-" + $(this).text() + ", ";
                    input_del_text = input_del_text.replace(text_del, "");
                    input_del_topps.attr('value', input_del_text);
                    ctr_extra_3_array.push(1);
                    sum_ctr_extra_3_array = eval(ctr_extra_3_array.join("+"));
                    sum_ctr_extra_3_array = parseInt(sum_ctr_extra_3_array);
                    i_extra_3.text(sum_ctr_extra_3_array);
                }
            });
        }
        if (($(this).attr("class").split((/\s+/))[0]) == 11) {
            $(this).on("click", function () {
                if ($(this).hasClass("btn-danger")) {
                    $(this).removeClass("in");
                    calc_topps();
                    $(this).removeClass("btn-danger");
                    $(this).addClass("btn-secondary");
                    text_del = "-" + $(this).text() + ", ";
                    ul_del.append('<li>' + text_del + '</li>');
                    input_del_text += text_del
                    input_del_topps.attr('value', input_del_text);
                    ctr_extra_4_array.push(-1);
                    sum_ctr_extra_4_array = eval(ctr_extra_4_array.join("+"));
                    sum_ctr_extra_4_array = parseInt(sum_ctr_extra_4_array);
                    i_extra_4.text(sum_ctr_extra_4_array);

                } else {
                    $(this).addClass("in");
                    calc_topps();
                    $(this).removeClass("btn-secondary");
                    $(this).addClass("btn-danger");
                    $('#text_change_topps_del li:contains(' + $(this).text() + ')').remove();
                    text_del = "-" + $(this).text() + ", ";
                    input_del_text = input_del_text.replace(text_del, "");
                    input_del_topps.attr('value', input_del_text);
                    ctr_extra_4_array.push(1);
                    sum_ctr_extra_4_array = eval(ctr_extra_4_array.join("+"));
                    sum_ctr_extra_4_array = parseInt(sum_ctr_extra_4_array);
                    i_extra_4.text(sum_ctr_extra_4_array);
                }
            });
        }


    });

    function input() {
        var topps_add = $('button.add');
        var text_add_topps123 = "";
        topps_add.each(function (index) {
            text_add_topps123 += "+" + $(this).text() + ", ";
        });
        // console.log(text_add_topps123);
        input_add_topps.attr('value', text_add_topps123);
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
                'data-vege_price': price_vege_toops,
                click: function () {
                    $(this).remove();
                    calc_topps();
                    $('#text_change_topps_add li:contains(' + $(this).text() + ')').first().remove();
                    ctr_vege_array.push(-1);
                    sum_ctr_vege_array = eval(ctr_vege_array.join("+"));
                    sum_ctr_vege_array = parseInt(sum_ctr_vege_array);
                    i_vege.text(sum_ctr_vege_array);
                    console.log('funckja');
                    input();
                    console.log('funckja koniec')
                },
            })
            new_button.appendTo(add_topps);
            calc_topps();
            text_add = "+" + $(this).text() + ", ";
            ul_add.append('<li class="align-top">' + text_add + '</li>');
            input_add_text += text_add
            // input_add_topps.attr('value', input_add_text);
            input();



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
                'data-beef_price': price_beef_toops,
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
                'data-cheese_price': price_cheese_toops,
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
                'data-extra_price': price_extra_toops,
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
            // input_add_topps.attr('value', input_add_text);
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
                'data-extra_1_price': price_extra_1_toops,
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
                'data-extra_2_price': price_extra_2_toops,
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
                'data-extra_3_price': price_extra_3_toops,
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
                'data-extra_4_price': price_extra_4_toops,
                click: function () {
                    $(this).remove();
                    calc_topps();
                    $('#text_change_topps_add li:contains(' + $(this).text() + ')').first().remove();
                    ctr_extra_4_array.push(-1);
                    sum_ctr_extra_4_array = eval(ctr_extra_4_array.join("+"));
                    sum_ctr_extra_4_array = parseInt(sum_ctr_extra_4_array);
                    i_extra_4.text(sum_ctr_extra_4_array);
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