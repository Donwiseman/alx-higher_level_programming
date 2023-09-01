#!/bin/bash
#takes in a URL and displays the body of the response after adding a header.
curl -s -H "X-School-User-Id: 98" "$1"
