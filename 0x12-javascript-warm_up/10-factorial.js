#!/usr/bin/node

const { argv } = require('node:process');

function factorial (counter) {
  if (isNaN(counter) || counter === 1) return 1;

  return counter * factorial(counter - 1);
}

console.log(factorial(parseInt(argv[2])));
