#!/usr/bin/node
// prints all characters of a Star Wars movie

const request = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];

request(url, (err, res, body) => {
  if (err) {
    console.log(err);
  } else {
    const charactersUrls = JSON.parse(body).characters;

    function getCharacterByName (charactersUrls) {
      if (charactersUrls.length === 0) {
        return;
      }
      const url = charactersUrls.shift();
      request(url, (err, res, body) => {
        if (err) {
          console.log(err);
        } else {
          console.log(JSON.parse(body).name);
        }
        getCharacterByName(charactersUrls);
      });
    }
    getCharacterByName(charactersUrls);
  }
});
