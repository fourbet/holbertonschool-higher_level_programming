#!/usr/bin/node
const nbr = parseInt(process.argv[2]);
if (Number.isNaN(nbr) === true) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < nbr; i++) {
    console.log('C is fun');
  }
}
