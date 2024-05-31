//This script fetches the character name from the SWAPI API and

$(document).ready(function() {
  $.ajax({
    url: 'https://swapi-api.alx-tools.com/api/people/5/?format=json',
    method: 'GET',
    success: function(data) {
      $('#character').text(data.name);
    }
  });
});
