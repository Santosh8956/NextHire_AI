"""
===========================================================
Project     : NextHire AI
File        : home.py
Author      : Santosh Kolagani

Purpose:
    Landing Page with NextHire Smart Resume Import & Feature Showcase.
===========================================================
"""

import streamlit as st
from app.components.navbar import render_navbar
from app.config.constants import SAMPLE_RESUME_DATA
from app.services.parser.resume_parser import extract_text_from_pdf, parse_resume_content


def show_home():
    """Renders modern Landing Page."""
    render_navbar()

    # Hero Section
    st.markdown(
        """
        <div style='text-align: center; padding: 20px 10px;'>
            <h1 style='font-size: 3rem; color: #1E3A8A;'>Build & Edit ATS-Optimized Resumes with <span style='color: #2563EB;'>NextHire AI</span></h1>
            <p style='font-size: 1.2rem; color: #4B5563; max-width: 850px; margin: 0 auto;'>
                NextHire Smart AI Resume Builder: Upload and edit your existing resume (PDF/TXT), generate tailored summaries, enhance experience bullet points with AI, evaluate ATS scores, and export publication-ready PDFs.
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.write("")

    # NextHire Action Buttons
    col_a, col_b, col_c = st.columns([1, 3, 1])
    with col_b:
        c1, c2, c3 = st.columns(3)
        with c1:
            if st.button("🚀 Build New Resume", type="primary", use_container_width=True):
                st.session_state["current_page"] = "data_collection"
                st.rerun()
        with c2:
            if st.button("📄 Edit Existing Resume", use_container_width=True):
                st.session_state["current_page"] = "data_collection"
                st.rerun()
        with c3:
            if st.button("⚡ Load Sample Data", use_container_width=True):
                st.session_state["resume_data"] = SAMPLE_RESUME_DATA
                st.session_state["current_page"] = "data_collection"
                st.success("Loaded sample profile for Santosh Kolagani!")
                st.rerun()

    # NextHire Smart Feature Box
    st.write("")
    with st.expander("⚡ NextHire Smart Feature: Drag & Drop Existing Resume PDF to Edit", expanded=False):
        uploaded_file = st.file_uploader("Upload PDF/TXT resume to import instantly:", type=["pdf", "txt"], key="home_resume_upload")
        if uploaded_file is not None:
            if st.button("🚀 Parse & Launch Editor", type="primary"):
                with st.spinner("Extracting & parsing resume text..."):
                    file_bytes = uploaded_file.read()
                    if uploaded_file.name.endswith(".pdf"):
                        extracted_text = extract_text_from_pdf(file_bytes)
                    else:
                        extracted_text = file_bytes.decode("utf-8", errors="ignore")

                    if extracted_text:
                        parsed = parse_resume_content(extracted_text)
                        st.session_state["resume_data"] = parsed
                        st.session_state["current_page"] = "data_collection"
                        st.success("Resume imported! Redirecting to editor...")
                        st.rerun()

    st.divider()

    # Key Features Section
    st.markdown("### ✨ Why NextHire AI?")
    
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.markdown(
            """
            <div style='background: #F0F9FF; padding: 20px; border-radius: 12px; border-left: 4px solid #0284C7; height: 100%;'>
                <h4>📄 NextHire Resume Import</h4>
                <p style='font-size: 0.9rem; color: #334155;'>Upload your existing resume to parse, edit, and re-template without starting from scratch.</p>
            </div>
            """,
            unsafe_allow_html=True
        )

    with col2:
        st.markdown(
            """
            <div style='background: #F0FDF4; padding: 20px; border-radius: 12px; border-left: 4px solid #16A34A; height: 100%;'>
                <h4>🎨 Classified Templates</h4>
                <p style='font-size: 0.9rem; color: #334155;'>Classified templates across ATS Friendly, Modern, Tech, Creative, Executive, and Academic.</p>
            </div>
            """,
            unsafe_allow_html=True
        )

    with col3:
        st.markdown(
            """
            <div style='background: #FAF5FF; padding: 20px; border-radius: 12px; border-left: 4px solid #9333EA; height: 100%;'>
                <h4>🤖 AI Content Polish</h4>
                <p style='font-size: 0.9rem; color: #334155;'>Generate professional summaries and enhance bullet points with action verbs and metrics.</p>
            </div>
            """,
            unsafe_allow_html=True
        )

    with col4:
        st.markdown(
            """
            <div style='background: #FFF7ED; padding: 20px; border-radius: 12px; border-left: 4px solid #EA580C; height: 100%;'>
                <h4>📊 ATS Scoring & PDF Export</h4>
                <p style='font-size: 0.9rem; color: #334155;'>Instant keyword check, ATS scoring dashboard, and publication-ready PDF download.</p>
            </div>
            """,
            unsafe_allow_html=True
        )

    st.write("")
    st.divider()

    # Footer banner
    st.markdown(
        """
        <div style='text-align: center; color: #6B7280; font-size: 0.85rem;'>
            NextHire AI — Designed & Developed by <b>Santosh Kolagani</b> (Academic Major Project)
        </div>
        """,
        unsafe_allow_html=True
    )