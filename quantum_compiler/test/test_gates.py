from ..qbit import QuantumCircuit


def test_x_gate_on_single_qbit():
    a1 = QuantumCircuit(1)
    assert a1.measure() == "|0>", "Circuit initialized with invalide value"
    a1.x(0)
    assert a1.measure() == "|1>", "Not gate isnt working properly for single qbit"


def test_x_gate_on_multiple_qbits():
    a1 = QuantumCircuit(5)
    assert a1.measure() == "|00000>", "Circuit initialized with invalide value"
    a1.x(0)
    a1.x(2)
    a1.x(4)
    assert a1.measure() == "|10101>", "Not gate isnt working properly for multiple qbits"
    a1.x(2)
    assert a1.measure() == "|10001>", "Reverse operation for not gate isnt working properly"


def test_z_gate_on_single_qbit():
    a1 = QuantumCircuit(1)
    assert a1.measure() == "|0>", "Circuit initialized with invalide value"
    a1.z(0)
    assert a1.measure() == "|0>", "Z-gate shouldnt change value after operation on 0"
    a1.x(0)
    assert a1.measure() == "|1>", "Not-gate isnt working properly for single qbit"
    a1.z(0)
    assert a1.measure() == "-|1>", "Z-gate didnt flip sign for |1>"


def test_z_gate_on_multiple_qbits():
    a1 = QuantumCircuit(4)
    assert a1.measure() == "|0000>", "Circuit initialized with invalide value"
    a1.z(1)
    a1.z(3)
    assert a1.measure() == "|0000>", "Z-gate shouldnt change value after operation on 0"
    a1.x(0)
    a1.x(2)
    assert a1.measure() == "|1010>", "Not-gate isnt working properly for multiple qbits"
    a1.z(0)
    a1.z(1)
    assert a1.measure() == "-|1010>", "Sign didnt change properly, it should change once"
    a1.z(0)
    assert a1.measure() == "|1010>", "Z-gate didnt flip sign for |1> backwards"

