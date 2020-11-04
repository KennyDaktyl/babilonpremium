$(document).ready(function () {

    var url_adress = window.location.href;
    var time_zero = $('.time_zero button');



    var pay_method = $('button.pay_method');
    var delivery_method = $('button.delivery');

    set_time_zero = $('#set_time_zero');
    var time_zero_info = $('#time_zero_info');
    set_time_zero.on('click', function () {
        set_time_zero.removeClass('btn-primary');
        set_time_zero.addClass('btn-success');
        set_time_zero.text('OK');
    })

    // var time_realisation=('button.time_realisation');

    // $(document).keyup(function (event) {
    //     if (event.keyCode === 13) {
    //         $('#enter').click();
    //     }
    // });

    time_zero.each(function (index) {
        $(this).on("click", function () {
            time_zero.removeClass('btn-success');
            time_zero.addClass('btn-primary');
            $.ajax({
                url: url_adress,
                type: "GET",
                data: {
                    time_zero: $(this).data('time'),

                    csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val()
                },
                // dataType: "json"
            }).done(function (result) {}).fail(function (xhr, status, err) {}).always(function (xhr, status) {});
            $(this).addClass('btn-success');
            console.log($(this).data('time'));
        });
    });

    pay_method.each(function (index) {

        $(this).on("click", function () {
            pay_method.removeClass('btn-primary');
            pay_method.addClass('btn-secendary');
            console.log($(this).data('pay_method'));
            $.ajax({
                url: url_adress,
                type: "GET",
                data: {
                    pay_method: $(this).data('pay_method'),

                    csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val()
                },
                // dataType: "json"
            }).done(function (result) {}).fail(function (xhr, status, err) {}).always(function (xhr, status) {});

            $(this).addClass('btn-primary');

        });
    });

    delivery_method.each(function (index) {
        $(this).on("click", function () {
            delivery_method.removeClass('btn-primary');
            delivery_method.addClass('btn-secendary');
            console.log($(this).data('delivery'));
            $.ajax({
                url: url_adress,
                type: "GET",
                data: {
                    delivery_method: $(this).data('delivery'),

                    csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val()
                },
                // dataType: "json"
            }).done(function (result) {}).fail(function (xhr, status, err) {}).always(function (xhr, status) {});

            $(this).addClass('btn-primary');
            location.reload();
        });

    });

})