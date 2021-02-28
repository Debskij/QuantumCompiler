import typing
import numpy as np
import math

from matrix import Matrix, MatrixOperator

QUBIT_MATRICES = {
    "0": [1.0, 0.0],
    "1": [0.0, 1.0],
    "+": [1 / math.sqrt(2.0), 1 / math.sqrt(2.0)],
    "-": [1 / math.sqrt(2.0), -1 / math.sqrt(2.0)],
}


class States:
    @staticmethod
    def decode_state(qubit_representation: str) -> np.ndarray:
        """Converts string representation of qubit (ex. |01>, |+>, |->, |001>, |+++>) to matrix form

        :param qubit_representation: string started with | and ended with >
                                     containing any number of 0, 1, + and -
        :return: matrix containing float values of qubit('s). Size of matrix is determined by
                 length of symbols. It will always contain pow(2, len(qubit_representation)-2)
        """

        def strip_braket_signs():
            return qubit_representation[1:-1]

        if len(qubit_representation) < 3:
            raise ValueError("Qubit string representation has to have at least 1 character e.g. |1>")

        qubit_representation = strip_braket_signs()

        first_qubit = qubit_representation[0]
        current_matrix = Matrix(QUBIT_MATRICES.get(first_qubit))
        qubit_representation = qubit_representation[1:]

        for qubit in qubit_representation:
            current_matrix = MatrixOperator.kronecker_product(current_matrix, Matrix(QUBIT_MATRICES.get(qubit)))

        return current_matrix

    @staticmethod
    def encode_state(matrix_representation: np.ndarray) -> typing.Optional[str]:
        """Converts matrix representation of qubit to string form

        :param matrix_representation: single dimensional matrix with one column and amount of rows being power of two
        :return: string representation of qubit, if possible to describe without precision losses otherwise return None
        """
