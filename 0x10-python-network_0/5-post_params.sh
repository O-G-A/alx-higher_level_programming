#!/bin/bash
# Script which takes in a URL, sends a POST request to the passed URL, then displays body of the response
curl -s "$1" -X POST -d "email=test@gmail.com&subject=I will always be here for PLD"
