#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    import hidden_4

names = list(dir(hidden_4))

for name in names:
    if name[0] is not '_':
        print("{:s}".format(name))
