from typing import List

import numpy as np


class Matrix:
    def __init__(self, value: List[float]):
        if type(value[0]) is list:
            self.value = np.array(value)
        else:
            self.value = np.swapaxes(np.array(value))

    def __mul__(self, other) -> np.array:
        np.matmul(self.value, other.value)

    def reverse_value(self) -> np.array:
        return np.swapaxes(self.value)

class MatrixOperator:
    @staticmethod
    def kronecker_product(first_element: Matrix, second_element: Matrix) -> Matrix:
        """most important operation for multiple qubit processing, also called tensor product, order of elements
        is important. Both elements might be different sizes.

        :param first_element: matrix notation of first element
        :param second_element: matrix notation of first element
        :return: size of expected matrix is equal to n1*n2 and m1*m2 for n and m being amount of rows and columns
        """

    @staticmethod
    def matrix_multiply(quantum_value: Matrix, gate_value: Matrix) -> Matrix:
        """ function that allows to use gates on calculated quantum value

        :param quantum_value: matrix with single column and rows number equal to 2**(amount of qbits)
        :param gate_value: square matrix with amount of rows and columns equal 2**(amount of qbits)
        :return: new matrix being product of q_val and gate_val
        """
