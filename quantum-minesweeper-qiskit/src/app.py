import math

import streamlit as st
from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator

BOARD_SIZE = 3
CELL_COUNT = BOARD_SIZE * BOARD_SIZE

st.set_page_config(
    page_title="Quantum Minesweeper",
    page_icon="💠",
    layout="centered",
)

st.markdown(
    """
    <style>
    .stApp { background: #0b1020; color: #edf3ff; }
    h1, h2, h3 { color: #67e8f9 !important; }
    div.stButton > button {
        min-height: 64px;
        font-size: 24px;
        border: 1px solid #334155;
        border-radius: 12px;
        background: #17233b;
        color: #e2e8f0;
    }
    div.stButton > button:hover {
        border-color: #67e8f9;
        color: #67e8f9;
    }
    </style>
    """,
    unsafe_allow_html=True,
)


def create_quantum_board(mine_probability):
    """Sample a hidden board using real Qiskit gates and measurements."""
    circuit = QuantumCircuit(CELL_COUNT, CELL_COUNT)

    # RY(theta)|0> gives a probability sin(theta/2)^2 of measuring 1.
    theta = 2 * math.asin(math.sqrt(mine_probability))

    for qubit in range(CELL_COUNT):
        circuit.ry(theta, qubit)
        circuit.measure(qubit, qubit)

    simulator = AerSimulator()
    compiled = transpile(circuit, simulator)
    result = simulator.run(compiled, shots=1).result()
    bitstring = next(iter(result.get_counts()))

    # Qiskit displays classical bitstrings in reverse qubit order.
    board = [int(bitstring[-1 - i]) for i in range(CELL_COUNT)]
    return board, circuit, bitstring


def start_game(probability):
    board, circuit, bitstring = create_quantum_board(probability)
    st.session_state.board = board
    st.session_state.circuit = circuit
    st.session_state.bitstring = bitstring
    st.session_state.revealed = set()
    st.session_state.game_over = False
    st.session_state.won = False
    st.session_state.probability = probability


def count_neighbours(board, index):
    row, col = divmod(index, BOARD_SIZE)
    total = 0

    for r in range(max(0, row - 1), min(BOARD_SIZE, row + 2)):
        for c in range(max(0, col - 1), min(BOARD_SIZE, col + 2)):
            neighbour = r * BOARD_SIZE + c
            if neighbour != index:
                total += board[neighbour]

    return total


if "board" not in st.session_state:
    start_game(0.25)

st.title("💠 Quantum Minesweeper")
st.caption("A tiny puzzle powered by real Qiskit quantum-circuit measurements.")

st.markdown(
    """
    **Mission:** Reveal every safe tile without hitting a mine.

    - 💠 Covered tile — its outcome is hidden.
    - 💣 Mine — the round ends.
    - A number tells you how many neighbouring tiles contain mines.
    """
)

with st.sidebar:
    st.header("Quantum settings")
    probability = st.slider(
        "Probability of a mine per qubit",
        min_value=0.10,
        max_value=0.45,
        value=0.25,
        step=0.05,
    )
    st.caption(
        "Changing this setting takes effect when you start a new round."
    )

    if st.button("🔄 New quantum board", use_container_width=True):
        start_game(probability)
        st.rerun()

board = st.session_state.board
revealed = st.session_state.revealed
game_over = st.session_state.game_over
safe_count = CELL_COUNT - sum(board)
safe_revealed = sum(1 for i in revealed if board[i] == 0)

m1, m2, m3 = st.columns(3)
m1.metric("Safe tiles found", f"{safe_revealed}/{safe_count}")
m2.metric("Tiles revealed", f"{len(revealed)}/{CELL_COUNT}")
m3.metric("Mine probability", f"{st.session_state.probability:.0%}")

st.subheader("Explore the board")

for row in range(BOARD_SIZE):
    columns = st.columns(BOARD_SIZE)

    for col in range(BOARD_SIZE):
        index = row * BOARD_SIZE + col

        if index in revealed or game_over:
            if board[index] == 1:
                label = "💣"
            elif index in revealed:
                label = str(count_neighbours(board, index))
                if label == "0":
                    label = "·"
            else:
                label = "·"
        else:
            label = "⬡"

        if columns[col].button(
            label,
            key=f"tile_{index}",
            use_container_width=True,
            disabled=game_over or index in revealed,
        ):
            revealed.add(index)

            if board[index] == 1:
                st.session_state.game_over = True
                st.session_state.won = False
            elif all(
                i in revealed or board[i] == 1
                for i in range(CELL_COUNT)
            ):
                st.session_state.game_over = True
                st.session_state.won = True

            st.rerun()

if st.session_state.game_over:
    if st.session_state.won:
        st.success("🎉 You won! Every safe tile has been revealed.")
    else:
        st.error("💥 Mine found! Start a new quantum board to try again.")
else:
    st.info("Choose any covered tile to reveal its outcome.")

with st.expander("🔬 Inspect the Qiskit circuit"):
    st.write(
        "Each qubit represents one board cell. An RY rotation sets its "
        "mine probability, and measurement produces the hidden board."
    )
    st.code(st.session_state.circuit.draw(output="text"))
    st.caption(
        "The complete board is sampled at round creation. Tile clicks "
        "reveal stored outcomes; they do not remeasure the same qubits."
    )

with st.expander("🧠 Quantum concepts in this game"):
    st.markdown(
        """
        - **Qubit:** represents one tile.
        - **RY rotation:** prepares a state with a chosen probability of
          measuring 1.
        - **Measurement:** converts the quantum state into a classical
          0 (safe) or 1 (mine).
        - **Classical game logic:** calculates neighbour clues and checks
          whether the player wins.

        This version uses quantum sampling, not a quantum speedup.
        Independent qubits do not provide entanglement, and the same
        probability distribution can be sampled classically.
        """
    )
