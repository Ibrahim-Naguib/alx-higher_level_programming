#!/usr/bin/python3
"""Defines a matrix multiplication function."""


def matrix_mul(m_a, m_b):
    """Multiply two matrices.

    Args:
        m_a : The first matrix.
        m_b : The second matrix.
    Raises:
        TypeError: If m_a or m_b is not a list of lists of ints or floats.
        TypeError: If m_a or m_b is empty.
        TypeError: If m_a or m_b has different-sized rows.
        ValueError: If m_a and m_b cannot be multiplied.
    Returns:
        A new matrix representing the multiplication of m_a by m_b.
    """

    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")

    for row in m_a:
        if not isinstance(row, list):
            raise TypeError("m_a must be a list of lists")
        if m_a == [] or m_a == [[]]:
            raise ValueError("m_a can't be empty")
        for item in row:
            if not isinstance(item, (int, float)):
                raise TypeError("m_a should contain only integers or floats")
        if not len(row) == len(m_a[0]):
            raise TypeError("each row of m_a must be of the same size")

    for row in m_b:
        if not isinstance(row, list):
            raise TypeError("m_b must be a list of lists")
        if m_b == [] or m_b == [[]]:
            raise ValueError("m_b can't be empty")
        for item in row:
            if not isinstance(item, (int, float)):
                raise TypeError("m_b should contain only integers or floats")
        if not len(row) == len(m_a[0]):
            raise TypeError("each row of m_a must be of the same size")

    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    result = [[] for i in range(len(m_a))]

    for i in range(len(m_a)):
        for j in range(len(m_b[0])):
            c = 0
            for k in range(len(m_b)):
                c += m_a[i][k] * m_b[k][j]
            result[i].append(c)
   
    return result
