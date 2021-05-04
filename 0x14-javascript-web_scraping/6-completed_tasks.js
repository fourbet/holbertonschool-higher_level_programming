#!/usr/bin/node
const request = require('request');

request(process.argv[2], function (error, response, body) {
  if (error) {
    console.log('error:', error);
  } else {
    const dict = JSON.parse(body).reduce((acc, curr) => {
      if (!acc[curr.userId]) {
        if (curr.completed) {
          acc[curr.userId] = 1;
        }
      } else {
        if (curr.completed) {
          acc[curr.userId] += 1;
        }
      }
      return acc;
    }, {});
    console.log(dict);
  }
});
