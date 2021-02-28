import pytest
import numpy as np
from itertools import product
from .. import states

QUBIT_SYMBOLS = ["0", "1", "+", "-"]
QUBITS = []

for i in range(1, 5):
    qubits_i = [s for s in product(QUBIT_SYMBOLS, repeat=i)]
    QUBITS.extend(["|" + "".join(s) + ">" for s in qubits_i])


@pytest.mark.parametrize("qubit", QUBITS)
def test_decode_state(qubit):
    decoded_state = states.States.decode_state(qubit)
    possibilities = np.square(decoded_state)
    assert abs(1 - np.sum(possibilities)) < states.EPSILON
