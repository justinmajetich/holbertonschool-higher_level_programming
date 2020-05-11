#!/usr/bin/node
exports.converter = function (base) {
  return function (x) {
    return x.toString(base);
  };
};
