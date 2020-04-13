#!/usr/bin/python3
"""Make a POST request
"""

import requests
from sys import argv

if __name__ == '__main__':

    url = argv[1]
    email = argv[2]

    r = requests.post(url, data={'email': email})
    print(r.text)
