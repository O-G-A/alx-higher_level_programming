#!/bin/bash
# Script which sends a JSON POST request to a URL passed as the first argument, then displays body of the response.
curl -s "$1" -d "@$2" -X POST -H "Content-Type: application/json"
