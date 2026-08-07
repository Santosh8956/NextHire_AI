"""
===========================================================
Project     : NextHire AI
File        : footer.py
Author      : Santosh Kolagani

Purpose:
Reusable footer component for the application.

Responsibilities:
- Copyright Information
- Quick Links
- Contact Information
- Social Links
===========================================================
"""

# ==========================================================
# Imports
# ==========================================================

import streamlit as st


# ==========================================================
# Footer Component
# ==========================================================

def render_footer():
    """
    Render the reusable footer.
    """

    st.divider()

    col1, col2, col3 = st.columns(3)

    # ------------------------------------------------------
    # Brand
    # ------------------------------------------------------

    with col1:

        st.markdown("### 🚀 NextHire AI")

        st.caption(
            "AI-Powered Resume Builder for students and professionals."
        )

    # ------------------------------------------------------
    # Quick Links
    # ------------------------------------------------------

    with col2:

        st.markdown("### Quick Links")

        st.write("🏠 Home")
        st.write("📄 Templates")
        st.write("🤖 Resume Builder")
        st.write("📊 Resume Analysis")

    # ------------------------------------------------------
    # Contact
    # ------------------------------------------------------

    with col3:

        st.markdown("### Contact")

        st.write("📧 support@nexthireai.com")
        st.write("🌐 www.nexthireai.com")
        st.write("📍 India")

    st.divider()

    st.markdown(
        """
        <div style="text-align:center; color:gray; padding:10px;">
            © 2026 <b>NextHire AI</b> • All Rights Reserved
        </div>
        """,
        unsafe_allow_html=True,
    )