#!/usr/bin/python3
"""This module defines a program that parses stdin

The line is taken from stdin and split into distinct tokens. The
tokens or interest are added to a sequence and counted on a need
to know basis.
"""

import sys
codes = ['200', '301', '400', '401',
         '403', '404', '405', '500']
code_hist = []
total_size = 0
"""These variables are used to track codes received and filesize
"""
try:
    while True:
        for cnt, line in enumerate(sys.stdin):
            tokens = line.split(' ')
            total_size += int(tokens[-1])
            code_hist.append(tokens[-2])
            if cnt == 9:
                print('File size: ' + str(total_size))
                for code in codes:
                    if code in code_hist:
                        print('{}: {}'.format(code, code_hist.count(code)))
                break
except KeyboardInterrupt:
    print('File size: ' + str(total_size))
    for code in codes:
        if code in code_hist:
            print('{}: {}'.format(code, code_hist.count(code)))
    sys.exit()
