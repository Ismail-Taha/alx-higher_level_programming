#!/usr/bin/python3
"""function to finds a peak in a list of unsorted integers"""


def find_peak(list_of_integers):

    """Finds a peak in a list of unsorted integers."""
    if not list_of_integers:
        return None

    n = len(list_of_integers)

    for i in range(n):
        is_peak = True

        if i > 0 and list_of_integers[i] <= list_of_integers[i - 1]:
            is_peak = False
        if i < n - 1 and list_of_integers[i] <= list_of_integers[i + 1]:
            is_peak = False

        if is_peak:
            return list_of_integers[i]

    return None    
