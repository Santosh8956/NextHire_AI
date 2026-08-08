"""
===========================================================
Project     : NextHire AI
File        : review.py
Author      : Santosh Kolagani

Purpose:
    Screen 7 – Review: Final candidate information review before resume generation
    with high-contrast explicit dark text for 100% legibility.
===========================================================
"""

import streamlit as st
from app.components.navbar import render_navbar
from app.config.constants import TEMPLATES
from app.services.analyzer.resume_analyzer import analyze_resume_strength
from app.config.settings import get_api_key
from app.utils.helpers import render_html


def show_review():
    """Renders Screen 7 – Review."""
    render_navbar()

    render_html(
        """
        <div style='text-align: center; margin-bottom: 25px;'>
            <div style='font-size: 2.5rem; margin-bottom: 8px;'>Everything looks good!</div>
            <h2 style='color: #1E3A8A; font-weight: 700;'>Review your information before generating your resume.</h2>
        </div>
        """
    )

    resume = st.session_state.get("resume_data", {})
    personal = resume.get("personal_info", {})
    education = resume.get("education", [])
    experience = resume.get("experience", [])
    projects = resume.get("projects", [])
    skills = resume.get("skills", [])
    certs = resume.get("certifications", [])
    job_target = resume.get("job_target", {})
    selected_template = st.session_state.get("selected_template", "ats_1")
    t_info = TEMPLATES.get(selected_template, list(TEMPLATES.values())[0])

    api_key = get_api_key()
    analysis = analyze_resume_strength(resume, api_key=api_key)
    resume["analysis"] = analysis
    st.session_state["resume_data"] = resume

    overall_score = analysis.get("overall_score", 85)
    score_color = "#16A34A" if overall_score >= 80 else "#D97706"

    col1, col2 = st.columns(2)

    with col1:
        render_html(
            f"""
            <div style='background: #FFFFFF; border: 2px solid #CBD5E1; border-radius: 12px; padding: 20px; margin-bottom: 15px;'>
                <h4 style='color: #0F172A; margin-top: 0; font-size: 1.15rem;'>👤 Candidate Profile & Contact</h4>
                <p style='color: #334155; margin-bottom: 6px; font-size: 0.95rem;'><b style='color: #0F172A;'>Name:</b> {personal.get('full_name', 'Not set')}</p>
                <p style='color: #334155; margin-bottom: 6px; font-size: 0.95rem;'><b style='color: #0F172A;'>Email:</b> {personal.get('email', 'Not set')}</p>
                <p style='color: #334155; margin-bottom: 6px; font-size: 0.95rem;'><b style='color: #0F172A;'>Phone:</b> {personal.get('phone', 'Not set')}</p>
                <p style='color: #334155; margin-bottom: 0; font-size: 0.95rem;'><b style='color: #0F172A;'>Location:</b> {personal.get('location', 'Not set')}</p>
            </div>
            """
        )

        render_html(
            f"""
            <div style='background: #FFFFFF; border: 2px solid #CBD5E1; border-radius: 12px; padding: 20px; margin-bottom: 15px;'>
                <h4 style='color: #0F172A; margin-top: 0; font-size: 1.15rem;'>🎨 Active Template Selection</h4>
                <p style='color: #334155; margin-bottom: 6px; font-size: 0.95rem;'><b style='color: #0F172A;'>Template:</b> {t_info.get('name')}</p>
                <p style='color: #334155; margin-bottom: 0; font-size: 0.95rem;'><b style='color: #0F172A;'>Category:</b> {t_info.get('category')}</p>
            </div>
            """
        )

        if job_target.get("job_title"):
            render_html(
                f"""
                <div style='background: #F0F9FF; border: 2px solid #BAE6FD; border-radius: 12px; padding: 20px; margin-bottom: 15px;'>
                    <h4 style='color: #0369A1; margin-top: 0; font-size: 1.15rem;'>🎯 Personalization Target</h4>
                    <p style='color: #0369A1; margin-bottom: 6px; font-size: 0.95rem;'><b style='color: #0C4A6E;'>Target Role:</b> {job_target.get('job_title')}</p>
                    <p style='color: #0369A1; margin-bottom: 0; font-size: 0.95rem;'><b style='color: #0C4A6E;'>Target Company:</b> {job_target.get('company_name', 'Not specified')}</p>
                </div>
                """
            )

    with col2:
        render_html(
            f"""
            <div style='background: #0F172A; border: 2px solid {score_color}; border-radius: 12px; padding: 20px; color: white; margin-bottom: 15px;'>
                <h4 style='color: #94A3B8; margin-top: 0; font-size: 1.05rem;'>📊 Estimated ATS Compatibility Score</h4>
                <h1 style='color: {score_color}; margin: 5px 0; font-size: 2.8rem;'>{overall_score} / 100</h1>
                <p style='color: #CBD5E1; font-size: 0.85rem; margin-bottom: 0;'>Verified with NextHire ATS Keyword & Format Engine</p>
            </div>
            """
        )

        render_html(
            f"""
            <div style='background: #FFFFFF; border: 2px solid #CBD5E1; border-radius: 12px; padding: 20px; margin-bottom: 15px;'>
                <h4 style='color: #0F172A; margin-top: 0; font-size: 1.15rem;'>📑 Content Sections Overview</h4>
                <p style='color: #334155; margin-bottom: 6px; font-size: 0.95rem;'>🎓 <b style='color: #0F172A;'>Education Items:</b> {len(education)}</p>
                <p style='color: #334155; margin-bottom: 6px; font-size: 0.95rem;'>💼 <b style='color: #0F172A;'>Experience Roles:</b> {len(experience)}</p>
                <p style='color: #334155; margin-bottom: 6px; font-size: 0.95rem;'>🚀 <b style='color: #0F172A;'>Projects:</b> {len(projects)}</p>
                <p style='color: #334155; margin-bottom: 6px; font-size: 0.95rem;'>📜 <b style='color: #0F172A;'>Certifications:</b> {len(certs)}</p>
                <p style='color: #334155; margin-bottom: 0; font-size: 0.95rem;'>💡 <b style='color: #0F172A;'>Skill Categories:</b> {len(skills)}</p>
            </div>
            """
        )

    st.write("")
    st.divider()

    # Action Buttons: [ Edit ] and [ Generate Resume ]
    col_btn1, col_btn2 = st.columns([1, 1])

    with col_btn1:
        if st.button("✏️ Edit", use_container_width=True, key="btn_review_edit"):
            st.session_state["current_page"] = "data_collection"
            st.rerun()

    with col_btn2:
        if st.button("🚀 Generate Resume", type="primary", use_container_width=True, key="btn_review_generate"):
            st.session_state["current_page"] = "ai_processing"
            st.rerun()
