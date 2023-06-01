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
    Function that determines who the winner of each game is.
    """
    if not nums or x < 1:
        return None

    n = max(nums)

    # create a list of prime numbers
    primes = [True for i in range(n + 1)]
    primes[0] = primes[1] = False
    for i in range(2, n + 1):
        if primes[i] is True:
            for j in range(i * i, n + 1, i):
                primes[j] = False

    # create a list of winners
    winners = [0 for i in range(n + 1)]
    for i in range(1, n + 1):
        if primes[i] is True:
            winners[i] = 1
        else:
            winners[i] = 2

    # create a list of winners for each round
    winners_round = [0 for i in range(x + 1)]
    for i in range(1, x + 1):
        winners_round[i] = winners[nums[i - 1]]
    if winners_round.count(1) > winners_round.count(2):
        return "Maria"
    elif winners_round.count(1) < winners_round.count(2):
        return "Ben"
    else:
        return None
