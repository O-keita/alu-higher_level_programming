#!/usr/bin/python3
"""8-json_api.py"""


import requests
import sys

if len(sys.argv) != 2:
    q = ""
else:
    q = sys.argv[1]

url = "http://0.0.0.0:5000/search_user"
data = {'q': q}

response = requests.post(url, data=data)

try:
    json_data = response.json()
    if json_data:
        user_id = json_data.get('id')
        user_name = json_data.get('name')
        print(f"[{user_id}] {user_name}")
    else:
        print("No result")
except ValueError:
    print("Not a valid JSON")
