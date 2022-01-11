#!/usr/bin/node

const request = require('request');
const movie_id = process.argv[2];
const url = 'https://swapi-api.hbtn.io/api/films/' + movie_id;
request.get(url , function (error, response, body) {
  if (error) {
    console.error(error);
  }
  console.log(JSON.parse(body).title);
});
