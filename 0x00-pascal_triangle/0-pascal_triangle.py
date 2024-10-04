#!/usr/bin/python3
"""
===================
|Pascal's Triangle|
===================
"""


def pascal_triangle(n):
    """
    Generates Pascal's Triangle up to the specified number of rows.

    Args:
        n (int): The number of rows in Pascal's Triangle.

    Returns:
        list of list of int: A list of lists of integers representing
        Pascal's Triangle.
    """
    if n <= 0:
        return []

    triangle = []

    for i in range(n):
        # Start with a row of 1s
        row = [1] * (i + 1)

        # Calculate the intermediate values
        for j in range(1, i):
            row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]

        # Append the row to the triangle
        triangle.append(row)

    return triangle
