#!/usr/bin/node
// Compute factorial with Javascript

let argv = process.argv;

if (argv.length < 4) { console.log(0); } else {
  // Strip extraneous args
  argv = argv.slice(2);
  // Convert elems to ints and sort
  const nums = argv.map(x => parseInt(x)).sort();
  // Find max int in list
  console.log(nums[nums.length - 2]);
}
