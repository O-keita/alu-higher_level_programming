#!/usr/bin/python3
""" 1-hbtn_header.py"""


import urllib.request
import sys

if len(sys.argv) != 2:
    print("Usage: python script.py <URL>")
    sys.exit(1)

url = sys.argv[1]

req = urllib.request.Request(url)
with urllib.request.urlopen(req) as response:
    x_request_id = response.info().get('X-Request-Id')
    print(x_request_id)
