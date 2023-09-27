#!/usr/bin/node
// gets the contents of a webpage and stores it in a file.
const request = require('request');
const fs = require('fs');
const argv = process.argv;
request.get(argv[2], (error, response, body) => {
  if (error) {
    console.error('Error:', error);
  } else {
    if (response.statusCode === 200) {
      // Successful request
      try {
        fs.writeFileSync(argv[3], body, 'utf8');
      } catch (error) {
        console.error(error);
      }
    } else {
      // Handle other status codes as needed
      console.error('Error:', body);
    }
  }
});
