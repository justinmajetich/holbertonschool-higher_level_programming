#!/usr/bin/python3
for c in range(122, 96, -1):
    if c % 2 != 0:  # if ASCII value is odd
        print("{:s}".format(chr(c - 32)), end='')
    else:
        print("{:s}".format(chr(c)), end='')
