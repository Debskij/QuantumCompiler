import numpy as np
import typing
from functools import reduce
from random import random
from .gates import QuantumGates
from .states import States

if typing.TYPE_CHECKING:
    from .matrix import Matrix


class QuantumCircuit:
    def __init__(self, qbit_amount: int):
        """ class describing circuit basic operations

        :param qbit_amount: integer value describing amount of qbits in circuit
        """
        self.qbit_amount = qbit_amount
        self.string_representation = "|" + "0" * qbit_amount + ">"
        self.matrix_representation = States.decode_state(self.string_representation)

    def gate_creator(self, position: int, gate: QuantumGates) -> Matrix:
        operator_list = [QuantumGates.unitary for _ in range(self.qbit_amount)]  # type: ignore
        operator_list[position] = gate  # type: ignore
        return reduce((lambda x, y: x + y), operator_list)

    def x(self, position: int) -> np.array:
        """ x-pauli gate, also called not-gate, changes |0> to |1> and |1> to |0>

        :param position: declares which qbit has to be reverted
        """
        return self.matrix_representation * self.gate_creator(position, QuantumGates.x_pauli)  # type: ignore

    def z(self, position: int) -> np.array:
        """ z-pauli gate, also called phase-flip-gate, leaves |0> unchanged and replaces |1> with -|1>

        :param position: declares which qbit has to be modified
        """
        return self.matrix_representation * self.gate_creator(position, QuantumGates.z_pauli)  # type: ignore

    def h(self, position: int) -> np.array:
        """ h-gate, called Hadamard gate, changes status from |0> to (|0> + |1>)/sqrt(2) and |1> to (|0> - |1>)/sqrt(2)

        :param position: declares which qbit has to be modified
        """
        return self.matrix_representation * self.gate_creator(position, QuantumGates.hadamard)  # type: ignore

    def measure(self) -> typing.Optional[str]:
        """ function measuring value of superpositioned qbit basing on digital random module

        :return: integer value 0 or 1 of measured qbits
        """
        probability = np.cumsum(self.matrix_representation)
        return_val = np.zeros(2 ** self.qbit_amount)
        random_val = random()
        return_val[list(probability).index(random_val)] = 1.0
        return States.encode_state(return_val)
