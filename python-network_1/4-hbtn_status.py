#!/usr/bin/python3
"""4-hbtn_status.py"""


import requests

url = "https://alu-intranet.hbtn.io/status"

try:
    response = requests.get(url)
    response.raise_for_status()
    print("\t- {}".format(response.text))
except requests.exceptions.RequestException as e:
    print(f"Error: {e}")
