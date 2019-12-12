#!/usr/bin/python3
if __name__ == '__main__':
    from calculator_1 import add, sub, mul, div
    from sys import argv, exit

if len(argv) is not 4:
    print("{}".format("Usage: ./100-my_calculator.py <a> <operator> <b>"))
    exit(1)

a = argv[1]
b = argv[3]
op = argv[2]

if op is '+':
    print("{} + {} = {}".format(a, b, add(int(a), int(b))))
elif op is '-':
    print("{} - {} = {}".format(a, b, sub(int(a), int(b))))
elif op is '*':
    print("{} * {} = {}".format(a, b, mul(int(a), int(b))))
elif op is '/':
    print("{} / {} = {}".format(a, b, div(int(a), int(b))))
else:
    print("{}".format("Unknown operator. Available operators: +, -, * and /"))
    exit(1)
