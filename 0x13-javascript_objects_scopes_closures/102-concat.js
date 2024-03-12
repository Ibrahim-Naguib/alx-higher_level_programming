#!/usr/bin/node

const { argv } = require('node:process');
const fs = require('node:fs');

const file1 = fs.readFileSync(argv[2]).toString();
const file2 = fs.readFileSync(argv[3]).toString();

fs.writeFileSync(argv[4], file1 + file2);
