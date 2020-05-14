$.ajax({
  type: 'GET',
  url: 'https://swapi-api.hbtn.io/api/people/5/?format=json',
  success: (character) => {
    $('DIV#character').text(character.name);
  }
});
