#!/usr/bin/python3
"""Making change module."""


def makeChange(coins, total):
    """makeChange: Given a pile of coins of different values, determine the\
    fewest number of coins needed to meet a given amount total.

    Args:
        coins (list): is a list of the values of the coins in your possession
        total (int): is the total number of cents needed to make change

    Returns:
        If total is 0 or less, return 0
    """
    if total <= 0:
        return 0
    numCoins = len(coins)
    dcp = [[float('inf')] * (total + 1) for _ in range(numCoins)]
    for j in range(total + 1):
        if j % coins[0] == 0:
            dcp[0][j] = j // coins[0]
    for i in range(1, numCoins):
        for j in range(total + 1):
            if coins[i] > j:
                dcp[i][j] = dcp[i - 1][j]
            else:
                dcp[i][j] = min(dcp[i - 1][j], dcp[i][j - coins[i]] + 1)
    return dcp[-1][-1] if dcp[-1][-1] != float('inf') else -1
