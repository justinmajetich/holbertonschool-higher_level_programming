#!/usr/bin/node
const fs = require('fs');
const filePath = process.argv[2];

fs.readFile(filePath, 'utf-8', (error, data) => {
  if (error) { console.log(error); } else { console.log(data); }
});
