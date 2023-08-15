#!/usr/bin/python3

"""
rotate an nxn matrix
90 degrees to the right
in-place. No returning anything
"""


def rotate_2d_matrix(matrix):
    """
    rotate a 2d (n x n matrix)
    Args:
        matrix (list): A list of list
    """
    n = len(matrix)
    # Transpose the matrix in-place
    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    for i in range(n):
        matrix[i] = matrix[i][::-1]
