#!/usr/bin/python3
""" Project: Python - Inheritance """


class MyInt(int):
    """ class that inherits from int """

    def __init__(self, nbr):
        """initialization """
        self.__nbr = nbr

    def __eq__(self, other):
        """ equal comparison """
        return self.__nbr != other

    def __ne__(self, other):
        """ different comparison """
        return self.__nbr == other
