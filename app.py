"""MIRAGE - Algae Exchange Network: Streamlit host for the interactive simulation.

The whole simulation (model, AI controller, charts, hardware link) lives in
mirage.html and runs in the visitor's browser. This app only serves it.
"""
from pathlib import Path

import streamlit as st
import streamlit.components.v1 as components

HERE = Path(__file__).parent
HTML_FILE = HERE / "mirage.html"

st.set_page_config(
    page_title="MIRAGE · Algae Exchange Network",
    page_icon="🌿",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# Let the simulation use the full window: remove Streamlit's padding, header and footer.
st.markdown(
    """
    <style>
      .block-container {padding: 0 !important; max-width: 100% !important;}
      header[data-testid="stHeader"] {background: transparent; height: 0;}
      footer, #MainMenu, [data-testid="stToolbar"], [data-testid="stDecoration"] {visibility: hidden;}
      .stApp {background: #06051a;}
      iframe {border: 0; display: block;}
    </style>
    """,
    unsafe_allow_html=True,
)

html = HTML_FILE.read_text(encoding="utf-8")

with st.sidebar:
    st.markdown("### 🌿 MIRAGE")
    st.caption("Algae Exchange Network · Cities That Help Each Other")
    st.markdown(
        "All values on the page are **simulated** by the model it describes. "
        "Nothing is a lab or field measurement."
    )
    st.markdown("**Using the real Arduino pumps?**")
    st.markdown(
        "Browsers block USB access inside embedded pages, so on this website the "
        "pumps stay in Demo mode. Download the file below and open it directly in "
        "Chrome or Edge to connect the Arduino."
    )
    st.download_button(
        "⬇ Download MIRAGE_Simulation.html",
        data=html,
        file_name="MIRAGE_Simulation.html",
        mime="text/html",
        use_container_width=True,
    )
    height = st.slider("Simulation window height (px)", 600, 1600, 950, 50)

components.html(html, height=height, scrolling=True)
