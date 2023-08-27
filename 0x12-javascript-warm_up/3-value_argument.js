#!/usr/bin/node
// Prints the first argument passed to it
const argv = process.argv;
let x = 0;
argv.forEach((val, index) => {
  x++;
});
if (x < 3) {
  console.log('No argument');
} else {
  console.log(argv[2]);
}
