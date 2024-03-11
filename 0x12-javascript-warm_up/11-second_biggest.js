#!/usr/bin/node
const { argv } = require('node:process');

if (argv.length < 4) {
  console.log(0);
} else {
  const list = argv.slice(2).map(Number).sort().reverse();
  console.log(list[1]);
}
