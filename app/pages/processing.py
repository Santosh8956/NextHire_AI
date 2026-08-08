"""
===========================================================
Project     : NextHire AI
File        : processing.py
Author      : Santosh Kolagani

Purpose:
    Screen 8 – AI Processing: Reassuring visual progress screen with safe HTML rendering.
===========================================================
"""

import streamlit as st
from app.components.navbar import render_navbar
from app.utils.pdf_generator import generate_resume_pdf
from app.utils.helpers import render_html


def show_ai_processing():
    """Renders Screen 8 – AI Processing visual loading screen."""
    render_navbar()

    col1, col2, col3 = st.columns([1, 2, 1])

    with col2:
        render_html(
            """
            <div style='background: linear-gradient(135deg, #0F172A 0%, #1E293B 100%);
                        border: 2px solid #3B82F6;
                        border-radius: 20px;
                        padding: 35px 30px;
                        text-align: center;
                        box-shadow: 0 20px 40px rgba(0,0,0,0.3);'>
                <div style='font-size: 3rem; margin-bottom: 10px;'>🤖</div>
                <h2 style='color: #F8FAFC; margin-bottom: 20px; font-weight: 700;'>AI is working...</h2>
                
                <div style='text-align: left; background: #1E293B; border-radius: 12px; padding: 20px; border: 1px solid #334155; margin-bottom: 25px;'>
                    <p style='color: #4ADE80; font-size: 1.1rem; margin-bottom: 12px; font-weight: 600;'>✔ Generating Professional Summary</p>
                    <p style='color: #4ADE80; font-size: 1.1rem; margin-bottom: 12px; font-weight: 600;'>✔ Optimizing ATS Keywords</p>
                    <p style='color: #4ADE80; font-size: 1.1rem; margin-bottom: 12px; font-weight: 600;'>✔ Improving Project Descriptions</p>
                    <p style='color: #4ADE80; font-size: 1.1rem; margin-bottom: 0; font-weight: 600;'>✔ Creating Resume Layout</p>
                </div>

                <div style='color: #60A5FA; font-size: 1.2rem; font-weight: 600;'>
                    ⚡ Almost Done...
                </div>
            </div>
            """
        )

        st.write("")
        st.write("")

        resume = st.session_state.get("resume_data", {})
        selected_template = st.session_state.get("selected_template", "ats_1")

        try:
            pdf_bytes = generate_resume_pdf(resume, template_id=selected_template)
            st.session_state["compiled_pdf"] = pdf_bytes
        except Exception:
            pass

        if st.button("View Resume Preview ➡️", type="primary", use_container_width=True, key="btn_processing_view"):
            st.session_state["current_page"] = "resume_preview"
            st.rerun()
