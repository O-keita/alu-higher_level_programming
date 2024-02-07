#!/usr/bin/node

const fs = require('fs');

const readFiles = (path) => {
  try {
    const content = fs.readFileSync(path, 'utf-8');

    console.log(content);
  } catch (error) {
    console.log(error);
  }
};

if (require.main === module) {
  if (process.argv.length !== 3) {
    console.log('Please Provide a file ');
  } else {
    const path = process.argv[2];
    readFiles(path);
  }
}
