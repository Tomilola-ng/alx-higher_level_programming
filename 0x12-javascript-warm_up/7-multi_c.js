#!/usr/bin/node

const { argv } = require('node:process');

const isNumber = Number(argv[2]);

if (isNumber) {
  let i = 0;

  while (i < argv[2]) {
    console.log('C is fun');
    i++;
  }
} else {
  console.log('Missing number of occurrences');
}
