window.onload = () => {
  $('INPUT#btn_translate').click(() => {
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
  });
};
