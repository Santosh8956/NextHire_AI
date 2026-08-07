"""
===========================================================
Project     : NextHire AI
File        : stats.py
Author      : Santosh Kolagani

Purpose:
Reusable Statistics Section Component.

Responsibilities:
- Display Platform Statistics
- Display Trust Metrics
===========================================================
"""

# ==========================================================
# Imports
# ==========================================================

import streamlit as st


# ==========================================================
# Statistics Section
# ==========================================================

def render_stats():
    """
    Render platform statistics.
    """

    st.markdown("## 📊 Trusted by Job Seekers")

    st.write(
        "Everything you need to build a professional resume with confidence."
    )

    col1, col2, col3, col4 = st.columns(4)

    with col1:

        st.metric(
            label="👥 Users",
            value="10,000+"
        )

    with col2:

        st.metric(
            label="🎯 ATS Success",
            value="98%"
        )

    with col3:

        st.metric(
            label="📄 Templates",
            value="12+"
        )

    with col4:

        st.metric(
            label="⚡ Average Time",
            value="5 Min"
        )

    st.divider()