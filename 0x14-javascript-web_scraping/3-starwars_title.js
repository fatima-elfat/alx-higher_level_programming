#!/usr/bin/node
const url = 'http://swapi.co/api/films/';
const id_ = process.argv[2];
const request = require('request');
request(url + id_, function (error, response, body) {
  if (error) console.log(error);
  else if (response.statusCode === 200) {
    const a = JSON.parse(body);
    console.log(a.title);
  } else console.log('Erorr Code:' + response.statusCode);
});
