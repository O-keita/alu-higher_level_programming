#!/bin/bash
#This networking sucks
[ "$(curl -sSL -H "X-HolbertonSchool-User-Id: 98" "$1" | tr -d '\n')" == "OK" ] && echo "OK" || echo "Error"
