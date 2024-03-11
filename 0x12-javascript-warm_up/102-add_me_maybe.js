#!/usr/bin/node
function addMeMaybe (number, func) {
  func(++number);
}

module.exports = { addMeMaybe };
