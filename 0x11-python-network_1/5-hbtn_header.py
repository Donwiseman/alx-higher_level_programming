#!/usr/bin/python3
""" A script that displays the value of the X-Request-Id variable found"""

import requests
import sys

if __name__ == "__main__":
    r = requests.get(sys.argv[1])
    print(r.headers.get("X-Request-Id", None))
