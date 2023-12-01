#!/usr/bin/python3
""" Module documented """


import requests
import sys

if len(sys.argv) != 3:
    print("Usage: python script.py <username> <token>")
    sys.exit(1)

username = sys.argv[1]
token = sys.argv[2]

url = "https://api.github.com/user"

response = requests.get(url, auth=(username, token))

if response.status_code == 200:
    user_data = response.json()
    user_id = user_data.get('id')
    print(f"Your GitHub user ID is: {user_id}")
else:
    print(f"Error: Unable to fetch user information. Status code: {response.status_code}")
    print(response.text)
