#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    list_cp = my_list.copy()
    for i in range(0, len(my_list)):
        if (my_list[i] % 2) == 0:
            list_cp[i] = 1
        else:
            list_cp[i] = 0
    return list_cp
