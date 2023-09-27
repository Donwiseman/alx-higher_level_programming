#!/usr/bin/node
// Uses Request module to access the SWAPI and get episode names
const argv = process.argv;
const request = require('request');
const url = 'https://swapi-api.alx-tools.com/api/films/' + argv[2];
request.get(url, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
  } else {
    if (response.statusCode === 200) {
      // Parse the JSON response
      const data = JSON.parse(body);

      // Now you can work with the JSON data
      console.log(data.title);
    } else {
      console.error('Error:', body);
    }
  }
});
