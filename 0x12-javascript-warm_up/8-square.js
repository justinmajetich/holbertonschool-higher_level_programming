#!/usr/bin/node
// Basic print with Javascript

if (process.argv.length >= 3) {
  const size = process.argv[2];
  let i = 0;
  while (i < size) {
    const row = 'X'.repeat(size);
    console.log(row);
    i++;
  }
} else {
  console.log('Missing size');
}
