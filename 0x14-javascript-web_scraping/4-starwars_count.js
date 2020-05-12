#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
const wedge = 'https://swapi-api.hbtn.io/api/people/18/';

request(url, (error, response, body) => {
  if (error) { console.log(error); }
  const jsonBody = JSON.parse(body);
  let wedgeCount = 0;
  for (const result of jsonBody.results) {
    if (result.characters.includes(wedge)) {
      wedgeCount++;
    }
  }
  console.log(wedgeCount);
});
