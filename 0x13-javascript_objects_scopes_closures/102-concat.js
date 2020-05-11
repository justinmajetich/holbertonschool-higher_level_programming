#!/usr/bin/node
const fs = require('fs');
const file1 = process.argv[2];
const file2 = process.argv[3];

const content1 = fs.readFileSync(file1);
const content2 = fs.readFileSync(file2);

const contentNew = content1 + content2;

fs.writeFile(process.argv[4], contentNew, 'utf-8', (err) => {
  if (err) {
    throw err;
  }
});
