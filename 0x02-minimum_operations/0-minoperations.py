#!/usr/bin/python3
'''Minimum Operations'''


def minOperations(n):
    """
    Calculate the minimum number of operations needed to get exactly n 'H'
    characters using only "Copy All" and "Paste" operations.

    Parameters:
    n (int): The target number of 'H' characters.

    Returns:
    int: The minimum number of operations required to achieve n 'H' characters.
         Returns 0 if n is impossible to achieve.
    """
    # If n is less than or equal to 1, no operations are needed
    if n <= 1:
        return 0

    operations = 0  # Initialize the count of operations
    divisor = 2     # Start with the smallest prime number

    # Factorize n by dividing it by the smallest possible divisor
    while n > 1:
        # While n is divisible by the current divisor
        while n % divisor == 0:
            operations += divisor  # Add the divisor to the operations count
            n //= divisor          # Divide n by the divisor
        divisor += 1  # Move to the next possible divisor

    return operations  # Return the total number of operations
