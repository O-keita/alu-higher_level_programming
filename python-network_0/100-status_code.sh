#!/bin/bash
#The first advance question
(status_code=$(curl -s -o /dev/null -w "%{http_code}" "$1") && echo -n $status_code)
