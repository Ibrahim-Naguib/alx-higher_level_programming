$(function () {
  $('DIV#add_item').on('click', function () {
    $('UL.my_list').append('<li>Item</li>');
  });
  $('DIV#add_item').css('cursor', 'pointer');
});
