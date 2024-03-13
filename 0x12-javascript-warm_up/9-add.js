#!/usr/bin/node

const { argv } = require('node:process');

function add (a, b) {
  return (Number(a) + Number(b));
}

if (argv.length < 4) {
  console.log('NaN');
} else {
  console.log(add(argv[2], argv[3]));
}
