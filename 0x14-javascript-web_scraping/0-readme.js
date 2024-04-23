#!/usr/bin/node

const fs = require('node:fs');

const file = process.argv[2];
fs.readFile(file, 'utf-8', function (error, content) {
  console.log(error || content);
});
