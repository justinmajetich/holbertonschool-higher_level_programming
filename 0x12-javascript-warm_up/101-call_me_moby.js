#!/usr/bin/node
exports.callMeMoby = function (x, func) {
  for (;x > 0; x--) { func(); }
};
