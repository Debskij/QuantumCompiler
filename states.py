from typing import List, Optional


class states:
    @staticmethod
    def decode_state(qubit_representation: str) -> List[float]:
        """Converts string representation of qubit (ex. |01>, |+>, |->, |001>) to matrix form
        :keyword
        qubit_representation: string started with | and ended with >
                              containing any number of binary digits or single + or -
        :return
        matrix: matrix containing float values of qubit('s). Size of matrix is determined by
                length of symbols. It will always contain pow(2, len(qubit_representation)-2)
        """

    @staticmethod
    def encode_state(matrix_representation: List[float]) -> Optional[str]:
        """Converts matrix representation of qubit to string form
        :keyword
        matrix_representation: single dimensional matrix with one column and amount of rows being power of two
        :return
        qubit_representation: string representation of qubit if possible to describe without losses otherwise
                              returns None
        """