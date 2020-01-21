$(document).ready(function () {

    var hours = $('#h');
    var minutes = $('#m');
    var seconds = $('#s');

    var hour_zero = $('.hour_zero span');
    var min_zero = $('.min_zero span');
    var sec_zero = $('.sec_zero span');


    var time_zero = $('span.time_zero');
    var timer = $('span.timer');

    var set_driver = $('button.driver');
    var div_modal = $('#driverModal');

    var close_order = $('button.close_order');
    var cancell_order = $('button.cancell_order');
    var hide_button = $('button.hide_button');
    var drivers_button = $('button.drivers_button');

    var driver_name;
    var driver_from_python;

    var button_close_order_with_driver = $('button.3').hide();

    function show_close_button() {
        button_close_order_with_driver.each(function (index) {
            if ($(this).hasClass('True')) {
                $(this).show();
            };
        });
    }
    show_close_button();

    var orders = $('tr.order');

    hide_button.each(function (index) {
        $(this).hide();
    });

    var url_adress = window.location.href;

    function pretty_time_string(num) {
        return (num < 10 ? "0" : "") + num;
    }

    var inprogress_order = $('#inprogress_order');
    var inprogress_button = $('#inprogress');

    var inprogress_order_quantity = 0;
    var not_closed_button = $('#not_closed');
    var not_closed_order = $('#not_closed_order');
    var not_closed_quantity = 0;
    var in_delivery_button = $('#in_delivery');
    var go_to_order = $('#go_to_order');
    var go_to_order_quantity = 0;
    var done_order = $('#done_order');
    var done_button = $('#done');
    var done_order_quantity = 0;
    var cancelled_order = $('#cancelled_order');
    var cancelled_button = $('#cancelled');
    var cancelled_order_quantity = 0;
    var all_button = $('#all');
    var all_order_quantity = 0;
    var empty_button = $('#empty_order');
    var empty_counter = $('#empty_counter');
    var empty_order_quantity = 0;

    var wynos_order = $('#wynos_order');
    var wynos_button = $('#wynos');
    var lokal_order = $('#lokal_order');
    var lokal_button = $('#lokal');
    var dostawa_order = $('#dostawa_order');
    var dostawa_button = $('#dostawa');
    var lista = $('tr.lista');

    all_button.on("click", function () {
        location.reload();
    })



    empty_button.on("click", function () {
        lista.hide();
        // $.cookie("name", "value");
        // console.log(cookie);
        lista.each(function (index) {
            if ($(this).hasClass('1')) {
                $(this).show();
            };
        });
    });

    lokal_button.on("click", function () {
        lista.hide();
        lista.each(function (index) {

            if ($(this).hasClass('Lokal')) {
                if (!($(this).hasClass('5'))) {
                    if (!($(this).hasClass('1'))) {
                        $(this).show();
                    };
                };
            };
        });
    });


    wynos_button.on("click", function () {
        lista.hide();
        lista.each(function (index) {

            if ($(this).hasClass('Wynos')) {
                if (!($(this).hasClass('5'))) {
                    if (!($(this).hasClass('1'))) {
                        $(this).show();
                    };
                };
            };
        });
    });

    dostawa_button.on("click", function () {
        lista.hide();
        lista.each(function (index) {

            if ($(this).hasClass('Dostawa')) {
                if (!($(this).hasClass('5'))) {
                    if (!($(this).hasClass('1'))) {
                        $(this).show();
                    };
                };
            };

        });
    });

    cancelled_button.on("click", function () {
        lista.hide();
        lista.each(function (index) {

            if ($(this).hasClass('5')) {
                $(this).show();
            };
        });
    });

    function button_status() {

        cancelled_order_quantity = 0;
        cancelled_order.text(cancelled_order_quantity);
        orders.each(function (index) {


            if ($(this).hasClass('5')) {
                cancelled_order_quantity += 1;
                cancelled_order.text(cancelled_order_quantity);
            }
            if ($(this).hasClass('1')) {
                empty_order_quantity += 1;
                empty_counter.text(empty_order_quantity);
            }

        });
    };
    button_status();

    function delivery_status() {
        lokal_order_quantity = 0;
        lokal_order.text(lokal_order_quantity);
        wynos_order_quantity = 0;
        wynos_order.text(wynos_order_quantity);
        dostawa_order_quantity = 0;
        dostawa_order.text(dostawa_order_quantity);

        orders.each(function (index) {
            if (($(this).hasClass('2')) || ($(this).hasClass('3')) || ($(this).hasClass('4')) || ($(this).hasClass('1'))) {

                if ($(this).hasClass('Lokal')) {
                    if (!($(this).hasClass('5'))) {
                        if (!($(this).hasClass('1'))) {
                            lokal_order_quantity += 1;
                            lokal_order.text(lokal_order_quantity);
                        };
                    };
                }
                if ($(this).hasClass('Wynos')) {
                    if (!($(this).hasClass('5'))) {
                        if (!($(this).hasClass('1'))) {
                            wynos_order_quantity += 1;
                            wynos_order.text(wynos_order_quantity);
                        };
                    };
                }
                if ($(this).hasClass('Dostawa')) {
                    if (!($(this).hasClass('5'))) {
                        if (!($(this).hasClass('1'))) {
                            dostawa_order_quantity += 1;
                            dostawa_order.text(dostawa_order_quantity);
                        };
                    };
                }
            }
        });
    };
    delivery_status();



    set_driver.each(function (index) {

        $(this).on("click", function () {
            var set_driver_op = $(this).data('driver');
            event.preventDefault();
            var order_id = $(this).data('order');

            function testAjax() {
                var result = "";
                $.ajax({
                    url: url_adress,
                    async: false,
                    type: "POST",
                    data: {
                        driver_id: set_driver_op,
                        order_id: order_id,
                        csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val()
                    },
                    dataType: "json",
                    success: function (data) {
                        result = JSON.parse(data.save_driver);
                    }
                });
                return result;
            }
            result = testAjax();
            var name = (result[0].fields.first_name);
            var sec_name = (result[0].fields.last_name);
            driver_name = name + " " + sec_name;
            $(this).parent().parent().parent().parent().siblings('form').show();
            $(this).parent().parent().parent().parent().siblings('span.new_set_driver').text(driver_name);
            $(this).parent().parent().parent().parent().siblings('span.new_set_driver').show();
            $(this).parent().parent().parent().parent().siblings('button').hide();
            $(this).parent().parent().parent().parent().parent().parent().removeClass('table-light');
            $(this).parent().parent().parent().parent().parent().parent().removeClass('table-primary');
            $(this).parent().parent().parent().parent().parent().parent().addClass('table-warning');
            $(this).parent().parent().parent().parent().parent().parent().removeClass('2');
            $(this).parent().parent().parent().parent().parent().parent().addClass('3');
            $(this).parent().parent().parent().parent().siblings().children().children('button.close_order').addClass('True');
            $(this).parent().parent().parent().parent().parent().siblings().children().children('span.driver_warning').hide();
            button_status();
            delivery_status();
            show_close_button();
            location.reload();


        })
    })

    close_order.each(function (index) {
        $(this).on("click", function () {
            event.preventDefault();
            var order_id = $(this).data('order');

            function closeOrderAjax() {
                result = "";
                $.ajax({
                    url: url_adress,
                    async: false,
                    type: "POST",
                    data: {
                        order_close: order_id,
                        csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val()
                    },
                    dataType: "json",
                    success: function (data) {
                        result = JSON.parse(data.order);
                    }
                });
                return result;
            }
            result = closeOrderAjax();
            var time_close = result[0].fields.time_delivery_in;
            console.log(time_close)
            $(this).parent().parent().parent().removeClass('table-warning');
            $(this).parent().parent().parent().addClass('table-secondary');
            $(this).parent().parent().parent().removeClass('2');
            $(this).parent().parent().parent().removeClass('3');
            $(this).parent().parent().parent().addClass('4');
            $(this).parent().siblings().show();
            $(this).hide();
            var today = new Date();
            var h = today.getHours();
            var m = today.getMinutes();
            var s = today.getSeconds();
            if (s < 10) {
                s = "0" + s;
            }
            if (m < 10) {
                m = "0" + m;
            }
            var time_close_order = h + ":" + m + ":" + s;
            $(this).parent().parent().siblings().children('span.time_close_order').text(time_close_order);
            $(this).parent().parent().siblings().children('form').hide();
            $(this).parent().parent().siblings().children('span.timer').hide();
            button_status();
            delivery_status();
            // go_to_order.text('chuj');
        });
    })

    cancell_order.each(function (index) {
        $(this).on("click", function () {
            event.preventDefault();
            var order_id = $(this).data('order');

            function cancellOrderAjax() {
                result = "";
                $.ajax({
                    url: url_adress,
                    async: false,
                    type: "POST",
                    data: {
                        order_cancell_id: order_id,
                        csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val()
                    },
                    dataType: "json",
                    success: function (data) {
                        result = JSON.parse(data.order);
                    }
                });
                return result;
            }
            result = cancellOrderAjax();
            console.log(result);
            console.log('działa');
            // console.log(result[0].pk)
            $(this).parent().parent().parent().removeClass('table-warning');
            $(this).parent().parent().parent().removeClass('table-secondary');
            $(this).parent().parent().parent().addClass('table-danger');
            $(this).parent().parent().parent().removeClass('2');
            $(this).parent().parent().parent().removeClass('3');
            $(this).parent().parent().parent().removeClass('4');
            $(this).parent().parent().parent().addClass('5');
            $(this).parent().parent().siblings().children('button.cancelled').hide();
            console.log($(this).parent().parent().siblings().children('button'));

            $(this).hide();
            button_status();
            delivery_status();
            location.reload();
        });
    })


});

