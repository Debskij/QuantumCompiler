from numpy import array


class sq_gates:
    unitary = array([1, 0],
                    [0, 1])

    x_pauli = array([0, 1],
                    [1, 0])

    z_pauli = array([1, 0],
                    [0, -1])

    hadamard = 1 / 2 ** (1 / 2) * array([1, 1],
                                        [1, -1])
