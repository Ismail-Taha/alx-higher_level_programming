#!/usr/bin/node
const request = require('request');
const movieId = process.argv[2];
const url = `https://swapi.dev/api/films/${movieId}/`;

request(url, function (error, response, body) {
  if (!error && response.statusCode === 200) {
    const characters = JSON.parse(body).characters;
    characters.forEach((characterUrl) => {
      request(characterUrl, function (error, response, body) {
        if (!error && response.statusCode === 200) {
          console.log(JSON.parse(body).name);
        }
      });
    });
  }
});
