"""
===========================================================
Project     : NextHire AI
File        : main.py
Author      : Santosh Kolagani

Purpose:
    Entry point of the NextHire AI application.

Responsibilities:
    - Configure Streamlit
    - Initialize Session State
    - Load Global Styles
    - Handle Navigation
    - Launch Application
===========================================================
"""

# =========================================================
# Imports
# =========================================================

import streamlit as st
from pathlib import Path

# Future Page Imports
# from pages.home import show_home
# from pages.data_collection import show_data_collection
# from pages.template_selection import show_template_selection
# from pages.resume_editor import show_resume_editor
# from pages.resume_analysis import show_resume_analysis
# from pages.download import show_download


# =========================================================
# Page Configuration
# =========================================================

st.set_page_config(
    page_title="NextHire AI",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="collapsed"
)


# =========================================================
# Global CSS Loader
# =========================================================

def load_css():
    """
    Loads the global CSS stylesheet.
    """

    css_path = Path(__file__).parent / "styles" / "custom.css"

    if css_path.exists():

        with open(css_path, "r", encoding="utf-8") as css:

            st.markdown(
                f"<style>{css.read()}</style>",
                unsafe_allow_html=True
            )


# =========================================================
# Session State Initialization
# =========================================================

def initialize_session():
    """
    Creates all required Session State variables only once.
    """

    defaults = {

        # Navigation
        "current_page": "home",

        # Resume
        "resume_data": {},

        # Template
        "selected_template": None,

        # Analysis
        "resume_score": 0,
        "previous_score": 0,

        # AI
        "analysis_completed": False,

        # Personalized Resume
        "job_role": "",
        "company_name": "",
        "job_description": "",

        # User Preferences
        "personalized_mode": False,

        # Download
        "generated_resume_path": None
    }

    for key, value in defaults.items():

        if key not in st.session_state:
            st.session_state[key] = value


# =========================================================
# Navigation Controller
# =========================================================

def route():

    page = st.session_state.current_page

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
        st.error("Page not found.")


# =========================================================
# Temporary Home Screen
# =========================================================

def show_home():
    """
    Temporary Home Page.

    Later this function will be moved to:
    pages/home.py
    """

    st.title("🚀 NextHire AI")

    st.subheader("AI Resume Builder")

    st.write(
        """
        Welcome to NextHire AI.

        Build ATS-friendly resumes,
        improve existing resumes,
        analyze resume quality,
        and download professional templates.
        """
    )

    st.success("Project Structure Initialized Successfully ✅")

    if st.button("Start Building Resume"):

        st.session_state.current_page = "data_collection"

        st.rerun()


# =========================================================
# Main Application
# =========================================================

def main():

    load_css()

    initialize_session()

    route()


# =========================================================
# Entry Point
# =========================================================

if __name__ == "__main__":

    main()