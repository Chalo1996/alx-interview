#!/usr/bin/python3
"""2D Matrix Rotation module."""


def rotate_2d_matrix(matrix):
    """Rotate a 2D matrix 90 degrees clockwise.

    Args:
        matrix (list): 2D matrix to rotate.

    Returns:
        None.
    """
    new_matrix = []
    for i in range(len(matrix)):
        new_matrix.append([])
        for j in range(len(matrix)):
            new_matrix[i].append(matrix[j][i])
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            matrix[i][j] = new_matrix[i][len(matrix) - 1 - j]
