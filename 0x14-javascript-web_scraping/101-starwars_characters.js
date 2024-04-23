#!/usr/bin/node

const request = require('request');

const id = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${id}`;

request.get(url, (err, res, body) => {
  if (err) {
    console.log(err);
  } else {
    const content = JSON.parse(body);
    const characters = content.characters;
    for (const char of characters) {
      request.get(char, (err, res, body) => {
        if (err) {
          console.log(err);
        } else {
          const name = JSON.parse(body);
          console.log(name.name);
        }
      });
    }
  }
});
