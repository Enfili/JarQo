"""Create a Bell state with PennyLane's local quantum simulator."""

import pennylane as qml


device = qml.device("default.qubit", wires=2)


@qml.qnode(device)
def bell_state():
    qml.Hadamard(wires=0)
    qml.CNOT(wires=[0, 1])
    return qml.probs(wires=[0, 1])


if __name__ == "__main__":
    print(qml.draw(bell_state)())
    print("Probabilities for |00>, |01>, |10>, |11>:")
    print(bell_state())  # Expected: [0.5, 0.0, 0.0, 0.5]
