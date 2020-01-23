#!/usr/bin/python3
import sys
codes = ['200', '301', '400', '401',
         '403', '404', '405', '500']
code_hist = []
total_size = 0
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
