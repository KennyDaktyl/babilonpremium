$(document).ready(function () {

    var search_client = $('#search_client');
    var main = $('#main');
    var lista = $('.lista');
    var client = $('#client').hide();
    var lista = $('.lista');


    $(function () {
        search_client.keyup(function () {
            main.hide();
            client.show();
            var text = $(this).val();

            //         //na dziendobry ukryj wszystko po nacisnieciu klawisza
            lista.hide();

            // lecz nastepnie pokaż pasujące frary
            $('.lista:contains("' + text + '")').show();
        });
    });
})