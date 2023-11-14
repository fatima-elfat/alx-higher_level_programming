#!/usr/bin/node

const dict = require('./101-data').dict;

const dikt = {};
for (const key in dict) {
  //const listk = [];
  if (dikt[dict[key]] === undefined) {
    dikt[dict[key]] = [];
  }
  //listk.unshift(key);
  //dikt[dict[key]] = listk;
  dikt[dict[key]].push(key);
}

console.log(dikt);
