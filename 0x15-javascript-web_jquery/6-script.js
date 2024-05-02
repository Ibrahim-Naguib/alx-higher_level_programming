$(function () {
  $('DIV#update_header').on('click', function () {
    $('header').text('New Header!!!');
  });
  $('DIV#update_header').css('cursor', 'pointer');
});
