#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    dict_cp = a_dictionary.copy()
    for key in dict_cp:
        dict_cp[key] = dict_cp[key] * 2
    return dict_cp
