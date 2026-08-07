"""
===========================================================
Project     : NextHire AI
File        : template_selection.py
Author      : Santosh Kolagani

Purpose:
    NextHire Classified Resume Template Gallery with High-Contrast
    Template Details & Edge-safe Preview Drawer.
===========================================================
"""

import streamlit as st
from app.components.navbar import render_navbar
from app.config.constants import TEMPLATES
from app.utils.pdf_generator import generate_resume_pdf
from app.utils.image_generator import generate_template_preview_image


# 6 Distinct Category Sections
SECTIONS = [
    {"name": "ATS Friendly", "icon": "🎯", "tagline": "Single-Column ATS Optimized Layouts"},
    {"name": "Modern Professional", "icon": "💼", "tagline": "Clean Corporate & Product Engineering Designs"},
    {"name": "Tech & Developer", "icon": "💻", "tagline": "Code Monospace, Full-Stack & Cloud Architecture Styles"},
    {"name": "Creative & Design", "icon": "🎨", "tagline": "Vibrant Accent Layouts for UI/UX & Creative Directors"},
    {"name": "Executive & Senior", "icon": "👔", "tagline": "Authoritative Serif & Executive Leadership Layouts"},
    {"name": "Academic & Research", "icon": "🎓", "tagline": "Formal Academic CVs for Grants, PhDs & Researchers"}
]


