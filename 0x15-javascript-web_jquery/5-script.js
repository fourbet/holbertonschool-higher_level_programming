const list = $('UL.my_list');

$('DIV#add_item').click(function () {
  list.append('<li>Item</li>');
});
