#!/usr/bin/node

const { argv } = require('node:process');

function add (a, b) {
  if (!Number(a) || !Number(b)) {
    return NaN;
  }

  return a + b;
}

console.log(add(argv[2], argv[3]));
