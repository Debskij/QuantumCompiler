from random import random

import numpy as np

from .states import states


class QuantumCircuit:
    def __init__(self, qbit_amount: int):
        """ class describing circuit basic operations

        :param qbit_amount: integer value describing amount of qbits in circuit
        """
        self.qbit_amount = qbit_amount
        self.string_representation = '|' + '0' * qbit_amount + '>'
        self.matrix_representation = states.decode_state(self.string_representation)

    def x(self, position: int):
        """ x-pauli gate, also called not-gate, changes |0> to |1> and |1> to |0>

        :param position: declares which qbit has to be reverted
        """

    def z(self, position: int):
        """ z-pauli gate, also called phase-flip-gate, leaves |0> unchanged and replaces |1> with -|1>

        :param position: declares which qbit has to be modified
        """

    def h(self, position: int):
        """ h-gate, called Hadamard gate, changes status from |0> to (|0> + |1>)/sqrt(2) and |1> to (|0> - |1>)/sqrt(2)

        :param position: declares which qbit has to be modified
        """

    def measure(self) -> str:
        """ function measuring value of superpositioned qbit basing on digital random module

        :return: integer value 0 or 1 of measured qbits
        """
        probability = np.cumsum(self.matrix_representation)
        return_val = np.zeros(2 ** self.qbit_amount)
        random_val = random()
        return_val[probability.index(random_val)] = 1.0
        return states.encode_state(return_val)
