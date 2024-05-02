$(function () {
  $('INPUT#btn_translate').on('click', function () {
    $.post(
      'https://hellosalut.stefanbohacek.dev',
      {
        lang: $('INPUT#language_code').val()
      },
      function (data) {
        $('DIV#hello').html(data.hello);
      }
    );
  });
});
