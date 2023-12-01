#!/usr/bin/python3
""" 0-hbtn_status.py"""


import urllib.request

url = "https://alu-intranet.hbtn.io/status"

with urllib.request.urlopen(url) as response:
    content = response.read().decode('utf-8')
