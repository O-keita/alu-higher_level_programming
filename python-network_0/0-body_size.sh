#!/bin/bash
# script should be one line
curl -sI "$1" | awk '/Content-Length/ {print $2}' | tr -d '\r'
