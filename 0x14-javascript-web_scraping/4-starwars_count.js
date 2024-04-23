#!/usr/bin/node

const request = require('request');

const url = process.argv[2];
let count = 0;
request(url, function (err, res, body) {
  if (err) {
    console.log(err);
  } else {
    const content = JSON.parse(body).results;
    content.forEach((film) => {
      film.characters.forEach((char) => {
        if (char.endsWith('/18/')) {
          count += 1;
        }
      });
    });
    console.log(count);
  }
});
