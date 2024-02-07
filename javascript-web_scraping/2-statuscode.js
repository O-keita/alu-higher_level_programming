#!/usr/bin/node

const request = require('request');

const statusCode = (url) => {
  request.get(url, (error, response) => {
    if (error) {
      console.log(`Error: ${error.message}`);
    } else {
      console.log(`Code: ${response.statusCode}`);
    }
  });
};

if (require.main === module) {
  if (process.argv.length !== 3) {
    console.log('Please provide a URL');
  } else {
    const url = process.argv[2];
    statusCode(url);
  }
}
