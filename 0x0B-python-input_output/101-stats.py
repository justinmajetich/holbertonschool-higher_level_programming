#!/usr/bin/python3
"""This module defines a program that parses logs"""


import sys
codes = ['200', '301', '400', '401',
         '403', '404', '405', '500']
code_hist = []
total_size = 0
i = 0
try:
    for line in sys.stdin:
        # if line == '':
        # sys.exit()
        tokens = line.split(' ')
        total_size += int(tokens[-1])
        code_hist.append(tokens[-2])
        if i == 9:
            i = 0
            print('File size: ' + str(total_size))
            for code in codes:
                if code in code_hist:
                    print('{}: {}'.format(code, code_hist.count(code)))
        else:
            i += 1
except KeyboardInterrupt:
    print('File size: ' + str(total_size))
    for code in codes:
        if code in code_hist:
            print('{}: {}'.format(code, code_hist.count(code)))
    sys.exit()
