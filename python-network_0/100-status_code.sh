#!/bin/bash
#The first advance question
curl -s --write-out %{http_code} --output /dev/null "$1"
