#!/usr/bin/python3
"""4-hbtn_status.py"""


import requests

def fetch_and_display_status():
    """
    Fetches the content of https://alu-intranet.hbtn.io/status using the requests package
    and displays the response body with tabulation before each line.
    """
    url = "https://alu-intranet.hbtn.io/status"

    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an HTTPError for bad responses (4xx or 5xx)

        # Display the response body with tabulation before each line
        print("\t- {}".format(response.text))
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")

# Execute the function
fetch_and_display_status()
