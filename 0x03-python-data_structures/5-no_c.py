#!/bin/usr/python3
def no_c(my_string):
    idx = 0
    for letter in my_string:
        if letter == 'c' or letter == 'C':
            my_string = my_string[:idx] + my_string[(idx+1):]
        idx += 1
    return my_string
