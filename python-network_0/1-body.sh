#!/bin/bash
# Check if a URL is provided
r=$(curl -sSL -w "%{http_code}" "$1"); [ "${r: -3}" -eq 200 ] && echo -n "${r::-3}" || echo -n "Error: HTTP status code ${r: -3}"
