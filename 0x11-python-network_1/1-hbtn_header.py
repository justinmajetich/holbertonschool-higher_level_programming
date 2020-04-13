#!/usr/bin/python3
"""Request and parse header
"""

import urllib.request
from sys import argv

if __name__ == "__main__":
    with urllib.request.urlopen(argv[1]) as response:
        for header in response.getheaders():
            if header[0] == 'X-Request-Id':
                print(header[1])
