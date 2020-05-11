#!/usr/bin/node
exports.logMe = function (item) {
  if (this.count === undefined) { this.count = 0; } else { this.count++; }
  const line = this.count + ': ' + item;
  console.log(line);
};
