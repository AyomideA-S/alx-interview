#!/usr/bin/python3
"""
This module provides a function to determine the minimum number of coins
needed to achieve a given total amount from a given pile of coins of different
values.
"""
import sys


def makeChange(coins, total):
    '''
    Determines the fewest number of coins needed to meet the given total.
    Args:
        coins (list): A list of the values of the available coins.
        total (int): The total amount to be achieved.
    Returns:
        int: The minimum number of coins needed to achieve the total.
            Returns 0 if the total is 0 or less.
            Returns -1 if the total cannot be met by any combination of the
            available coins.
    '''
    if total <= 0:
        return 0
    coins = sorted(coins)
    table = [float('inf')] * (total + 1)
    table[0] = 0
    for coin in coins:
        for i in range(coin, total + 1):
            if table[i - coin] + 1 < table[i]:
                table[i] = table[i - coin] + 1
    if table[total] == float('inf'):
        return -1
    return table[total]
