"""
===========================================================
Project     : NextHire AI
File        : navbar.py
Author      : Santosh Kolagani

Purpose:
    Ultra-clean SaaS navigation with high-contrast glowing developer credit badge
    for Santosh Kumar Kolagani and custom interactive sidebar navigation menu.
===========================================================
"""

import streamlit as st
from app.utils.helpers import render_html


def render_navbar():
    """
    Renders ultra-clean top navigation bar with high-contrast glowing developer credit badge
    and interactive sidebar navigation controller.
    """
    curr_page = st.session_state.get("current_page", "home")
    user_name = st.session_state.get("user_name", "")

    step_labels = {
        "home": "Welcome & Onboarding",
        "dashboard": "Dashboard",
        "welcome": "AI Onboarding",
        "resume_type": "Resume Type",
        "template_selection": "Template Gallery",
        "personalization": "Target Personalization",
        "data_collection": "Resume Workspace",
        "review": "Summary Review",
        "ai_processing": "AI Processing",
        "preview": "Resume Preview",
        "resume_preview": "Resume Preview",
        "completion": "Complete",
        "resume_editor": "Live Content Editor",
        "resume_analysis": "ATS Score Dashboard",
        "download": "Export & Download"
    }

    curr_step_name = step_labels.get(curr_page, "Dashboard")
    display_user = f"👤 {user_name}" if (user_name and user_name.strip()) else "👤 Guest Candidate"

    theme_mode = st.session_state.get("theme_mode", "dark")
    is_dark = (theme_mode == "dark")

    # Dynamic Theme Colors for Header Elements
    dev_bg = "linear-gradient(135deg, #1E293B 0%, #0F172A 100%)" if is_dark else "linear-gradient(135deg, #FFFFFF 0%, #F8FAFC 100%)"
    dev_border = "#3B82F6" if is_dark else "#2563EB"
    dev_shadow = "rgba(59, 130, 246, 0.3)" if is_dark else "rgba(37, 99, 235, 0.2)"
    dev_text_color = "#F8FAFC" if is_dark else "#0F172A"
    dev_name_color = "#60A5FA" if is_dark else "#2563EB"

    sec_bg = "#1E293B" if is_dark else "#FFFFFF"
    sec_border = "#334155" if is_dark else "#CBD5E1"
    sec_label_color = "#94A3B8" if is_dark else "#475569"
    sec_val_color = "#60A5FA" if is_dark else "#2563EB"

    user_bg = "#1E293B" if is_dark else "#FFFFFF"
    user_border = "#334155" if is_dark else "#CBD5E1"
    user_text_color = "#F8FAFC" if is_dark else "#0F172A"

    # ---------------------------------------------------------
    # CUSTOM INTERACTIVE SIDEBAR NAVIGATION MENU
    # ---------------------------------------------------------
    with st.sidebar:
        sb_card_bg = "linear-gradient(135deg, #0F172A 0%, #1E3A8A 100%)" if is_dark else "linear-gradient(135deg, #EFF6FF 0%, #DBEAFE 100%)"
        sb_card_border = "#3B82F6" if is_dark else "#2563EB"
        sb_title_color = "#F8FAFC" if is_dark else "#1E3A8A"
        sb_sub_color = "#93C5FD" if is_dark else "#1D4ED8"

        render_html(
            f"""
            <div style='background: {sb_card_bg};
                        border: 1.5px solid {sb_card_border};
                        border-radius: 16px;
                        padding: 16px;
                        margin-bottom: 20px;
                        text-align: center;
                        box-shadow: 0 10px 25px rgba(0, 0, 0, 0.15);'>
                <div style='font-size: 2.2rem; margin-bottom: 4px;'>🚀</div>
                <h3 style='color: {sb_title_color}; margin: 0; font-size: 1.15rem; font-weight: 800;'>NextHire AI</h3>
                <p style='color: {sb_sub_color}; margin: 2px 0 0 0; font-size: 0.78rem; font-weight: 600;'>AI Career Assistant v2.0</p>
            </div>
            """
        )

        st.markdown("### 🧭 Application Navigation")

        menu_items = [
            ("🏠 Home & Onboarding", "home"),
            ("🎯 Target Personalization", "personalization"),
            ("🎨 Template Gallery", "template_selection"),
            ("📝 Resume Workspace", "data_collection"),
            ("✍️ Live Content Editor", "resume_editor"),
            ("📊 ATS Score Dashboard", "resume_analysis"),
            ("👁️ Resume Final Preview", "preview"),
            ("📥 Export & Download PDF", "download"),
            ("🤖 AI Assistant Chatbot", "ai_chatbot"),
        ]

        for label, page_key in menu_items:
            is_active = (curr_page == page_key) or (curr_page == f"resume_{page_key}")
            if st.button(label, key=f"sb_nav_{page_key}", use_container_width=True, type="primary" if is_active else "secondary"):
                st.session_state["current_page"] = page_key
                st.rerun()

        st.write("")
        sb_theme_btn = "☀️ Light Theme" if is_dark else "🌙 Dark Theme"
        if st.button(sb_theme_btn, key="btn_sb_toggle_theme", use_container_width=True):
            st.session_state["theme_mode"] = "light" if is_dark else "dark"
            st.rerun()

        st.divider()

        sb_dev_bg = "#0F172A" if is_dark else "#F8FAFC"
        sb_dev_border = "#334155" if is_dark else "#E2E8F0"
        sb_dev_sub = "#94A3B8" if is_dark else "#64748B"
        sb_dev_name = "#60A5FA" if is_dark else "#2563EB"

        render_html(
            f"""
            <div style='background: {sb_dev_bg}; border: 1px solid {sb_dev_border}; border-radius: 12px; padding: 12px; text-align: center;'>
                <p style='margin: 0; font-size: 0.75rem; color: {sb_dev_sub};'>Architected & Developed by</p>
                <p style='margin: 2px 0 0 0; font-size: 0.85rem; font-weight: 800; color: {sb_dev_name};'>Santosh Kumar Kolagani</p>
            </div>
            """
        )

    # ---------------------------------------------------------
    # TOP HEADER NAVIGATION BAR
    # ---------------------------------------------------------
    c_logo, c_dev, c_step, c_user, c_bot, c_theme = st.columns([1.1, 2.1, 1.5, 1.2, 1.1, 0.9])

    with c_logo:
        if st.button("🚀 NextHire AI", key="nav_logo_home", use_container_width=True):
            st.session_state["current_page"] = "home"
            st.rerun()

    with c_dev:
        render_html(
            f"""
            <div style='text-align: center; padding-top: 2px;'>
                <div style='background: {dev_bg};
                            border: 2px solid {dev_border};
                            box-shadow: 0 4px 18px {dev_shadow};
                            border-radius: 25px;
                            padding: 5px 14px;
                            display: inline-flex;
                            align-items: center;
                            justify-content: center;
                            gap: 8px;
                            white-space: nowrap;'>
                    <span style='background: linear-gradient(135deg, #2563EB 0%, #1D4ED8 100%); width: 22px; height: 22px; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-size: 0.72rem; color: white; font-weight: bold;'>✨</span>
                    <span style='font-size: 0.8rem; font-weight: 700; color: {dev_text_color}; letter-spacing: 0.2px;'>
                        Developed by <b style='color: {dev_name_color}; text-transform: uppercase; font-weight: 800;'>Santosh Kumar Kolagani</b>
                    </span>
                </div>
            </div>
            """
        )

    with c_step:
        render_html(
            f"""
            <div style='text-align: center; background: {sec_bg}; border: 1px solid {sec_border}; border-radius: 20px; padding: 5px 14px; margin-top: 2px;'>
                <span style='color: {sec_label_color}; font-size: 0.8rem; font-weight: 600;'>Section:</span>
                <span style='color: {sec_val_color}; font-size: 0.85rem; font-weight: 700; margin-left: 4px;'>{curr_step_name}</span>
            </div>
            """
        )

    with c_user:
        render_html(
            f"""
            <div style='text-align: right; padding-top: 4px;'>
                <span style='background: {user_bg}; border: 1px solid {user_border}; color: {user_text_color}; padding: 5px 12px; border-radius: 14px; font-size: 0.82rem; font-weight: 700; display: inline-block; white-space: nowrap;'>
                    {display_user}
                </span>
            </div>
            """
        )

    with c_bot:
        if st.button("🤖 AI Chatbot", key="btn_top_ai_chatbot", type="primary", use_container_width=True):
            st.session_state["current_page"] = "ai_chatbot"
            st.rerun()

    with c_theme:
        top_theme_btn = "☀️ Light" if is_dark else "🌙 Dark"
        if st.button(top_theme_btn, key="btn_top_toggle_theme", use_container_width=True):
            st.session_state["theme_mode"] = "light" if is_dark else "dark"
            st.rerun()

    st.divider()