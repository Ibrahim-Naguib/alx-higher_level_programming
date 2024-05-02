$(function () {
  $('DIV#add_item').on('click', function () {
    $('UL.my_list').append('<li>Item</li>');
  });
  $('DIV#remove_item').on('click', function () {
    $('UL.my_list').children().last().remove();
  });
  $('DIV#clear_list').on('click', function () {
    $('UL.my_list').empty();
  });
  $('DIV#add_item, DIV#remove_item, DIV#clear_list').css('cursor', 'pointer');
});
