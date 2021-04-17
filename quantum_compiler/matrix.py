import typing
import numpy as np


class Matrix:
    """Class for overriding Matrix basic computation operations."""

    def __init__(self, value: typing.Union[list, np.ndarray]):
        self.value = np.array(value)

    def __mul__(self, other) -> np.ndarray:  # type: ignore
        return np.matmul(self.value, other.value)

    def __add__(self, other) -> np.ndarray:  # type: ignore
        return np.kron(self.value, other.value)

    def __str__(self) -> str:
        return str(self.value)

    def reverse_value(self) -> np.ndarray:
        return np.array([x[0] for x in self.value])


class MatrixOperator:
    """Class for handling matrix operations."""

    @staticmethod
    def kronecker_product(first_element: Matrix, second_element: Matrix) -> Matrix:
        """
        Most important operation for multiple qbit processing, also called tensor product, order of elements
        is important. Both elements might be different sizes. Size of returned matrix is equal to n1*n2 and m1*m2
        for n and m being amount of rows and columns.

        :param first_element: matrix notation of first element
        :param second_element: matrix notation of first element
        :return: kronecker product of first_element and second_element
        """
        return Matrix(first_element + second_element)

    @staticmethod
    def matrix_multiply(quantum_value: Matrix, gate_value: Matrix) -> Matrix:
        """
        Operation that allows to use gates on calculated quantum value.

        :param quantum_value: matrix with single column and rows number equal to 2**(amount of qbits)
        :param gate_value: square matrix with amount of rows and columns equal 2**(amount of qbits)
        :return: product of q_val and gate_val
        """
        return Matrix(quantum_value * gate_value)
