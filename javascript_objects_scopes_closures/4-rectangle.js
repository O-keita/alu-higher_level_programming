#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (w <= 0 || h <= 0 || !Number.isInteger(w) || !Number.isInteger(h)) return null;
    this.width = w;
    this.height = h;
  }

  print () {
    let rec = '';
    for (let i = 0; i < this.height; i++) {
      for (let j = 0; j < this.width; j++) {
        rec = rec + 'X';
      }

      console.log(rec);
      rec = '';
    }
  }

  rotate () {
    const newWidth = this.width;

    this.width = this.height;
    this.height = newWidth;
  }

  double () {
    this.width *= 2;
    this.height *= 2;
  }
}

module.exports = Rectangle;
