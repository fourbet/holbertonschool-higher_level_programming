#!/usr/bin/node
const request = require('request');

request('https://swapi-api.hbtn.io/api/films/' + process.argv[2], function (error, response, body) {
  if (error) {
    console.log('error:', error);
  } else {
    JSON.parse(body).characters.forEach(function (urlChar, callback) {
      request(urlChar, function (error, response, body) {
        if (error) {
          console.log('error:', error);
        } else {
          console.log(JSON.parse(body).name);
        }
      });
    });
  }
});
