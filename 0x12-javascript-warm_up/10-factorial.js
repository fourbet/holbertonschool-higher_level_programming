#!/usr/bin/node
function fact (nbr) {
  nbrInt = parseInt(nbr);
  if (nbrInt === 0 || nbrInt === 1) {
    return 1;
  }
  else {
  return (nbrInt * fact (nbrInt - 1));
  }
}
let res = fact (process.argv[2]);
console.log(res);
