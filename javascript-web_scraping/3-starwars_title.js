#!/usr/bin/node

const request = require('request');

const printTitle = (movieId) => {
  const url = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

  request.get(url, (error, response, body) => {
    if (error) {
      console.log(`Error: ${error}`);
    } else {
      try {
        const movie = JSON.parse(body);
        console.log(`${movie.title}`);
      } catch (parseError) {
        console.log(parseError.message);
      }
    }
  });
};

if (require.main === module) {
  if (process.argv.length !== 3) {
    console.log('Please provide movie ID');
  } else {
    const movieId = process.argv[2];

    printTitle(movieId);
  }
}
