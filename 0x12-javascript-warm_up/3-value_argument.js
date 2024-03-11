#!/usr/bin/node
const { argv } = require('node:process');
if (!argv[2]) {
  console.log('No argument');
}
if (argv[2]) {
  console.log(argv[2]);
}
