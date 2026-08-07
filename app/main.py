"""
===========================================================
Project     : NextHire AI
File        : main.py
Author      : Santosh Kolagani

Purpose:
    Entry point of the NextHire AI application.
===========================================================
"""

import sys
from pathlib import Path

# Automatically add project root directory to sys.path
ROOT_DIR = Path(__file__).resolve().parent.parent
if str(ROOT_DIR) not in sys.path:
    sys.path.insert(0, str(ROOT_DIR))

import streamlit as st

# Page Imports
from app.pages.home import show_home
from app.pages.data_collection import show_data_collection
from app.pages.template_selection import show_template_selection
from app.pages.resume_editor import show_resume_editor
from app.pages.resume_analysis import show_resume_analysis
from app.pages.download import show_download
from app.config.constants import SAMPLE_RESUME_DATA


# Page Configuration
st.set_page_config(
    page_title="NextHire AI - Resume Builder & Analyzer",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="collapsed"
)


# Global CSS Loader
def load_css():
    """Loads custom CSS stylesheet if present."""
    css_path = Path(__file__).parent / "styles" / "custom.css"
    if css_path.exists():
        with open(css_path, "r", encoding="utf-8") as css:
            st.markdown(f"<style>{css.read()}</style>", unsafe_allow_html=True)


# Session State Initialization
def initialize_session():
    """Initializes session state defaults."""
    defaults = {
        "current_page": "home",
        "resume_data": SAMPLE_RESUME_DATA.copy(),
        "selected_template": "ats_classic",
        "api_key": ""
    }

    for key, value in defaults.items():
        if key not in st.session_state:
            st.session_state[key] = value


# Navigation Controller
def route():
    page = st.session_state.get("current_page", "home")

    if page == "home":
        show_home()
    elif page == "data_collection":
        show_data_collection()
    elif page == "template_selection":
        show_template_selection()
    elif page == "resume_editor":
        show_resume_editor()
    elif page == "resume_analysis":
        show_resume_analysis()
    elif page == "download":
        show_download()
    else:
        show_home()


def main():
    load_css()
    initialize_session()
    route()


if __name__ == "__main__":
    main()