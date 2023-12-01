#!/usr/bin/python3

import urllib.request
import urllib.error
import sys

def fetch_url(url):
    try:
        # Open the URL and read the response
        with urllib.request.urlopen(url) as response:
            # Decode the response body using UTF-8 and print it
            body = response.read().decode('utf-8')
            print(body)
    except urllib.error.HTTPError as e:
        # Handle HTTPError by printing the error code
        print(f"Error code: {e.code}")

# Test the script with a URL (assuming the web server is running on port 5000)
if __name__ == "__main__":
    # Replace this URL with the actual URL you want to test against
    test_url = "http://localhost:5000"
    fetch_url(test_url)
