#!/usr/bin/node

function computeFactorial (n, isFirstCall = true) {
  if (isNaN(n)) {
    if (isFirstCall) {
      console.log(1);
    }
    return 1;
  } else if (n <= 1) {
    if (isFirstCall) {
      console.log(1);
    }
    return 1;
  } else {
    const result = BigInt(n) * BigInt(computeFactorial(n - 1, false));
    if (isFirstCall) {
      console.log(result.toString());
    }
    return result;
  }
}

// Parse the first command-line argument as an integer
const input = process.argv[2] ? parseInt(process.argv[2], 10) : NaN;

// Example usage:
computeFactorial(input);
