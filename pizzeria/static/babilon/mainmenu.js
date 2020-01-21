$(document).ready(function () {

    var size_button = $('button.sizes');
    var product_button = $('a.pizza');

    // size_button.each(function (index) {
    //     $(this).on("click", function () {
    //         var size_class = ($(this).attr("class").split((/\s+/))[0]);
    //         // pizza_button.hide();
    //         product_button.each(function (el) {
    //             if (($(this).hasClass(size_class))) {
    //                 $(this).show();
    //             } else {
    //                 $(this).hide();
    //             };
    //         });

    //     });

    // });

    $(document).keyup(function (event) {
        if (event.keyCode === 32) {
            $('#code').focus();
            // alert('hello');
        }
    });

    $(document).keyup(function (event) {
        if (event.keyCode === 121) {
            $('#enter').click();
            // alert('hello');
        }
    });

    // var code = $('#code');
    // var products_menu = $('span.code');
    // var products = $('.products');

    // $(function () {
    //     code.keyup(function () {
    //         var text = $(this).val();
    //         console.log(text);

    //         //         //na dziendobry ukryj wszystko po nacisnieciu klawisza
    //         products.css("display", "none");
    //         // lecz nastepnie pokaż pasujące frary
    //         $('.products:contains("' + text + '")').css("display", "block");
    //     });
    // });
})