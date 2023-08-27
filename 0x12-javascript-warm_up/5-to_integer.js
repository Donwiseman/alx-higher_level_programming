#!/usr/bin/node
// Prints the number  if the first argument can be converted to an integer.
const argv = process.argv;
let value;
if (argv[2]) {
  value = parseInt(argv[2], 10);
}
if (value) {
  console.log('My number: ' + value);
} else {
  console.log('Not a number');
}
