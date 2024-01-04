#!/usr/bin/python3
"""
a function def pascal_triangle(n): that returns a list of
lists of integers representing the Pascal’s triangle of n:
"""


def pascal_triangle(n):
    """
    function for pascal triangle
    """
    triangle = []

    if (n <= 0):
        return triangle

    for i in range(n):
        row = []
        for j in range(i + 1):
            if (j == 0 or j == i):
                row.append(1)
            else:
                nextvalue = triangle[i - 1][j - 1] + triangle[i - 1][j]
                row.append(nextvalue)
        triangle.append(row)

    return triangle
