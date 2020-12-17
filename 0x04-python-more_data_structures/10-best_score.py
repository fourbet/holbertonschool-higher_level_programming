#!/usr/bin/python3
def best_score(a_dictionary):
    max = 0
    key = None
    if a_dictionary:
        for k, v in a_dictionary.items():
            if v > max:
                max = v
                key = k
    return key
