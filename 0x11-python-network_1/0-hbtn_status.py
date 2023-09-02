#!/usr/bin/python3
""" A script that fetches https://alx-intranet.hbtn.io/status"""

from urllib.request import Request, urlopen
if __name__ == "__main__":
    with urlopen('https://alx-intranet.hbtn.io/status') as response:
        html = response.read()

    print('Body response:')
    print(f"\t- type: {type(html)}")
    print(f"\t- content: {html}")
    print(f"\t- utf8 content: {html.decode()}")
