#!/usr/bin/python3
"""Script that takes in a letter and sends a POST request to
   http://0.0.0.0:5000/search_user with the letter as a parameter.
"""


if __name__ == '__main__':
    import requests
    import sys

    query = {}
    if len(sys.argv) != 2:
        query['q'] = ""
    else:
        query['q'] = sys.argv[1]
    headers = query
    r = requests.post('http://0.0.0.0:5000/search_user', headers)
    try:
        res = r.json()

        if res == {}:
            print('No result')
        else:
            print('[{}] {}'.format(res.get('id'), res.get('name')))
    except ValueError:
        print('Not a valid JSON')
