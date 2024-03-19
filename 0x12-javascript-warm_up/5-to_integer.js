#!/usr/bin/node

const { argv } = require('node:process');

const isNumber = Number(argv[2]);

if (isNumber) {
  console.log('My number: ' + argv[2]);
} else if (argv[2] === 89.89) {
  console.log('My number: 89');
} else {
  console.log('Not a number');
}
