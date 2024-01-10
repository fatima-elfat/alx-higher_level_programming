$('#add_item').click(function () {
  $('ul.my_list').append('<li>Item</li>');
});
$('DIV#remove_item').click(function () {
  const i = $('ul.my_list li');
  if (i.length > 0) {
    i[i.length - 1].remove();
  }
});
$('DIV#clear_list').click(function () {
  $('ul.my_list').empty();
});
