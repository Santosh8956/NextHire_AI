"""
===========================================================
Project     : NextHire AI
File        : navbar.py
Author      : Santosh Kumar Kolagani

Purpose:
Reusable Streamlit Navigation Bar
===========================================================
"""

import streamlit as st


def render_navbar():
    """
    Render the reusable navigation bar.
    """

    col1, col2, col3 = st.columns([2, 6, 2])

    with col1:
        st.markdown("## 🚀 NextHire AI")

    with col2:

        menu = st.radio(
            "",
            [
                "Home",
                "Templates",
                "Resume Builder",
                "Analysis",
                "Download"
            ],
            horizontal=True,
            label_visibility="collapsed"
        )

    with col3:

        login, start = st.columns(2)

        with login:
            st.button(
                "Login",
                use_container_width=True
            )

        with start:
            st.button(
                "Get Started",
                type="primary",
                use_container_width=True
            )

    st.divider()

    return menu