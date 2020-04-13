#!/usr/bin/python3
"""Fetch url using requests module
"""

import requests


if __name__ == '__main__':

    url = 'https://intranet.hbtn.io/status'

    response = requests.get(url)

    print('Body response:')
    print('\t- type: {}'.format(type(response.text)))
    print('\t- content: {}'.format(response.text))
