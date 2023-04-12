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
    n = len(coins)
    dp = [float('inf')] * (total + 1)
    dp[0] = 0
    for i in range(n):
        for j in range(coins[i], total + 1):
            dp[j] = min(dp[j], dp[j - coins[i]] + 1)
    return dp[total] if dp[total] != float('inf') else -1
