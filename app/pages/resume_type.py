"""
===========================================================
Project     : NextHire AI
File        : resume_type.py
Author      : Santosh Kolagani

Purpose:
    Screen 3 – Resume Type: Choose between General Resume or Personalized Resume with sequential navigation.
===========================================================
"""

import streamlit as st
from app.components.navbar import render_navbar
from app.utils.helpers import render_html


def show_resume_type():
    """Renders Screen 3 – Resume Type Selection."""
    render_navbar()

    col1, col2, col3 = st.columns([1, 2.2, 1])

    with col2:
        render_html(
            """
            <div style='text-align: center; margin-bottom: 25px;'>
                <h1 style='color: #1E3A8A; font-size: 2.2rem; font-weight: 700;'>What would you like to create?</h1>
                <p style='color: #64748B; font-size: 1.05rem;'>Select the resume option that best matches your target application goals.</p>
            </div>
            """
        )

        curr_choice = st.session_state.get("resume_type_choice", "General Resume")

        choice = st.radio(
            "Select Resume Type:",
            options=["General Resume", "Personalized Resume"],
            index=0 if curr_choice == "General Resume" else 1,
            label_visibility="collapsed",
            key="radio_resume_type"
        )

        st.session_state["resume_type_choice"] = choice

        st.write("")

        if choice == "General Resume":
            st.info("💡 **General Resume**: Create a clean, versatile resume highlighting your overall experience, projects, skills, and background.")
        else:
            st.success("🎯 **Personalized Resume**: Tailor your resume specifically for a target job role, target company, and job description for maximum ATS keyword alignment.")

        st.write("")
        st.write("")

        c_back, c_next = st.columns([1, 1])
        with c_back:
            if st.button("⬅️ Back", use_container_width=True, key="btn_type_back"):
                st.session_state["current_page"] = "welcome"
                st.rerun()
        with c_next:
            if st.button("Continue ➡️", type="primary", use_container_width=True, key="btn_type_continue"):
                st.session_state["current_page"] = "template_selection"
                st.rerun()
