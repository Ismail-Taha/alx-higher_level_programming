#!/usr/bin/node
const fileSystem = require('fs');

const fArg = fileSystem.readFileSync(process.argv[2]).toString();
const sArg = fileSystem.readFileSync(process.argv[3]).toString();
fileSystem.writeFileSync(process.argv[4], fArg + sArg);