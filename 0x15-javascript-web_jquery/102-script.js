// This script fetches and displays the translation of "Hello" based on the language code entered by the user
$(document).ready(function() {
    $('#btn_translate').click(function() {
        const languageCode = $('#language_code').val();
        const url = `https://www.fourtonfish.com/hellosalut/hello/?lang=${languageCode}`;

        $.get(url, function(data) {
            $('#hello').text(data.hello);
        });
    });
});
