#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv

argc = len(argv) - 1
if argc > 1:
    print("{:d} arguments:".format(argc))
elif argc == 1:
    print("1 argument:")
else:
    print("0 arguments.")

cnt = 1
for i in argv[1:]:
    print("{:d}: {:s}".format(cnt, i))
    cnt += 1
