$.ajax({
  type: 'POST',
  url: 'https://fourtonfish.com/hellosalut/?lang=fr',
  success: (translation) => {
    $('DIV#hello').text(translation.hello);
  },
  error: () => {
    console.log('Error loading orders');
  }
});
