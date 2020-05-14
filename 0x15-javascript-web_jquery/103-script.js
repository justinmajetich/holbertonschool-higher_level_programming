function postLang () {
  const lang = $('INPUT#language_code').val();
  $.ajax({
    type: 'POST',
    url: 'https://fourtonfish.com/hellosalut/?lang=' + lang,
    success: (translation) => {
      $('DIV#hello').text(translation.hello);
    },
    error: () => {
      console.log('Error loading orders');
    }
  });
}

window.onload = () => {
  $('INPUT#btn_translate').focus(() => {
    $('INPUT#btn_translate').keypress((key) => {
      if (key.which === 13) {
        postLang();
      }
    });
    $('INPUT#btn_translate').click(() => {
      postLang();
    });
  });
};
