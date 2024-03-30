#!/usr/bin/node

let numIcr = 0;

exports.logMe = function (item) {
  console.log(numIcr + ": " + item);
  numIcr++;
};
