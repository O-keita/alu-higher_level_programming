#!/bin/bash
# Check if a URL is provided
r=$(curl -sSL -w "%{http_code}" "$1"); [ "${r: -3}" -eq 200 ] && echo "${r::-3}" || echo "Error: HTTP status code ${r: -3}"
