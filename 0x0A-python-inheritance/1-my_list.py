#!/usr/bin/python3
""" Project: Python - Inheritance """


class MyList(list):
    """ class that inherits from list """

    def print_sorted(self):
        """ prints the list sorted """
        list_sorted = self[:]
        list_sorted.sort()
        print(list_sorted)
