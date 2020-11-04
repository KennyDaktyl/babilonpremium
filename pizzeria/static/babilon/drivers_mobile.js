$(document).ready(function () {

    var pizzeria = $('#workplace').data('pizzeria');
    var orders_length = $('#workplace').data('length');
    // var ulr_1 = "http://localhost:8000/for_drivers_orders/" + String(pizzeria);
    var ulr_1 = "https://pizzeriasystem.herokuapp.com/for_drivers_orders/" + String(pizzeria);

    function ShowOrderMobileAjax() {
        result = "";
        $.ajax({
            url: ulr_1,
            async: true,
            type: "GET",
            data: {
                // order_close: order_id,
                csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val()
            },
            dataType: "json",
            success: function (data) {
                result = data;
                console.log(result['length']);
                console.log(orders_length);
                if (result['length'] != orders_length) {
                    location.reload();
                }
            }
        });
        return result;
    }




    setInterval(ShowOrderMobileAjax, 5000);





    // function show_orders() {
    //     orders = ShowOrderMobileAjax();
    //     if (orders.length != orders_length) {
    //         location.reload();
    //     }
    //     console.log(orders.length);
    //     setTimeout(function () {
    //         show_orders()
    //     }, delay = 5000);
    // };

    ShowOrderMobileAjax();

    // show_orders();

    // ShowOrderMobileAjax();
});