#!/usr/bin/node
// Import the 'request' module.
const request = require('request');

request.get(process.argv[2])

  .on('response', function (response) {
    // Set up an event listener for the 'response' event emitted by the HTTP request.

    console.log(`code: ${response.statusCode}`);
    // Log the HTTP status code of the response to the console.
  });

