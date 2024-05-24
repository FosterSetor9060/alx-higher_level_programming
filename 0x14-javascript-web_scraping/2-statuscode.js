#!/usr/bin/node
// checks wether there are exactly 3 arguments 
const request = require('request');

if (process.argv.length !== 3) {
  console.log('Usage: ./2-statuscode.js <URL>');
  process.exit(1);
}

const url = process.argv[2];

request.get(url).on('response', function (response) {
  console.log(`code: ${response.statusCode}`);
});

