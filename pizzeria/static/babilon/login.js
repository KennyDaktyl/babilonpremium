$(document).ready(function () {
    // check native support
    $('#support').text($.fullscreen.isNativelySupported() ? 'supports' : 'doesn\'t support');
    // open in fullscreen
    $('#fullscreen .requestfullscreen').click(function () {
        $('#fullscreen').fullscreen();
        return false;
    });
    // exit fullscreen
    $('#fullscreen .exitfullscreen').click(function () {
        $.fullscreen.exit();
        return false;
    });
    // document's event
    $(document).bind('fscreenchange', function (e, state, elem) {
        // if we currently in fullscreen mode
        if ($.fullscreen.isFullScreen()) {
            $('#fullscreen .requestfullscreen').hide();
            $('#fullscreen .exitfullscreen').show();
        } else {
            $('#fullscreen .requestfullscreen').show();
            $('#fullscreen .exitfullscreen').hide();
        }
        $('#state').text($.fullscreen.isFullScreen() ? '' : 'not');
    });

});