#!/usr/bin/node
function fact (nbr) {
  if (Number.isNaN(nbr) === true) {
    return 1;
  } if (nbr === 0 || nbr === 1) {
    return 1;
  } else {
    return (nbr * fact(nbr - 1));
  }
}
const res = fact(parseInt(process.argv[2]));
console.log(res);
