\# Quantum Games Lab



\### Qiskit Fall Fest 2026 — IIIT Kottayam Quantum Hackathon



\*\*Track 1: Quantum Games \& Interactive Puzzles\*\*



\---



\## Project Overview



Quantum Games Lab is a collection of interactive educational games designed to introduce quantum computing concepts through familiar puzzles and hands-on experimentation.



This repository contains two projects:



1\. \*\*Quantum Circuit Puzzle Lab\*\* — an interactive game for learning quantum gates and circuit behavior.

2\. \*\*Quantum Minesweeper: The Superposition Challenge\*\* — a Minesweeper-inspired game that uses Qiskit quantum-circuit simulation to generate a hidden minefield.



Both projects combine Python-based development with interactive learning experiences to help users explore quantum computing concepts.



\## Project Metadata



\* \*\*Project Title:\*\* Quantum Games Lab

\* \*\*Featured Game:\*\* Quantum Minesweeper: The Superposition Challenge

\* \*\*Team Name:\*\* Quantum Minesweepers

\* \*\*Chosen Track:\*\* Track 1 — Quantum Games \& Interactive Puzzles

\* \*\*Team Size:\*\* 1 member currently listed

\* \*\*Video Presentation:\*\* To be added after recording

\* \*\*Live Demo Timestamp:\*\* To be added after recording



\### Team Members



| Name                  | Email                                                                 | GitHub                                                         |

| --------------------- | --------------------------------------------------------------------- | -------------------------------------------------------------- |

