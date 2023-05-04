#!/usr/bin/node

/*
      * Script that prints all characters of a Star Wars movie:
      * The first argument is the Movie ID - example: 3 = “Return of the Jedi”
      * Display one character name by line
      * must use the Star wars API
      * must use the module request
  */

const request = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];

request(url, function (err, response, body) {
  if (err) {
    console.log(err);
  } else {
    const characters = JSON.parse(body).characters;
    for (const character of characters) {
      request(character, function (err, response, body) {
        if (err) {
          console.log(err);
        } else {
          console.log(JSON.parse(body).name);
        }
      });
    }
  }
});
