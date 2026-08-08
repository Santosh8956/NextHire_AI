"""
===========================================================
Project     : NextHire AI
File        : template_selection.py
Author      : Santosh Kolagani

Purpose:
    Screen 4 – Resume Template: High-resolution template gallery supporting dynamic
    return navigation to download hub, preview hub, or workspace.
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

    return_target = st.session_state.get("return_to_page", "data_collection")
    target_names = {
        "download": "Export & Download Hub",
        "preview": "Final Preview Hub",
        "resume_preview": "Final Preview Hub",
        "resume_analysis": "ATS Score Dashboard",
        "resume_editor": "Live Content Editor",
        "data_collection": "Details Workspace",
    }
    target_name = target_names.get(return_target, "Details Workspace")

    render_html(
        f"""
        <div style='text-align: center; margin-bottom: 25px;'>
            <h1 style='color: #1E3A8A; font-size: 2.2rem; font-weight: 700;'>Choose Resume Template</h1>
            <p style='color: #64748B; font-size: 1.05rem;'>Clicking <b>Select 🚀</b> will automatically apply your chosen template and return to the <b>{target_name}</b>.</p>
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
            options=["ALL CATEGORIES"] + TEMPLATE_CATEGORIES,
            key="tpl_category_filter"
        )
    with c_srch:
        search_query = st.text_input("Search Templates:", placeholder="e.g. ATS, Executive, Modern...", key="tpl_search_input")

    # Filter logic
    filtered_templates = {}
    for t_id, t_info in TEMPLATES.items():
        cat_match = (selected_category == "ALL CATEGORIES") or (t_info.get("category") == selected_category)
        srch_match = (not search_query.strip()) or (search_query.lower() in t_info.get("name", "").lower()) or (search_query.lower() in t_info.get("tags_str", "").lower())
        if cat_match and srch_match:
            filtered_templates[t_id] = t_info

    if not filtered_templates:
        st.info("No templates found matching your search. Displaying all available templates.")
        filtered_templates = TEMPLATES

    # Direct Fullscreen Preview Modal (If clicked)
    if st.session_state["preview_template_id"] in TEMPLATES:
        p_id = st.session_state["preview_template_id"]
        p_info = TEMPLATES[p_id]

        render_html(
            f"""
            <div style='background-color: #0F172A; border: 2px solid {p_info.get("color", "#2563EB")}; padding: 18px; border-radius: 12px; margin-bottom: 20px; color: white;'>
                <div style='display: flex; justify-content: space-between; align-items: center;'>
                    <h3 style='margin: 0; color: #F8FAFC;'>👁️ FULL-SCREEN RESUME PREVIEW: {p_info.get("name")}</h3>
                    <span style='background: {p_info.get("color")}; color: white; padding: 4px 12px; border-radius: 12px; font-weight: bold;'>
                        {p_info.get("category")} Layout
                    </span>
                </div>
            </div>
            """
        )

        try:
            preview_png = generate_template_preview_image(p_info, resume_data=resume_data)
            st.image(
                preview_png,
                caption=f"Ultra HD 4K Preview — {p_info.get('name')} ({p_info.get('layout_style', 'default').replace('_', ' ').title()})",
                use_container_width=True
            )
        except Exception as e:
            st.error(f"Error generating template preview: {e}")

        c_close, c_use = st.columns([1, 1])
        with c_close:
            if st.button("❌ Close Preview", key="btn_close_preview", use_container_width=True):
                st.session_state["preview_template_id"] = None
                st.rerun()
        with c_use:
            if st.button(f"Use This Template ({p_info.get('name')}) 🚀", key="btn_use_modal_template", type="primary", use_container_width=True):
                st.session_state["selected_template"] = p_id
                st.session_state["preview_template_id"] = None
                ret_p = st.session_state.get("return_to_page")
                if ret_p:
                    st.session_state["current_page"] = ret_p
                else:
                    rtype = st.session_state.get("resume_type_choice", "General Resume")
                    if rtype == "Personalized Resume" and not resume_data.get("job_target", {}).get("job_title"):
                        st.session_state["current_page"] = "personalization"
                    else:
                        st.session_state["current_page"] = "data_collection"
                st.rerun()

        st.markdown("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")

    st.markdown(f"### Showing {len(filtered_templates)} Classified Templates")

    # Grid Display of High-Resolution Template Cards
    t_items = list(filtered_templates.items())
    cols_per_row = 3

    for i in range(0, len(t_items), cols_per_row):
        row_items = t_items[i:i+cols_per_row]
        cols = st.columns(cols_per_row)

        for col_idx, (t_id, t_info) in enumerate(row_items):
            with cols[col_idx]:
                is_selected = (t_id == curr_selected)
                border_color = "#16A34A" if is_selected else "#CBD5E1"
                card_bg = "#F0FDF4" if is_selected else "#FFFFFF"

                try:
                    card_png = generate_template_preview_image(t_info, resume_data=resume_data)

                    render_html(
                        f"""
                        <div style='background: {card_bg}; border: 2px solid {border_color}; border-radius: 12px; padding: 14px; margin-bottom: 10px; box-shadow: 0 4px 10px rgba(0,0,0,0.05);'>
                            {'<div style="background: #16A34A; color: white; padding: 4px 10px; border-radius: 8px; font-weight: bold; font-size: 0.8rem; text-align: center; margin-bottom: 8px;">✓ ACTIVE SELECTED TEMPLATE</div>' if is_selected else ''}
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
                            ret_p = st.session_state.get("return_to_page")
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

                except Exception as e:
                    st.error(f"Error rendering card preview: {e}")

    st.write("")
    st.divider()

    c_back1, c_back2, c_back3 = st.columns([1, 2, 1])
    with c_back2:
        if st.button(f"⬅️ Return to {target_name}", use_container_width=True, key="btn_tpl_back_bottom"):
            ret_p = st.session_state.get("return_to_page")
            if ret_p:
                st.session_state["current_page"] = ret_p
            else:
                st.session_state["current_page"] = "data_collection"
            st.rerun()
