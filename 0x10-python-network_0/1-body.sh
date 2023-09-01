#!/bin/bash
#takes in a URL and displays the body of the response
curl -s --fail -X GET "$1"
