$(function () {
  $('INPUT#btn_translate, INPUT#language_code').on(
    'click keypress',
    function (e) {
      if (e.type === 'click' || (e.type === 'keypress' && e.key === 'Enter')) {
        $.post(
          'https://hellosalut.stefanbohacek.dev',
          {
            lang: $('INPUT#language_code').val()
          },
          function (data) {
            $('DIV#hello').html(data.hello);
          }
        );
      }
    }
  );
});
