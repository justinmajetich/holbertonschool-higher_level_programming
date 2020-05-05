#!/usr/bin/node
// Handle arguments with Javascript

let parsed = parseInt(process.argv[2]);

if (parsed) {
  parsed = 'My number: ' + parsed;
  console.log(parsed);
} else {
  console.log('Not a number');
}
