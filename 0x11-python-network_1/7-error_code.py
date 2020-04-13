#!/usr/bin/python3
"""Display response body
"""

import requests
from sys import argv

if __name__ == '__main__':

    url = argv[1]

    try:
        r = requests.get(url)
        r.raise_for_status()
        print(r.text)
    except:
        print('Error code: {}'.format(r.status_code))
