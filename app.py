
import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Recursive Salience Synthesizer", layout="wide")
st.title("🧠 Recursive Salience Synthesizer")

st.markdown("""
Explore how symbolic salience intensifies through recursive feedback loops.
This tool simulates attention-amplified identity attractors in recursive cognitive systems.
""")

# Sidebar Inputs
st.sidebar.header("Simulation Parameters")
attention_curve = st.sidebar.slider("Attention Focus Strength A(t)", 0.1, 5.0, 2.0)
recursion_depth = st.sidebar.slider("Recursive Loop Intensity R(t)", 1, 20, 10)
symbolic_temperature = st.sidebar.slider("Symbolic Temperature Θ", 0.0, 2.0, 1.0)

# Simulation Logic
time = np.arange(0, 100, 1)
salience = attention_curve * np.exp(-symbolic_temperature * time / 100) * np.sin(recursion_depth * time / 100 * np.pi)
salience += np.random.normal(0, 0.05, size=time.shape)  # symbolic noise

df = pd.DataFrame({'Time': time, 'Salience': salience})

# Plotting
fig = px.line(df, x='Time', y='Salience', title="Symbolic Salience Over Recursive Focus Cycles",
              labels={'Salience': 'Salience Intensity'})
st.plotly_chart(fig, use_container_width=True)

# Interpretation
st.markdown("""
### Interpretation
- **A(t)** increases attention intensity — sharper, stronger salience peaks.
- **R(t)** controls recursive loop speed — higher values trigger faster oscillations.
- **Θ** increases symbolic noise and instability — flattening or diffusing signal.

Use this to visualize:
- Symbolic obsession
- Viral memetic amplification
- Recursive identity feedback
""")
