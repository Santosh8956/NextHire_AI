"""
===========================================================
Project     : NextHire AI
File        : main.py
Author      : Santosh Kolagani

Purpose:
    Entry point of the NextHire AI application supporting sequential
    step-by-step wizard navigation and user authentication portal.
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
from app.pages.auth import show_auth
from app.pages.home import show_home
from app.pages.welcome import show_ai_welcome
from app.pages.resume_type import show_resume_type
from app.pages.template_selection import show_template_selection
from app.pages.personalization import show_personalization
from app.pages.data_collection import show_data_collection
from app.pages.review import show_review
from app.pages.processing import show_ai_processing
from app.pages.preview import show_resume_preview
from app.pages.completion import show_completion

from app.pages.resume_editor import show_resume_editor
from app.pages.resume_analysis import show_resume_analysis
from app.pages.download import show_download
from app.config.constants import SAMPLE_RESUME_DATA


# Page Configuration
st.set_page_config(
    page_title="NextHire AI - Your AI Career Assistant",
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
        "authenticated": False,
        "user_name": "",
        "user_email": "",
        "resume_data": SAMPLE_RESUME_DATA.copy(),
        "selected_template": "ats_1",
        "resume_type_choice": "General Resume",
        "api_key": ""
    }

    for key, value in defaults.items():
        if key not in st.session_state:
            st.session_state[key] = value


# Navigation Controller
def route():
    page = st.session_state.get("current_page", "home")

    if page == "auth":
        show_auth()
    elif page == "home":
        show_home()
    elif page == "welcome":
        show_ai_welcome()
    elif page == "resume_type":
        show_resume_type()
    elif page == "template_selection":
        show_template_selection()
    elif page == "personalization":
        show_personalization()
    elif page == "data_collection":
        show_data_collection()
    elif page == "review":
        show_review()
    elif page == "ai_processing":
        show_ai_processing()
    elif page in ["preview", "resume_preview"]:
        show_resume_preview()
    elif page == "completion":
        show_completion()
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