#!/usr/bin/node

let numrg = 0;
module.exports.logMe = function (item) {
  process.stdout.write(numrg + ': ' + item + '\n');
  numrg += 1;
};
