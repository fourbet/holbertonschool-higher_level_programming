#!/usr/bin/python3
def uppercase(str):
    for i in str:
        if ord(i) >= 97 and ord(i) <= 122:
            i = ord(i) - 32
        else:
            i = ord(i)
        print("{:c}".format(i), end="")
    print()