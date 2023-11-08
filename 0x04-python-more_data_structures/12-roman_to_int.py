#!/usr/bin/python3
def roman_to_int(roman_string):
    rvalues = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50,
        'C': 100, 'D': 500, 'M': 1000
    }

    res = 0
    prev_value = 0

    for numeral in reversed(roman_string):
        cur_value = rvalues.get(numeral, 0)

        if cur_value < prev_value:
            res -= cur_value
        else:
            res += cur_value

        prev_value = cur_value

    return res
