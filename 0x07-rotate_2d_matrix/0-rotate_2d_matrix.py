#!/usr/bin/python3
"""
    objective: rotate a 2D matrix 90 degrees clockwise
    def rotate_2d_matrix(matrix):
        - matrix: list of lists
        - return: nothing
"""


def rotate_2d_matrix(matrix) -> None:
    """
        Rotate 2D Matrix 90 degrees clockwise
    """
    for i in range(len(matrix)):
        for j in range(i, len(matrix)):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    for i in range(len(matrix)):
        matrix[i].reverse()
