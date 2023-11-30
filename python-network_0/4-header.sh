#!/bin/bash
#This networking sucks
curl -X GET "$1" -H "X-HolbertonSchool-User-Id: 98" | cat
