#!/usr/bin/python3
"""Script that sends a POST request to the passed URL with
   the email as a parameter"""


if __name__ == '__main__':
    import requests
    import sys

    r = requests.get(sys.argv[1])
    if r.status_code >= 400:
        print('Error code: {}'.format(r.status_code))
    else:
        print(r.text)
