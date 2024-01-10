$('document').ready(function () {
  $.get('https://hellosalut.stefanbohacek.dev/?lang=fr', function (responce) {
    $('DIV#hello').text(responce.hello);
  });
});
