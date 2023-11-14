#!/usr/bin/node

let r = 0;

exports.logMe = function (item) {
  console.log(r + ': ' + item);
  r++;
};
