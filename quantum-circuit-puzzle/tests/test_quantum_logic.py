import unittest

from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector


class QuantumGateTests(unittest.TestCase):
    def test_x_gate_flips_zero_to_one(self):
        circuit = QuantumCircuit(1)
        circuit.x(0)

        state = Statevector.from_instruction(circuit)

        self.assertAlmostEqual(abs(state.data[1]) ** 2, 1.0, places=7)

    def test_two_hadamard_gates_return_zero(self):
        circuit = QuantumCircuit(1)
        circuit.h(0)
        circuit.h(0)

        state = Statevector.from_instruction(circuit)

        self.assertAlmostEqual(abs(state.data[0]) ** 2, 1.0, places=7)

    def test_hadamard_creates_equal_probabilities(self):
        circuit = QuantumCircuit(1)
        circuit.h(0)

        state = Statevector.from_instruction(circuit)
        probabilities = state.probabilities()

        self.assertAlmostEqual(probabilities[0], 0.5, places=7)
        self.assertAlmostEqual(probabilities[1], 0.5, places=7)

    def test_h_then_z_creates_minus_state(self):
        circuit = QuantumCircuit(1)
        circuit.h(0)
        circuit.z(0)

        state = Statevector.from_instruction(circuit)

        self.assertAlmostEqual(abs(state.data[0] - state.data[1]) ** 2, 0.0, places=7)
        self.assertAlmostEqual(abs(state.data[0]) ** 2, 0.5, places=7)
        self.assertAlmostEqual(abs(state.data[1]) ** 2, 0.5, places=7)


if __name__ == "__main__":
    unittest.main()
