# Quantum Games Lab

### Qiskit Fall Fest 2026 — IIIT Kottayam Quantum Hackathon

**Track 1: Quantum Games & Interactive Puzzles**

---

## Project Overview

Quantum Games Lab is a collection of interactive educational games designed to introduce quantum computing concepts through familiar puzzles and hands-on experimentation.

This repository contains two Python-based Streamlit applications:

1. **Quantum Circuit Puzzle Lab** — an interactive learning game for exploring quantum gates, circuits, and measurement behavior.
2. **Quantum Minesweeper: The Superposition Challenge** — a Minesweeper-inspired game that uses Qiskit quantum-circuit simulation to generate a hidden minefield.

Both projects combine interactive gameplay with educational explanations of quantum computing concepts.

## Project Metadata

* **Project Title:** Quantum Games Lab
* **Featured Game:** Quantum Minesweeper: The Superposition Challenge
* **Team Name:** Quantum Minesweepers
* **Hackathon Track:** Track 1 — Quantum Games & Interactive Puzzles
* **Team Size:** 1 member currently listed
* **Video Presentation:** To be added after recording
* **Live Demo Timestamp:** To be added after recording

### Team Member

| Name                  | Email                                                                 | GitHub                                                         |
| --------------------- | --------------------------------------------------------------------- | -------------------------------------------------------------- |
| Thavalam Reddy Rohith | [reddyrohiththavalam@gmail.com](mailto:reddyrohiththavalam@gmail.com) | [@reddyrohiththavalam](https://github.com/reddyrohiththavalam) |

---

## Project 1: Quantum Circuit Puzzle Lab

### Overview

Quantum Circuit Puzzle Lab is an interactive Streamlit application that introduces users to quantum gates and simple quantum circuits through hands-on challenges.

### Features

* Ten configured learning levels.
* Visualization of one-qubit quantum circuits.
* Experiments using X, H, and Z gates.
* Quantum circuit simulation using Qiskit Aer.
* Interactive exploration of quantum behavior.

### Technologies

* Python
* Streamlit
* Qiskit
* Qiskit Aer
* NumPy

### Run Locally

From the repository root, open PowerShell and run:

```powershell
cd quantum-circuit-puzzle
python -m pip install -r requirements.txt
python -m streamlit run app.py
```

Streamlit will display a local URL, usually `http://localhost:8501`.

### Streamlit Cloud Deployment

Use the following settings when creating a deployment:

* **Repository:** `reddyrohiththavalam/quantum-games-lab`
* **Branch:** `main`
* **Main file path:** `quantum-circuit-puzzle/app.py`

Ensure that `quantum-circuit-puzzle/requirements.txt` contains the dependencies required by this application.

---
## 🚀 Live Demo

**Quantum Circuit Puzzle Lab:** [Play Online](https://quantum-games-lab-fxyurfskfyfukngxicibys.streamlit.app/)

**Quantum Minesweeper:** Deployment pending verification.


## Project 2: Quantum Minesweeper — The Superposition Challenge

### Overview

Quantum Minesweeper is a 3 × 3 Minesweeper-inspired game that uses Qiskit to generate a hidden board through quantum measurement.

The application prepares nine qubits, applies probability-controlled RY rotation gates, and measures the qubits to produce classical outcomes. These outcomes determine which tiles contain mines. Players reveal tiles and use neighboring mine counts as clues.

The game combines quantum-circuit simulation, classical game logic, and an interactive Streamlit interface.

### Motivation

Minesweeper is a familiar puzzle based on uncertainty, logical reasoning, and decision-making. Integrating a quantum circuit offers a practical way to explore qubits, state preparation, measurement, and probability through an accessible game.

### Quantum Architecture

The application demonstrates the following concepts:

* **Qubits:** Nine qubits represent the nine board positions.
* **State preparation:** RY rotation gates prepare qubits in probabilistic quantum states.
* **Measurement:** Each qubit is measured to obtain a classical bit.
* **Measurement probability:** The rotation angle controls the probability of measuring `1`.
* **Classical post-processing:** Python maps the measurement outcomes to board tiles and calculates neighboring mine counts.

### Circuit Details

| Property              | Description                     |
| --------------------- | ------------------------------- |
| Board size            | 3 × 3                           |
| Number of qubits      | 9                               |
| Rotation gate         | RY                              |
| Measurement           | Computational-basis measurement |
| Simulator             | Qiskit Aer                      |
| Application framework | Streamlit                       |
| Other technologies    | Python, NumPy, Matplotlib       |

For a desired mine probability \(p\), the RY rotation angle is:

$$
\theta = 2\arcsin(\sqrt{p})
$$

An illustrative circuit is shown below:

```python
from math import asin, sqrt
from qiskit import QuantumCircuit

n_qubits = 9
mine_probability = 0.25
theta = 2 * asin(sqrt(mine_probability))

qc = QuantumCircuit(n_qubits, n_qubits)

for qubit in range(n_qubits):
    qc.ry(theta, qubit)

qc.measure(range(n_qubits), range(n_qubits))
```

This example illustrates the circuit preparation. Refer to the actual application source code for the complete runnable implementation.

### Run Locally

From the repository root, open PowerShell and run:

```powershell
cd quantum-minesweeper-qiskit
python -m pip install -r requirements.txt
python -m streamlit run src/app.py
```

Streamlit will display a local URL, usually `http://localhost:8501`.

If the project dependencies do not include Streamlit, add it to this project's `requirements.txt` before installing.

### Streamlit Cloud Deployment

Use the following settings for the Minesweeper deployment:

* **Repository:** `reddyrohiththavalam/quantum-games-lab`
* **Branch:** `main`
* **Main file path:** `quantum-minesweeper-qiskit/src/app.py`

The Minesweeper application has its own dependency file:

`quantum-minesweeper-qiskit/requirements.txt`

Ensure this file is committed to GitHub and contains compatible versions of Streamlit, Qiskit, Qiskit Aer, and the other packages imported by the application.

**Important:** The dependency file must be located inside `quantum-minesweeper-qiskit/` for this deployment configuration. Verify the installation logs after deploying to confirm that Qiskit is installed successfully.

### Explore the Notebook

If the repository includes `notebooks/solution.ipynb`, you can explore it locally using:

```powershell
python -m pip install jupyter
python -m jupyter notebook notebooks/solution.ipynb
```

Run these commands from the `quantum-minesweeper-qiskit` directory.

---

## Repository Structure

The combined repository is organized as follows:

```text
quantum-games-lab/
├── README.md
├── .gitignore
│
├── quantum-circuit-puzzle/
│   ├── app.py
│   ├── requirements.txt
│   ├── README.md
│   ├── tests/
│   └── screenshots/
│
└── quantum-minesweeper-qiskit/
    ├── README.md
    ├── requirements.txt
    ├── runtime.txt
    ├── HACKATHON_GUIDE.md
    ├── LICENSE
    ├── view.pdf
    ├── src/
    │   └── app.py
    ├── notebooks/
    └── references/
```

This is the intended structure. Keep only the files and folders that actually exist in your repository, and update this section if the project structure changes.

---

## Gameplay and Demonstration

### Quantum Circuit Puzzle Lab

1. Launch the Streamlit application.
2. Select a learning level.
3. Experiment with the available quantum gates.
4. Inspect the circuit and simulated behavior.
5. Complete the configured challenges.

### Quantum Minesweeper

1. Launch the Streamlit application.
2. Choose the desired mine probability, if supported by the interface.
3. Generate a new board.
4. Prepare and measure the quantum circuit using the simulator.
5. Map the measurement outcomes to mine and safe tiles.
6. Reveal tiles and examine neighboring mine-count clues.
7. Generate another board to obtain a new set of measurement outcomes.
8. Explore the notebook, if available, to inspect the circuit and experiment with simulation statistics.

The steps above describe the intended gameplay flow. Confirm each feature against the actual implementation before using it in a recorded demonstration.

---

## Screenshots and Video

Add genuine project evidence before final submission:

* Screenshot of Quantum Circuit Puzzle Lab running.
* Screenshot of the Minesweeper board before revealing tiles.
* Screenshot showing revealed tiles and neighboring mine-count clues.
* Screenshot of the quantum circuit or notebook visualization.
* Video presentation link.
* Live demo timestamp, if required by the hackathon.

Only include screenshots, videos, and experimental results obtained from the actual implementation.

---

## Classical vs. Quantum Comparison

For the described Quantum Minesweeper model, a classical baseline can independently assign a mine to each tile with probability \(p\).

The quantum circuit applies RY rotations chosen so that each qubit has probability \(p\) of producing the designated mine outcome. For independently prepared qubits, ideal measurements reproduce the corresponding independent Bernoulli probability model.

This makes the circuit a useful educational demonstration of quantum state preparation and measurement. It does **not** establish a quantum speedup or gameplay advantage over classical random sampling.

---

## Results and Limitations

### Project Highlights

* Two interactive quantum-learning games.
* Quantum gate and circuit exploration.
* Nine-qubit board generation in Quantum Minesweeper.
* Measurement outcomes mapped to a playable grid.
* Classical logic for neighboring mine counts.
* Notebook-based circuit exploration, if included in the implementation.

### Limitations

* Quantum Minesweeper uses a small nine-qubit board.
* The described circuit prepares independent qubits rather than using entanglement to solve the puzzle.
* Qiskit Aer simulation runs on classical computing hardware.
* Finite measurement shots can introduce statistical variation.
* The project does not demonstrate quantum advantage.
* Neighboring mine-count calculations and gameplay rules are classical.
* Larger boards would require additional qubits and more application logic.
* Real quantum hardware can introduce gate errors, readout errors, and decoherence.

Any numerical performance claims or experimental conclusions should be added only after running the corresponding tests and experiments.

---

## Testing

Quantum Circuit Puzzle Lab includes a test suite. From the repository root, run:

```powershell
python -m unittest discover -s quantum-circuit-puzzle/tests -v
```

Review the test output and resolve failures before presenting the project.

For Quantum Minesweeper, follow any testing or experiment instructions documented in its project files.

---

## Installation Requirements

* Python version compatible with the selected project dependencies.
* pip.
* A modern web browser.
* Git.
* Jupyter Notebook, if you want to explore the experiment notebook.

Install dependencies separately using each project's `requirements.txt` file. If both applications share a Python environment, check that their dependency versions are compatible.

---

## References

* [Qiskit Documentation](https://docs.quantum.ibm.com/)
* [Qiskit Aer](https://github.com/Qiskit/qiskit-aer)
* [Streamlit Documentation](https://docs.streamlit.io/)
* [NumPy Documentation](https://numpy.org/doc/)
* [Matplotlib Documentation](https://matplotlib.org/stable/)
* [Qiskit Fall Fest 2026 — IIIT Kottayam Hackathon Template](https://github.com/Shanwis/Qiskit-Fall-Fest-2026-IIITKottayam-Hackathon-Template)

---

## Acknowledgments

This project is intended for educational exploration of quantum computing through interactive games.

AI assistance was used during development. The project author is responsible for reviewing, understanding, testing, and presenting the implementation.

Additional contributors, resources, and collaborators should be acknowledged before final submission.

## License

Review the license and reuse conditions of both individual projects before redistributing the combined repository. Preserve applicable copyright notices and license terms.

---

**Quantum Games Lab**

*Explore quantum gates. Experiment with measurement. Learn through play.*
