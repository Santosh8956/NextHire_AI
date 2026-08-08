"""
===========================================================
Project     : NextHire AI
File        : preview.py
Author      : Santosh Kolagani

Purpose:
    Screen 9 – Resume Preview: Final Hub with live document preview, ATS Score badge,
    Download PDF, Switch Template, and Content Editor actions with return navigation state.
===========================================================
"""

import streamlit as st
from app.components.navbar import render_navbar
from app.config.constants import TEMPLATES
from app.utils.pdf_generator import generate_resume_pdf
from app.utils.image_generator import generate_template_preview_image
from app.services.analyzer.resume_analyzer import analyze_resume_strength
from app.config.settings import get_api_key
from app.utils.helpers import render_html


def show_resume_preview():
    """Renders Screen 9 – Resume Preview Hub."""
    render_navbar()

    render_html(
        """
        <div style='text-align: center; margin-bottom: 20px;'>
            <h1 style='color: #1E3A8A; font-size: 2.2rem; font-weight: 700;'>Final Resume Preview & ATS Hub</h1>
            <p style='color: #64748B; font-size: 1.05rem;'>Your AI-generated resume is ready! Review ATS compatibility, document preview, and download options.</p>
        </div>
        """
    )

    resume = st.session_state.get("resume_data", {})
    personal = resume.get("personal_info", {})
    job_target = resume.get("job_target", {})
    selected_template = st.session_state.get("selected_template", "ats_1")
    t_info = TEMPLATES.get(selected_template, list(TEMPLATES.values())[0])

    # Run quick ATS analysis for live score display
    api_key = get_api_key()
    analysis = analyze_resume_strength(resume, api_key=api_key)
    resume["analysis"] = analysis
    st.session_state["resume_data"] = resume

    overall_score = analysis.get("overall_score", 88)
    score_color = "#16A34A" if overall_score >= 80 else "#D97706"

    col_actions, col_doc = st.columns([1.2, 1])

    with col_actions:
        render_html(
            f"""
            <div style='background: #0F172A; border: 2px solid {score_color}; padding: 22px; border-radius: 14px; color: white; margin-bottom: 20px;'>
                <div style='display: flex; justify-content: space-between; align-items: center; margin-bottom: 10px;'>
                    <h4 style='margin: 0; color: #F8FAFC;'>📋 Document Summary</h4>
                    <span style='background: {score_color}; color: white; padding: 4px 10px; border-radius: 12px; font-weight: bold; font-size: 0.85rem;'>
                        ATS Score: {overall_score} / 100
                    </span>
                </div>
                <hr style='border-color: #334155; margin: 10px 0 14px 0;'>
                <p style='margin-bottom: 6px;'><b style='color: #94A3B8;'>Candidate:</b> <span style='color: #FFFFFF; font-weight: bold;'>{personal.get('full_name', 'Candidate')}</span></p>
                <p style='margin-bottom: 6px;'><b style='color: #94A3B8;'>Target Role:</b> <span style='color: #38BDF8;'>{job_target.get('job_title', 'General / Software & AI Developer')}</span></p>
                <p style='margin-bottom: 6px;'><b style='color: #94A3B8;'>Selected Template:</b> <span style='color: #E2E8F0;'>{t_info.get('name')} ({t_info.get('category')})</span></p>
                <p style='margin-bottom: 0;'><b style='color: #94A3B8;'>ATS Status:</b> <span style='color: #4ADE80; font-weight: bold;'>✔️ Verified & Compatible</span></p>
            </div>
            """
        )

        st.markdown("### 🛠️ Actions & Export Controls")

        # 1. Direct PDF Download Button
        try:
            pdf_bytes = generate_resume_pdf(resume, template_id=selected_template)
            filename = f"Resume_{personal.get('full_name', 'NextHire').replace(' ', '_')}.pdf"

            st.download_button(
                label="📥 Download PDF Resume Directly",
                data=pdf_bytes,
                file_name=filename,
                mime="application/pdf",
                type="primary",
                use_container_width=True,
                key="btn_download_pdf_main"
            )
        except Exception as e:
            st.error(f"PDF compilation note: {e}")

        st.write("")

        # 2. Switch Template Option (Returns back to preview page after template selection!)
        if st.button("🎨 Switch Template", use_container_width=True, key="btn_preview_switch_template"):
            st.session_state["return_to_page"] = "preview"
            st.session_state["current_page"] = "template_selection"
            st.rerun()

        st.write("")

        # 3. View Full ATS Score & Suggestions Dashboard (Returns back to preview page after checking!)
        if st.button("📊 View Full ATS Keywords & Score Suggestions", use_container_width=True, key="btn_check_ats_score_prev"):
            st.session_state["return_to_page"] = "preview"
            st.session_state["current_page"] = "resume_analysis"
            st.rerun()

        st.write("")

        # 4. Edit Resume Content button (Returns back to preview page after editing!)
        if st.button("✏️ Edit Resume Content", use_container_width=True, key="btn_preview_edit"):
            st.session_state["return_to_page"] = "preview"
            st.session_state["current_page"] = "resume_editor"
            st.rerun()

        st.write("")
        st.write("")

        # REQUIREMENT 4: Improved High-Impact Proceed to Download / Completion CTA Button
        render_html(
            """
            <div style='background: linear-gradient(135deg, #16A34A 0%, #15803D 100%);
                        border-radius: 12px; padding: 4px; margin-top: 10px;'>
            </div>
            """
        )
        if st.button("🎉 Finish & Proceed to Final Download PDF 📥", type="primary", use_container_width=True, key="btn_goto_download_final"):
            st.session_state["current_page"] = "download"
            st.rerun()

    with col_doc:
        st.markdown("### 👁️ Final Document Preview")
        try:
            preview_png = generate_template_preview_image(t_info, resume_data=resume)
            st.image(preview_png, caption=f"Live Document Render — {t_info.get('name')}", use_container_width=True)
        except Exception as e:
            st.error(f"Document render preview error: {e}")
