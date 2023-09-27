#!/usr/bin/node
// Uses Request module to access the SWAPI and amount of films of character 18
const argv = process.argv;
const request = require('request');
const url = argv[2];
const match = 'https://swapi-api.alx-tools.com/api/people/18/';
let num = 0;
request.get(url, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
  } else {
    if (response.statusCode === 200) {
      // Parse the JSON response
      const data = JSON.parse(body);

      // Now you can work with the JSON data
      const count = data.count;
      for (let i = 0; i < count; i++) {
        const charLists = data.results[i].characters;
        if (charLists.includes(match)) {
          num++;
        }
      }
      console.log(num);
    } else {
      console.error('Error:', body);
    }
  }
});
