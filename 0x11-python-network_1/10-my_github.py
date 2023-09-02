#!/usr/bin/python3
""" takes your GitHub credentials (username and password) and uses the GitHub
API to display your id. """

import requests
from requests.auth import HTTPBasicAuth
import sys

if __name__ == "__main__":
    val = {
            'Accept': "application/vnd.github+json",
            'X-GitHub-Api-Version': '2022-11-28'
            }
    try:
        r = requests.get("https://api.github.com/user",
                         auth=HTTPBasicAuth(sys.argv[1], sys.argv[2]),
                         headers=val)
        r.raise_for_status()
        print(r.json()['id'])
    except requests.exceptions.RequestException as e:
        print('None')
