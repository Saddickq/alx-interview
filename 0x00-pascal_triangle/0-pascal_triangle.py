#!/usr/bin/python3


def pascal_triangle(n):
    triangle = []

    if (n > 0):
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
