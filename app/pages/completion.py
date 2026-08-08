"""
===========================================================
Project     : NextHire AI
File        : completion.py
Author      : Santosh Kolagani

Purpose:
    Screen 10 – Completion: Celebration screen with Download PDF, Check ATS Score button,
    and Build Another Resume action.
===========================================================
"""

import streamlit as st
from app.components.navbar import render_navbar
from app.utils.pdf_generator import generate_resume_pdf
from app.config.constants import SAMPLE_RESUME_DATA
from app.utils.helpers import render_html


def show_completion():
    """Renders Screen 10 – Completion."""
    render_navbar()

    col1, col2, col3 = st.columns([1, 2.2, 1])

    with col2:
        render_html(
            """
            <div style='background: linear-gradient(135deg, #0F172A 0%, #166534 100%);
                        border: 2px solid #22C55E;
                        border-radius: 20px;
                        padding: 40px 30px;
                        text-align: center;
                        box-shadow: 0 20px 40px rgba(0, 0, 0, 0.3);'>
                <div style='font-size: 4rem; margin-bottom: 15px;'>🎉</div>
                <h1 style='color: #F8FAFC; font-size: 2.3rem; font-weight: 700; margin-bottom: 10px;'>
                    Congratulations!
                </h1>
                <h3 style='color: #4ADE80; font-size: 1.4rem; font-weight: 600; margin-bottom: 15px;'>
                    Your resume is ready.
                </h3>
                <p style='color: #E2E8F0; font-size: 1.2rem; margin-bottom: 30px;'>
                    Good luck with your applications! 🚀
                </p>
            </div>
            """
        )

        st.write("")
        st.write("")

        resume = st.session_state.get("resume_data", {})
        personal = resume.get("personal_info", {})
        selected_template = st.session_state.get("selected_template", "ats_1")

        # 1. Download PDF Action
        try:
            pdf_bytes = generate_resume_pdf(resume, template_id=selected_template)
            filename = f"Resume_{personal.get('full_name', 'Candidate').replace(' ', '_')}.pdf"

            st.download_button(
                label="📥 Download PDF Resume",
                data=pdf_bytes,
                file_name=filename,
                mime="application/pdf",
                type="primary",
                use_container_width=True,
                key="btn_completion_download"
            )
        except Exception as e:
            st.error(f"Download note: {e}")

        st.write("")

        # 2. Check ATS Score & Suggestions Action (Requirement)
        if st.button("📊 Check ATS Score & Suggestions to Increase Score", use_container_width=True, key="btn_completion_check_ats"):
            st.session_state["current_page"] = "resume_analysis"
            st.rerun()

        st.write("")

        # 3. Build Another Resume Action
        if st.button("🔄 Build Another Resume", use_container_width=True, key="btn_completion_restart"):
            st.session_state["resume_data"] = SAMPLE_RESUME_DATA.copy()
            st.session_state["selected_template"] = "ats_1"
            st.session_state["home_step"] = 1
            st.session_state["current_page"] = "home"
            st.rerun()
