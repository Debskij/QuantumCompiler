# Quantum Compiler
[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/Debskij/QuantumCompiler/main?filepath=examples%2Fpresentation.ipynb)
![Sanity check](https://github.com/DebskiJ/QuantumCompiler/actions/workflows/main.yml/badge.svg)

Library for basic computations on quantum bit circuits.
To get started quickly, click on "Binder" badge above to run simple example in Jupyter Notebook online.

## API of public methods

#### `QuantumCircuit`
Class describing basic circuit operations.

1. X-pauli gate.

    ```python
    x(self, position: int) -> None:
        """
        X-pauli gate, also called not-gate, change |0> to |1> and |1> to |0>.
    
        :param position: index of qbit to be reverted
        :return: None
        """
    ```

2. Z-pauli gate.

    ```python
    z(self, position: int) -> None:
        """
        Z-pauli gate, also called phase-flip-gate, leave |0> unchanged and replaces |1> with -|1>.
    
        :param position: index of qbit to be reverted
        :return: None
        """
    ```

3. H-pauli gate.

    ```python
    h(self, position: int) -> None:
        """
        H-gate, called Hadamard gate, change status from |0> to (|0> + |1>)/sqrt(2) and |1> to (|0> - |1>)/sqrt(2).

        :param position: index of ubit to be reverted
        :return: None
        """
    ```

4. Show state of qubit.

    ```python
    show_state(self) -> str:
        """
        Return current string representation of qbit.

        :return: string representation of qbit
        """
    ```
   
5. Measure qubit.

    ```python
    measure(self) -> typing.Optional[str]:
        """
        Measure value of superpositioned qbit based on digital random module.

        :return: integer value 0 or 1 of measured qbits
        """
    ```
   
#### Drawing qubits
Set of functions for plotting quantum circuits.

1. Draw sample qubits on the plane.

    ```python
    draw_qbit() -> None:
        """Draw sample qbits on the plane."""
    ```

2. Draw quantum state of qubit.

    ```python
    draw_quantum_state(coords: typing.List[int], name: str, color: str = "blue") -> None:
        """
        Draw quantum state of qbit.
    
        :param coords: coordinates of quantum state on the plane.
        :param name: name of the quantum state to plot
        :param color: color of drawn arrow
        :return: None
        """
    ```
   
---

Authors:
* Jakub Dębski
* Bazyli Polednia