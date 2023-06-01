#!/usr/bin/python3
"""
 objective:
    Given a set of consecutive integers starting from 1 up to and including n,
    choose a prime number from the set and remove that number and its multiples
    from the set. The player that cannot make a move loses the game.
    Assuming Maria always goes first and both players play optimally,
    determine who the winner of each game is.
 Prototype: def isWinner(x, nums)
                x = number of rounds
                nums = array of n
                n and x < 10000
                Return: name of the player that won the most rounds
                If the winner cannot be determined:
                    return None
"""


def isWinner(x, nums):
    """
        function that determines who the winner of each game is
    """
    if not nums or x < 1:
        return None
    n = max(nums)
    primes = [True for _ in range(n + 1)]
    p = 2
    while (p * p <= n):
        if primes[p]:
            for i in range(p * 2, n + 1, p):
                primes[i] = False
        p += 1
    primes[0] = False
    primes[1] = False
    c = 0
    for i in range(len(primes)):
        if primes[i]:
            c += 1
        primes[i] = c
    player1 = 0
    for n in nums:
        player1 += primes[n] % 2 == 1
    if player1 * 2 == len(nums):
        return None
    if player1 * 2 > len(nums):
        return "Maria"
    return "Ben"
