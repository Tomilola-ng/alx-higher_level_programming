#!/usr/bin/node

const fs = require("fs");
const filePath = process.argv[2];
const stringToWrite = process.argv[3];

fs.writeFile(filePath, stringToWrite, function (err) {
  if (err) {
    return console.log(err);
  }
});
