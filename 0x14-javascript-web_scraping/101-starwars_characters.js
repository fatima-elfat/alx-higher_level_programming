#!/usr/bin/node
const url = 'https://swapi-api.alx-tools.com/api/films/';
const id_ = process.argv[2];
const request = require('request');
request(url + id_, function (error, response, body) {
  if (error) console.log(error);
  else {
    const c = JSON.parse(body).characters;
    getchars(0, c);
  }
});
function getchars (i, c) {
  request(c[i], function (error, response, body) {
    if (error) console.log(error);
    else {
      console.log(JSON.parse(body).name);
      if (c.length > i + 1) getchars(i + 1, c);
    }
  });
}
