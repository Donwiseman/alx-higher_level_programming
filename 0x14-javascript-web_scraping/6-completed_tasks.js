#!/usr/bin/node
// Uses Request module to access an API and get number of completed tasks.
const argv = process.argv;
const request = require('request');
const url = argv[2];
const taskDone = {
  1: 0,
  2: 0,
  3: 0,
  4: 0,
  5: 0,
  6: 0,
  7: 0,
  8: 0,
  9: 0,
  10: 0
};
request.get(url, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
  } else {
    if (response.statusCode === 200) {
      // Parse the JSON response
      const data = JSON.parse(body);

      // Now you can work with the JSON data
      data.forEach(function (task) {
        if (task.completed) {
          taskDone[task.userId]++;
        }
      });
      console.log(taskDone);
    } else {
      console.error('Error:', body);
    }
  }
});
