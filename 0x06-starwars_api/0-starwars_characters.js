#!/usr/bin/node
// prints all characters of a Star Wars movie

const request = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];

request(url, async (err, res, body) => {
  if (err) {
    console.log(err);
  } else {
    const charactersUrl = await JSON.parse(body).characters;
    charactersUrl.forEach((characterUrl) => {
      request(characterUrl, async (err, res, body) => {
        if (err) {
          console.log(err);
        } else {
          console.log(await JSON.parse(body).name);
        }
      });
    });
  }
});
