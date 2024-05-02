$(function () {
  $('DIV#red_header').on('click', function () {
    $('header').addClass('red');
  });
  $('DIV#red_header').css('cursor', 'pointer');
});
