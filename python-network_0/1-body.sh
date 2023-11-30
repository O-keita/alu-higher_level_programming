#!/bin/bash
# Will check later
curl -fsSL "$1" | awk 'NR==1{if($2==200)print $0}'
