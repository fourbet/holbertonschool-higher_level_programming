#!/usr/bin/node
let msg;
if ((process.argv[2] === undefined)) {
  msg = 'No argument';
} else if ((process.argv[3] === undefined)) {
  msg = 'Argument found';
} else {
  msg = 'Arguments found';
}
console.log(msg);
