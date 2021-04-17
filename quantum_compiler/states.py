import math
import typing
from itertools import product

import numpy as np

from .matrix import Matrix, MatrixOperator

QBIT_MATRICES = {
    "0": [1.0, 0.0],
    "1": [0.0, 1.0],
    "+": [1 / math.sqrt(2.0), 1 / math.sqrt(2.0)],
    "-": [1 / math.sqrt(2.0), -1 / math.sqrt(2.0)],
}
EPSILON = 0.00001


class States:
    """Class for handling operations on qbit states."""

    @staticmethod
    def decode_state(qbit_representation: str) -> np.ndarray:
        """
        Convert string representation of qbit (ex. |01>, |+>, |->, |001>, |+++>) to matrix form.

        :param qbit_representation: string started with | and ended with >
                                     containing any number of 0, 1, + and -
        :return: matrix containing float values of qbit('s). Size of matrix is determined by
                 length of symbols. It will always contain pow(2, len(qbit_representation)-2)
        :raises ValueError: when qbit_representation does not have at least 1 character e.g. "|>"
        :raises RuntimeError: when possibilities matrix does not sum to 1
        """

        def strip_braket_signs():
            return qbit_representation[2:-1] if negative else qbit_representation[1:-1]

        if len(qbit_representation) < 3:
            raise ValueError("Qbit string representation has to have at least 1 character e.g. |1>")

        negative = qbit_representation[0] == "-"
        qbit_representation = strip_braket_signs()

        first_qbit = qbit_representation[0]
        current_matrix = Matrix(QBIT_MATRICES[first_qbit])
        qbit_representation = qbit_representation[1:]

        for qbit in qbit_representation:
            current_matrix = MatrixOperator.kronecker_product(current_matrix, Matrix(QBIT_MATRICES[qbit]))

        if negative:
            current_matrix = Matrix(np.negative(current_matrix.value))

        if 1 - np.sum(np.square(current_matrix.value)) > EPSILON:
            raise RuntimeError("Possibilities matrix does not sum to 1")
        return current_matrix.value

    @staticmethod
    def encode_state(matrix_representation: np.ndarray) -> typing.Optional[str]:
        """Convert matrix representation of qbit to string form.

        :param matrix_representation: single dimensional matrix with one column and amount of rows being power of two
        :return: string representation of qbit, if possible to describe without precision losses otherwise return None
        :raises ValueError: when no matching braket representation was found
        :raises RuntimeError: when more than one braket representation was found
        """
        braket_length = int(math.log2(matrix_representation.size))

        possible_braket_representations = [
            "|" + "".join(s) + ">" for s in product(QBIT_MATRICES.keys(), repeat=braket_length)
        ] + ["-|" + "".join(s) + ">" for s in product(QBIT_MATRICES.keys(), repeat=braket_length)]
        matches_found = []

        for braket in possible_braket_representations:
            if np.allclose(States.decode_state(braket), matrix_representation):
                matches_found.append(braket)
        if not matches_found:
            raise ValueError("No braket representation was found")

        if len(matches_found) > 1:
            raise RuntimeError("More than one braket representation was found")

        return matches_found[0]
