"""
===========================================================
Project     : NextHire AI
File        : resume_editor.py
Author      : Santosh Kolagani

Purpose:
    Interactive Live Resume Editor with full-view bullet text areas, AI Section Enhancer,
    and return navigation to preview hub or workspace.
===========================================================
"""

import streamlit as st
from app.components.navbar import render_navbar
from app.services.generator.resume_generator import enhance_bullet_point
from app.config.settings import get_api_key
from app.utils.pdf_generator import generate_resume_pdf
from app.utils.image_generator import generate_template_preview_image
from app.config.constants import TEMPLATES
from app.utils.helpers import render_html


def show_resume_editor():
    """Renders side-by-side interactive Resume Editor and Live Document Preview."""
    render_navbar()

    render_html(
        """
        <div style='text-align: center; margin-bottom: 20px;'>
            <h1 style='color: #1E3A8A; font-size: 2.2rem; font-weight: 700;'>Interactive Content Editor & AI Polish</h1>
            <p style='color: #64748B; font-size: 1.05rem;'>Edit bullet points in full view and use AI to enhance action verbs and performance metrics.</p>
        </div>
        """
    )

    editor_focus = st.session_state.get("editor_focus")
    if editor_focus:
        st.info(f"🎯 Redirected from ATS Dashboard: Focusing on **{editor_focus.replace('_', ' ').title()}** section!")

    resume = st.session_state.get("resume_data", {})
    if not resume:
        st.warning("No resume data found. Please fill out details in the workspace first.")
        if st.button("Go to Workspace"):
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

    col_edit, col_prev = st.columns([1.2, 1])

    # ---------------------------------------------------------
    # LEFT COLUMN: Interactive AI Content Editor (Full-View Bullets)
    # ---------------------------------------------------------
    with col_edit:
        st.markdown("### ✏️ Full-View Content Editor & AI Polish")

        # 1. Summary Editor
        exp_summary = (editor_focus == "summary") or not editor_focus
        with st.expander("📝 Professional Summary", expanded=exp_summary):
            personal["summary"] = st.text_area(
                "Professional Summary Statement",
                value=personal.get("summary", ""),
                height=110,
                key="editor_summary_textarea"
            )

        # 2. Experience Bullets (Full View)
        exp_exp = (editor_focus == "experience") or not editor_focus
        with st.expander("💼 Experience Bullet Points (Full View)", expanded=exp_exp):
            if not experience:
                st.caption("No experience entries found. Add entries in the workspace.")
            for exp_idx, exp in enumerate(experience):
                st.markdown(f"#### Role #{exp_idx+1}: {exp.get('job_title', 'Role')} at {exp.get('company', 'Company')}")
                bullets = exp.get("bullet_points", [])
                for b_idx, bullet in enumerate(bullets):
                    bullets[b_idx] = st.text_area(
                        f"Bullet #{b_idx+1} (Full View)",
                        value=bullet,
                        height=80,
                        key=f"exp_b_full_{exp_idx}_{b_idx}"
                    )
                    c_txt, c_btn = st.columns([2, 1])
                    with c_btn:
                        if st.button("✨ AI Polish Bullet", key=f"btn_exp_ai_{exp_idx}_{b_idx}", type="primary", use_container_width=True):
                            api_key = get_api_key()
                            with st.spinner("AI Enhancing bullet point with action verbs & metrics..."):
                                res = enhance_bullet_point(
                                    bullets[b_idx],
                                    context=exp.get("job_title", ""),
                                    job_keywords=job_target.get("job_description", ""),
                                    api_key=api_key
                                )
                                bullets[b_idx] = res["enhanced_bullet"]
                                st.success("🎉 Bullet point enhanced with metrics!")
                                st.rerun()
                    st.write("")

        # 3. Project Bullets (Full View)
        exp_proj = (editor_focus == "projects") or not editor_focus
        with st.expander("🚀 Project Bullet Points (Full View)", expanded=exp_proj):
            if not projects:
                st.caption("No project entries found. Add entries in the workspace.")
            for proj_idx, proj in enumerate(projects):
                st.markdown(f"#### Project #{proj_idx+1}: {proj.get('title', 'Project')} [{proj.get('technologies', '')}]")
                bullets = proj.get("bullet_points", [])
                for b_idx, bullet in enumerate(bullets):
                    bullets[b_idx] = st.text_area(
                        f"Project Bullet #{b_idx+1} (Full View)",
                        value=bullet,
                        height=80,
                        key=f"proj_b_full_{proj_idx}_{b_idx}"
                    )
                    c_txt, c_btn = st.columns([2, 1])
                    with c_btn:
                        if st.button("✨ AI Polish Bullet", key=f"btn_proj_ai_{proj_idx}_{b_idx}", type="primary", use_container_width=True):
                            api_key = get_api_key()
                            with st.spinner("AI Enhancing project bullet point..."):
                                res = enhance_bullet_point(
                                    bullets[b_idx],
                                    context=proj.get("title", ""),
                                    job_keywords=job_target.get("job_description", ""),
                                    api_key=api_key
                                )
                                bullets[b_idx] = res["enhanced_bullet"]
                                st.success("🎉 Project bullet enhanced!")
                                st.rerun()
                    st.write("")

        st.write("")
        c_nav_b, c_nav_n = st.columns([1, 1])
        with c_nav_b:
            if st.button("⬅️ Back to Details Workspace", use_container_width=True):
                st.session_state["current_page"] = "data_collection"
                st.rerun()
        with c_nav_n:
            if st.button("Save & Return to Final Preview Hub 🚀 ➡️", type="primary", use_container_width=True):
                st.session_state["resume_data"] = resume
                ret_p = st.session_state.pop("return_to_page", None)
                if not ret_p:
                    ret_p = "preview"
                st.session_state["current_page"] = ret_p
                st.rerun()

    # ---------------------------------------------------------
    # RIGHT COLUMN: Side-by-Side Ultra HD Live Document Preview
    # ---------------------------------------------------------
    with col_prev:
        render_html(
            f"""
            <div style='background: #0F172A; border: 2px solid {template_info.get("color", "#2563EB")}; padding: 14px 18px; border-radius: 10px; color: white; margin-bottom: 12px;'>
                <div style='display: flex; justify-content: space-between; align-items: center;'>
                    <h4 style='margin: 0; color: #F8FAFC;'>📄 Live Preview: {template_info.get('name')}</h4>
                    <span style='background: {template_info.get("color")}; color: white; padding: 2px 8px; border-radius: 6px; font-size: 0.75rem; font-weight: bold;'>
                        {template_info.get('category')}
                    </span>
                </div>
            </div>
            """
        )
        try:
            preview_png = generate_template_preview_image(template_info, resume_data=resume)
            st.image(preview_png, use_container_width=True, caption=f"Live Ultra HD Document Render — {template_info.get('name')}")
        except Exception as e:
            st.error(f"Preview render note: {e}")

        st.write("")
        c_dl, c_sw = st.columns([1, 1])
        with c_dl:
            try:
                pdf_bytes = generate_resume_pdf(resume, template_id=selected_template)
                st.download_button(
                    label="⬇️ Download PDF",
                    data=pdf_bytes,
                    file_name=f"Resume_{personal.get('full_name', 'NextHire')}.pdf",
                    mime="application/pdf",
                    use_container_width=True
                )
            except Exception as e:
                st.error(f"PDF download note: {e}")
        with c_sw:
            if st.button("🎨 Switch Template", use_container_width=True, key="btn_editor_switch_tmpl"):
                st.session_state["return_to_page"] = "resume_editor"
                st.session_state["current_page"] = "template_selection"
                st.rerun()
