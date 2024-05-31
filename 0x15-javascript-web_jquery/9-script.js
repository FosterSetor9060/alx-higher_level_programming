$(document).ready(function() {
    // Fetch the translation of "hello" in French and display it in the DIV#hello element
    $.get('https://hellosalut.stefanbohacek.dev/?lang=fr', function(data) {
        $('#hello').text(data.hello);
    });
});

