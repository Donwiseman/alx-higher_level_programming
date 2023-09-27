#!/usr/bin/node
// Uses Request module to get a url and sipaly the status code
const argv = process.argv;
const request = require('request');
request.get(argv[2], (error, response, body) => {
  if (error) {
    console.error('Error:', error);
  } else {
    console.log('code:', response.statusCode);
  }
});
