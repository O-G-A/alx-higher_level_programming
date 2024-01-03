#!/bin/bash
# Script which sends request to a URL passed as an argument, then displays only status code of the response.
curl -s -L -X HEAD -w "%{http_code}" "$1"
