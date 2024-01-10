$.get('https://swapi-api.alx-tools.com/api/people/5/?format=json', function (responce, status) {
  if (status === 'success') {
    $('DIV#character').text(responce.name);
  }
});
