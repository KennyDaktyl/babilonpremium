$(document).ready(function () {

    var search_client = $('#search_client');
    var search_div = $('#search_div');
    var new_client = $('#new_client').css('display', 'none');
    var add_new_client = $('#add_new_client');
    var phone_number = $('#phone_number');
    var span_ok = $('#ok');
    var main = $('#main');
    var lista = $('.lista');
    var client = $('#client').css('display', 'none');
    var lista = $('.lista');

    $(document).keyup(function (event) {
        if (event.keyCode === 32) {
            search_client.focus();
            // alert('hello');
        }
    });

    $(function () {
        search_client.keyup(function () {
            main.css('display', 'none');
            // new_client.hide();
            client.css('display', 'block');
            new_client = $('#new_client').css('display', 'none');
            var text = $(this).val();

            //         //na dziendobry ukryj wszystko po nacisnieciu klawisza
            lista.css('display', 'none');

            // lecz nastepnie pokaż pasujące frary
            $('.lista:contains("' + text + '")').show();
        });
        add_new_client.click(function () {

            new_client = $('#new_client').css('display', 'block');
            client.css('display', 'none');
            var number = search_client.val();
            if (number.length < 9) {
                span_ok.text('numer niepoprawny');
                span_ok.addClass('text-danger');
                span_ok.removeClass('text-success');
            } else {
                span_ok.text('numer poprawny');
                span_ok.removeClass('text-danger');
                span_ok.addClass('text-success');
            };;
            phone_number.val(number);
            search_div.css('display', 'none');

        });
        phone_number.keyup(function () {
            var number = $(this).val();
            if (number.length < 9) {
                span_ok.text('numer niepoprawny');
                span_ok.addClass('text-danger');
                span_ok.removeClass('text-success');
            } else {
                span_ok.text('numer poprawny');
                span_ok.removeClass('text-danger');
                span_ok.addClass('text-success');
            };
        });
    });
})