#!/bin/bash
#takes in a URL and displays the body of the response
curl -s --fail "$1" | tr -d '\n'
