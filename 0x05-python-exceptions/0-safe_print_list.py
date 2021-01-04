#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    count = 0
    try:
        for nbr in range(x):
            print(my_list[nbr], end="")
            count = count + 1
    except:
        pass
    print()
    return count
