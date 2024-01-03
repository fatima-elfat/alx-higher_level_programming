#!/usr/bin/node
const url = 'https://swapi-api.alx-tools.com/api/films/';
const id_ = process.argv[2];
const request = require('request');
request(url + id_, function (error, response, body) {
  if (error) console.log(error);
  else console.log(JSON.parse(body).title);
});
