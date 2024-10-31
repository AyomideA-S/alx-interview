#!/usr/bin/python3
'''Prime Game'''


def isWinner(x, nums):
    '''Determine the game winner'''
    if x == 0:
        return None

    max_num = max(nums)
    sieve = [True] * (max_num + 1)
    sieve[0:2] = [False, False]
    for i in range(2, int(max_num**0.5) + 1):
        if sieve[i]:
            sieve[i*i:max_num+1:i] = [False] * len(range(i*i, max_num+1, i))

    prime_counts = [0] * (max_num + 1)
    count = 0
    for i in range(2, max_num + 1):
        if sieve[i]:
            count += 1
        prime_counts[i] = count

    maria = ben = 0
    for n in nums:
        if prime_counts[n] % 2:
            maria += 1
        else:
            ben += 1

    if maria > ben:
        return 'Maria'
    elif ben > maria:
        return 'Ben'
    else:
        return None
