//  This script updates the text of the <header> element to "New Header!
// It uses the jQuery API for DOM manipulation.
 

$(document).ready(function() {
  $('#update_header').click(function() {
    $('header').text('New Header!!!');
  });
});

