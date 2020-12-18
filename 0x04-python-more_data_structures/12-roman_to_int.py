#!/usr/bin/python3
def roman_to_int(roman_string):
    dic = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    sum = 0
    count = 0
    if roman_string:
        for nbr in roman_string:
            count += 1
            for k, v in dic.items():
                if nbr == 'I' and count < len(roman_string):
                    if roman_string[count] != "I":
                        sum -= 1
                        break
                if nbr == k:
                    sum += v
    return sum
