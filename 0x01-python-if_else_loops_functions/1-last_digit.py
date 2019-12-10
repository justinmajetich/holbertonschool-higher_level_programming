#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
sign = 1

if number < 0:  # track if neg number
    sign = -1
    number = number * -1  # make pos to take accurate remiander

last = number % 10  # take remainder

if sign == -1:
    number = number * sign  # restore number to neg if sign was neg
    last = last * sign  # convert last digit to match

if last > 5:
    print("Last digit of {:d} is {:d} \
and is greater than 5".format(number, last))
elif last < 6 and last != 0:
    print("Last digit of {:d} is {:d} \
and is less than 6 and not 0".format(number, last))
else:
    print("Last digit of {:d} is {:d} and is 0".format(number, last))
