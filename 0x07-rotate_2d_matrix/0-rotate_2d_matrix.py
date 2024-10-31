#!/usr/bin/python3
''' 2D matrix rotation module'''


def rotate_2d_matrix(matrix):
    """Rotate a 2D matrix 90 degrees clockwise in-place."""
    n = len(matrix)
    # Transpose the matrix
    for i in range(n):
        for j in range(i, n):
            matrix[j][i], matrix[i][j] = matrix[i][j], matrix[j][i]
    # Reverse each row
    for row in matrix:
        row.reverse()
