#!/usr/bin/node

function computeFactorial (n) {
  if (isNaN(n)) {
    console.log(1);
    return 1;
  } else if (n <= 1) {
    console.log(1);
    return 1;
  } else {
    const result = BigInt(n) * BigInt(computeFactorial(n - 1));
    console.log(result.toString());
    return result;
  }
}

// Parse the first command-line argument as an integer
const input = parseInt(process.argv[2], 10);

// Example usage:
computeFactorial(input);
