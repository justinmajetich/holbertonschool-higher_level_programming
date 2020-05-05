#!/usr/bin/node
// Basic print with Javascript

const fun = 'C is fun';

if (process.argv.length >= 3) {
  let i = process.argv[2];
  while (i > 0) {
    console.log(fun);
    i--;
  }
} else {
  console.log('Missing number of occurrences');
}
