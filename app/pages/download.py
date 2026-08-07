"""
===========================================================
Project     : NextHire AI
File        : download.py
Author      : Santosh Kolagani

Purpose:
    Final PDF Export & High-Res Document Preview Page.
===========================================================
"""

import streamlit as st
from app.components.navbar import render_navbar
from app.utils.pdf_generator import generate_resume_pdf
from app.utils.image_generator import generate_template_preview_image
from app.config.constants import TEMPLATES


def show_download():
    """Renders final Export screen with side-by-side Download & Final Document Preview."""
    render_navbar()

    st.markdown("## 📥 Step 5: Final Resume Export & Preview")
    st.caption("Your resume is fully generated, ATS-optimized, and ready for submission! Inspect the final look below before downloading.")

    resume = st.session_state.get("resume_data", {})
    if not resume:
        st.warning("No resume data found.")
        return

    personal = resume.get("personal_info", {})
    selected_template = st.session_state.get("selected_template", "ats_1")
    if selected_template not in TEMPLATES:
        selected_template = "ats_1"
    
    template_info = TEMPLATES.get(selected_template, list(TEMPLATES.values())[0])
    template_name = template_info.get("name", "Classic ATS Single-Column")

    st.success("🎉 Resume Successfully Generated & Verified for ATS Compatibility!")

    col_meta, col_preview = st.columns([1, 1])

    # ---------------------------------------------------------
    # LEFT COLUMN: Metadata & Download PDF Actions
    # ---------------------------------------------------------
    with col_meta:
        st.markdown("### 💾 Download & Document Summary")
        
        # Candidate Summary Card
        overall_score = resume.get('analysis', {}).get('overall_score', 90)
        score_color = "#16A34A" if overall_score >= 80 else "#D97706"

        st.markdown(
            f"""
            <div style='background-color: #0F172A; border: 2px solid {template_info.get("color", "#2563EB")}; padding: 18px; border-radius: 12px; margin-bottom: 20px; color: white;'>
                <h4 style='margin: 0; color: #F8FAFC;'>📋 Final Document Overview</h4>
                <hr style='border-color: #334155; margin: 10px 0;'>
                <p style='margin-bottom: 6px;'><b style='color: #94A3B8;'>Candidate Name:</b> <span style='color: #FFFFFF; font-weight: bold;'>{personal.get('full_name', 'Santosh Kolagani')}</span></p>
                <p style='margin-bottom: 6px;'><b style='color: #94A3B8;'>Target Role:</b> <span style='color: #38BDF8;'>{resume.get('job_target', {}).get('job_title', 'Data Science & AI Developer')}</span></p>
                <p style='margin-bottom: 6px;'><b style='color: #94A3B8;'>Active Template:</b> <span style='color: #E2E8F0;'>{template_name}</span></p>
                <p style='margin-bottom: 6px;'><b style='color: #94A3B8;'>Layout Style:</b> <span style='color: #E2E8F0;'>{template_info.get('layout_style', 'default').replace('_', ' ').title()}</span></p>
                <p style='margin-bottom: 0px;'><b style='color: #94A3B8;'>ATS Quality Score:</b> <span style='color: {score_color}; font-weight: bold;'>{overall_score} / 100</span></p>
            </div>
            """,
            unsafe_allow_html=True
        )

        # PDF Download Button
        st.markdown("#### ⬇️ Export PDF File")
        try:
            pdf_data = generate_resume_pdf(resume, template_id=selected_template)
            filename = f"Resume_{personal.get('full_name', 'Candidate').replace(' ', '_')}.pdf"
            
            st.download_button(
                label="⬇️ Download PDF Resume",
                data=pdf_data,
                file_name=filename,
                mime="application/pdf",
                type="primary",
                use_container_width=True
            )
            st.caption("🔒 100% ATS-compliant publication-ready PDF format.")

        except Exception as e:
            st.error(f"Error generating PDF file: {e}")

        st.write("")
        st.divider()

        # Action Buttons
        st.markdown("#### 🔄 Quick Modifications")
        c1, c2 = st.columns(2)
        with c1:
            if st.button("✍️ Edit Content", use_container_width=True):
                st.session_state["current_page"] = "resume_editor"
                st.rerun()
        with c2:
            if st.button("🎨 Switch Template", use_container_width=True):
                st.session_state["current_page"] = "template_selection"
                st.rerun()

    # ---------------------------------------------------------
    # RIGHT COLUMN: Final High-Res Resume Preview
    # ---------------------------------------------------------
    with col_preview:
        st.markdown("### 👁️ Final Resume Visual Preview")
        st.caption("Check the final look, formatting, and layout before sending to recruiters:")
        
        try:
            # Render Ultra HD 4K image preview
            preview_png = generate_template_preview_image(template_info, resume_data=resume)
            st.image(
                preview_png,
                caption=f"Final Render — {template_name} ({template_info.get('layout_style', 'default').replace('_', ' ').title()})",
                use_container_width=True
            )
        except Exception as e:
            st.error(f"Error displaying final document preview: {e}")
