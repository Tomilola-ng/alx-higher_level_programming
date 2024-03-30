#!/usr/bin/node

let myDict = require("./101-data.js").dict;

let newDict = {};

for (let key in myDict) {
  if (newDict[myDict[key]] === undefined) {
    newDict[myDict[key]] = [];
  }
  newDict[myDict[key]].push(key);
}
console.log(newDict);
