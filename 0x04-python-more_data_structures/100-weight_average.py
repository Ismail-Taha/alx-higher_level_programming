#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list is not None:
        tot_weighted = 0
        tot_occurrences = 0
        for tup in my_list:
            (weight, occurrence) = tup
            tot_weighted += (weight * occurrence)
            tot_occurrences += occurrence
        return (tot_weighted / tot_occurrences) if tot_occurrences > 0 else 0
    else:
        return 0
