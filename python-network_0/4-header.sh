#!/bin/bash
#This networking sucks
echo -n $(curl -sSL -w "%{http_code}" -H "X-HolbertonSchool-User-Id: 98" "$1" | grep -q 200 && echo "OK" || echo "Request failed")
