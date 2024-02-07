#!/usr/bin/node

const request = require('request');

const countMovies = (url) => {
  request.get(url, (error, response, body) => {
    if (error) {
      console.error(`${error}`);
    } else {
      try {
        const results = JSON.parse(body).results;

        console.log(results.reduce((count, movie) => (
          movie.characters.find((character) => character.endsWith('/18/')) ? count + 1 : count
        ), 0));
      } catch (parseError) {
        console.error(parseError);
      }
    }
  });
};

if (require.main === module) {
  if (process.argv.length !== 3) {
    console.error('Please enter a URL');
  } else {
    const url = process.argv[2];
    countMovies(url);
  }
}
