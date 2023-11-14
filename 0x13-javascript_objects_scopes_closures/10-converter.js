#!/usr/bin/node

exports.converter = function (base) {
  return function (r) {
    return r.toString(base);
  }
};
