#!/bin/bash
#The first advance question
curl -s -o /dev/null -w "%{http_code}" "$1" | tr -d '\n'