| Thavalam Reddy Rohith | \[reddyrohiththavalam@gmail.com](mailto:reddyrohiththavalam@gmail.com) | \[@reddyrohiththavalam](https://github.com/reddyrohiththavalam) |



\---



\## Project 1: Quantum Circuit Puzzle Lab



\### Overview



Quantum Circuit Puzzle Lab is an interactive Streamlit application that introduces users to quantum gates and simple quantum circuits through hands-on challenges.



\### Features



\* Ten configured learning levels.

\* Visualization of one-qubit quantum circuits.

\* Experiments using X, H, and Z gates.

\* Quantum circuit simulation using Qiskit Aer.

\* Interactive interface for exploring quantum behavior.



\### Technologies



\* Python

\* Streamlit

\* Qiskit

\* Qiskit Aer

\* NumPy



\### How to Run



From the repository root, run:



```powershell

cd quantum-circuit-puzzle

python -m pip install -r requirements.txt

python -m streamlit run app.py

```



Open the local URL displayed in the terminal, usually `http://localhost:8501`.



\---



\## Project 2: Quantum Minesweeper — The Superposition Challenge



\### Overview



Quantum Minesweeper is a 3×3 Minesweeper-inspired game that uses Qiskit to generate a hidden board through quantum measurement.



The game prepares nine qubits, applies probability-controlled RY rotation gates, and measures each qubit to determine whether its corresponding tile contains a mine. Players reveal tiles and use neighboring mine counts as clues to explore the board.



The project combines quantum circuit simulation, classical game logic, and an interactive Streamlit interface to demonstrate quantum measurement and probability.



\### Motivation



Minesweeper is a familiar puzzle involving uncertainty, logical reasoning, and decision-making. Integrating a quantum circuit provides a practical way to explore qubits, quantum gates, measurement, and probability in an accessible game environment.



\### Quantum Architecture



\*\*Core concepts:\*\*



\* \*\*Qubit superposition:\*\* RY rotation gates prepare qubits in probabilistic quantum states.

\* \*\*Quantum measurement:\*\* Each measured qubit produces a classical bit.

\* \*\*Measurement probability:\*\* The rotation angle controls the probability of measuring `1`.

\* \*\*Classical post-processing:\*\* Python converts the measured outcomes into a game board and calculates neighboring mine counts.



\### Circuit Details



\* \*\*Board size:\*\* 3 × 3

\* \*\*Number of qubits:\*\* 9

\* \*\*Gates:\*\* RY rotation gates

\* \*\*Measurement:\*\* Computational-basis measurement

\* \*\*Simulator:\*\* Qiskit Aer

\* \*\*Other technologies:\*\* Python, Streamlit, NumPy, Matplotlib, and Jupyter Notebook



For a mine probability \\(p\\), the rotation angle is:



$$

\\theta = 2\\arcsin(\\sqrt{p})

$$



An illustrative circuit preparation is:



```python

from math import asin, sqrt

from qiskit import QuantumCircuit



n\_qubits = 9

mine\_probability = 0.25

theta = 2 \* asin(sqrt(mine\_probability))



qc = QuantumCircuit(n\_qubits, n\_qubits)



for qubit in range(n\_qubits):

&#x20;   qc.ry(theta, qubit)



qc.measure(range(n\_qubits), range(n\_qubits))

```



This is a representative example of the circuit approach. Refer to the project's source code and notebook for the runnable implementation.



\### How to Run



From the repository root:



```powershell

cd quantum-minesweeper-qiskit

python -m pip install -r requirements.txt

python -m pip install streamlit

python -m streamlit run src/app.py

```



Open the local URL displayed in the terminal, usually `http://localhost:8501`.



To explore the experiment notebook:



```powershell

python -m pip install jupyter

python -m jupyter notebook notebooks/solution.ipynb

```



Follow the individual project's README if its installation or execution instructions differ from these commands.



\---



\## Repository Structure



```text

quantum/

├── README.md

├── .gitignore

├── quantum-circuit-puzzle/

│   ├── app.py

│   ├── requirements.txt

│   ├── README.md

│   ├── tests/

│   └── screenshots/

└── quantum-minesweeper-qiskit/

&#x20;   ├── README.md

&#x20;   ├── requirements.txt

&#x20;   ├── HACKATHON\_GUIDE.md

&#x20;   ├── LICENSE

&#x20;   ├── view.pdf

&#x20;   ├── src/

&#x20;   ├── notebooks/

&#x20;   └── references/

```



This structure describes the intended combined repository. Some files or folders may change as development continues.



\---



\## Gameplay and Demonstration



\### Quantum Circuit Puzzle Lab



1\. Launch the Streamlit application.

2\. Select a learning level.

3\. Experiment with available quantum gates.

4\. Inspect the circuit and simulated behavior.

5\. Complete the configured challenges.



\### Quantum Minesweeper



1\. Launch the Streamlit application.

2\. Choose the desired mine probability.

3\. Generate a new quantum board.

4\. Prepare and measure the nine-qubit circuit using the simulator.

5\. Map the measured bits to mine and safe tiles.

6\. Reveal tiles and examine neighboring mine-count clues.

7\. Generate another board to obtain a new set of measurement outcomes.

8\. Use the notebook to inspect the circuit and compare simulation statistics with a classical baseline.



\### Screenshots and Video



Add genuine project evidence before final submission:



\* Screenshot of Quantum Circuit Puzzle Lab running.

\* Screenshot of the Minesweeper board before revealing tiles.

\* Screenshot of revealed tiles and neighboring mine counts.

\* Screenshot of the quantum circuit or notebook visualization.

\* Video presentation link and live demo timestamp.



Only include screenshots and experimental results obtained from the actual implementation.



\---



\## Classical vs. Quantum Comparison



For Quantum Minesweeper, the classical baseline assigns each tile a mine independently with probability \\(p\\).



The quantum circuit uses RY rotations chosen so that the probability of measuring `1` is \\(p\\). For independently prepared qubits, the ideal measurement distribution matches the corresponding classical independent Bernoulli model.



The quantum implementation demonstrates circuit-based sampling, but it does not establish a quantum speedup or gameplay advantage over classical random sampling. Its main purpose is educational: making quantum state preparation and measurement easier to explore through a familiar puzzle.



\---



\## Results and Limitations



\### Project Highlights



\* Interactive quantum-learning experiences.

\* Quantum gates and circuit visualization.

\* Nine-qubit board generation in Quantum Minesweeper.

\* Measurement outcomes converted into a playable grid.

\* Classical game logic for neighboring mine counts.

\* An experiment notebook for circuit inspection and statistical comparison.



\### Limitations



\* Quantum Minesweeper uses a small nine-qubit board.

\* The described circuit prepares independent qubits and does not use entanglement to solve the puzzle.

\* Qiskit Aer simulation runs on classical computing hardware.

\* Finite measurement shots introduce statistical variation.

\* The game does not demonstrate quantum advantage.

\* Neighboring mine-count calculations and gameplay rules are classical.

\* Larger boards would require additional qubits and more complex application logic.

\* Real quantum hardware can introduce gate errors, readout errors, and decoherence.



Any numerical performance claims or experimental conclusions should be added only after running the corresponding tests and experiments.



\---



\## Testing



Quantum Circuit Puzzle Lab includes a test suite. From the repository root, run:



```powershell

python -m unittest discover -s quantum-circuit-puzzle/tests -v

```



Review the test output and resolve failures before presenting the project.



For Quantum Minesweeper, follow any test or experiment instructions documented in its own project files.



\---



\## Installation Requirements



\* Python compatible with the dependencies specified by each project.

\* pip.

\* A modern web browser for Streamlit applications.

\* Git for repository management.

\* Jupyter Notebook for notebook-based experiments.



Install dependencies separately using each project's `requirements.txt` file. If using one virtual environment for both games, verify that their dependency versions are compatible.



\---



\## References



\* \[Qiskit Documentation](https://docs.quantum.ibm.com/)

\* \[Qiskit Aer](https://github.com/Qiskit/qiskit-aer)

\* \[Streamlit Documentation](https://docs.streamlit.io/)

\* \[NumPy Documentation](https://numpy.org/doc/)

\* \[Matplotlib Documentation](https://matplotlib.org/stable/)

\* \[Qiskit Fall Fest 2026 — IIIT Kottayam Hackathon Template](https://github.com/Shanwis/Qiskit-Fall-Fest-2026-IIITKottayam-Hackathon-Template)



\## Acknowledgments



This project is intended for educational exploration of quantum computing through interactive games. AI assistance was used during development; the project author is responsible for reviewing, understanding, testing, and presenting the implementation.



Any additional contributors, resources, or collaborators should be acknowledged before final submission.



\## License



Review the license and reuse conditions of both individual projects before redistributing the combined repository. Preserve the applicable copyright and license notices.



\---



\*\*Quantum Games Lab\*\*

\*Explore quantum gates. Experiment with measurement. Learn through play.\*



