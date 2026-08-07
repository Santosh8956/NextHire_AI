"""
===========================================================
Project     : NextHire AI
File        : hero.py
Author      : Santosh Kolagani

Purpose:
Reusable Hero Section Component.

Responsibilities:
- Display Hero Heading
- Display Hero Description
- Display CTA Buttons
- Display Hero Information Panel
===========================================================
"""

# ==========================================================
# Imports
# ==========================================================

import streamlit as st

from components.buttons import (
    primary_button,
    secondary_button
)


# ==========================================================
# Hero Section
# ==========================================================

def render_hero():
    """
    Render the Hero Section.
    """

    left, right = st.columns([1.6, 1])

    # ------------------------------------------------------
    # Left Section
    # ------------------------------------------------------

    with left:

        st.markdown("# 🚀 NextHire AI")

        st.markdown(
            "### Build Professional ATS-Friendly Resumes with AI"
        )

        st.write(
            """
Create beautiful ATS-friendly resumes within minutes.

Whether you're a Student, Fresher or Experienced Professional,
NextHire AI helps you build recruiter-ready resumes using Artificial Intelligence.

Simply provide the essential details and let AI generate,
improve and optimize your resume automatically.
            """
        )

        col1, col2 = st.columns(2)

        with col1:

            primary_button(
                "🚀 Create Resume",
                key="hero_create_resume"
            )

        with col2:

            secondary_button(
                "📄 Browse Templates",
                key="hero_browse_templates"
            )

    # ------------------------------------------------------
    # Right Section
    # ------------------------------------------------------

    with right:

        with st.container(border=True):

            st.markdown("### 💡 Why NextHire AI?")

            st.markdown("""
✅ ATS-Friendly Resume

✅ AI Resume Generator

✅ Resume Improvement

✅ Resume Analysis

✅ Multiple Professional Templates

✅ One Click PDF Download
            """)

    st.divider()