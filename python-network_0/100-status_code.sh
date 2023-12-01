#!/bin/bash
#The first advance question
curl -s -o /dev/null -w "%{http_code}\n" "$1"
