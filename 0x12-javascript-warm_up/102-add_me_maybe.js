#!/usr/bin/node
function addMeMaybe (number, theFunction) {
  number++;
  theFunction(number);
}

exports.addMeMaybe = addMeMaybe;
