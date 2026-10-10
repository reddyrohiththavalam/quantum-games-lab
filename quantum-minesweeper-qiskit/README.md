# Qiskit Fall Fest 2026 — Project Submission Template

**IIIT Kottayam Quantum Hackathon (24-Hour Sprint)**

---

# Project Title

## Project Metadata

* **Project Title:** Quantum Minesweeper: The Superposition Challenge
* **Team Name:** Quantum Minesweepers
* **Chosen Track:** Track 1: Quantum Games & Interactive Puzzles
* **Video Presentation Link:** To be added after recording the final presentation.
* **Live Demo Timestamp in Video:** To be added after recording.

### Team Members (Max 4 members)

| Name                   | Email              | GitHub Username        |
| :--------------------- | :----------------- | :--------------------- |
| [Enter your full name] | [Enter your email] | [@reddyrohiththavalam] |

---

## 1. Project Overview & Motivation

* **Summary (3–4 sentences):**

  Quantum Minesweeper is an interactive 3×3 Minesweeper-inspired game that uses Qiskit to generate a hidden board through quantum measurement. The game prepares nine qubits, applies probability-controlled rotation gates, and measures each qubit to determine whether its corresponding tile contains a mine. Players reveal tiles and use neighboring mine counts as clues to explore the board. The project combines quantum circuit simulation, classical game logic, and an interactive Streamlit interface to demonstrate how quantum measurement can be used in a simple game.

* **Why this problem / game?**

  Minesweeper is an accessible puzzle that combines uncertainty, logical reasoning, and decision-making. By using a quantum circuit to generate the hidden board, this project provides a practical introduction to qubits, quantum gates, measurement, and probability. The small board makes the game easy to understand while allowing users to inspect the quantum circuit and compare its behavior with a classical random baseline.

---

## 2. Quantum Architecture & Mechanics

* **Core Quantum Principles Used:**

  * **Qubit superposition:** Rotation gates prepare qubits in probabilistic quantum states.
  * **Quantum measurement:** Measuring each qubit produces a classical bit that determines the corresponding tile.
  * **Measurement probabilities:** The rotation angle controls the probability of measuring a mine bit.
  * **Classical post-processing:** The measured bit string is converted into the game board, and ordinary Python logic calculates neighboring mine counts.

  This implementation does not use entanglement or claim a quantum computational advantage.

* **How the Quantum Circuit is Integrated:**

  The game uses a 3×3 grid represented by nine qubits. For a selected mine probability \(p\), each qubit is prepared with an RY rotation whose angle is \(\theta = 2\arcsin(\sqrt{p})\). Each qubit is then measured in the computational basis. A measured `1` represents a mine and a measured `0` represents a safe tile.

  The resulting board is stored for the current round. When the player reveals a tile, the application displays the result and calculates the number of neighboring mines using classical Python logic. Creating a new board runs the circuit again to obtain a fresh measured outcome.

* **Circuit Details:**

  * **Number of Qubits:** 9
  * **Key Gates Used:** RY rotation gates and computational-basis measurements.
  * **Primitives Used:** Qiskit circuit simulation with Qiskit Aer.
  * **Other Technologies Used:** Python, Streamlit, NumPy, Matplotlib, and Jupyter Notebook.

Representative circuit preparation:

```python
from qiskit import QuantumCircuit
from math import asin, sqrt

n_qubits = 9
mine_probability = 0.25
theta = 2 * asin(sqrt(mine_probability))

qc = QuantumCircuit(n_qubits, n_qubits)

for qubit in range(n_qubits):
    qc.ry(theta, qubit)

qc.measure(range(n_qubits), range(n_qubits))
```

The circuit is illustrative of the preparation and measurement approach used in the project. The application and notebook contain the runnable implementation.

---

## 3. Repository Structure & How to Run

### Project Structure

```text
quantum-minesweeper-qiskit/
├── README.md
├── requirements.txt
├── HACKATHON_GUIDE.md
├── src/
│   └── app.py
├── notebooks/
│   └── solution.ipynb
└── references/
    └── Track-specific hackathon resources
```

### Installation & Execution Instructions

**Requirements:** Python, pip, and the dependencies listed in `requirements.txt`.

1. **Clone the repository:**

   ```bash
   git clone https://github.com/reddyrohiththavalam/quantum-minesweeper-qiskit.git
   cd quantum-minesweeper-qiskit
   ```

2. **Create and activate a virtual environment (recommended):**

   On Windows PowerShell:

   ```powershell
   python -m venv .venv
   .\.venv\Scripts\Activate.ps1
   ```

   On macOS/Linux:

   ```bash
   python -m venv .venv
   source .venv/bin/activate
   ```

