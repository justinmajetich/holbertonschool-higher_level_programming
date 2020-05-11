#!/usr/bin/node

exports.esrever = function (list) {
  const rList = [];
  for (let i = list.length - 1; i >= 0; i--) { rList.push(list[i]); }
  return rList;
};
