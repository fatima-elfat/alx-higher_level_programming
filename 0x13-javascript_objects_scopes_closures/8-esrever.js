#!/usr/bin/node

exports.esrever = function (list) {
  let a = 0;
  let len = list.length;
  while (a < len - 1) {
    let r = list[a];
    list[a] = list[len - 1];
    list[len - 1] = r;
    len--;
    a++;
  }
  return list;
};
