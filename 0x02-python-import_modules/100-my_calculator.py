#!/usr/bin/python3
if __name__ == '__main__':
    from calculator_1 import add, sub, mul, div
    from sys import argv, exit

if len(argv) is not 4:
    print("{}".format("Usage: ./100-my_calculator.py <a> <operator> <b>"))
    exit(1)

if argv[2] is '+':
    print("{}".format(add(int(argv[1]), int(argv[3]))))
elif argv[2] is '-':
    print("{}".format(sub(int(argv[1]), int(argv[3]))))
elif argv[2] is '*':
    print("{}".format(mul(int(argv[1]), int(argv[3]))))
elif argv[2] is '/':
    print("{}".format(div(int(argv[1]), int(argv[3]))))
else:
    print("{}".format("Unknown operator. Available operators: +, -, * and /"))
    exit(1)
