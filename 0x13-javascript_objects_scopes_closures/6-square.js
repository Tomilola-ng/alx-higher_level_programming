#!/usr/bin/node

const MainSquare = require("./5-square");

class Square extends MainSquare {
  charPrint(c) {
    if (c === undefined) c = "X";

    for (let row = 0; row < this.height; row++) {
      let shape = "";
      for (let col = 0; col < this.width; col++) {
        shape += c;
      }
      console.log(shape);
    }
  }
}

module.exports = Square;
