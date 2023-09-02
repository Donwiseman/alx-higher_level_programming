#!/usr/bin/python3
""" A script that displays the value of the X-Request-Id variable found"""

from urllib.request import Request, urlopen
import sys

if __name__ == "__main__":
    with urlopen(sys.argv[1]) as response:
        heads = response.headers

    print(heads.get("X-Request-Id", None))
