#!/bin/bash
# Trying te cose
curl -X DELETE "$1" | cat | grep -q "DELETE method accepted" && echo "PASS" || echo "FAIL"
