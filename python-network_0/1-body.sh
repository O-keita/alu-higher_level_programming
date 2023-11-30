#!/bin/bash

# Check if a URL is provided
if [ -z "$1" ]; then
  echo "Usage: $0 <URL>"
  exit 1
fi

# Get the URL from the command line argument
url="$1"

# Use curl to fetch the URL and display the body for 200 status code
response=$(curl -sSL -w "%{http_code}" "$url")

# Extract the status code
status_code=$(echo "$response" | tail -n1)

# Check if the status code is 200
if [ "$status_code" -eq 200 ]; then
  # Display the response body
  echo "Response Body:"
  echo "$response" | head -n -1
else
  echo "Error: HTTP status code $status_code"
fi

