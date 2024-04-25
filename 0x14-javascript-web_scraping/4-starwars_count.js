#!/usr/bin/node

const request = require("request");
const apiUrl = process.argv[2];

request(apiUrl, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const films = JSON.parse(body).results;

    let count = 0;

    for (const film of films) {
      if (film.characters.endsWith("/18/")) {
        count++;
      }
    }

    console.log(count);
  }
});
