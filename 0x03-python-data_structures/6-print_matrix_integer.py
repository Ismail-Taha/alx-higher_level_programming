#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        row_string = ' '.join(['{:d}'.format(i) for i in row])
        print(row_string)
