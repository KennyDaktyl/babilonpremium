$(document).ready(function () {

    var button_add = $('#add_driver_button');
    var button_close = $('#close_driver_button').hide();;
    var form = $('#add_driver').hide();

    button_add.on("click", function () {
        form.show();
        button_close.removeClass('btn-dark');
        button_close.addClass('btn-danger');
        button_close.show().addClass('btd-danger');
        $(this).hide();

    });
    button_close.on("click", function () {
        form.hide();
        button_add.show();
        $(this).hide();
    });
});