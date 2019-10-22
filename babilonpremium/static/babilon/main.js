$(document).ready(function () {
    //Button ze składnikami pizzy stworzonymi przez autora
    var topps = $('button.topps');
    var add_topps = $('#add_topps');
    var changes = 0;


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

    var change_extra = $('#change_extra').data('extra_plus');
    var extra_toops_array = [];
    var ctr_extra_array = [];
    var sum_ctr_extra_array = 0;
    var price_extra_toops = ($('#price_size_extra').data('price'));
    price_extra_toops = price_extra_toops.replace(',', ".");
    price_extra_toops = parseFloat(price_extra_toops).toFixed(2);
    var price_vege = 0;
    var price_beef = 0;
    var price_cheese = 0;
    var price_extra = 0;
    var price = 0;


    var cheese_toops_array = [];
    var extra_toops_array = [];

    var extra_price_text = $('#extra_price');

    var text_changes = $('#text_change_topps');
    var text = " ";

    var vegetopps = $('button.vegetopps');
    var beeftopps = $('button.beeftopps');
    var extratopps = $('button.extratopps');

    var i_vege = $('#change_vege');
    var i_beef = $('#change_beef');
    var i_cheese = $('#change_cheese');
    var i_extra = $('#change_extra');
    var i_cake = $('#change_cake');

    topps.each(function (el) {
        if (($(this).attr("class").split((/\s+/))[0]) == 1) {
            vege_toops_array.push(1);
            $(this).on("click", function () {
                if ($(this).hasClass("btn-danger")) {
                    $(this).removeClass("btn-danger");
                    $(this).addClass("btn-secondary");
                    ctr_vege_array.push(-1);
                    sum_ctr_vege_array = eval(ctr_vege_array.join("+"));
                    sum_ctr_vege_array = parseInt(sum_ctr_vege_array);
                    i_vege.text(sum_ctr_vege_array);
                    if ((sum_ctr_beef_array < 0) && (sum_ctr_extra_array < 0)) {
                        price_vege = (sum_ctr_vege_array + (sum_ctr_beef_array + sum_ctr_extra_array)) * price_vege_toops;
                        if ((price_vege) < 0) {
                            price_vege = 0;
                        }
                        extra_price_text = extra_price_text.text(price_vege + price_beef + price_extra);
                    }
                    if ((sum_ctr_beef_array == 0) && (sum_ctr_extra_array < 0)) {
                        price_vege = (sum_ctr_vege_array + (sum_ctr_extra_array)) * price_vege_toops;
                        if ((price_vege) < 0) {
                            price_vege = 0;
                        }
                        extra_price_text = extra_price_text.text(price_vege + price_beef + price_extra);
                    }
                    if ((sum_ctr_beef_array > 0) && (sum_ctr_extra_array == 0)) {
                        price_vege = (sum_ctr_vege_array * price_vege_toops);
                        if ((price_vege) < 0) {
                            price_vege = 0;
                        }
                        extra_price_text = extra_price_text.text(price_vege + price_beef + price_extra);
                    }

                    if ((sum_ctr_beef_array < 0) && (sum_ctr_extra_array == 0)) {
                        price_vege = ((sum_ctr_vege_array + sum_ctr_beef_array) * price_vege_toops);
                        if ((price_vege) < 0) {
                            price_vege = 0;
                        }
                        extra_price_text = extra_price_text.text(price_vege + price_beef + price_extra);
                    }
                    if ((sum_ctr_beef_array > 0) && (sum_ctr_extra_array > 0)) {
                        price_vege = (sum_ctr_vege_array * price_vege_toops);
                        if ((price_vege) < 0) {
                            price_vege = 0;
                        }
                        extra_price_text = extra_price_text.text(price_vege + price_beef + price_extra);
                    }
                    if ((sum_ctr_beef_array == 0) && (sum_ctr_extra_array == 0)) {
                        price_vege = sum_ctr_vege_array * price_vege_toops;
                        if ((price_vege) < 0) {
                            price_vege = 0;
                        }
                        extra_price_text = extra_price_text.text(price_vege + price_beef + price_extra);
                    }
                    if ((sum_ctr_beef_array == 0) && (sum_ctr_extra_array > 0)) {
                        price_vege = sum_ctr_vege_array * price_vege_toops;
                        if ((price_vege) < 0) {
                            price_vege = 0;
                        }
                        extra_price_text = extra_price_text.text(price_vege + price_beef + price_extra);
                    }



                    if (sum_ctr_extra_array < 0) {
                        price_beef = (sum_ctr_beef_array + sum_ctr_extra_array) * price_beef_toops;
                        if ((price_beef) < 0) {
                            price_beef = 0;
                        }

                        extra_price_text = extra_price_text.text(price_vege + price_beef + price_extra);
                    }
                    if (sum_ctr_extra_array == 0) {
                        price_beef = sum_ctr_beef_array * price_beef_toops;
                        if ((price_beef) < 0) {
                            price_beef = 0;
                        }
                        extra_price_text = extra_price_text.text(price_vege + price_beef + price_extra);
                    }
                    if (sum_ctr_extra_array > 0) {
                        price_beef = sum_ctr_beef_array * price_beef_toops;
                        if ((price_beef) < 0) {
                            price_beef = 0;
                        }
                        extra_price_text = extra_price_text.text(price_vege + price_beef + price_extra);
                    }
                    if (sum_ctr_extra_array > 0) {
                        price_extra = sum_ctr_extra_array * price_extra_toops;

                        extra_price_text = extra_price_text.text(price_vege + price_beef + price_extra);
                    }
                    if (sum_ctr_extra_array == 0) {
                        price_extra = 0;

                        extra_price_text = extra_price_text.text(price_vege + price_beef + price_extra);
                    }

                } else {
                    $(this).removeClass("btn-secondary");
                    $(this).addClass("btn-danger");
                    ctr_vege_array.push(1);
                    sum_ctr_vege_array = eval(ctr_vege_array.join("+"));
                    sum_ctr_vege_array = parseInt(sum_ctr_vege_array);
                    i_vege.text(sum_ctr_vege_array);
                    if ((sum_ctr_beef_array < 0) && (sum_ctr_extra_array < 0)) {
                        price_vege = (sum_ctr_vege_array + (sum_ctr_beef_array + sum_ctr_extra_array)) * price_vege_toops;
                        if ((price_vege) < 0) {
                            price_vege = 0;
                        }
                        extra_price_text = extra_price_text.text(price_vege + price_beef + price_extra);
                    }
                    if ((sum_ctr_beef_array == 0) && (sum_ctr_extra_array < 0)) {
                        price_vege = (sum_ctr_vege_array + (sum_ctr_extra_array)) * price_vege_toops;
                        if ((price_vege) < 0) {
                            price_vege = 0;
                        }
                        extra_price_text = extra_price_text.text(price_vege + price_beef + price_extra);
                    }
                    if ((sum_ctr_beef_array > 0) && (sum_ctr_extra_array == 0)) {
                        price_vege = (sum_ctr_vege_array * price_vege_toops);
                        if ((price_vege) < 0) {
                            price_vege = 0;
                        }
                        extra_price_text = extra_price_text.text(price_vege + price_beef + price_extra);
                    }

                    if ((sum_ctr_beef_array < 0) && (sum_ctr_extra_array == 0)) {
                        price_vege = ((sum_ctr_vege_array + sum_ctr_beef_array) * price_vege_toops);
                        if ((price_vege) < 0) {
                            price_vege = 0;
                        }
                        extra_price_text = extra_price_text.text(price_vege + price_beef + price_extra);
                    }
                    if ((sum_ctr_beef_array > 0) && (sum_ctr_extra_array > 0)) {
                        price_vege = (sum_ctr_vege_array * price_vege_toops);
                        if ((price_vege) < 0) {
                            price_vege = 0;
                        }
                        extra_price_text = extra_price_text.text(price_vege + price_beef + price_extra);
                    }
                    if ((sum_ctr_beef_array == 0) && (sum_ctr_extra_array == 0)) {
                        price_vege = sum_ctr_vege_array * price_vege_toops;
                        if ((price_vege) < 0) {
                            price_vege = 0;
                        }
                        extra_price_text = extra_price_text.text(price_vege + price_beef + price_extra);
                    }
                    if ((sum_ctr_beef_array == 0) && (sum_ctr_extra_array > 0)) {
                        price_vege = sum_ctr_vege_array * price_vege_toops;
                        if ((price_vege) < 0) {
                            price_vege = 0;
                        }
                        extra_price_text = extra_price_text.text(price_vege + price_beef + price_extra);
                    }



                    if (sum_ctr_extra_array < 0) {
                        price_beef = (sum_ctr_beef_array + sum_ctr_extra_array) * price_beef_toops;
                        if ((price_beef) < 0) {
                            price_beef = 0;
                        }

                        extra_price_text = extra_price_text.text(price_vege + price_beef + price_extra);
                    }
                    if (sum_ctr_extra_array == 0) {
                        price_beef = sum_ctr_beef_array * price_beef_toops;
                        if ((price_beef) < 0) {
                            price_beef = 0;
                        }
                        extra_price_text = extra_price_text.text(price_vege + price_beef + price_extra);
                    }
                    if (sum_ctr_extra_array > 0) {
                        price_beef = sum_ctr_beef_array * price_beef_toops;
                        if ((price_beef) < 0) {
                            price_beef = 0;
                        }
                        extra_price_text = extra_price_text.text(price_vege + price_beef + price_extra);
                    }
                    if (sum_ctr_extra_array > 0) {
                        price_extra = sum_ctr_extra_array * price_extra_toops;

                        extra_price_text = extra_price_text.text(price_vege + price_beef + price_extra);
                    }
                    if (sum_ctr_extra_array == 0) {
                        price_extra = 0;

                        extra_price_text = extra_price_text.text(price_vege + price_beef + price_extra);
                    }

                }
            });
        }
        if (($(this).attr("class").split((/\s+/))[0]) == 2) {
            beef_toops_array.push(1);
            $(this).on("click", function () {
                if ($(this).hasClass("btn-danger")) {
                    changes -= 1;
                    $(this).removeClass("btn-danger");
                    $(this).addClass("btn-secondary");
                    ctr_beef_array.push(-1);
                    sum_ctr_beef_array = eval(ctr_beef_array.join("+"));
                    sum_ctr_beef_array = parseInt(sum_ctr_beef_array);
                    i_beef.text(sum_ctr_beef_array);
                    if ((sum_ctr_beef_array < 0) && (sum_ctr_extra_array < 0)) {
                        price_vege = (sum_ctr_vege_array + (sum_ctr_beef_array + sum_ctr_extra_array)) * price_vege_toops;
                        if ((price_vege) < 0) {
                            price_vege = 0;
                        }
                        extra_price_text = extra_price_text.text(price_vege + price_beef + price_extra);
                    }
                    if ((sum_ctr_beef_array == 0) && (sum_ctr_extra_array < 0)) {
                        price_vege = (sum_ctr_vege_array + (sum_ctr_extra_array)) * price_vege_toops;
                        if ((price_vege) < 0) {
                            price_vege = 0;
                        }
                        extra_price_text = extra_price_text.text(price_vege + price_beef + price_extra);
                    }
                    if ((sum_ctr_beef_array > 0) && (sum_ctr_extra_array == 0)) {
                        price_vege = (sum_ctr_vege_array * price_vege_toops);
                        if ((price_vege) < 0) {
                            price_vege = 0;
                        }
                        extra_price_text = extra_price_text.text(price_vege + price_beef + price_extra);
                    }

                    if ((sum_ctr_beef_array < 0) && (sum_ctr_extra_array == 0)) {
                        price_vege = ((sum_ctr_vege_array + sum_ctr_beef_array) * price_vege_toops);
                        if ((price_vege) < 0) {
                            price_vege = 0;
                        }
                        extra_price_text = extra_price_text.text(price_vege + price_beef + price_extra);
                    }
                    if ((sum_ctr_beef_array > 0) && (sum_ctr_extra_array > 0)) {
                        price_vege = (sum_ctr_vege_array * price_vege_toops);
                        if ((price_vege) < 0) {
                            price_vege = 0;
                        }
                        extra_price_text = extra_price_text.text(price_vege + price_beef + price_extra);
                    }
                    if ((sum_ctr_beef_array == 0) && (sum_ctr_extra_array == 0)) {
                        price_vege = sum_ctr_vege_array * price_vege_toops;
                        if ((price_vege) < 0) {
                            price_vege = 0;
                        }
                        extra_price_text = extra_price_text.text(price_vege + price_beef + price_extra);
                    }
                    if ((sum_ctr_beef_array == 0) && (sum_ctr_extra_array > 0)) {
                        price_vege = sum_ctr_vege_array * price_vege_toops;
                        if ((price_vege) < 0) {
                            price_vege = 0;
                        }
                        extra_price_text = extra_price_text.text(price_vege + price_beef + price_extra);
                    }



                    if (sum_ctr_extra_array < 0) {
                        price_beef = (sum_ctr_beef_array + sum_ctr_extra_array) * price_beef_toops;
                        if ((price_beef) < 0) {
                            price_beef = 0;
                        }

                        extra_price_text = extra_price_text.text(price_vege + price_beef + price_extra);
                    }
                    if (sum_ctr_extra_array == 0) {
                        price_beef = sum_ctr_beef_array * price_beef_toops;
                        if ((price_beef) < 0) {
                            price_beef = 0;
                        }
                        extra_price_text = extra_price_text.text(price_vege + price_beef + price_extra);
                    }
                    if (sum_ctr_extra_array > 0) {
                        price_beef = sum_ctr_beef_array * price_beef_toops;
                        if ((price_beef) < 0) {
                            price_beef = 0;
                        }
                        extra_price_text = extra_price_text.text(price_vege + price_beef + price_extra);
                    }
                    if (sum_ctr_extra_array > 0) {
                        price_extra = sum_ctr_extra_array * price_extra_toops;

                        extra_price_text = extra_price_text.text(price_vege + price_beef + price_extra);
                    }
                    if (sum_ctr_extra_array == 0) {
                        price_extra = 0;

                        extra_price_text = extra_price_text.text(price_vege + price_beef + price_extra);
                    }

                } else {
                    changes += 1;
                    $(this).removeClass("btn-secondary");
                    $(this).addClass("btn-danger");
                    ctr_beef_array.push(1);
                    sum_ctr_beef_array = eval(ctr_beef_array.join("+"));
                    sum_ctr_beef_array = parseInt(sum_ctr_beef_array);
                    i_beef.text(sum_ctr_beef_array);
                    if ((sum_ctr_beef_array < 0) && (sum_ctr_extra_array < 0)) {
                        price_vege = (sum_ctr_vege_array + (sum_ctr_beef_array + sum_ctr_extra_array)) * price_vege_toops;
                        if ((price_vege) < 0) {
                            price_vege = 0;
                        }
                        extra_price_text = extra_price_text.text(price_vege + price_beef + price_extra);
                    }
                    if ((sum_ctr_beef_array == 0) && (sum_ctr_extra_array < 0)) {
                        price_vege = (sum_ctr_vege_array + (sum_ctr_extra_array)) * price_vege_toops;
                        if ((price_vege) < 0) {
                            price_vege = 0;
                        }
                        extra_price_text = extra_price_text.text(price_vege + price_beef + price_extra);
                    }
                    if ((sum_ctr_beef_array > 0) && (sum_ctr_extra_array == 0)) {
                        price_vege = (sum_ctr_vege_array * price_vege_toops);
                        if ((price_vege) < 0) {
                            price_vege = 0;
                        }
                        extra_price_text = extra_price_text.text(price_vege + price_beef + price_extra);
                    }

                    if ((sum_ctr_beef_array < 0) && (sum_ctr_extra_array == 0)) {
                        price_vege = ((sum_ctr_vege_array + sum_ctr_beef_array) * price_vege_toops);
                        if ((price_vege) < 0) {
                            price_vege = 0;
                        }
                        extra_price_text = extra_price_text.text(price_vege + price_beef + price_extra);
                    }
                    if ((sum_ctr_beef_array > 0) && (sum_ctr_extra_array > 0)) {
                        price_vege = (sum_ctr_vege_array * price_vege_toops);
                        if ((price_vege) < 0) {
                            price_vege = 0;
                        }
                        extra_price_text = extra_price_text.text(price_vege + price_beef + price_extra);
                    }
                    if ((sum_ctr_beef_array == 0) && (sum_ctr_extra_array == 0)) {
                        price_vege = sum_ctr_vege_array * price_vege_toops;
                        if ((price_vege) < 0) {
                            price_vege = 0;
                        }
                        extra_price_text = extra_price_text.text(price_vege + price_beef + price_extra);
                    }
                    if ((sum_ctr_beef_array == 0) && (sum_ctr_extra_array > 0)) {
                        price_vege = sum_ctr_vege_array * price_vege_toops;
                        if ((price_vege) < 0) {
                            price_vege = 0;
                        }
                        extra_price_text = extra_price_text.text(price_vege + price_beef + price_extra);
                    }



                    if (sum_ctr_extra_array < 0) {
                        price_beef = (sum_ctr_beef_array + sum_ctr_extra_array) * price_beef_toops;
                        if ((price_beef) < 0) {
                            price_beef = 0;
                        }

                        extra_price_text = extra_price_text.text(price_vege + price_beef + price_extra);
                    }
                    if (sum_ctr_extra_array == 0) {
                        price_beef = sum_ctr_beef_array * price_beef_toops;
                        if ((price_beef) < 0) {
                            price_beef = 0;
                        }
                        extra_price_text = extra_price_text.text(price_vege + price_beef + price_extra);
                    }
                    if (sum_ctr_extra_array > 0) {
                        price_beef = sum_ctr_beef_array * price_beef_toops;
                        if ((price_beef) < 0) {
                            price_beef = 0;
                        }
                        extra_price_text = extra_price_text.text(price_vege + price_beef + price_extra);
                    }
                    if (sum_ctr_extra_array > 0) {
                        price_extra = sum_ctr_extra_array * price_extra_toops;

                        extra_price_text = extra_price_text.text(price_vege + price_beef + price_extra);
                    }
                    if (sum_ctr_extra_array == 0) {
                        price_extra = 0;

                        extra_price_text = extra_price_text.text(price_vege + price_beef + price_extra);
                    }
                }
            });
        }
        if (($(this).attr("class").split((/\s+/))[0]) == 3) {
            cheese_toops_array.push(1);
        }

        if (($(this).attr("class").split((/\s+/))[0]) == 4) {
            extra_toops_array.push(1);
            $(this).on("click", function () {
                if ($(this).hasClass("btn-danger")) {
                    changes -= 1;
                    $(this).removeClass("btn-danger");
                    $(this).addClass("btn-secondary");
                    ctr_extra_array.push(-1);
                    sum_ctr_extra_array = eval(ctr_extra_array.join("+"));
                    sum_ctr_extra_array = parseInt(sum_ctr_extra_array);
                    i_extra.text(sum_ctr_extra_array);
                    if ((sum_ctr_beef_array < 0) && (sum_ctr_extra_array < 0)) {
                        price_vege = (sum_ctr_vege_array + (sum_ctr_beef_array + sum_ctr_extra_array)) * price_vege_toops;
                        if ((price_vege) < 0) {
                            price_vege = 0;
                        }
                        extra_price_text = extra_price_text.text(price_vege + price_beef + price_extra);
                    }
                    if ((sum_ctr_beef_array == 0) && (sum_ctr_extra_array < 0)) {
                        price_vege = (sum_ctr_vege_array + (sum_ctr_extra_array)) * price_vege_toops;
                        if ((price_vege) < 0) {
                            price_vege = 0;
                        }
                        extra_price_text = extra_price_text.text(price_vege + price_beef + price_extra);
                    }
                    if ((sum_ctr_beef_array > 0) && (sum_ctr_extra_array == 0)) {
                        price_vege = (sum_ctr_vege_array * price_vege_toops);
                        if ((price_vege) < 0) {
                            price_vege = 0;
                        }
                        extra_price_text = extra_price_text.text(price_vege + price_beef + price_extra);
                    }

                    if ((sum_ctr_beef_array < 0) && (sum_ctr_extra_array == 0)) {
                        price_vege = ((sum_ctr_vege_array + sum_ctr_beef_array) * price_vege_toops);
                        if ((price_vege) < 0) {
                            price_vege = 0;
                        }
                        extra_price_text = extra_price_text.text(price_vege + price_beef + price_extra);
                    }
                    if ((sum_ctr_beef_array > 0) && (sum_ctr_extra_array > 0)) {
                        price_vege = (sum_ctr_vege_array * price_vege_toops);
                        if ((price_vege) < 0) {
                            price_vege = 0;
                        }
                        extra_price_text = extra_price_text.text(price_vege + price_beef + price_extra);
                    }
                    if ((sum_ctr_beef_array == 0) && (sum_ctr_extra_array == 0)) {
                        price_vege = sum_ctr_vege_array * price_vege_toops;
                        if ((price_vege) < 0) {
                            price_vege = 0;
                        }
                        extra_price_text = extra_price_text.text(price_vege + price_beef + price_extra);
                    }
                    if ((sum_ctr_beef_array == 0) && (sum_ctr_extra_array > 0)) {
                        price_vege = sum_ctr_vege_array * price_vege_toops;
                        if ((price_vege) < 0) {
                            price_vege = 0;
                        }
                        extra_price_text = extra_price_text.text(price_vege + price_beef + price_extra);
                    }



                    if (sum_ctr_extra_array < 0) {
                        price_beef = (sum_ctr_beef_array + sum_ctr_extra_array) * price_beef_toops;
                        if ((price_beef) < 0) {
                            price_beef = 0;
                        }

                        extra_price_text = extra_price_text.text(price_vege + price_beef + price_extra);
                    }
                    if (sum_ctr_extra_array == 0) {
                        price_beef = sum_ctr_beef_array * price_beef_toops;
                        if ((price_beef) < 0) {
                            price_beef = 0;
                        }
                        extra_price_text = extra_price_text.text(price_vege + price_beef + price_extra);
                    }
                    if (sum_ctr_extra_array > 0) {
                        price_beef = sum_ctr_beef_array * price_beef_toops;
                        if ((price_beef) < 0) {
                            price_beef = 0;
                        }
                        extra_price_text = extra_price_text.text(price_vege + price_beef + price_extra);
                    }
                    if (sum_ctr_extra_array > 0) {
                        price_extra = sum_ctr_extra_array * price_extra_toops;

                        extra_price_text = extra_price_text.text(price_vege + price_beef + price_extra);
                    }
                    if (sum_ctr_extra_array == 0) {
                        price_extra = 0;

                        extra_price_text = extra_price_text.text(price_vege + price_beef + price_extra);
                    }

                } else {
                    changes += 1;
                    $(this).removeClass("btn-secondary");
                    $(this).addClass("btn-danger");
                    ctr_extra_array.push(1);
                    sum_ctr_extra_array = eval(ctr_extra_array.join("+"));
                    sum_ctr_extra_array = parseInt(sum_ctr_extra_array);
                    i_extra.text(sum_ctr_extra_array);
                    if ((sum_ctr_beef_array < 0) && (sum_ctr_extra_array < 0)) {
                        price_vege = (sum_ctr_vege_array + (sum_ctr_beef_array + sum_ctr_extra_array)) * price_vege_toops;
                        if ((price_vege) < 0) {
                            price_vege = 0;
                        }
                        extra_price_text = extra_price_text.text(price_vege + price_beef + price_extra);
                    }
                    if ((sum_ctr_beef_array == 0) && (sum_ctr_extra_array < 0)) {
                        price_vege = (sum_ctr_vege_array + (sum_ctr_extra_array)) * price_vege_toops;
                        if ((price_vege) < 0) {
                            price_vege = 0;
                        }
                        extra_price_text = extra_price_text.text(price_vege + price_beef + price_extra);
                    }
                    if ((sum_ctr_beef_array > 0) && (sum_ctr_extra_array == 0)) {
                        price_vege = (sum_ctr_vege_array * price_vege_toops);
                        if ((price_vege) < 0) {
                            price_vege = 0;
                        }
                        extra_price_text = extra_price_text.text(price_vege + price_beef + price_extra);
                    }

                    if ((sum_ctr_beef_array < 0) && (sum_ctr_extra_array == 0)) {
                        price_vege = ((sum_ctr_vege_array + sum_ctr_beef_array) * price_vege_toops);
                        if ((price_vege) < 0) {
                            price_vege = 0;
                        }
                        extra_price_text = extra_price_text.text(price_vege + price_beef + price_extra);
                    }
                    if ((sum_ctr_beef_array > 0) && (sum_ctr_extra_array > 0)) {
                        price_vege = (sum_ctr_vege_array * price_vege_toops);
                        if ((price_vege) < 0) {
                            price_vege = 0;
                        }
                        extra_price_text = extra_price_text.text(price_vege + price_beef + price_extra);
                    }
                    if ((sum_ctr_beef_array == 0) && (sum_ctr_extra_array == 0)) {
                        price_vege = sum_ctr_vege_array * price_vege_toops;
                        if ((price_vege) < 0) {
                            price_vege = 0;
                        }
                        extra_price_text = extra_price_text.text(price_vege + price_beef + price_extra);
                    }
                    if ((sum_ctr_beef_array == 0) && (sum_ctr_extra_array > 0)) {
                        price_vege = sum_ctr_vege_array * price_vege_toops;
                        if ((price_vege) < 0) {
                            price_vege = 0;
                        }
                        extra_price_text = extra_price_text.text(price_vege + price_beef + price_extra);
                    }



                    if (sum_ctr_extra_array < 0) {
                        price_beef = (sum_ctr_beef_array + sum_ctr_extra_array) * price_beef_toops;
                        if ((price_beef) < 0) {
                            price_beef = 0;
                        }

                        extra_price_text = extra_price_text.text(price_vege + price_beef + price_extra);
                    }
                    if (sum_ctr_extra_array == 0) {
                        price_beef = sum_ctr_beef_array * price_beef_toops;
                        if ((price_beef) < 0) {
                            price_beef = 0;
                        }
                        extra_price_text = extra_price_text.text(price_vege + price_beef + price_extra);
                    }
                    if (sum_ctr_extra_array > 0) {
                        price_beef = sum_ctr_beef_array * price_beef_toops;
                        if ((price_beef) < 0) {
                            price_beef = 0;
                        }
                        extra_price_text = extra_price_text.text(price_vege + price_beef + price_extra);
                    }
                    if (sum_ctr_extra_array > 0) {
                        price_extra = sum_ctr_extra_array * price_extra_toops;

                        extra_price_text = extra_price_text.text(price_vege + price_beef + price_extra);
                    }
                    if (sum_ctr_extra_array == 0) {
                        price_extra = 0;

                        extra_price_text = extra_price_text.text(price_vege + price_beef + price_extra);
                    }

                }
            });
        }

    });

    vegetopps.each(function (index) {
        $(this).on("click", function () {
            ctr_vege_array.push(1);
            sum_ctr_vege_array = eval(ctr_vege_array.join("+"));
            sum_ctr_vege_array = parseInt(sum_ctr_vege_array);
            i_vege.text(sum_ctr_vege_array);
            new_button = $(this).clone();
            new_button.appendTo(add_topps);
            if ((sum_ctr_beef_array < 0) && (sum_ctr_extra_array < 0)) {
                price_vege = (sum_ctr_vege_array + (sum_ctr_beef_array + sum_ctr_extra_array)) * price_vege_toops;
                if ((price_vege) < 0) {
                    price_vege = 0;
                }
                extra_price_text = extra_price_text.text(price_vege + price_beef + price_extra);
            }
            if ((sum_ctr_beef_array == 0) && (sum_ctr_extra_array < 0)) {
                price_vege = (sum_ctr_vege_array + (sum_ctr_extra_array)) * price_vege_toops;
                if ((price_vege) < 0) {
                    price_vege = 0;
                }
                extra_price_text = extra_price_text.text(price_vege + price_beef + price_extra);
            }
            if ((sum_ctr_beef_array > 0) && (sum_ctr_extra_array == 0)) {
                price_vege = (sum_ctr_vege_array * price_vege_toops);
                if ((price_vege) < 0) {
                    price_vege = 0;
                }
                extra_price_text = extra_price_text.text(price_vege + price_beef + price_extra);
            }

            if ((sum_ctr_beef_array < 0) && (sum_ctr_extra_array == 0)) {
                price_vege = ((sum_ctr_vege_array + sum_ctr_beef_array) * price_vege_toops);
                if ((price_vege) < 0) {
                    price_vege = 0;
                }
                extra_price_text = extra_price_text.text(price_vege + price_beef + price_extra);
            }
            if ((sum_ctr_beef_array > 0) && (sum_ctr_extra_array > 0)) {
                price_vege = (sum_ctr_vege_array * price_vege_toops);
                if ((price_vege) < 0) {
                    price_vege = 0;
                }
                extra_price_text = extra_price_text.text(price_vege + price_beef + price_extra);
            }
            if ((sum_ctr_beef_array == 0) && (sum_ctr_extra_array == 0)) {
                price_vege = sum_ctr_vege_array * price_vege_toops;
                if ((price_vege) < 0) {
                    price_vege = 0;
                }
                extra_price_text = extra_price_text.text(price_vege + price_beef + price_extra);
            }
            if ((sum_ctr_beef_array == 0) && (sum_ctr_extra_array > 0)) {
                price_vege = sum_ctr_vege_array * price_vege_toops;
                if ((price_vege) < 0) {
                    price_vege = 0;
                }
                extra_price_text = extra_price_text.text(price_vege + price_beef + price_extra);
            }



            if (sum_ctr_extra_array < 0) {
                price_beef = (sum_ctr_beef_array + sum_ctr_extra_array) * price_beef_toops;
                if ((price_beef) < 0) {
                    price_beef = 0;
                }

                extra_price_text = extra_price_text.text(price_vege + price_beef + price_extra);
            }
            if (sum_ctr_extra_array == 0) {
                price_beef = sum_ctr_beef_array * price_beef_toops;
                if ((price_beef) < 0) {
                    price_beef = 0;
                }
                extra_price_text = extra_price_text.text(price_vege + price_beef + price_extra);
            }
            if (sum_ctr_extra_array > 0) {
                price_beef = sum_ctr_beef_array * price_beef_toops;
                if ((price_beef) < 0) {
                    price_beef = 0;
                }
                extra_price_text = extra_price_text.text(price_vege + price_beef + price_extra);
            }
            if (sum_ctr_extra_array > 0) {
                price_extra = sum_ctr_extra_array * price_extra_toops;

                extra_price_text = extra_price_text.text(price_vege + price_beef + price_extra);
            }
            if (sum_ctr_extra_array == 0) {
                price_extra = 0;

                extra_price_text = extra_price_text.text(price_vege + price_beef + price_extra);
            }
        });
    });

    beeftopps.each(function (index) {
        $(this).on("click", function () {
            ctr_beef_array.push(1);
            sum_ctr_beef_array = eval(ctr_beef_array.join("+"));
            sum_ctr_beef_array = parseInt(sum_ctr_beef_array);
            i_beef.text(sum_ctr_beef_array);
            new_button = $(this).clone();
            new_button.appendTo(add_topps);
            if ((sum_ctr_beef_array < 0) && (sum_ctr_extra_array < 0)) {
                price_vege = (sum_ctr_vege_array + (sum_ctr_beef_array + sum_ctr_extra_array)) * price_vege_toops;
                if ((price_vege) < 0) {
                    price_vege = 0;
                }
                extra_price_text = extra_price_text.text(price_vege + price_beef + price_extra);
            }
            if ((sum_ctr_beef_array == 0) && (sum_ctr_extra_array < 0)) {
                price_vege = (sum_ctr_vege_array + (sum_ctr_extra_array)) * price_vege_toops;
                if ((price_vege) < 0) {
                    price_vege = 0;
                }
                extra_price_text = extra_price_text.text(price_vege + price_beef + price_extra);
            }
            if ((sum_ctr_beef_array > 0) && (sum_ctr_extra_array == 0)) {
                price_vege = (sum_ctr_vege_array * price_vege_toops);
                if ((price_vege) < 0) {
                    price_vege = 0;
                }
                extra_price_text = extra_price_text.text(price_vege + price_beef + price_extra);
            }

            if ((sum_ctr_beef_array < 0) && (sum_ctr_extra_array == 0)) {
                price_vege = ((sum_ctr_vege_array + sum_ctr_beef_array) * price_vege_toops);
                if ((price_vege) < 0) {
                    price_vege = 0;
                }
                extra_price_text = extra_price_text.text(price_vege + price_beef + price_extra);
            }
            if ((sum_ctr_beef_array > 0) && (sum_ctr_extra_array > 0)) {
                price_vege = (sum_ctr_vege_array * price_vege_toops);
                if ((price_vege) < 0) {
                    price_vege = 0;
                }
                extra_price_text = extra_price_text.text(price_vege + price_beef + price_extra);
            }
            if ((sum_ctr_beef_array == 0) && (sum_ctr_extra_array == 0)) {
                price_vege = sum_ctr_vege_array * price_vege_toops;
                if ((price_vege) < 0) {
                    price_vege = 0;
                }
                extra_price_text = extra_price_text.text(price_vege + price_beef + price_extra);
            }
            if ((sum_ctr_beef_array == 0) && (sum_ctr_extra_array > 0)) {
                price_vege = sum_ctr_vege_array * price_vege_toops;
                if ((price_vege) < 0) {
                    price_vege = 0;
                }
                extra_price_text = extra_price_text.text(price_vege + price_beef + price_extra);
            }



            if (sum_ctr_extra_array < 0) {
                price_beef = (sum_ctr_beef_array + sum_ctr_extra_array) * price_beef_toops;
                if ((price_beef) < 0) {
                    price_beef = 0;
                }

                extra_price_text = extra_price_text.text(price_vege + price_beef + price_extra);
            }
            if (sum_ctr_extra_array == 0) {
                price_beef = sum_ctr_beef_array * price_beef_toops;
                if ((price_beef) < 0) {
                    price_beef = 0;
                }
                extra_price_text = extra_price_text.text(price_vege + price_beef + price_extra);
            }
            if (sum_ctr_extra_array > 0) {
                price_beef = sum_ctr_beef_array * price_beef_toops;
                if ((price_beef) < 0) {
                    price_beef = 0;
                }
                extra_price_text = extra_price_text.text(price_vege + price_beef + price_extra);
            }
            if (sum_ctr_extra_array > 0) {
                price_extra = sum_ctr_extra_array * price_extra_toops;

                extra_price_text = extra_price_text.text(price_vege + price_beef + price_extra);
            }
            if (sum_ctr_extra_array == 0) {
                price_extra = 0;

                extra_price_text = extra_price_text.text(price_vege + price_beef + price_extra);
            }

        })
    });

    extratopps.each(function (index) {
        $(this).on("click", function () {
            ctr_extra_array.push(1);
            sum_ctr_extra_array = eval(ctr_extra_array.join("+"));
            sum_ctr_extra_array = parseInt(sum_ctr_extra_array);
            i_extra.text(sum_ctr_extra_array);
            new_button = $(this).clone();
            new_button.appendTo(add_topps);
            if ((sum_ctr_beef_array < 0) && (sum_ctr_extra_array < 0)) {
                price_vege = (sum_ctr_vege_array + (sum_ctr_beef_array + sum_ctr_extra_array)) * price_vege_toops;
                if ((price_vege) < 0) {
                    price_vege = 0;
                }
                extra_price_text = extra_price_text.text(price_vege + price_beef + price_extra);
            }
            if ((sum_ctr_beef_array == 0) && (sum_ctr_extra_array < 0)) {
                price_vege = (sum_ctr_vege_array + (sum_ctr_extra_array)) * price_vege_toops;
                if ((price_vege) < 0) {
                    price_vege = 0;
                }
                extra_price_text = extra_price_text.text(price_vege + price_beef + price_extra);
            }
            if ((sum_ctr_beef_array > 0) && (sum_ctr_extra_array == 0)) {
                price_vege = (sum_ctr_vege_array * price_vege_toops);
                if ((price_vege) < 0) {
                    price_vege = 0;
                }
                extra_price_text = extra_price_text.text(price_vege + price_beef + price_extra);
            }

            if ((sum_ctr_beef_array < 0) && (sum_ctr_extra_array == 0)) {
                price_vege = ((sum_ctr_vege_array + sum_ctr_beef_array) * price_vege_toops);
                if ((price_vege) < 0) {
                    price_vege = 0;
                }
                extra_price_text = extra_price_text.text(price_vege + price_beef + price_extra);
            }
            if ((sum_ctr_beef_array > 0) && (sum_ctr_extra_array > 0)) {
                price_vege = (sum_ctr_vege_array * price_vege_toops);
                if ((price_vege) < 0) {
                    price_vege = 0;
                }
                extra_price_text = extra_price_text.text(price_vege + price_beef + price_extra);
            }
            if ((sum_ctr_beef_array == 0) && (sum_ctr_extra_array == 0)) {
                price_vege = sum_ctr_vege_array * price_vege_toops;
                if ((price_vege) < 0) {
                    price_vege = 0;
                }
                extra_price_text = extra_price_text.text(price_vege + price_beef + price_extra);
            }
            if ((sum_ctr_beef_array == 0) && (sum_ctr_extra_array > 0)) {
                price_vege = sum_ctr_vege_array * price_vege_toops;
                if ((price_vege) < 0) {
                    price_vege = 0;
                }
                extra_price_text = extra_price_text.text(price_vege + price_beef + price_extra);
            }



            if (sum_ctr_extra_array < 0) {
                price_beef = (sum_ctr_beef_array + sum_ctr_extra_array) * price_beef_toops;
                if ((price_beef) < 0) {
                    price_beef = 0;
                }

                extra_price_text = extra_price_text.text(price_vege + price_beef + price_extra);
            }
            if (sum_ctr_extra_array == 0) {
                price_beef = sum_ctr_beef_array * price_beef_toops;
                if ((price_beef) < 0) {
                    price_beef = 0;
                }
                extra_price_text = extra_price_text.text(price_vege + price_beef + price_extra);
            }
            if (sum_ctr_extra_array > 0) {
                price_beef = sum_ctr_beef_array * price_beef_toops;
                if ((price_beef) < 0) {
                    price_beef = 0;
                }
                extra_price_text = extra_price_text.text(price_vege + price_beef + price_extra);
            }
            if (sum_ctr_extra_array > 0) {
                price_extra = sum_ctr_extra_array * price_extra_toops;

                extra_price_text = extra_price_text.text(price_vege + price_beef + price_extra);
            }
            if (sum_ctr_extra_array == 0) {
                price_extra = 0;

                extra_price_text = extra_price_text.text(price_vege + price_beef + price_extra);
            }

        })
    });


})


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