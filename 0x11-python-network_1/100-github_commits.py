#!/usr/bin/python3
""" list 10 commits (from the most recent to oldest) of a
repository by the user """

import requests
import sys

if __name__ == "__main__":
    val = {
            'Accept': "application/vnd.github+json",
            'X-GitHub-Api-Version': '2022-11-28'
            }
    url = f"https://api.github.com/repos/{sys.argv[2]}/{sys.argv[1]}/commits"
    try:
        r = requests.get(url, headers=val)
        r.raise_for_status()
        commits = r.json()
        for index, commit in enumerate(commits):
            if index < 10:
                sha = commit['sha']
                name = commit['commit']['author'].get("name", None)
                print(f"{sha}: {name}")
            else:
                break
    except requests.exceptions.RequestException as e:
        print(f"Error occurred: {r.status_code}")
    except Exception as e:
        print('JSON ERROR')
