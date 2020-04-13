#!/usr/bin/python3
"""Request and print response body, including error codes
"""

import urllib.request
from sys import argv


if __name__ == '__main__':
    url = argv[1]

    try:
        with urllib.request.urlopen(url) as response:
            print(response.read().decode('utf-8'))

    except urllib.error.HTTPError as error:
        print('Error code: {}'.format(error.code))
