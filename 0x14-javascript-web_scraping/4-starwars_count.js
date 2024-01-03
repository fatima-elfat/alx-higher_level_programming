#!/usr/bin/node
const url = process.argv[2];
const request = require('request');
request(url, function (error, response, body) {
  if (error) console.log(error);
  else {
    const movies = JSON.parse(body);
    let count = 0;
    for (const m in movies) {
      const c = movies[m].c;
      for (const p in c) {
        if (c[p].includes('18')) count++;
      }
    }
    console.log(count);
  }
});
