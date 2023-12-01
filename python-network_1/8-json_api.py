#!/usr/bin/python3
""" module is documented as you can see"""


import requests
import sys

# Check if the correct number of arguments is provided
if len(sys.argv) != 2:
    # If no argument is given, set q to an empty string
    q = ""
else:
    # Use the provided argument as the value for q
    q = sys.argv[1]

# Define the URL for the POST request
url = "http://0.0.0.0:5000/search_user"
# Prepare the data to be sent in the POST request
data = {'q': q}

# Send a POST request to the specified URL with the provided data
response = requests.post(url, data=data)

try:
    # Try to parse the response content as JSON
    json_data = response.json()
    # Check if the JSON data is not empty
    if json_data:
        # Extract user id and name from the JSON data
        user_id = json_data.get('id')
        user_name = json_data.get('name')
        # Display the user id and name
        print(f"[{user_id}] {user_name}")
    else:
        # If JSON data is empty, display "No result"
        print("No result")
except ValueError:
    # If the response content is not valid JSON, display "Not a valid JSON"
    print("Not a valid JSON")
