#!/usr/bin/python3
"""Script that fetches https://alx-intranet.hbtn.io/status"""
import requests


if __name__ == '__main__':

    r = requests.get('https://alx-intranet.hbtn.io/status')
    text = r.text
    print('Body response:')
    print('\t- type: {}'.format(type(text)))
    print('\t- content: {}'.format(text))
