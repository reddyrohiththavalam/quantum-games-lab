
import html
import numpy as np
import streamlit as st
from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator

st.set_page_config(
    page_title="Quantum Puzzle Lab",
    page_icon="⚛️",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# --------------------------------------------------
# THEME
# --------------------------------------------------
st.markdown("""
<style>
:root {
    color-scheme: dark;
}
.stApp {
    background:
        radial-gradient(ellipse at 15% 0%, #172554 0%, transparent 38%),
        radial-gradient(ellipse at 95% 20%, #312e81 0%, transparent 30%),
        #080e1d;
    color: #f1f5f9;
}
[data-testid="stHeader"] {
    background: rgba(8, 14, 29, 0.9);
}
.block-container {
    max-width: 1120px;
    padding-top: 1.6rem;
    padding-bottom: 3rem;
}
h1, h2, h3, h4 {
    color: #f8fafc !important;
    letter-spacing: -0.025em;
}
p, li, label, .stMarkdown, [data-testid="stCaptionContainer"] {
    color: #cbd5e1;
}
.hero {
    background: linear-gradient(120deg, #172554, #1e1b4b 65%, #312e81);
    border: 1px solid #4338ca;
    border-radius: 22px;
    padding: 25px 28px;
    margin-bottom: 20px;
    box-shadow: 0 12px 38px rgba(0,0,0,.22);
}
.hero-tag {
    color: #67e8f9;
    font-size: 12px;
    font-weight: 800;
    letter-spacing: 2px;
}
.hero-title {
    color: #ffffff;
    font-size: clamp(28px, 4vw, 42px);
    font-weight: 850;
    margin: 8px 0;
}
.hero-copy {
    color: #dbeafe;
    font-size: 16px;
}
.panel {
    background: #111c30;
    border: 1px solid #293952;
    border-radius: 17px;
    padding: 18px;
    margin: 8px 0 15px 0;
}
.panel-title {
    color: #f8fafc;
    font-size: 17px;
    font-weight: 750;
    margin-bottom: 12px;
}
.target {
    background: #14253b;
    border: 1px solid #2b4865;
    border-radius: 14px;
    padding: 16px;
    text-align: center;
}
.target-label {
    color: #94a3b8;
    font-size: 11px;
    font-weight: 800;
    letter-spacing: 1.5px;
}
.target-state {
    color: #67e8f9;
    font-size: 29px;
    font-weight: 800;
    margin-top: 6px;
}
.circuit-box {
    background: #080f1e;
    border: 1px solid #293952;
    border-radius: 15px;
    padding: 20px 14px;
    overflow-x: auto;
}
.circuit-row {
    display: flex;
    align-items: center;
    min-width: max-content;
    height: 66px;
}
.wire-label {
    color: #94a3b8;
    font-size: 13px;
    width: 42px;
    flex-shrink: 0;
}
.wire {
    display: flex;
    align-items: center;
    min-width: 35px;
    height: 2px;
    background: #3b587a;
}
.gate {
    width: 48px;
    height: 43px;
    display: flex;
    align-items: center;
    justify-content: center;
    margin: 0 5px;
    border-radius: 10px;
    font-size: 17px;
    font-weight: 900;
    flex-shrink: 0;
    box-shadow: 0 0 16px rgba(34,211,238,.08);
}
.gate-x {
    color: #a5f3fc;
    background: #164e63;
    border: 1px solid #22d3ee;
}
.gate-h {
    color: #ddd6fe;
    background: #4c1d95;
    border: 1px solid #a78bfa;
}
.gate-z {
    color: #fbcfe8;
    background: #831843;
    border: 1px solid #f472b6;
}
.measure {
    color: #bbf7d0;
    border: 1px solid #34d399;
    background: #064e3b;
    padding: 9px;
    border-radius: 9px;
    margin-left: 9px;
    font-size: 12px;
    font-weight: 750;
}
.empty-wire {
    color: #64748b;
    font-size: 13px;
    font-style: italic;
    padding: 12px;
}
div.stButton > button {
    min-height: 45px;
    border-radius: 11px;
    background: #17263e;
    border: 1px solid #3c5271;
    color: #f8fafc !important;
    font-weight: 700;
    transition: .15s ease;
}
div.stButton > button p {
    color: #f8fafc !important;
}
div.stButton > button:hover {
    background: #263b5a;
    border-color: #67e8f9;
    color: #ffffff !important;
}
div.stButton > button[kind="primary"] {
    background: linear-gradient(90deg, #0891b2, #4f46e5);
    border: 1px solid #67e8f9;
    color: #ffffff !important;
}
div.stButton > button[kind="primary"] p {
    color: #ffffff !important;
}
div[data-baseweb="select"] > div {
    background: #111c30;
    border-color: #3c5271;
}
div[data-baseweb="select"] * {
    color: #f8fafc;
}
[data-testid="stAlert"] {
    background: #14253b;
    border: 1px solid #3c5271;
    border-radius: 12px;
}
[data-testid="stAlert"] p {
    color: #f1f5f9 !important;
}
[data-testid="stExpander"] {
    background: #111c30;
    border: 1px solid #293952;
    border-radius: 12px;
}
[data-testid="stExpander"] summary,
[data-testid="stExpander"] summary span {
    color: #f1f5f9 !important;
}
[data-testid="stMetricValue"] {
    color: #67e8f9;
}
[data-testid="stProgressBar"] > div {
    background: #24334c;
}
[data-testid="stProgressBar"] > div > div {
    background: linear-gradient(90deg, #22d3ee, #818cf8);
}
hr {
    border-color: #293952;
}
small {
    color: #94a3b8;
}
</style>
""", unsafe_allow_html=True)

# --------------------------------------------------
# QUANTUM STATES
# --------------------------------------------------
ZERO = np.array([1, 0], dtype=complex)
ONE = np.array([0, 1], dtype=complex)
PLUS = np.array([1, 1], dtype=complex) / np.sqrt(2)
MINUS = np.array([1, -1], dtype=complex) / np.sqrt(2)

# --------------------------------------------------
# PUZZLES
# --------------------------------------------------
LEVELS = [
    {
        "name": "Flip the Qubit", "target": ONE, "symbol": "|1⟩",
        "goal": "Change the starting state |0⟩ into |1⟩.",
        "hint": "Add one X gate.",
        "learn": "X flips |0⟩ and |1⟩.",
        "minimum": 1,
    },
    {
        "name": "Create Superposition", "target": PLUS, "symbol": "|+⟩",
        "goal": "Give |0⟩ and |1⟩ equal measurement probabilities.",
        "hint": "Try one H gate.",
        "learn": "H creates an equal superposition from |0⟩.",
        "minimum": 1,
    },
    {
        "name": "Back to Zero", "target": ZERO, "symbol": "|0⟩",
        "goal": "Return to |0⟩ using at least two gates.",
        "hint": "Try X followed by X.",
        "learn": "Two X gates cancel each other.",
        "minimum": 2,
    },
    {
        "name": "Change the Phase", "target": MINUS, "symbol": "|−⟩",
        "goal": "Create the state |−⟩.",
        "hint": "Try H followed by Z.",
        "learn": "Z changes the relative phase in a superposition.",
        "minimum": 2,
    },
    {
        "name": "Flip Then Mix", "target": MINUS, "symbol": "|−⟩",
        "goal": "Reach |−⟩ by flipping first, then mixing.",
        "hint": "Try X followed by H.",
        "learn": "X then H changes |0⟩ into |−⟩.",
        "minimum": 2,
    },
    {
        "name": "Two H Gates", "target": ZERO, "symbol": "|0⟩",
        "goal": "Return to |0⟩ using two H gates.",
        "hint": "Apply H twice.",
        "learn": "H followed by H returns the original state.",
        "minimum": 2,
    },
    {
        "name": "Reach One", "target": ONE, "symbol": "|1⟩",
        "goal": "Reach |1⟩ using three gates.",
        "hint": "Try H, then Z, then H.",
        "learn": "H-Z-H has the same effect as X.",
        "minimum": 3,
    },
    {
        "name": "Superposition Again", "target": PLUS, "symbol": "|+⟩",
        "goal": "Create |+⟩ using three gates.",
        "hint": "Try H, X, then X.",
        "learn": "The two X gates cancel, leaving H's effect.",
        "minimum": 3,
    },
    {
        "name": "Phase Challenge", "target": MINUS, "symbol": "|−⟩",
        "goal": "Reach |−⟩ using three gates.",
        "hint": "Try H, X, then Z.",
        "learn": "X leaves |+⟩ unchanged; Z changes |+⟩ to |−⟩.",
        "minimum": 3,
    },
    {
        "name": "Final Challenge", "target": ZERO, "symbol": "|0⟩",
        "goal": "Return to |0⟩ using four gates.",
        "hint": "Try X, H, Z, then H.",
        "learn": "The sequence X-H-Z-H returns |0⟩.",
        "minimum": 4,
    },
]

GATE_INFO = {
    "X": ("Bit flip", "Switches |0⟩ and |1⟩."),
    "H": ("Hadamard", "Creates or changes superposition."),
    "Z": ("Phase flip", "Changes the phase of a quantum state."),
}


def apply_gate(circuit, gate):
    if gate == "X":
        circuit.x(0)
    elif gate == "H":
        circuit.h(0)
    elif gate == "Z":
        circuit.z(0)


def make_circuit(gates):
    circuit = QuantumCircuit(1)
    for gate in gates:
        apply_gate(circuit, gate)
    return circuit


def draw_visual_circuit(gates):
    """Render the circuit as a readable HTML diagram."""
    parts = [
        '<div class="circuit-box">',
        '<div class="circuit-row">',
        '<div class="wire-label">q₀</div>',
        '<div class="wire" style="width:24px"></div>',
    ]

    for gate in gates:
        css_class = {"X": "gate-x", "H": "gate-h", "Z": "gate-z"}[gate]
        parts.append(
            f'<div class="gate {css_class}">{html.escape(gate)}</div>'
        )
        parts.append('<div class="wire" style="width:28px"></div>')

    parts.extend([
        '<div class="measure">M</div>',
        '</div>',
        '<div style="color:#94a3b8;font-size:12px;margin-top:4px;">'
        'Quantum wire · Gate sequence runs from left to right'
        '</div>',
        '</div>',
    ])

    st.markdown("".join(parts), unsafe_allow_html=True)


def simulate(gates):
    simulator = AerSimulator(method="statevector")

    circuit = make_circuit(gates)
    state_circuit = circuit.copy()
    state_circuit.save_statevector()

    compiled = transpile(state_circuit, simulator)
    state_result = simulator.run(compiled).result()
    state = np.asarray(state_result.get_statevector())

    measured = circuit.copy()
    measured.measure_all()
    compiled_measurement = transpile(measured, simulator)
    result = simulator.run(
        compiled_measurement, shots=500
    ).result()

    return state, result.get_counts(), circuit


# --------------------------------------------------
# SESSION STATE
# --------------------------------------------------
if "completed" not in st.session_state:
    st.session_state.completed = set()

if "gates" not in st.session_state:
    st.session_state.gates = []

if "active_level" not in st.session_state:
    st.session_state.active_level = 0

# --------------------------------------------------
# HEADER
# --------------------------------------------------
st.markdown("""
<div class="hero">
  <div class="hero-tag">QUANTUM LEARNING • INTERACTIVE LAB</div>
  <div class="hero-title">⚛ Quantum Puzzle Lab</div>
  <div class="hero-copy">
    Build quantum circuits, reach target states, and learn one gate at a time.
  </div>
</div>
""", unsafe_allow_html=True)

completed_count = len(st.session_state.completed)

metric1, metric2, metric3 = st.columns(3)
with metric1:
    st.metric("Levels completed", f"{completed_count} / {len(LEVELS)}")
with metric2:
    st.metric("Current level", f"{st.session_state.active_level + 1:02d}")
with metric3:
    st.metric("Gates in circuit", len(st.session_state.gates))

st.progress(completed_count / len(LEVELS))

# --------------------------------------------------
# LEVEL PICKER
# --------------------------------------------------
selected_level = st.selectbox(
    "CHOOSE YOUR CHALLENGE",
    options=list(range(len(LEVELS))),
    format_func=lambda i: (
        f"{'✓ ' if i in st.session_state.completed else ''}"
        f"Level {i + 1:02d} · {LEVELS[i]['name']}"
    ),
    index=st.session_state.active_level,
)

if selected_level != st.session_state.active_level:
    st.session_state.active_level = selected_level
    st.session_state.gates = []

level = LEVELS[selected_level]

st.markdown(
    f'<div class="panel">'
    f'<div class="panel-title">🎯 Mission {selected_level + 1:02d}: '
    f'{html.escape(level["name"])}</div>'
    f'<div style="color:#cbd5e1;font-size:15px;">'
    f'{html.escape(level["goal"])}</div></div>',
    unsafe_allow_html=True,
)

state_col1, state_col2 = st.columns(2)

with state_col1:
    st.markdown(
        '<div class="target"><div class="target-label">START STATE</div>'
        '<div class="target-state">|0⟩</div></div>',
        unsafe_allow_html=True,
    )

with state_col2:
    st.markdown(
        f'<div class="target"><div class="target-label">TARGET STATE</div>'
        f'<div class="target-state">{html.escape(level["symbol"])}</div></div>',
        unsafe_allow_html=True,
    )

# --------------------------------------------------
# GATE SELECTOR
# --------------------------------------------------
st.subheader("1 · Add quantum gates")
st.caption("Choose a gate to add it to your circuit.")

gate_cols = st.columns(3)

for i, gate in enumerate(["X", "H", "Z"]):
    title, description = GATE_INFO[gate]
    with gate_cols[i]:
        if st.button(
            f"＋  {gate} gate",
            key=f"add_{gate}",
            use_container_width=True,
        ):
            if len(st.session_state.gates) < 20:
                st.session_state.gates.append(gate)

        st.caption(f"{title}: {description}")

# --------------------------------------------------
# CIRCUIT DIAGRAM
# --------------------------------------------------
st.subheader("2 · Your quantum circuit")

if st.session_state.gates:
    draw_visual_circuit(st.session_state.gates)
else:
    st.markdown("""
    <div class="circuit-box">
      <div class="empty-wire">
        Your circuit is empty. Add X, H, or Z to begin.
      </div>
    </div>
    """, unsafe_allow_html=True)

undo_col, clear_col = st.columns(2)

with undo_col:
    if st.button("↩ Undo last gate", use_container_width=True):
        if st.session_state.gates:
            st.session_state.gates.pop()

with clear_col:
    if st.button("✕ Clear circuit", use_container_width=True):
        st.session_state.gates = []

with st.expander("💡 Reveal a hint"):
    st.write(level["hint"])

with st.expander("📘 Learn the quantum gates"):
    for gate, (title, description) in GATE_INFO.items():
        st.markdown(f"**{gate} · {title}**")
        st.write(description)

# --------------------------------------------------
# SIMULATION
# --------------------------------------------------
st.divider()
st.subheader("3 · Test your solution")

if st.button(
    "▶  RUN QUANTUM CIRCUIT",
    type="primary",
    use_container_width=True,
):
    if not st.session_state.gates:
        st.warning("Add at least one gate before running your circuit.")
    elif len(st.session_state.gates) < level["minimum"]:
        st.warning(
            f"This challenge requires at least "
            f"{level['minimum']} gates."
        )
    else:
        state, counts, circuit = simulate(st.session_state.gates)

        # Fidelity is insensitive to an overall global phase.
        fidelity = float(
            abs(np.vdot(level["target"], state)) ** 2
        )
        passed = fidelity > 0.999

        st.markdown("#### Circuit used by Qiskit")
        st.code(circuit.draw(output="text"))

        result_col1, result_col2 = st.columns(2)

        with result_col1:
            st.metric("Target match", f"{fidelity * 100:.1f}%")
            st.caption(
                "State comparison, not just a single random measurement."
            )

        with result_col2:
            st.metric("Measurement shots", "500")
            st.caption("Repeated simulator measurements.")

        chart_col1, chart_col2 = st.columns(2)

        with chart_col1:
            st.markdown("**Measurement counts**")
            st.bar_chart(counts)

        with chart_col2:
            st.markdown("**State probabilities**")
            st.bar_chart({
                "|0⟩": float(abs(state[0]) ** 2),
                "|1⟩": float(abs(state[1]) ** 2),
            })

        if passed:
            st.session_state.completed.add(selected_level)
            st.success("🎉 Excellent! You reached the target state.")
            st.markdown("**Quantum concept:**")
            st.write(level["learn"])

            if selected_level < len(LEVELS) - 1:
                if st.button(
                    "Continue to next level →",
                    type="primary",
                    use_container_width=True,
                ):
                    st.session_state.active_level = selected_level + 1
                    st.session_state.gates = []
                    st.rerun()
            else:
                st.balloons()
                st.success("🏆 You completed all 10 quantum puzzles!")

        else:
            st.error("Not quite! Your final state does not match the target.")
            st.write("**Try this:**", level["hint"])

# --------------------------------------------------
# FOOTER
# --------------------------------------------------
st.divider()
st.caption(
    "Built with Python · Qiskit · Qiskit Aer · Streamlit | "
    "Runs on a local quantum simulator, not a physical quantum computer."
)