#!/usr/bin/node

class Rectangle {
  constructor(w, h) {
    if (h >= 1 && w >= 1) {
      this.width = w;
      this.height = h;
    }
  }
}

module.exports = Rectangle;
