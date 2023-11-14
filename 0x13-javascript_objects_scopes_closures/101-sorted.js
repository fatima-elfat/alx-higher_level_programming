#!/usr/bin/node

const dict = require('./101-data').dict;

let dikt = {};
for (let key in dict) {
  const listk = [];
  if (dikt[dict[key]] === undefined) {
    dikt[dict[key]] = [];
  }
  listk.unshift(key);
  dikt[dict[key]] = listk;
}

console.log(dikt);
