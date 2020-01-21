$(document).ready(function () {


    var lokal_order_button = $('#lokal_order');
    var lokal_order_quantity = lokal_order_button.text();
    lokal_order_quantity = parseInt(lokal_order_quantity);

    var wynos_order_button = $('#wynos_order');
    var wynos_order_quantity = wynos_order_button.text();
    wynos_order_quantity = parseInt(wynos_order_quantity);

    var dostawa_order_button = $('#dostawa_order');
    var dostawa_order_quantity = dostawa_order_button.text();
    dostawa_order_quantity = parseInt(dostawa_order_quantity);

    var done_order = $('#done_order');
    var done_order_quantity = done_order.text();
    done_order_quantity = parseInt(done_order_quantity);

    var not_closed_order_button = $('#not_closed_order');
    var not_closed_order_quantity = not_closed_order_button.text();
    not_closed_order_quantity = parseInt(not_closed_order_quantity);

    var go_to_order = $('#go_to_order');
    var go_to_order_quantity = go_to_order.text();
    go_to_order_quantity = parseInt(go_to_order_quantity);

    var cancelled_order_button = $('#cancelled_order_button');
    var cancelled_order_quantity = cancelled_order_button.text();
    cancelled_order_quantity = parseInt(cancelled_order_quantity);

    var inprogress_order_button = $('#inprogress_order');
    var inprogress_order_quantity = inprogress_order_button.text();
    inprogress_order_quantity = parseInt(inprogress_order_quantity);

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

    var driver_name;

    var button_close_order_with_driver = $('button.3').hide();

    function show_close_button() {
        button_close_order_with_driver.each(function (index) {
            if ($(this).hasClass('True')) {
                $(this).show();
            };
        });
    }
    show_close_button();


    hide_button.each(function (index) {
        $(this).hide();
    });

    var url_adress = window.location.href;

    function pretty_time_string(num) {
        return (num < 10 ? "0" : "") + num;
    }



    function getdate() {
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
        hours.text(h);
        minutes.text(m);
        seconds.text(s);

        time_zero.each(function (index) {
            if ($(this).data('status') != 4) {
                var time_z = ($(this).text());
                var arr = time_z.split(':');
                var time_delivery = new Date();
                time_delivery.setHours(arr[0]);
                time_delivery.setMinutes(arr[1]);

                if (time_delivery > today) {
                    var total_seconds = (time_delivery - today) / 1000;

                    var hours_timer = (Math.floor(total_seconds / 3600));
                    total_seconds = total_seconds % 3600;
                    var minutes_timer = Math.floor(total_seconds / 60);
                    total_seconds = total_seconds % 60;

                    var seconds_timer = Math.floor(total_seconds);
                    hours_timer = pretty_time_string(hours_timer)
                    minutes_timer = pretty_time_string(minutes_timer)
                    // seconds_timer = pretty_time_string(seconds_timer)
                    var currentTimeString = hours_timer + ":" + minutes_timer;
                    var timer = ($(this).siblings());
                    timer.text(currentTimeString);
                } else {
                    var total_seconds = (today - time_delivery) / 1000;
                    var hours_timer = (Math.floor(total_seconds / 3600));
                    total_seconds = total_seconds % 3600;
                    var minutes_timer = Math.floor(total_seconds / 60);
                    total_seconds = total_seconds % 60;
                    var seconds_timer = Math.floor(total_seconds);

                    hours_timer = pretty_time_string(hours_timer)
                    minutes_timer = pretty_time_string(minutes_timer)
                    // seconds_timer = pretty_time_string(seconds_timer)
                    var currentTimeString = "-" + hours_timer + ":" + minutes_timer + "!";
                    var timer = ($(this).siblings());
                    timer.text(currentTimeString);
                    timer.removeClass('text-success');
                    timer.addClass('text-danger');
                    // console.log(timer.text());
                }
            }
        })
        setTimeout(function () {
            getdate()
        }, 1000);
    }

    getdate();

    var new_set_driver = ($("#new_set_driver")).hide();
    var old_set_driver = ($("#old_set_driver"));
    var del_button = $("form.del_driver_form").hide();

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
            $(this).parent().parent().parent().parent().parent().siblings().children().children('span.driver_warning').hide();
            $(this).parent().parent().parent().parent().parent().siblings().children().children('button.close_order').addClass('True');
            go_to_order_quantity += 1;
            go_to_order.text(go_to_order_quantity);
            inprogress_order_quantity -= 1;
            inprogress_order_button.text(inprogress_order_quantity);
            show_close_button();
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
            if ($(this).parent().parent().parent().hasClass('Lokal')) {
                lokal_order_quantity -= 1;
                lokal_order_button.text(lokal_order_quantity);
            };
            if ($(this).parent().parent().parent().hasClass('Wynos')) {
                wynos_order_quantity -= 1;
                wynos_order_button.text(wynos_order_quantity);
            };
            if ($(this).parent().parent().parent().hasClass('Dostawa')) {
                dostawa_order_quantity -= 1;
                dostawa_order_button.text(dostawa_order_quantity);
            };


            if ($(this).parent().parent().parent().hasClass('3')) {
                go_to_order_quantity -= 1;
                go_to_order.text(go_to_order_quantity);
            };

            if ($(this).parent().parent().parent().hasClass('2')) {
                inprogress_order_quantity -= 1;
                inprogress_order_button.text(inprogress_order_quantity);
            };
           
            not_closed_order_quantity -= 1;
            not_closed_order_button.text(not_closed_order_quantity);
            done_order_quantity += 1;
            done_order.text(done_order_quantity);

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
            if ($(this).parent().parent().parent().hasClass('Lokal')) {
                lokal_order_quantity -= 1;
                lokal_order_button.text(lokal_order_quantity);
            };
            if ($(this).parent().parent().parent().hasClass('Wynos')) {
                wynos_order_quantity -= 1;
                wynos_order_button.text(wynos_order_quantity);
            };
            if ($(this).parent().parent().parent().hasClass('Dostawa')) {
                dostawa_order_quantity -= 1;
                dostawa_order_button.text(dostawa_order_quantity);
            };


            if ($(this).parent().parent().parent().hasClass('3')) {
                go_to_order_quantity -= 1;
                go_to_order.text(go_to_order_quantity);
            };

            if ($(this).parent().parent().parent().hasClass('2')) {
                // go_to_order_quantity -= 1;
                // go_to_order.text(go_to_order_quantity);
                inprogress_order_quantity -= 1;
                inprogress_order_button.text(inprogress_order_quantity);
            };
            if ($(this).parent().parent().parent().hasClass('3')) {
                go_to_order_quantity -= 1;
                go_to_order.text(go_to_order_quantity);
            };
            not_closed_order_quantity -= 1;
            not_closed_order_button.text(not_closed_order_quantity);

            $(this).parent().parent().parent().removeClass('table-warning');
            $(this).parent().parent().parent().removeClass('table-secondary');
            $(this).parent().parent().parent().addClass('table-danger');
            $(this).parent().parent().parent().removeClass('2');
            $(this).parent().parent().parent().removeClass('3');
            $(this).parent().parent().parent().removeClass('4');
            $(this).parent().parent().parent().addClass('5');
            $(this).parent().parent().siblings().children('button.cancelled').hide();
            $(this).hide();
            cancelled_order_quantity += 1;
            cancelled_order_button.text(cancelled_order_quantity);

        });
    })

    var send_sms = $('button.send_sms');
    send_sms.each(function (index) {
        $(this).on("click", function () {
            event.preventDefault();
            var order_id = $(this).data('order');
            var phone_number = $(this).data('phone_number');
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
            var time_sent_sms = h + ":" + m + ":" + s;
            var message = $(this).parent().siblings('div.modal-body.massage').text();

            function sendSMSAjax() {
                result = "";
                $.ajax({
                    url: url_adress,
                    async: false,
                    type: "POST",
                    data: {
                        order_send_sms: order_id,
                        message: message,
                        phone_number: phone_number,
                        time_send_sms: time_sent_sms,
                        csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val()
                    },
                    dataType: "json",
                    success: function (data) {
                        result = JSON.parse(data.order);
                        // console.log($(this).parent().parent().siblings('div.message').text());
                    }
                });
                return result;
            }
            result = sendSMSAjax();
            $(this).text('Wysłano');
            $(this).parent().parent().parent().parent().siblings().removeClass('btn-success');
            $(this).parent().parent().parent().parent().siblings('button').addClass('btn-secondary');
            $(this).parent().parent().parent().parent().siblings('button').text('Wysłano');
            $(this).parent().parent().parent().parent().siblings('span').text(time_sent_sms);

            // $(this).removeClass('btn-success');
            // $(this).removeClass('send_sms');
            // $(this).addClass('btn-secondary');
            // $(this).parent().parent().removeClass('2');
            if ($(this).parent().parent().parent().parent().parent().parent().hasClass('2')) {
                $(this).parent().parent().parent().parent().parent().parent().removeClass('table-primary');
                $(this).parent().parent().parent().parent().parent().parent().removeClass('table-primary');
                $(this).parent().parent().parent().parent().parent().parent().addClass('3');
                $(this).parent().parent().parent().parent().parent().parent().addClass('table-warning');
            }

        });
    });


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