#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${movieId}`;
request(url, function (err, res, body) {
  console.log(err || JSON.parse(body).title);
});
