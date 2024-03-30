#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  let count = 0;
  let index = 0;

  while (index < list.length) {
    if (searchElement === list[index]) count++;
    index++;
  }

  return count;
};
