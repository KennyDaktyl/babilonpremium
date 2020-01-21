$(document).ready(function () {

    function ShowOrderMobileAjax() {
        result = "";
        $.ajax({
            url: "http://localhost:8000/orders_for_drivers/1",
            async: false,
            type: "GET",
            data: {
                // order_close: order_id,
                csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val()
            },
            dataType: "json",
            success: function (data) {
                result = data;
            }
        });
        setTimeout(function () {
            ShowOrderMobileAjax()
        }, delay = 5000);
        return result;
    }


    function show_orders() {
        orders = ShowOrderMobileAjax();
        console.log(orders);
        setTimeout(function () {
            show_orders()
        }, delay = 5000);
    };

    ShowOrderMobileAjax();

    show_orders();

    // ShowOrderMobileAjax();
});