#!/usr/bin/env python3

'''
    Objective write a method that calculates the fewest number of operations
    needed to result in exactly n H characters in the file.
    and return value as integer
'''


def minOperations(n: int) -> int:
    ''' Method that calculates the fewest number of operations
        needed to result in exactly n H characters in the file.
    '''
    spy = 0  # spy keeps track of the number of operations
    if n <= 1:  # If n is impossible to achieve, return 0
        return 0
    for i in range(2, n + 1):  # finding the factor of n
        while n % i == 0:
            spy = spy + i
            n = n // i
    return spy
