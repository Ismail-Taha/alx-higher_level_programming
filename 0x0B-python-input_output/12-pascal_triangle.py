#!/usr/bin/python3
"""Defines a Pascal's Triangle function"""


def pascal_triangle(rows):
    """Representing Pascal triangle of rows"""

    if rows <= 0:
        return []

    triangle_rows = [[1]]
    while len(triangle_rows) != rows:
        current_row = triangle_rows[-1]
        new_row = [1]
        for i in range(len(current_row) - 1):
            new_row.append(current_row[i] + current_row[i + 1])
        new_row.append(1)
        triangle_rows.append(new_row)
    return triangle_rows
