#!/usr/bin/node
const S = require('./5-square.js');
class Square extends S {
  charPrint (c) {
    let charP;
    if (c === undefined) {
      charP = 'X';
    } else {
      charP = c;
    }
    let string = '';
    for (let i = 0; i < this.width; i++) {
      string += charP;
    } for (let i = 0; i < this.width; i++) {
      console.log(string);
    }
  }
}
module.exports = Square;
