#!/usr/bin/node
let msg;
if ((process.argv[2] === undefined)) {
  msg = 'No argument';
} else {
  msg = process.argv[2];
}
console.log(msg);
