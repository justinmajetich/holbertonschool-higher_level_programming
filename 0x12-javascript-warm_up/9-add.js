#!/usr/bin/node
// Basic addition with Javascript

const a = parseInt(process.argv[2]);
const b = parseInt(process.argv[3]);

function add (a, b) {
  console.log(a + b);
}

add(a, b);
