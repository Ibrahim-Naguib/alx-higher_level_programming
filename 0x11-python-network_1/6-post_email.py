#!/usr/bin/python3
"""Script that sends a POST request to the passed URL with
   the email as a parameter"""


if __name__ == '__main__':
    import requests
    import sys

    headers = {'email': sys.argv[2]}
    r = requests.post(sys.argv[1], headers)
    print(r.text)
