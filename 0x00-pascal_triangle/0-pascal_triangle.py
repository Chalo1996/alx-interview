#!/usr/bin/python3
"""0-pascal_triangle."""

triangle = list()
triangle.append([1])


def pascal_triangle(n):
    """
    Return a list of lists of intergers representing the Pascal's Triangle.

    temp is temporary list to be storing the elements of to manipulate /
    to form the new row.
    row will be every new row of the values of that row position.
    sumNextValue will be the sum of the values that forms the current row.

    Args:
        n (int): The number of rows of the triangle.
    """
    if n <= 0:
        return list()
    else:
        for i in range(n - 1):
            temp = [0] + triangle[-1] + [0]
            row = list()
            for j in range(len(triangle[-1]) + 1):
                sumNextVal = temp[j] + temp[j + 1]
                row.append(sumNextVal)
            triangle.append(row)
        return triangle
