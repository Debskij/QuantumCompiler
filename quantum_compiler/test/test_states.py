import pytest
import numpy as np
from itertools import product
from .. import states

QUBITS = []

for i in range(1, 4):
    qubits_i = [s for s in product(states.QUBIT_MATRICES.keys(), repeat=i)]
    QUBITS.extend(["|" + "".join(s) + ">" for s in qubits_i])
    QUBITS.extend(["-|" + "".join(s) + ">" for s in qubits_i])


@pytest.mark.parametrize("qubit", QUBITS)
def test_decode_state(qubit):
    decoded_state = states.States.decode_state(qubit)
    possibilities = np.square(decoded_state)
    assert abs(1 - np.sum(possibilities)) < states.EPSILON


def test_encode_state_positive():
    assert (
        states.States.encode_state(
            np.array(
                [
                    0.0,
                    0.0,
                    -0.0,
                    -0.0,
                    0.0,
                    0.0,
                    -0.0,
                    -0.0,
                    0.0,
                    0.0,
                    -0.0,
                    -0.0,
                    0.0,
                    0.0,
                    -0.0,
                    -0.0,
                    0.0,
                    0.0,
                    -0.0,
                    -0.0,
                    0.5,
                    0.5,
                    -0.5,
                    -0.5,
                    0.0,
                    0.0,
                    -0.0,
                    -0.0,
                    0.0,
                    0.0,
                    -0.0,
                    -0.0,
                ]
            )
        )
        == "|101-+>"
    )


def test_encode_state_negative():
    assert states.States.encode_state(np.array([0.0, -1.0])) == "-|1>"


@pytest.mark.parametrize("qubit", QUBITS)
def test_cycle_decode_encode(qubit):
    assert states.States.encode_state(states.States.decode_state(qubit)) == qubit
