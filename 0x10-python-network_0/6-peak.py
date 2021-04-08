#!/usr/bin/python3
""" Python Network Project """


def find_peak(list):
    """ finds a peak in a list of unsorted integers """
    peaks = []
    if list:
        m = list[0]
        mpos = 0
        for i, elem in enumerate(list):
            if elem > m:
                m = elem
                mpos = i
        return list[mpos]
