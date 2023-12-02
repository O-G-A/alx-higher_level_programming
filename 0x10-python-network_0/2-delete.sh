#!/bin/bash
# Script which sends a DELETE request to the URL and passed as the first argument, then displays body of the response
curl -s "$1" -X DELETE
