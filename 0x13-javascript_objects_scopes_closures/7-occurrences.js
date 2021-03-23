#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let nbr = 0;
  for (const element of list) {
    if (element === searchElement) {
      nbr += 1;
    }
  }
  return nbr;
};
