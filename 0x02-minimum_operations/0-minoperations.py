#!/usr/bin/python3
""" a method that calculates the fewest
number of operations needed to result
in exactly n H characters in the file."""


def minOperations(n: int) -> int:
    """ function documentation"""

    if type(n) != int or n < 0:
        return 0

    min_ops = 0
    operations = 1
    copy = 0

    while operations < n:
        if n % operations == 0:
            copy = operations
            operations += copy
            min_ops += 2
        else:
            operations += copy
            min_ops += 1

    return min_ops
