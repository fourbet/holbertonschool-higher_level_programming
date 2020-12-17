#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_dic = a_dictionary.copy()
    for k, v in a_dictionary.items():
        new_dic[k] = v * 2
    return (new_dic)
