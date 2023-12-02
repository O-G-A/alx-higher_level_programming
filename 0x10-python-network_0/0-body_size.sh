#!/bin/bash
# Script that takes in a URL, sends request to that URL, then displays size of body of the response.
curl -sI "$1" | grep -i Content-Length | cut -d " " -f 2
