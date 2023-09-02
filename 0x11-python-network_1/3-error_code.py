#!/usr/bin/python3
""" Displays the body of the response (decoded in utf-8) and handles error"""

from urllib.request import Request, urlopen
from urllib.error import HTTPError
import sys

if __name__ == "__main__":
    try:
        with urlopen(sys.argv[1]) as response:
            html = response.read()

        print(html.decode('utf-8'))
    except HTTPError as e:
        print('Error code:', e.code)
