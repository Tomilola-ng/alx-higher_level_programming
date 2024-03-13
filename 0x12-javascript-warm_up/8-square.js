#!/usr/bin/node

const { argv } = require('node:process');

const isNumber = Number(argv[2]);

if (!isNumber) {
  console.log('Missing size');
} else {
  let i = 0;

  while (i < argv[2]) {
    let xList = '';

    for (let j = 0; j < argv[2]; j++) {
      xList += 'X';
    }

    console.log(xList);
    i++;
  }
}
