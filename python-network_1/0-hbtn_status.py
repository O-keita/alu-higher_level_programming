#!/usr/bin/python3
""" 0-hbtn_status.py"""


import urllib.request

url = "https://alu-intranet.hbtn.io/status"

with urllib.request.urlopen(url) as response:
    content = response.read()

    print("Body response:")
    print("\t- type:", type(content))
    print("\t- content:", content)
    print("\t- utf8 content:", content.decode('utf-8'))
