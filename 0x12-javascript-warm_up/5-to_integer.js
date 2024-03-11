#!/usr/bin/node
const { argv } = require('node:process');
const arg = parseInt(argv[2]);
if (isNaN(arg)) {
  console.log('Not a number');
} else {
  console.log('My number: ' + arg);
}
