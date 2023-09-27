#!/usr/bin/node
// This reads the contents of a file passed as argument
const fs = require('fs');
const argv = process.argv;
try {
  const data = fs.readFileSync(argv[2], 'utf8');
  console.log(data);
} catch (error) {
  console.error(error)
}
