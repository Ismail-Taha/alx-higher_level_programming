#!/usr/bin/python3
def roman_to_int(roman_string):
    rvalues = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50,
        'C': 100, 'D': 500, 'M': 1000
    }

    res = 0
    prevalue = 0
    len_roman = len(roman_string)

    for i in range(len_roman - 1, -1, -1):
        curvalue = rvalues.get(roman_string[i], 0)

        if i > 0 and curvalue < rvalues.get(roman_string[i - 1], 0):
            res -= curvalue
        else:
            res += curvalue

        prevalue = curvalue

    return res
