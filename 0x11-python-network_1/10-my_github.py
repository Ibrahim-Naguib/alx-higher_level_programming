#!/usr/bin/python3
"""Script that takes GitHub credentials and uses the GitHub
   API to display the id
"""


if __name__ == '__main__':
    import requests
    import sys

    username = sys.argv[1]
    password = sys.argv[2]
    url = 'https://api.github.com/user'
    res = requests.get(url, auth=(username, password))
    json = res.json()
    print(json.get('id'))
