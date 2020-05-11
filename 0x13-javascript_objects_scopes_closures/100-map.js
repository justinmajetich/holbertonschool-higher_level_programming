#!/usr/bin/node
const list = require('./100-data.js').list;

const mappedList = list.map(function (value, index) {
  return value * index;
});

console.log(list);
console.log(mappedList);
