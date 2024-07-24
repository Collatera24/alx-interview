#!/usr/bin/python3
"""
def pascal_triangle(n)
"""


def pascal_triangle(n):
    """a function that returns a list of lists of integers
    representing the Pascal’s triangle of n
    """
    res = []
    if n > 0:
        for i in range(1, n + 1):
            level = []
            K = 1
            for j in range(1, i + 1):
                level.append(K)
                K = K * (i - j) // j
            res.append(level)
    return res

