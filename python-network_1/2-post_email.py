#!/usr/bin/python3
"""2-post_email.py"""


import urllib.request
import urllib.parse
import sys

if len(sys.argv) != 3:
    print("Usage: python script.py <URL> <email>")
    sys.exit(1)

url = sys.argv[1]
email = sys.argv[2]

data = urllib.parse.urlencode({'email': email}).encode('utf-8')
req = urllib.request.Request(url, data=data, method='POST')

with urllib.request.urlopen(req) as response:
    content = response.read().decode('utf-8')
    print(content)