3. **Install dependencies:**

   ```bash
   python -m pip install -r requirements.txt
   python -m pip install streamlit
   ```

4. **Run the interactive game:**

   ```bash
   python -m streamlit run src/app.py
   ```

   Open the local URL displayed in the terminal, usually `http://localhost:8501`.

5. **Run the experiment notebook:**

   ```bash
   python -m jupyter notebook notebooks/solution.ipynb
   ```

   The notebook includes circuit preparation, measurement experiments, visualization, a probability check, and a classical comparison.

---

## 4. Implementation Walkthrough & Live Demo

* **Walkthrough of Gameplay / Optimization Pipeline:**

  1. Launch the Streamlit application.
  2. Choose the desired mine probability using the application controls.
  3. Generate a new quantum board.
  4. The application prepares nine qubits, applies rotation gates, and measures the circuit using the quantum simulator.
  5. The measurement outcomes are mapped to mine and safe tiles.
  6. Reveal tiles to see their outcomes and the neighboring mine-count clues.
  7. Start a new board to obtain a new set of measurement outcomes.
  8. Use the notebook to inspect the circuit, visualize outcomes, and compare measured statistics with a classical random model.

* **Key Screenshots / Terminal Output:**

  Capture and add the following before final submission:

  * A screenshot of the running game before revealing tiles.
  * A screenshot showing revealed tiles and neighboring mine-count clues.
  * A screenshot of the quantum circuit or notebook probability plot.
  * A screenshot of the classical-versus-quantum sampling experiment.

  Screenshots should come from the actual running project and should not be presented as measured results unless the experiment was executed.

---

## 5. Classical vs. Quantum Comparison

* **Classical Baseline / Counterpart:**

  The classical baseline is an independent random-board model in which each tile is assigned a mine with probability \(p\). For a fair comparison, the classical model uses the same board size and mine probability as the quantum circuit. The notebook compares observed mine frequencies from quantum-circuit simulation with frequencies from classical Bernoulli sampling.

* **Comparative Analysis:**

  For each qubit, the rotation angle is chosen so that the probability of measuring `1` is \(p\). With the same probability and independent qubit preparation, the ideal quantum measurement distribution for this circuit matches the corresponding classical independent Bernoulli model.

  The quantum implementation demonstrates how a circuit can generate the board, but it does not establish a speedup or a gameplay advantage over classical sampling. The main contribution is educational: players can explore a familiar puzzle while examining the quantum preparation and measurement process.

---

## 6. Performance, Results & Limitations

* **Key Results & Observations:**

  * The game represents a 3×3 board using nine qubits.
  * The mine probability is controlled through rotation-gate parameters.
  * Circuit measurement outcomes are converted into a playable grid.
  * Classical logic calculates neighboring mine counts.
  * The notebook executes circuit experiments, displays outputs, visualizes results, and compares quantum-simulator statistics with classical sampling.

  The notebook's finite-shot results are statistical samples; observed frequencies can differ from the selected probability due to sampling variation. Exact numerical conclusions should be reported from the saved experiment outputs rather than assumed in advance.

* **Critical Reflection on Limitations:**

  * The game uses a small nine-qubit board and does not demonstrate quantum advantage.
  * The circuit prepares independent qubits; it does not use entanglement or interference to solve the puzzle.
  * Qiskit Aer simulation runs on classical computing hardware and is not evidence of execution on a physical quantum processor.
  * Finite measurement shots introduce statistical variation.
  * Larger boards require more qubits, additional circuit resources, and more complex user-interface logic.
  * On real quantum hardware, gate errors, readout errors, decoherence, and other noise can affect the measured board.
  * The game logic and neighboring mine-count calculations are classical.
  * The current project is an educational prototype, not a quantum-accelerated Minesweeper solver.

---

## 7. References & Acknowledgments

* **Qiskit:** https://qiskit.org/
* **Qiskit Aer:** https://github.com/Qiskit/qiskit-aer
* **Streamlit documentation:** https://docs.streamlit.io/
* **NumPy documentation:** https://numpy.org/doc/
* **Matplotlib documentation:** https://matplotlib.org/stable/
* **Hackathon template:** https://github.com/Shanwis/Qiskit-Fall-Fest-2026-IIITKottayam-Hackathon-Template

**Acknowledgments:** This project was developed for Qiskit Fall Fest 2026, Track 1: Quantum Games & Interactive Puzzles. AI assistance was used during development; the project author is responsible for reviewing, understanding, testing, and presenting the implementation. Any additional resources or collaborators used in the final project should be acknowledged here.
