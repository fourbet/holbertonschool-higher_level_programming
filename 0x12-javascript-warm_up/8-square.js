#!/usr/bin/node
const nbr = parseInt(process.argv[2]);
if (Number.isNaN(nbr) === true) {
  console.log('Missing size');
} else {
  let string = '';
  for (let i = 0; i < nbr; i++) {
    string += 'X';
  } for (let i = 0; i < nbr; i++) {
    console.log(string);
  }
}
