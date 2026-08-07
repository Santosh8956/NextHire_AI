"""
===========================================================
Project     : NextHire AI
File        : home.py
Author      : Santosh Kolagani

Purpose:
Landing Page of the NextHire AI Application.

Responsibilities:
- Render Navigation Bar
- Render Hero Section
- Render Statistics Section
- Render Features Section
- Render Resume Templates Section
- Render Call-To-Action Section
- Render Footer
===========================================================
"""

# ==========================================================
# Imports
# ==========================================================

import streamlit as st

from components.navbar import render_navbar
from components.hero import render_hero
from components.stats import render_stats
from components.footer import render_footer


# ==========================================================
# Home Page
# ==========================================================

def show_home():
    """
    Render the Landing Page.
    """

    # ------------------------------------------------------
    # Navigation Bar
    # ------------------------------------------------------

    render_navbar()

    # ------------------------------------------------------
    # Hero Section
    # ------------------------------------------------------

    render_hero()

    # ------------------------------------------------------
    # Statistics Section
    # ------------------------------------------------------

    render_stats()

    # ------------------------------------------------------
    # Features Section
    # ------------------------------------------------------

    st.header("✨ Features")

    st.info(
        "Features Component will be added here."
    )

    st.divider()

    # ------------------------------------------------------
    # Resume Templates Section
    # ------------------------------------------------------

    st.header("📄 Resume Templates")

    st.info(
        "Resume Templates Component will be added here."
    )

    st.divider()

    # ------------------------------------------------------
    # Call To Action Section
    # ------------------------------------------------------

    st.header("🚀 Ready to Build Your Resume?")

    st.write(
        "Start building your ATS-friendly professional resume in just a few minutes."
    )

    st.button(
        "🚀 Start Building Resume",
        type="primary",
        use_container_width=True
    )

    st.divider()

    # ------------------------------------------------------
    # Footer
    # ------------------------------------------------------

    render_footer()


# ==========================================================
# Standalone Execution
# ==========================================================

if __name__ == "__main__":
    show_home()