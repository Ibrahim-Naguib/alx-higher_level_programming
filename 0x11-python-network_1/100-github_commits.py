#!/usr/bin/python3
""" Script that gets the first 10 commits from a github repo"""


if __name__ == '__main__':
    import requests
    import sys

    repo = sys.argv[1]
    owner = sys.argv[2]
    url = 'https://api.github.com/repos/{}/{}/commits'.format(owner, repo)
    res = requests.get(url)
    json = res.json()
    for commit in json[:10]:
        sha = commit['sha']
        name = commit['commit']['author']['name']
        print('{}: {}'.format(sha, name))
