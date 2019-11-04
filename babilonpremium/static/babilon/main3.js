$(document).ready(function () {

    var size_button = $('.Pizza');
    var pizza_button = $('.product button');
    
    size_button.each(function (index) {
        $(this).on("click", function () {
            var size_class = ($(this).attr("class").split((/\s+/))[0]);
            // pizza_button.hide();
            pizza_button.each(function (el) {
                if (($(this).hasClass(size_class))) {
                    $(this).show();
                } else {
                    $(this).hide();
                };
            });

        });

    })
})