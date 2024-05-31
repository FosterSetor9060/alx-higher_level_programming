/**
 * This script adds a new <li> element with the text 'Item' to the <ul> element
 * with the class 'my_list' whenever the <div> element with the id 'add_item' is clicked.
 * It uses the jQuery API for DOM manipulation.
 */

$(document).ready(function() {
  $('#add_item').click(function() {
    $('.my_list').append('<li>Item</li>');
  });
});

