#!/usr/bin/python3
"""Script that displays the value of the variable X-Request-Id"""


if __name__ == '__main__':
    import requests
    import sys

    r = requests.get(sys.argv[1])
    print(r.headers['X-Request-Id'])
