#!/usr/bin/python3
""" Displays the body of the response (decoded in utf-8) and handles error"""

import requests
import sys

if __name__ == "__main__":
    try:
        r = requests.get(sys.argv[1])
        r.raise_for_status()
        print(r.text)
    except requests.exceptions.RequestException as e:
        print('Error code:', r.status_code)
