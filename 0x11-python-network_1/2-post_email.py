#!/usr/bin/python3
""" A script that sends a POST request to the passed URL with the email as a
parameter, and displays the body of the response."""

import urllib.request
import urllib.parse
import sys

if __name__ == "__main__":
    parsed = urllib.parse.urlencode({"email": sys.argv[2]})
    parsed = parsed.encode('utf-8')
    req = urllib.request.Request(sys.argv[1], parsed)
    with urllib.request.urlopen(req) as response:
        html = response.read()

    print(html.decode('utf-8'))
