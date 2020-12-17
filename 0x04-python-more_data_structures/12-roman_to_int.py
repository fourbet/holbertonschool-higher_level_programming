#!/usr/bin/python3
def roman_to_int(roman_string):
    dic = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    sum = 0
    for nbr in roman_string:
        for k, v in dic.items():
            if nbr == k:
                sum += v
    return sum
