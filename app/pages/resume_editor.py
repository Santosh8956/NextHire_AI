"""
===========================================================
Project     : NextHire AI
File        : resume_editor.py
Author      : Santosh Kolagani

Purpose:
    Interactive Live Resume Editor with AI Section Enhancer & Redirection Focus.
===========================================================
"""

import streamlit as st
from app.components.navbar import render_navbar
from app.services.generator.resume_generator import enhance_bullet_point
from app.config.settings import get_api_key
from app.utils.pdf_generator import generate_resume_pdf
from app.utils.image_generator import generate_template_preview_image
from app.config.constants import TEMPLATES


def show_resume_editor():
    """Renders side-by-side interactive Resume Editor and Live Document Preview."""
    render_navbar()

    st.markdown("## ✍️ Step 3: Interactive Resume Editor & AI Polish")
    st.caption("Edit bullet points live and use AI to enhance action verbs and performance metrics.")

    # Check focus redirection from analysis dashboard
    editor_focus = st.session_state.get("editor_focus")
    if editor_focus:
        st.info(f"🎯 Redirected from ATS Dashboard: Focusing on **{editor_focus.replace('_', ' ').title()}** section!")

    resume = st.session_state.get("resume_data", {})
    if not resume:
        st.warning("No resume data found. Please complete Step 1 first.")
        if st.button("Go to Step 1"):
            st.session_state["current_page"] = "data_collection"
            st.rerun()
        return

    personal = resume.setdefault("personal_info", {})
    experience = resume.setdefault("experience", [])
    projects = resume.setdefault("projects", [])
    job_target = resume.setdefault("job_target", {})
    
    selected_template = st.session_state.get("selected_template", "ats_1")
    if selected_template not in TEMPLATES:
        selected_template = "ats_1"
    template_info = TEMPLATES.get(selected_template, list(TEMPLATES.values())[0])

    col_edit, col_prev = st.columns([1, 1])

    # ---------------------------------------------------------
    # LEFT COLUMN: Interactive AI Editor
    # ---------------------------------------------------------
    with col_edit:
        st.markdown("### ✏️ Content Editor & AI Enhancer")

        # Summary Editor
        exp_summary = (editor_focus == "summary") or not editor_focus
        with st.expander("📝 Professional Summary", expanded=exp_summary):
            personal["summary"] = st.text_area("Summary Statement", value=personal.get("summary", ""), height=100)

        # Experience Bullets
        exp_exp = (editor_focus == "experience") or not editor_focus
        with st.expander("💼 Experience Bullet Points", expanded=exp_exp):
            for exp_idx, exp in enumerate(experience):
                st.markdown(f"**{exp.get('job_title', 'Role')} at {exp.get('company', 'Company')}**")
                bullets = exp.get("bullet_points", [])
                for b_idx, bullet in enumerate(bullets):
                    c_txt, c_btn = st.columns([3, 1])
                    with c_txt:
                        bullets[b_idx] = st.text_input(f"Bullet #{b_idx+1}", value=bullet, key=f"exp_b_{exp_idx}_{b_idx}")
                    with c_btn:
                        st.write("")
                        if st.button("✨ AI Polish", key=f"btn_exp_ai_{exp_idx}_{b_idx}", help="Enhance with action verbs and metrics"):
                            api_key = get_api_key()
                            with st.spinner("Enhancing..."):
                                res = enhance_bullet_point(bullet, context=exp.get("job_title", ""), job_keywords=job_target.get("job_description", ""), api_key=api_key)
                                bullets[b_idx] = res["enhanced_bullet"]
                                st.success("Bullet enhanced!")
                                st.rerun()

        # Project Bullets
        exp_proj = (editor_focus == "projects") or not editor_focus
        with st.expander("🚀 Project Bullet Points", expanded=exp_proj):
            for proj_idx, proj in enumerate(projects):
                st.markdown(f"**{proj.get('title', 'Project')}** [{proj.get('technologies', '')}]")
                bullets = proj.get("bullet_points", [])
                for b_idx, bullet in enumerate(bullets):
                    c_txt, c_btn = st.columns([3, 1])
                    with c_txt:
                        bullets[b_idx] = st.text_input(f"Bullet #{b_idx+1}", value=bullet, key=f"proj_b_{proj_idx}_{b_idx}")
                    with c_btn:
                        st.write("")
                        if st.button("✨ AI Polish", key=f"btn_proj_ai_{proj_idx}_{b_idx}", help="Enhance with action verbs and metrics"):
                            api_key = get_api_key()
                            with st.spinner("Enhancing..."):
                                res = enhance_bullet_point(bullet, context=proj.get("title", ""), job_keywords=job_target.get("job_description", ""), api_key=api_key)
                                bullets[b_idx] = res["enhanced_bullet"]
                                st.success("Bullet enhanced!")
                                st.rerun()

        st.write("")
        if st.button("Proceed to ATS Score Dashboard ➡️", type="primary", use_container_width=True):
            st.session_state["resume_data"] = resume
            st.session_state["current_page"] = "resume_analysis"
            st.rerun()

    # ---------------------------------------------------------
    # RIGHT COLUMN: High-Res Live Document Preview
    # ---------------------------------------------------------
    with col_prev:
        st.markdown(f"### 📄 Live Preview ({template_info.get('name')})")
        try:
            preview_png = generate_template_preview_image(template_info, resume_data=resume)
            st.image(preview_png, use_container_width=True)
        except Exception as e:
            st.error(f"Preview render note: {e}")

        st.write("")
        try:
            pdf_bytes = generate_resume_pdf(resume, template_id=selected_template)
            st.download_button(
                label="⬇️ Download PDF Resume",
                data=pdf_bytes,
                file_name=f"Resume_{personal.get('full_name', 'NextHire')}.pdf",
                mime="application/pdf",
                use_container_width=True
            )
        except Exception as e:
            st.error(f"PDF download note: {e}")
