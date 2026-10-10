# Quantum Circuit Puzzle Lab

An interactive educational game that helps beginners learn quantum computing by solving circuit puzzles with Qiskit.

## Features

- 10 quantum puzzle levels.
- Learn the X, H (Hadamard), and Z quantum gates.
- View a visual representation of a single-qubit circuit.
- Compare the resulting quantum state with the target state.
- Simulate measurements using Qiskit Aer.
- Explore measurement results through the Streamlit interface.

## Technology Stack

- Python
- Qiskit
- Qiskit Aer
- Streamlit
- NumPy

## How It Works

Players select a puzzle, study its target quantum state, and run the corresponding circuit. The application evaluates the simulated quantum state and displays measurement results.

The current project uses a classical computer to simulate quantum circuits. It does not claim execution on quantum hardware or a quantum speedup.

## Installation on Windows

1. Install Python and Git.
2. Clone this repository:

   ```powershell
   git clone YOUR_GITHUB_REPOSITORY_URL
   cd quantum-circuit-puzzle
   ```

3. Create and activate a virtual environment:

   ```powershell
   python -m venv .venv
   .\.venv\Scripts\Activate.ps1
   ```

4. Install dependencies:

   ```powershell
   python -m pip install -r requirements.txt
   ```

5. Start the application:

   ```powershell
   python -m streamlit run app.py
   ```

6. Open the local URL displayed in the terminal, usually http://localhost:8501.

## Screenshots

Add screenshots of the actual application in the `screenshots/` directory.

### Home Screen

![Quantum Puzzle Lab home screen](screenshots/home.png)

### Quantum Circuit

![Quantum circuit puzzle](screenshots/circuit.png)

### Simulation Results

![Quantum measurement results](screenshots/results.png)

## Testing

Run the test suite using:

```powershell
python -m unittest discover -s tests -v
```

## Project Structure

```text
quantum-circuit-puzzle/
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
├── screenshots/
└── tests/
```

## Future Improvements

- Interactive circuit construction.
- Persistent player progress and scoring.
- More quantum gates and multi-qubit challenges.
- Optional execution on supported quantum hardware.

## Responsible Claims

This project is an educational quantum-circuit simulator. Simulation results are generated on a classical computer using Qiskit Aer.

## Author

Add your name and relevant contact or project links before submission.
