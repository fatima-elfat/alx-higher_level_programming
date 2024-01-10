$.get('https://swapi.co/api/films/?format=json', function (responce, status) {
  if (status === 'success') {
    $('ul#list_movies').append(...responce.results.map(movie => `<li>${movie.title}</li>`));
  }
});
