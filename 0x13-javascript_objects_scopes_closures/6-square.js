#!/usr/bin/node

const SquareA = require('./5-square');

class Square extends SquareA {
  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }
    for (let i = 0; i < this.width; i += 1) {
      console.log(c.repeat(this.height));
    }
  }
}

module.exports = Square;
