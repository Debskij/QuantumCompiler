from .matrix import Matrix

SQRT2 = 1 / 2 ** (1 / 2)


class QuantumGates:
    """Class for describing gates' matrix values."""

    unitary = Matrix([[1, 0], [0, 1]])

    x_pauli = Matrix([[0, 1], [1, 0]])

    z_pauli = Matrix([[1, 0], [0, -1]])

    hadamard = Matrix([[SQRT2, SQRT2], [SQRT2, -SQRT2]])
