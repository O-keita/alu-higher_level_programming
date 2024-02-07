#!/usr/bin/node

const request = require('request');
const fs = require('fs');

const streamFile = (url, path) => {
  request(url).pipe(fs.createWriteStream(url));
};

if (require.main === module) {
  if (process.argv.length !== 4) {
    console.log('Please provide your argument');
  } else {
    const url = process.argv[2];
    const path = process.argv[3];

    streamFile(url, path);
  }
}
