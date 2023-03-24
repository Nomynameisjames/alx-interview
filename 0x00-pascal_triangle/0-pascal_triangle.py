#!/usr/bin/python3
""" Module for Pascal's triangle """


def pascal_triangle(n):
    """ Returns list of lists of ints representing Pascal’s triangle of n """
    pascal = [[1]]

    if n <= 0:
        return []

    if n == 1:
        return pascal

    for i in range(1, n):
        l = -1
        r = 0
        triangle_row = []
        for j in range(i+1):
            num = 0
            if l > -1:
                num += pascal[i - 1][l]
            if r < i:
                num += pascal[i - 1][r]
            l += 1
            r += 1
            triangle_row.append(num)
        pascal.append(triangle_row)
    return pascal
