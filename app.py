import streamlit as st
import streamlit.components.v1 as components
from pathlib import Path

st.set_page_config(
    page_title="Harshit Ahluwalia — AI Automation Developer",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="collapsed",
)

html_path = Path(__file__).parent / "preview.html"

if html_path.exists():
    html = html_path.read_text(encoding="utf-8")
    components.html(
        html,
        height=5000,
        scrolling=False
    )
else:
    st.error(
        "preview.html was not found. "
        "Make sure it is in the same GitHub repository as app.py."
    )
