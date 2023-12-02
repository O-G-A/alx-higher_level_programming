#!/bin/bash
# Script which takes in a URL, displays all HTTP methods the server will accept
curl -s -I -X OPTIONS "$1" | grep "Allow:" | cut -f2- -d" "
