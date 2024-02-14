#!/usr/bin/node

const { dict } = require('./101-data');

const userIDsByOccurrence = {};

for (const [userID, occurrence] of Object.entries(dict)) {
  if (!userIDsByOccurrence[occurrence]) {
    userIDsByOccurrence[occurrence] = [];
  }
  userIDsByOccurrence[occurrence].push(userID);
}

console.log(userIDsByOccurrence);

