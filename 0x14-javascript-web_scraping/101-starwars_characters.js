#!/usr/bin/node

const request = require("request");
const movieId = process.argv[2];

request.get(
  `https://swapi-api.alx-tools.com/api/films/${movieId}`,
  (error, response, body) => {
    if (error) {
      console.log(error);
    } else {
      const movie = JSON.parse(body);

      for (const characterUrl of movie.characters) {
        request.get(characterUrl, (error, response, body) => {
          if (error) {
            console.log(error);
          } else {
            const character = JSON.parse(body);
            console.log(character.name);
          }
        });
      }
    }
  }
);
