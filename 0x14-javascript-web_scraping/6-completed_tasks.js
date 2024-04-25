#!/usr/bin/node

const request = require("request");
const apiUrl = process.argv[2];

const result = {};

request(apiUrl, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const todos = JSON.parse(body);

    const completedTasks = {};

    for (const todo of todos) {
      if (todo.completed) {
        completedTasks[todo.userId] = (completedTasks[todo.userId] || 0) + 1;
      }
    }

    console.log(completedTasks);
  }
});