def show_template_selection():
    """Renders NextHire Classified Template Gallery with distinct section blocks."""
    render_navbar()

    st.markdown("## 🎨 Step 2: Choose Resume Template (NextHire Template Gallery)")
    st.caption("Browse templates classified into distinct professional category sections.")

    # Fix legacy template state
    if "selected_template" not in st.session_state or st.session_state["selected_template"] not in TEMPLATES:
        st.session_state["selected_template"] = "ats_1"

    if "preview_template_id" not in st.session_state:
        st.session_state["preview_template_id"] = None

    curr_selected = st.session_state["selected_template"]
    resume_data = st.session_state.get("resume_data", {})

    # Search & Quick Filter Bar
    s_col1, s_col2 = st.columns([2, 1])

    with s_col1:
        selected_category_filter = st.selectbox(
            "Filter Category Section:",
            ["All Classified Sections"] + [sec["name"] for sec in SECTIONS],
            index=0
        )

    with s_col2:
        search_query = st.text_input(
            "🔍 Search Templates:",
            placeholder="Search ATS, Developer, Executive..."
        ).strip().lower()

    st.divider()

    # ---------------------------------------------------------
    # DIRECT PREVIEW DRAWER (High-Contrast Template Details)
    # ---------------------------------------------------------
    if st.session_state.get("preview_template_id"):
        prev_id = st.session_state["preview_template_id"]
        if prev_id not in TEMPLATES:
            prev_id = "ats_1"
        prev_info = TEMPLATES.get(prev_id, list(TEMPLATES.values())[0])

        st.markdown(
            f"""
            <div style='background-color: #0F172A; border: 2px solid {prev_info.get("color", "#1E3A8A")}; padding: 18px; border-radius: 12px; margin-bottom: 20px; color: white;'>
                <div style='display: flex; justify-content: space-between; align-items: center;'>
                    <h3 style='margin: 0; color: #F8FAFC;'>👁️ TEMPLATE PREVIEW: {prev_info.get('name')}</h3>
                    <span style='background: {prev_info.get("color")}; color: white; padding: 4px 12px; border-radius: 12px; font-weight: bold;'>
                        {prev_info.get('tag')}
                    </span>
                </div>
                <p style='color: #94A3B8; margin-top: 6px;'>{prev_info.get('description')}</p>
            </div>
            """,
            unsafe_allow_html=True
        )

        p_col1, p_col2 = st.columns([1, 2])

        with p_col1:
            st.markdown("#### ℹ️ Template Specifications")
            st.markdown(
                f"""
                <div style='background-color: #1E293B; border: 1px solid #334155; padding: 18px; border-radius: 10px;'>
                    <p style='margin-bottom: 8px;'><b style='color: #94A3B8;'>Template Name:</b> <span style='color: #FFFFFF; font-weight: bold;'>{prev_info.get('name')}</span></p>
                    <p style='margin-bottom: 8px;'><b style='color: #94A3B8;'>Category Section:</b> <span style='color: #38BDF8; font-weight: bold;'>{prev_info.get('category')}</span></p>
                    <p style='margin-bottom: 8px;'><b style='color: #94A3B8;'>Layout Format:</b> <span style='color: #E2E8F0;'>{prev_info.get('layout_style', 'default').replace('_', ' ').title()}</span></p>
                    <p style='margin-bottom: 8px;'><b style='color: #94A3B8;'>Font Typography:</b> <span style='color: #E2E8F0;'>{prev_info.get('font')}</span></p>
                    <p style='margin-bottom: 0px;'><b style='color: #94A3B8;'>Theme Color Accent:</b> 
                        <span style='display: inline-flex; align-items: center; gap: 6px;'>
                            <span style='background-color: {prev_info.get("color")}; width: 14px; height: 14px; border-radius: 50%; display: inline-block;'></span>
                            <b style='color: {prev_info.get("color")};'>{prev_info.get("color")}</b>
                        </span>
                    </p>
                </div>
                """,
                unsafe_allow_html=True
            )
            st.write("")
            if st.button("✅ Select This Template", type="primary", use_container_width=True, key="prev_select_btn"):
                st.session_state["selected_template"] = prev_id
                st.session_state["preview_template_id"] = None
                st.success(f"Selected {prev_info.get('name')}!")
                st.rerun()

            st.write("")
            try:
                pdf_bytes = generate_resume_pdf(resume_data, template_id=prev_id)
                st.download_button(
                    label=f"⬇️ Download Sample PDF",
                    data=pdf_bytes,
                    file_name=f"Resume_{prev_id}.pdf",
                    mime="application/pdf",
                    use_container_width=True
                )
            except Exception as e:
                st.error(f"PDF compilation note: {e}")

            st.write("")
            if st.button("❌ Close Preview Drawer", use_container_width=True, key="prev_close_btn"):
                st.session_state["preview_template_id"] = None
                st.rerun()

        with p_col2:
            st.markdown("#### 📄 Formatted Candidate Resume Document Preview")
            try:
                # Render crisp high-res PNG image of candidate's formatted resume
                preview_png = generate_template_preview_image(prev_info, resume_data=resume_data)
                st.image(preview_png, caption=f"Live Document Render — {prev_info.get('name')}", use_container_width=True)
            except Exception as e:
                st.error(f"Error rendering document image: {e}")

        st.divider()

    # ---------------------------------------------------------
    # CLASSIFIED SECTIONS GALLERY
    # ---------------------------------------------------------
    for sec in SECTIONS:
        sec_name = sec["name"]

        if selected_category_filter != "All Classified Sections" and selected_category_filter != sec_name:
            continue

        section_templates = {
            t_id: t_info for t_id, t_info in TEMPLATES.items()
            if t_info.get("category") == sec_name
        }

        if search_query:
            section_templates = {
                t_id: t_info for t_id, t_info in section_templates.items()
                if search_query in t_info.get("name", "").lower()
                or search_query in t_info.get("description", "").lower()
                or search_query in t_info.get("tag", "").lower()
            }

        if not section_templates:
            continue

        # Section Header Block
        st.markdown(
            f"""
            <div style='background: #F1F5F9; border-left: 5px solid #2563EB; padding: 14px 18px; border-radius: 8px; margin-top: 15px; margin-bottom: 20px;'>
                <h3 style='margin: 0; color: #1E293B;'>{sec["icon"]} Section: {sec_name}</h3>
                <span style='color: #64748B; font-size: 0.9rem;'>{sec["tagline"]}</span>
            </div>
            """,
            unsafe_allow_html=True
        )

        # 3-Column Grid per Section
        template_items = list(section_templates.items())
        num_cols = 3

        for i in range(0, len(template_items), num_cols):
            cols = st.columns(num_cols)
            for j in range(num_cols):
                if i + j < len(template_items):
                    t_id, t_info = template_items[i + j]
                    with cols[j]:
                        is_active = (curr_selected == t_id)
                        card_png = generate_template_preview_image(t_info, resume_data=resume_data)

                        with st.container():
                            st.markdown(
                                f"""
                                <div style='display: flex; justify-content: space-between; align-items: center; margin-bottom: 6px;'>
                                    <span style='background: {t_info["color"]}; color: white; padding: 2px 8px; border-radius: 8px; font-size: 0.75rem; font-weight: bold;'>
                                        {t_info["tag"]}
                                    </span>
                                    <span style='font-size: 0.75rem; color: #475569; font-weight: 600;'>
                                        {t_info["font"]}
                                    </span>
                                </div>
                                <h4 style='margin: 0; color: #0F172A; font-size: 1rem;'>{t_info["name"]}</h4>
                                """,
                                unsafe_allow_html=True
                            )

                            # High-Res Image Display
                            st.image(card_png, use_container_width=True)
                            st.caption(f"Category: **{t_info.get('category')}**")

                            btn_c1, btn_c2 = st.columns(2)
                            with btn_c1:
                                if st.button("👁️ Preview", key=f"img_prev_{t_id}", use_container_width=True):
                                    st.session_state["preview_template_id"] = t_id
                                    st.rerun()
                            with btn_c2:
                                if st.button("Selected ✅" if is_active else "Select", key=f"img_select_{t_id}", type="primary" if is_active else "secondary", use_container_width=True):
                                    st.session_state["selected_template"] = t_id
                                    st.rerun()

                            st.write("")

        st.write("")
        st.divider()

    # Footer Navigation Action
    c_left, c_right = st.columns([3, 1])
    with c_right:
        if st.button("Proceed to Live Editor ➡️", type="primary", use_container_width=True):
            st.session_state["current_page"] = "resume_editor"
            st.rerun()
