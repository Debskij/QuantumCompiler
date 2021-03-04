import math
import typing
from itertools import product

import numpy as np

from .matrix import Matrix, MatrixOperator

QUBIT_MATRICES = {
    "0": [1.0, 0.0],
    "1": [0.0, 1.0],
    "+": [1 / math.sqrt(2.0), 1 / math.sqrt(2.0)],
    "-": [1 / math.sqrt(2.0), -1 / math.sqrt(2.0)],
}
EPSILON = 0.00001


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
            return qubit_representation[2:-1] if negative else qubit_representation[1:-1]

        if len(qubit_representation) < 3:
            raise ValueError("Qubit string representation has to have at least 1 character e.g. |1>")

        negative = qubit_representation[0] == "-"
        qubit_representation = strip_braket_signs()

        first_qubit = qubit_representation[0]
        current_matrix = Matrix(QUBIT_MATRICES[first_qubit])
        qubit_representation = qubit_representation[1:]

        for qubit in qubit_representation:
            current_matrix = MatrixOperator.kronecker_product(current_matrix, Matrix(QUBIT_MATRICES[qubit]))

        if negative:
            current_matrix = Matrix(np.negative(current_matrix.value))

        if 1 - np.sum(np.square(current_matrix.value)) > EPSILON:
            raise RuntimeError("Possibilities matrix does not sum to 1")
        return current_matrix.value

    @staticmethod
    def encode_state(matrix_representation: np.ndarray) -> str:
        """Converts matrix representation of qubit to string form

        :param matrix_representation: single dimensional matrix with one column and amount of rows being power of two
        :return: string representation of qubit, if possible to describe without precision losses otherwise return None
        """
        braket_length = int(math.log2(matrix_representation.size))

        possible_braket_representations = [
            "|" + "".join(s) + ">" for s in product(QUBIT_MATRICES.keys(), repeat=braket_length)
        ] + ["-|" + "".join(s) + ">" for s in product(QUBIT_MATRICES.keys(), repeat=braket_length)]
        matches_found = []

        for braket in possible_braket_representations:
            if np.allclose(States.decode_state(braket), matrix_representation):
                matches_found.append(braket)
        if not matches_found:
            raise ValueError("No braket representation was found")

        if len(matches_found) > 1:
            raise RuntimeError("More than one braket representation was found")

        return matches_found[0]
