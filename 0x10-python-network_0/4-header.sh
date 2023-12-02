#!/bin/bash
# Script which takes in a URL as an argument, sends GET request to the URL, then displays body of the response
curl -s "$1" -H "X-School-User-Id: 98"
