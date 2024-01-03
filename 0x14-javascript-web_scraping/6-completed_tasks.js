#!/usr/bin/node
const url = process.argv[2];
const request = require('request');
request(url, function (error, response, body) {
  if (error) console.log(error);
  else {
    const todos = JSON.parse(body);
    const tasks = {};
    for (const t in todos) {
      if (todos[t].completed === true) {
        if (tasks[todos[t].userId]) tasks[todos[t].userId]++;
        else tasks[todos[t].userId] = 1;
      }
    }
    console.log(tasks);
  }
});