// close_order.each(function (index) {
//     $(this).on("click", function () {
//         event.preventDefault();
//         $.ajax({
//             url: url_adress,
//             type: "POST",
//             data: {
//                 order_close: $(this).data('order'),
//                 csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val()
//             },
//             dataType: "json",
//         }).done(function (result) {
//             location.reload();
//         }).fail(function (xhr, status, err) {}).always(function (xhr, status) {});
//         $(this).hide();
//         // var id = $(this).data('order');
//         // $(this).parent('tr').removeClass('table-secondary');

//         // console.log($(this).parent().siblings('td').children('#del_driver_form'));
//         $(this).parent().parent().parent().addClass('table-secondary');
//         $(this).parent().siblings().show();
//         // $('#del_driver_form').hide();
//         // console.log($('#del_driver_form').hide());
//         $(this).parent().parent().siblings().children('form').hide();
//     });
// })



// $.ajax({
//     url: url_adress,
//     type: "POST",
//     data: {
//         driver_id: set_driver_op,
//         order_id: order_id,
//         csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val()
//     },
//     dataType: "json",
// }).done(function (result) {
//     driver_from_python = JSON.parse(result.save_driver);
//     var name = (driver_from_python[0].fields.first_name);
//     var sec_name = (driver_from_python[0].fields.last_name);
//     driver_name = name + " " + sec_name;
//     // console.log(driver_name);
//     // $('#new_set_driver').text(driver_name);
//     // $('#new_set_driver').show();
//     old_set_driver.hide();
//     console.log(driver_from_python);
//     location.reload();
//     // console.log('chuj');
//     // del_button.show();
//     // console.log(driver_name);
// }).fail(function (xhr, status, err) {}).always(function (xhr, status) {});



// function testAjax() {
//     var result = "";
//     $.ajax({
//         url: url_adress,
//         async: false,
//         type: "POST",
//         data: {
//             driver_id: set_driver_op,
//             order_id: order_id,
//             csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val()
//         },
//         dataType: "json",
//         success: function (data) {
//             result = JSON.parse(data.save_driver);;
//             console.log(result)

//         }
//     });
//     return result;

// }
// testAjax()
// result = testAjax();
// console.log(result.model);