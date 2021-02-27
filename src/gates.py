from numpy import array

from .matrix import Matrix


class QuantumGates:
    unitary = Matrix([[1, 0],
                      [0, 1]])

    x_pauli = Matrix([[0, 1],
                      [1, 0]])

    z_pauli = Matrix([[1, 0],
                      [0, -1]])

    hadamard = Matrix(list(1 / 2 ** (1 / 2) * array([1, 1],
                                                    [1, -1])))
