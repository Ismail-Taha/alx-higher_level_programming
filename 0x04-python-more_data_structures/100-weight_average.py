#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list is not None:
        total_weighted_sum = 0
        total_occurrences = 0
        
        for weight, occurrence in my_list:
            total_weighted_sum += weight * occurrence
            total_occurrences += occurrence
        
        return total_weighted_sum / total_occurrences if total_occurrences > 0 else 0
    else:
        return 0
