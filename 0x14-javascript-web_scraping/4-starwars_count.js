#!/usr/bin/node
const req = require('request');
req(process.argv[2], function (err, res, body) {
  if (!err) {
    const films = JSON.parse(body).results;
    console.log(films.reduce((acc, film) => {
      return film.characters.find((char) => char.endsWith('/18/'))
	? acc + 1
	: acc;
    }, 0));
  }
});
