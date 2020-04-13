#!/usr/bin/python3
"""Fetch web response
"""

import urllib.request

if __name__ == "__main__":
    with urllib.request.urlopen('https://intranet.hbtn.io/status') as response:
        content = response.read()

    print('    - type: {}'.format(type(content)))
    print('    - content: {}'.format(content))
    print('    - utf8 content: {}'.format(str(content)[2:-1]))
