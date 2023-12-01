#!/usr/bin/python3
"""
2-post_email.py
"""

import requests
import sys

def get_x_request_id(url):
    """
    Sends a GET request to the specified URL and displays the value of the X-Request-Id variable
    in the response header.

    Args:
        url (str): The URL to send the GET request to.
    """
    try:
        # Send a GET request to the specified URL
        response = requests.get(url)
        
        # Raise an HTTPError for bad responses (4xx or 5xx)
        response.raise_for_status()

        # Retrieve and display the value of the X-Request-Id variable in the response header
        x_request_id = response.headers.get('X-Request-Id')
        if x_request_id:
            print(f"X-Request-Id: {x_request_id}")
        else:
            print("X-Request-Id not found in the response header.")
    except requests.exceptions.RequestException as e:
        # Handle exceptions raised during the request
        print(f"Error: {e}")

if __name__ == "__main__":
    # Replace this URL with the actual URL you want to test against
    test_url = "http://example.com"

    # Call the function with the provided URL
    get_x_request_id(test_url)
