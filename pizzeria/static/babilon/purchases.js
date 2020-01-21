$(document).ready(function () {

    var button_add = $('#add_driver_button');
    var button_close = $('#close_driver_button').css('display', 'none');
    var form = $('#add_driver').css('display', 'none');

    button_add.on("click", function () {
        close_other_form()
        form.css('display', 'block');
        button_close.removeClass('btn-dark');
        button_close.addClass('btn-danger');
        button_close.show().addClass('btd-danger');
        $(this).css('display', 'none');

    });
    button_close.on("click", function () {
        form.css('display', 'none');
        button_add.css('display', 'block');
        $(this).css('display', 'none');
    });

    var add_reward_button = $('#add_reward_button');
    var button_close_reward = $('#close_add_reward_button').css('display', 'none');
    var formReward = $('#add_reward').css('display', 'none');

    add_reward_button.on("click", function () {
        close_other_form()
        formReward.css('display', 'block');
        button_close_reward.removeClass('btn-dark');
        button_close_reward.addClass('btn-danger');
        button_close_reward.show().addClass('btd-danger');
        $(this).css('display', 'none');

    });
    button_close_reward.on("click", function () {
        formReward.css('display', 'none');
        add_reward_button.css('display', 'block');
        $(this).css('display', 'none');
    });

    var add_tax_button = $('#add_tax_button');
    var button_close_tax = $('#close_add_tax_button').css('display', 'none');
    var formTax = $('#add_tax').css('display', 'none');

    add_tax_button.on("click", function () {
        close_other_form()
        formTax.css('display', 'block');
        button_close_tax.removeClass('btn-dark');
        button_close_tax.addClass('btn-danger');
        button_close_tax.show().addClass('btd-danger');
        $(this).css('display', 'none');

    });
    button_close_tax.on("click", function () {
        formTax.css('display', 'none');
        add_tax_button.css('display', 'block');
        $(this).css('display', 'none');
    });

    var add_const_button = $('#add_const_button');
    var button_close_const = $('#close_add_const_button').css('display', 'none');
    var formConst = $('#add_const').css('display', 'none');

    add_const_button.on("click", function () {
        close_other_form()
        formConst.css('display', 'block');
        button_close_const.removeClass('btn-dark');
        button_close_const.addClass('btn-danger');
        button_close_const.show().addClass('btd-danger');
        $(this).css('display', 'none');

    });
    button_close_const.on("click", function () {
        formConst.css('display', 'none');
        add_const_button.css('display', 'block');
        $(this).css('display', 'none');
    });

    var add_other_button = $('#add_other_button');
    var button_close_other = $('#close_add_other_button').css('display', 'none');
    var formOther = $('#add_other').css('display', 'none');

    add_other_button.on("click", function () {
        close_other_form()
        formOther.css('display', 'block');
        button_close_other.removeClass('btn-dark');
        button_close_other.addClass('btn-danger');
        button_close_other.show().addClass('btd-danger');
        $(this).css('display', 'none');

    });
    button_close_other.on("click", function () {
        formOther.css('display', 'none');
        add_other_button.css('display', 'block');
        $(this).css('display', 'none');
    });

    function close_other_form() {
        formOther.css('display', 'none');
        button_close.css('display', 'none');
        formConst.css('display', 'none');
        formTax.css('display', 'none');
        formReward.css('display', 'none');
        form.css('display', 'none');


        button_close.css('display', 'none');
        button_close_reward.css('display', 'none');
        button_close_tax.css('display', 'none');
        button_close_const.css('display', 'none');
        button_close_other.css('display', 'none');

        button_add.css('display', 'block');
        add_reward_button.css('display', 'block');
        add_tax_button.css('display', 'block');
        add_const_button.css('display', 'block');
        add_other_button.css('display', 'block');
    }
});