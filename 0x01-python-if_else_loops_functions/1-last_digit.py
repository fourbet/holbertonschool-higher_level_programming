#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number > 0:
    last = number % 10
else:
    if (number % 10) != 0:
        last = (10 - (number % 10))
    else:
        last = 0
if last > 5:
    digit = ("and is greater than 5")
elif last == 0:
    digit = ("and is 0")
else:
    digit = ("and is less than 6 and not 0")
print("Last digit of {:d} is {:d} {:s}".format(number, last, digit))
