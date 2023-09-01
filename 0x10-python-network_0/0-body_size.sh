#!/bin/bash
# This takes a URL argument and returns the content-length of the URL.
curl -sI "$1" | grep -i 'Content-Length' | awk '{print $2}'
