#!/usr/bin/node

exports.esrever = function (list) {
  const changed = [];

  for (let i = list.length - 1; i >= 0; i--) {
    changed.push(list[i]);
  }
  return changed;
};
