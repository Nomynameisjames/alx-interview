#!/usr/bin/python3
"""
    Prototype:
            def makeChange(coins, total)
                    Return: fewest number of coins needed to meet total
                    If total is 0 or less:
                        return 0
                    If total cannot be met by any number of coins you have:
                        return -1
    coins is a list of the values of the coins in your
    value of a coin will always be an integer greater than 0
    You can assume you have an infinite number of each denomination of coin
    in the list
"""


def makeChange(coins: list, total: int) -> int:
    """
        determine the fewest number of coins needed to meet a given amount
        total.
    """

    if total <= 0:
        return 0

    coins.sort(reverse=True)
    num_coins = 0

    for coin in coins:
        if total <= 0:
            break
        num_coins += total // coin
        total = total % coin

    if total != 0:
        return -1

    return num_coins
