#!/usr/bin/node
const nbr = parseInt(process.argv[2]);
if (Number.isNaN(nbr) === true) {
  console.log('Not a number');
} else {
  console.log('My number: ' + nbr);
}
