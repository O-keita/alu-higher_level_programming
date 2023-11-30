#!/bin/bash
#Write a Bash script that takes in a URL and displays all HTTP methods the server will accept.
curl -X OPTIONS "$1" -H "Host: $1" -sI | grep -Eo '^Allow: (.*)$' | sed -r 's/Allow: //'
