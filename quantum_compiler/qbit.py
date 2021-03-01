import typing
from bisect import bisect
from functools import reduce
from random import random

import numpy as np

from .gates import QuantumGates
from .matrix import Matrix
from .states import States


class QuantumCircuit:
    def __init__(self, qbit_amount: int):
        """class describing circuit basic operations

        :param qbit_amount: integer value describing amount of qbits in circuit
        """
        self.qbit_amount = qbit_amount
        self.string_representation = "|" + "0" * qbit_amount + ">"
        self.matrix_representation = States.decode_state(self.string_representation)

    def gate_creator(self, position: int, gate: QuantumGates) -> Matrix:
        operator_list = [QuantumGates.unitary for _ in range(self.qbit_amount)]  # type: ignore
        operator_list[position] = gate  # type: ignore
        return reduce((lambda x, y: x + y), operator_list)  # type: ignore

    def x(self, position: int) -> np.ndarray:
        """x-pauli gate, also called not-gate, changes |0> to |1> and |1> to |0>

        :param position: declares which qbit has to be reverted
        """
        self.matrix_representation = self.gate_creator(position, QuantumGates.x_pauli) * \
                                     Matrix(self.matrix_representation)  # type: ignore

    def z(self, position: int):
        """z-pauli gate, also called phase-flip-gate, leaves |0> unchanged and replaces |1> with -|1>

        :param position: declares which qbit has to be modified
        """
        self.matrix_representation = self.matrix_representation * self.gate_creator(position,
                                                                                    QuantumGates.z_pauli)  # type: ignore

    def h(self, position: int) -> np.ndarray:
        """h-gate, called Hadamard gate, changes status from |0> to (|0> + |1>)/sqrt(2) and |1> to (|0> - |1>)/sqrt(2)

        :param position: declares which qbit has to be modified
        """
        # return self.matrix_representation * self.gate_creator(position, QuantumGates.hadamard)  # type: ignore

    def show_state(self) -> str:
        return States.encode_state(self.matrix_representation)

    def measure(self) -> typing.Optional[str]:
        """function measuring value of superpositioned qbit basing on digital random module

        :return: integer value 0 or 1 of measured qbits
        """
        probability = np.cumsum(self.matrix_representation)
        return_val = np.zeros(2 ** self.qbit_amount)
        random_val = random()
        return_val[bisect(list(probability), random_val)] = 1.0
        return States.encode_state(return_val)
