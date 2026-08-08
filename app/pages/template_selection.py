"""
===========================================================
Project     : NextHire AI
File        : template_selection.py
Author      : Santosh Kolagani

Purpose:
    Screen 4 – Resume Template: High-resolution template gallery supporting dynamic
    return navigation to preview hub or workspace.
===========================================================
"""

import streamlit as st
from app.components.navbar import render_navbar
from app.config.constants import TEMPLATES, TEMPLATE_CATEGORIES
from app.utils.pdf_generator import generate_resume_pdf
from app.utils.image_generator import generate_template_preview_image
from app.utils.helpers import render_html


def show_template_selection():
    """Renders Screen 4 – High-Resolution Template Selection Gallery for ALL templates."""
    render_navbar()

    return_target = st.session_state.get("return_to_page")
    target_name = "Final Preview Hub" if return_target == "preview" else "Details Workspace"

    render_html(
        f"""
        <div style='text-align: center; margin-bottom: 25px;'>
            <h1 style='color: #1E3A8A; font-size: 2.2rem; font-weight: 700;'>Choose Resume Template</h1>
            <p style='color: #64748B; font-size: 1.05rem;'>Clicking <b>Select Template</b> will automatically return you to the <b>{target_name}</b>.</p>
        </div>
        """
    )

    if "selected_template" not in st.session_state or st.session_state["selected_template"] not in TEMPLATES:
        st.session_state["selected_template"] = "ats_1"

    if "preview_template_id" not in st.session_state:
        st.session_state["preview_template_id"] = None

    curr_selected = st.session_state["selected_template"]
    resume_data = st.session_state.get("resume_data", {})

    # Filter & Search Bar
    c_flt, c_srch = st.columns([2, 1])
    with c_flt:
        selected_category = st.selectbox(
            "Filter Category Section:",
            options=["All Templates"] + [c for c in TEMPLATE_CATEGORIES if c != "All Templates"],
            index=0
        )
    with c_srch:
        search_query = st.text_input("🔍 Search Templates:", placeholder="Search by name...").strip().lower()

    st.divider()

    # ---------------------------------------------------------
    # HIGH-RES PREVIEW DRAWER (When clicked)
    # ---------------------------------------------------------
    if st.session_state.get("preview_template_id"):
        prev_id = st.session_state["preview_template_id"]
        if prev_id not in TEMPLATES:
            prev_id = "ats_1"
        prev_info = TEMPLATES.get(prev_id, list(TEMPLATES.values())[0])

        render_html(
            f"""
            <div style='background-color: #0F172A; border: 2px solid {prev_info.get("color", "#1E3A8A")}; padding: 18px; border-radius: 12px; margin-bottom: 20px; color: white;'>
                <div style='display: flex; justify-content: space-between; align-items: center;'>
                    <h3 style='margin: 0; color: #F8FAFC;'>👁️ HIGH-RES PREVIEW: {prev_info.get('name')}</h3>
                    <span style='background: {prev_info.get("color")}; color: white; padding: 4px 12px; border-radius: 12px; font-weight: bold;'>
                        {prev_info.get('category')}
                    </span>
                </div>
            </div>
            """
        )

        p_col1, p_col2 = st.columns([1, 2])

        with p_col1:
            render_html(
                f"""
                <div style='background-color: #1E293B; border: 1px solid #334155; padding: 18px; border-radius: 10px;'>
                    <p style='margin-bottom: 8px;'><b style='color: #94A3B8;'>Template Name:</b> <span style='color: #FFFFFF; font-weight: bold;'>{prev_info.get('name')}</span></p>
                    <p style='margin-bottom: 8px;'><b style='color: #94A3B8;'>Category:</b> <span style='color: #38BDF8; font-weight: bold;'>{prev_info.get('category')}</span></p>
                    <p style='margin-bottom: 8px;'><b style='color: #94A3B8;'>Layout Style:</b> <span style='color: #E2E8F0;'>{prev_info.get('layout_style', 'default').replace('_', ' ').title()}</span></p>
                    <p style='margin-bottom: 8px;'><b style='color: #94A3B8;'>Font Typography:</b> <span style='color: #E2E8F0;'>{prev_info.get('font')}</span></p>
                    <p style='margin-bottom: 0px;'><b style='color: #94A3B8;'>Theme Color Accent:</b> 
                        <span style='background-color: {prev_info.get("color")}; width: 14px; height: 14px; border-radius: 50%; display: inline-block; vertical-align: middle;'></span>
                        <b style='color: {prev_info.get("color")}; vertical-align: middle;'>{prev_info.get("color")}</b>
                    </p>
                </div>
                """
            )
            st.write("")
            if st.button(f"🚀 Select Template & Return to {target_name}", type="primary", use_container_width=True, key="prev_select_btn"):
                st.session_state["selected_template"] = prev_id
                st.session_state["preview_template_id"] = None
                ret_p = st.session_state.pop("return_to_page", None)
                if ret_p:
                    st.session_state["current_page"] = ret_p
                else:
                    rtype = st.session_state.get("resume_type_choice", "General Resume")
                    if rtype == "Personalized Resume" and not resume_data.get("job_target", {}).get("job_title"):
                        st.session_state["current_page"] = "personalization"
                    else:
                        st.session_state["current_page"] = "data_collection"
                st.rerun()

            st.write("")
            try:
                pdf_bytes = generate_resume_pdf(resume_data, template_id=prev_id)
                st.download_button(
                    label="⬇️ Download Sample PDF",
                    data=pdf_bytes,
                    file_name=f"Resume_{prev_id}.pdf",
                    mime="application/pdf",
                    use_container_width=True,
                    key="prev_dl_btn"
                )
            except Exception as e:
                st.error(f"PDF compilation note: {e}")

            st.write("")
            if st.button("❌ Close Preview", use_container_width=True, key="prev_close_btn"):
                st.session_state["preview_template_id"] = None
                st.rerun()

        with p_col2:
            st.markdown("#### 📄 Ultra HD 4K High-Resolution Document Render")
            try:
                preview_png = generate_template_preview_image(prev_info, resume_data=resume_data)
                st.image(preview_png, caption=f"Ultra HD Document Render — {prev_info.get('name')}", use_container_width=True)
            except Exception as e:
                st.error(f"Error rendering image: {e}")

        st.divider()

    # ---------------------------------------------------------
    # ALL TEMPLATES GRID (Clicking Select automatically returns to previous page)
    # ---------------------------------------------------------
    filtered_templates = {}
    for t_id, t_info in TEMPLATES.items():
        if selected_category != "All Templates" and t_info.get("category") != selected_category:
            continue
        if search_query:
            if search_query not in t_info.get("name", "").lower() and search_query not in t_info.get("description", "").lower():
                continue
        filtered_templates[t_id] = t_info

    st.markdown("### 🎨 Template Gallery")

    template_items = list(filtered_templates.items())
    num_cols = 3

    for i in range(0, len(template_items), num_cols):
        cols = st.columns(num_cols)
        for j in range(num_cols):
            if i + j < len(template_items):
                t_id, t_info = template_items[i + j]
                is_active = (curr_selected == t_id)

                with cols[j]:
                    card_png = generate_template_preview_image(t_info, resume_data=resume_data)
                    border_clr = t_info.get("color", "#2563EB") if is_active else "#CBD5E1"
                    bg_clr = "#F0F9FF" if is_active else "#FFFFFF"

                    render_html(
                        f"""
                        <div style='border: 2px solid {border_clr}; background: {bg_clr}; border-radius: 12px; padding: 14px; margin-bottom: 10px;'>
                            <div style='display: flex; justify-content: space-between; align-items: center; margin-bottom: 6px;'>
                                <span style='background: {t_info.get("color")}; color: white; padding: 2px 8px; border-radius: 8px; font-size: 0.75rem; font-weight: bold;'>
                                    {t_info.get("tag")}
                                </span>
                                <span style='font-size: 0.75rem; color: #475569; font-weight: 600;'>
                                    Font: {t_info.get("font")}
                                </span>
                            </div>
                            <h4 style='margin: 0; color: #0F172A; font-size: 1rem;'>{t_info.get("name")}</h4>
                            <p style='font-size: 0.8rem; color: #64748B; margin: 4px 0 8px 0;'>Category: <b>{t_info.get("category")}</b></p>
                        </div>
                        """
                    )

                    st.image(card_png, use_container_width=True)

                    btn_c1, btn_c2 = st.columns(2)
                    with btn_c1:
                        if st.button("👁️ Preview", key=f"img_prev_{t_id}", use_container_width=True):
                            st.session_state["preview_template_id"] = t_id
                            st.rerun()
                    with btn_c2:
                        if st.button("Select 🚀", key=f"img_select_{t_id}", type="primary", use_container_width=True):
                            st.session_state["selected_template"] = t_id
                            ret_p = st.session_state.pop("return_to_page", None)
                            if ret_p:
                                st.session_state["current_page"] = ret_p
                            else:
                                rtype = st.session_state.get("resume_type_choice", "General Resume")
                                if rtype == "Personalized Resume" and not resume_data.get("job_target", {}).get("job_title"):
                                    st.session_state["current_page"] = "personalization"
                                else:
                                    st.session_state["current_page"] = "data_collection"
                            st.rerun()

                    st.write("")

    st.write("")
    st.divider()

    c_back1, c_back2, c_back3 = st.columns([1, 2, 1])
    with c_back2:
        if st.button("⬅️ Back to Dashboard", use_container_width=True, key="btn_template_back"):
            st.session_state["current_page"] = "home"
            st.rerun()
