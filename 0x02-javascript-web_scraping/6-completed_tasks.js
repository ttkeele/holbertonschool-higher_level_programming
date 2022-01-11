#!/usr/bin/node

const request = require('request');
const url = process.argv[2];
request.get(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const todo = JSON.parse(body);
    const completed = {};
    for (const i of todo) {
      if (i.completed === true) {
        if (i.userId in completed) {
	  completed[i.userId]++;
        } else {
	  completed[i.userId] = 1;
        }
      }
    }
    console.log(completed);
  }
});
