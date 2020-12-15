#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    if my_list:
        list = my_list[:]
        for i in range(len(list)):
            if (i % 2 == 0):
                list[i] = True
            else:
                list[i] = False
        return list
