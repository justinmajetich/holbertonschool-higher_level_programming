#!/usr/bin/node
// Compute factorial with Javascript

let argv = process.argv;

if (argv.length < 4) { console.log(0); } else {
  // Strip extraneous args
  argv = argv.slice(2);
  // Convert elems to ints
  const nums = argv.map(x => parseInt(x));
  // Find max int in list
  const max = Math.max(...nums);
  console.log(max);
}
