#!/usr/bin/node

const message = (arg) => {
  if (typeof arg === 'undefined') {
    console.log('No argument');
  } else {
    console.log('Arguments found');
  }
};

