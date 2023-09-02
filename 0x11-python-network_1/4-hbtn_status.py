#!/usr/bin/python3
""" A script that fetches https://alx-intranet.hbtn.io/status"""

import requests

if __name__ == "__main__":
    html = requests.get('https://alx-intranet.hbtn.io/status')
    print('Body response:')
    print(f"\t- type: {type(html.text)}")
    print(f"\t- content: {html.text}")
