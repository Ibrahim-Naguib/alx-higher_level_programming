#!/usr/bin/python3
"""Script that sends a POST request to the passed URL with the
   email as a parameter and displays the body of the response"""


if __name__ == '__main__':
    import urllib.request
    import urllib.parse
    import sys

    url = sys.argv[1]
    values = {'email': sys.argv[2]}
    data = urllib.parse.urlencode(values)
    data = data.encode('utf-8')
    req = urllib.request.Request(url, data)
    with urllib.request.urlopen(req) as res:
        body = res.read()
        print(body.decode('utf-8'))
