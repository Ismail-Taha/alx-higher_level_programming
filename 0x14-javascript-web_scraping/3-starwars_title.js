#!/usr/bin/node
const req = require('request');
const epNum = process.argv[2];
const API = 'https://swapi-api.hbtn.io/api/films/';

req(API + epNum, function (e, res, body) {
  if (e) {
    console.log(e);
  } else if (res.statusCode === 200) {
    const data = JSON.parse(body);
    console.log(data.title);
  } else {
    console.log('Error code: ' + res.statusCode);
  }
});
