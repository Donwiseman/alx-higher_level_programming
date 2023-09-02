#!/usr/bin/python3
""" sends a POST request to http://0.0.0.0:5000/search_user with the
letter as a parameter."""

import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) > 1:
        val = {"q": sys.argv[1]}
    else:
        val = {'q': ""}
    try:
        r = requests.post('http://0.0.0.0:5000/search_user', val)
        r_j = r.json()
        if r_j:
            print(f"[{r_j['id']}] {r_j['name']}")
        else:
            print('No result')
    except Exception as e:
        print('Not a valid JSON')
