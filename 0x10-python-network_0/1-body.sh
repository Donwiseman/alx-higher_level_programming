#!/bin/bash
#takes in a URL and displays the body of the response
STATUS=$(curl -s -o /dev/null -w '%{http_code}' "$1")
if [ "$STATUS" -eq 200 ]; then
	curl -s "$1" | tr -d '\n'
fi
