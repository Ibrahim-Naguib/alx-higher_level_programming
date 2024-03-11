#!/usr/bin/node
const { argv } = require('node:process');
const arg = parseInt(argv[2]);
if (isNaN(arg)) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < arg; i++) {
    console.log('C is fun');
  }
}
