from ..qbit import QuantumCircuit


def test_x_gate_on_single_qbit():
    a1 = QuantumCircuit(1)
    assert a1.measure() == "|0>", "Circuit initialized with invalid value"
    a1.x(0)
    assert a1.measure() == "|1>", "Not gate isn't working properly for single qbit"


def test_x_gate_on_multiple_qbits():
    a1 = QuantumCircuit(5)
    assert a1.measure() == "|00000>", "Circuit initialized with invalid value"
    a1.x(0)
    a1.x(2)
    a1.x(4)
    assert a1.measure() == "|10101>", "Not gate isn't working properly for multiple qbits"
    a1.x(2)
    assert a1.measure() == "|10001>", "Reverse operation for not gate isn't working properly"


def test_z_gate_1():
    a1 = QuantumCircuit(1)
    a1.x(0)
    a1.z(0)
    assert a1.measure() == "-|1>", "Z-gate isn't working properly for single qbit"


def test_z_gate_on_single_qbit():
    a1 = QuantumCircuit(1)
    assert a1.measure() == "|0>", "Circuit initialized with invalid value"
    a1.z(0)
    assert a1.measure() == "|0>", "Z-gate shouldn't change value after operation on 0"
    a1.x(0)
    assert a1.measure() == "|1>", "Not-gate isn't working properly for single qbit"
    a1.z(0)
    assert a1.measure() == "-|1>", "Z-gate didn't flip sign for |1>"


def test_z_gate_on_multiple_qbits():
    a1 = QuantumCircuit(4)
    assert a1.measure() == "|0000>", "Circuit initialized with invalid value"
    a1.z(1)
    a1.z(3)
    assert a1.measure() == "|0000>", "Z-gate shouldn't change value after operation on 0"
    a1.x(0)
    a1.x(2)
    assert a1.measure() == "|1010>", "Not-gate isn't working properly for multiple qbits"
    a1.z(0)
    a1.z(1)
    assert a1.measure() == "-|1010>", "Sign didn't change properly, it should change once"
    a1.z(0)
    assert a1.measure() == "|1010>", "Z-gate didn't flip sign for |1> backwards"


def test_h_gate_on_single_qbit():
    a1 = QuantumCircuit(1)
    assert a1.measure() == "|0>", "Circuit initialized with invalid value"
    a1.h(0)
    assert a1.show_state() == "|+>", "H-gate didn't work fine for single qbit"
    a1.h(0)
    assert a1.measure() == "|0>", "Reversion of h-gate didn't work fine for single qbit"
    a1.x(0)
    assert a1.measure() == "|1>", "X-gate didn't work fine"
    a1.h(0)
    assert a1.show_state() == "|->", "H-gate didn't work fine for single qbit"
    a1.h(0)
    assert a1.measure() == "|1>", "Reversion of h-gate didn't work fine for single qbit"


def test_h_gate_on_multiple_qbits():
    a1 = QuantumCircuit(3)
    assert a1.measure() == "|000>", "Circuit initialized with invalid value"
    a1.h(0)
    assert a1.show_state() == "|+00>", "H-gate didn't work fine for 0 state"
    a1.x(1)
    assert a1.show_state() == "|+10>", "X-gate didn't work fine for 0 state"
    a1.h(1)
    assert a1.show_state() == "|+-0>", "H-gate didn't work fine for 1 state"
    a1.h(0)
    assert a1.show_state() == "|0-0>", "H-gate didn't work fine for + state"
    a1.h(1)
    assert a1.show_state() == "|010>", "H-gate didn't work fine for - state"
