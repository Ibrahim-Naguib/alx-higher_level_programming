#!/usr/bin/node
const { argv } = require('node:process');

const arg = +argv[2];

function factorial (num) {
  if (num === 1 || isNaN(num)) {
    return 1;
  }
  return num * factorial(num - 1);
}

console.log(factorial(arg));
