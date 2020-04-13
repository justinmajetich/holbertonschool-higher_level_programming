#!/usr/bin/python3
"""Retrieve header with requests module
"""

import requests
from sys import argv


if __name__ == '__main__':
    url = argv[1]
    r = requests.get(url)
    r = r.headers
    print(r.get('X-Request-Id'))
