#!/usr/bin/python3
""" 3-error_code.py """


import urllib.request
import urllib.error
import sys

def fetch_url_content(url):
    """
    Fetches the content of a URL and displays it.

    Args:
        url (str): The URL to fetch content from.

    Returns:
        None: Displays the content or handles HTTPError and prints the error code.
    """
    try:
        with urllib.request.urlopen(url) as response:
            content = response.read().decode('utf-8')
            print(content)
    except urllib.error.HTTPError as e:
        # Handle HTTPError exceptions
        print(f"Error code: {e.code}")

def main():
    """
    Main function to handle command-line arguments and execute the script.
    """
    # Check if the correct number of arguments is provided
    if len(sys.argv) != 2:
        print("Usage: python script.py <URL>")
        sys.exit(1)

    # Use the provided URL from command-line arguments
    url = sys.argv[1]

    # Call the fetch_url_content function with the provided URL
    fetch_url_content(url)

# Check if the script is executed directly
if __name__ == "__main__":
    # Execute the main function
    main()
