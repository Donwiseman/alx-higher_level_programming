#!/usr/bin/node
// This write the contents passed as argument to a file also passed
const fs = require('fs');
const argv = process.argv;
try {
  const data = fs.writeFileSync(argv[2], argv[3], 'utf8');
} catch (error) {
  console.error(error);
}
