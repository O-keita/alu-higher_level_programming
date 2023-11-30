#!/bin/bash
#This networking sucks
curl -X GET -H "X-HolbertonSchool-User-Id: 98" "$1" | cat
