#!/usr/bin/node
// prints a message depending of the number of arguments passed
const argv = process.argv;
let x = 0;
argv.forEach((val, index) => {
  x++;
});
if (x < 3) {
  console.log('No argument');
} else if (x === 3) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
