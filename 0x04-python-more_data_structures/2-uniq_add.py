#!/usr/bin/python3
def uniq_add(my_list=[]):
    new_list=set(my_list)
    sum=0
    for elem in new_list :
        sum += elem
    return(sum)
