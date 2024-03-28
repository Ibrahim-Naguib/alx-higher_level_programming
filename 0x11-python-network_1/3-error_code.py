#!/usr/bin/python3
"""Script that sends a request to the URL and displays the body of the response
"""


if __name__ == '__main__':
    from urllib.request import Request, urlopen
    from urllib.error import HTTPError
    import sys

    req = Request(sys.argv[1])
    try:
        with urlopen(req) as res:
            body = res.read()
            print(body.decode('utf-8'))
    except HTTPError as e:
        print('Error code: {}'.format(e.code))
