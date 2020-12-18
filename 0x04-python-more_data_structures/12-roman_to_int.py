#!/usr/bin/python3
def roman_to_int(roman_string):
    dic = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    sum = 0
    count = 0
    for nbr in roman_string:
        for k, v in dic.items():
            if nbr == 'I' and count < len(roman_string) :
                sum -= 1
            if nbr == k:
                sum += v
            count+= 1
    return sum
