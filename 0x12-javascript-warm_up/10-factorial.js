#!/usr/bin/node
// Compute factorial with Javascript

const x = parseInt(process.argv[2]);

function findFactorial (x) {
  if (!x) { return 1; }

  if (x <= 0) { return; }
  return findFactorial(x - 1) * x;
}

console.log(findFactorial(x));
