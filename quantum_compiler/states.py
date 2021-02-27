import typing
import numpy as np


class States:
    @staticmethod
    def decode_state(qubit_representation: str) -> np.ndarray:
        """Converts string representation of qubit (ex. |01>, |+>, |->, |001>, |+++>) to matrix form

        :param qubit_representation: string started with | and ended with >
                                     containing any number of 0, 1, + and -
        :return: matrix containing float values of qubit('s). Size of matrix is determined by
                 length of symbols. It will always contain pow(2, len(qubit_representation)-2)
        """

        return []  # type: ignore

    @staticmethod
    def encode_state(matrix_representation: np.ndarray) -> typing.Optional[str]:
        """Converts matrix representation of qubit to string form

        :param matrix_representation: single dimensional matrix with one column and amount of rows being power of two
        :return: string representation of qubit, if possible to describe without precision losses otherwise return None
        """
