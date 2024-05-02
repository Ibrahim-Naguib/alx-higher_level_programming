$(function () {
  $('DIV#toggle_header').on('click', function () {
    $('header').toggleClass('green red');
  });
  $('DIV#toggle_header').css('cursor', 'pointer');
});
