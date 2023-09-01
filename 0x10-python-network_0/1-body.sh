#!/bin/bash
#takes in a URL and displays the body of the response
curl -sL --fail -X GET "$1"
