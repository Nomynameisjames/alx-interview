#!/usr/bin/python3

'''
    Objective write a method that calculates the fewest number of operations
    needed to result in exactly n H characters in the file.
    and return value as integer
'''


def minOperations(n) -> int:
    '''
        Method calculates the fewest number of operations
        needed to result in exactly n H characters in the file.
    '''
    '''
        spy keeps track of the number of operations
    '''
    spy = 0
    '''
        If n is impossible to achieve, return 0
    '''
    if n <= 1:
        return spy
    '''
        find factors of n
    '''
    for i in range(2, n + 1):
        while n % i == 0:
            spy = spy + i
            n = n // i

    return spy
