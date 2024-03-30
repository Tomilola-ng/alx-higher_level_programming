#!/usr/bin/node

class Rectangle {
  constructor(w, h) {
    if (h >= 1 && w >= 1) {
      this.width = w;
      this.height = h;
    }
  }

  print() {
    for (let row = 0; row < this.height; row++) {
      let shape = "";
      for (let col = 0; col < this.width; col++) {
        shape += "X";
      }
      console.log(shape);
    }
  }
}

module.exports = Rectangle;
