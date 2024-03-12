#!/usr/bin/node

const dict = require('./101-data').dict;

const newDict = {};

for (const userId in dict) {
  const value = dict[userId];

  if (!(value in newDict)) {
    newDict[value] = [];
  }

  newDict[value].push(userId);
}
console.log(newDict);
