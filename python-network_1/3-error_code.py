#!/usr/bin/python3
"""3-error_code.py"""


import urllib.request
import urllib.error
import sys

def fetch_url(url):
    """
    Fetches the content of a URL and prints the decoded body.

    Args:
        url (str): The URL to fetch.

    Raises:
        urllib.error.HTTPError: If the HTTP request returns an error status code.
    """
    try:
        # Open the URL and read the response
        with urllib.request.urlopen(url) as response:
            # Decode the response body using UTF-8 and print it
            body = response.read().decode('utf-8')
            print(body)
    except urllib.error.HTTPError as e:
        # Handle HTTPError by printing the error code
        print(f"Error code: {e.code}")

if __name__ == "__main__":
    # Check if the correct number of command-line arguments is provided
    if len(sys.argv) != 2:
        print("Usage: python script.py <URL>")
        sys.exit(1)

    # Extract the URL from the command-line argument
    url = sys.argv[1]

    # Call the fetch_url function with the provided URL
    fetch_url(url)
