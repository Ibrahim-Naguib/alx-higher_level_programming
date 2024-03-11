#!/usr/bin/node
const { argv } = require('node:process');
const arg = parseInt(argv[2]);
if (isNaN(arg)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < arg; i++) {
    let row = '';
    for (let j = 0; j < arg; j++) {
      row += 'X';
    }
    console.log(row);
  }
}
