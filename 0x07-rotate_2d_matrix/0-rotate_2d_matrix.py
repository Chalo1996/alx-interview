#!/usr/bin/python3
"""2D Matrix Rotation module."""


from typing import List


def rotate_2d_matrix(matrix: List[List[int]]) -> None:
    """Rotate a 2D matrix 90 degrees clockwise.

    Args:
        matrix (list): 2D matrix to rotate.

    Returns:
        None.
    """
    new_matrix: List[List[int]] = []
    for i in range(len(matrix)):
        new_matrix.append([])
        for j in range(len(matrix)):
            new_matrix[i].append(matrix[j][i])
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            matrix[i][j] = new_matrix[i][len(matrix) - 1 - j]

    for row in matrix:
        print(row)


if __name__ == '__main__':
    matrix = [[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]]
    rotate_2d_matrix(matrix)
