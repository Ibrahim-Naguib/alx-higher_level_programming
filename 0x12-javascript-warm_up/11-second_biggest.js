#!/usr/bin/node
const { argv } = require('node:process');

const list = argv.sort().reverse();
if (argv.length < 4) {
  console.log(0);
} else {
  console.log(+list[1]);
}
