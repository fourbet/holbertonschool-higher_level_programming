#!/usr/bin/python3
def max_integer(my_list=[]):
    max = 0
    if my_list:
        for i in range(len(my_list)):
            if max < my_list[i]:
                max = my_list[i]
        return max
    else:
        return None
