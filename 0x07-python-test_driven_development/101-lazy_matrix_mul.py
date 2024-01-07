#!/usr/bin/python3
"""
This module multiply 2 matricies using numpy module
"""
import numpy


def lazy_matrix_mul(m_a, m_b):
    """
    multiply 2 matricies using NumPy
    Args:
        m_a: first matrix
        m_b: second matrix
    Returns:
        return m_a * m_b
    """
    return numpy.matmul(m_a, m_b)
