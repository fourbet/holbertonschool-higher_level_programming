#!/usr/bin/python3
def remove_char_at(str, n):
    count = 0
    for c in str:
        if count == n:
            str = str[:n] + str[(n+1):]
        count += 1
    return (str)
