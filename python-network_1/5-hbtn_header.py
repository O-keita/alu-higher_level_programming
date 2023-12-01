#!/usr/bin/python3
"""
 Sends a request to the specified URL and displays the value of the X-Request-Id variable
    in the response header.

    Args:
        url (str): The URL to send the request to.
"""


import requests
import sys

def get_x_request_id(url):
    """
    Sends a request to the specified URL and displays the value of the X-Request-Id variable
    in the response header.

    Args:
        url (str): The URL to send the request to.
    """
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an HTTPError for bad responses (4xx or 5xx)

        # Display the value of the X-Request-Id variable in the response header
        x_request_id = response.headers.get('X-Request-Id')
        if x_request_id:
            print(f"X-Request-Id: {x_request_id}")
        else:
            print("X-Request-Id not found in the response header.")
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    # Replace this URL with the actual URL you want to test against
    test_url = "http://example.com"

    # Call the function with the provided URL
    get_x_request_id(test_url)
