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

    # ---------------------------------------------------------
    # CUSTOM INTERACTIVE SIDEBAR NAVIGATION MENU
    # ---------------------------------------------------------
    with st.sidebar:
        render_html(
            """
            <div style='background: linear-gradient(135deg, #0F172A 0%, #1E3A8A 100%);
                        border: 1.5px solid #3B82F6;
                        border-radius: 16px;
                        padding: 16px;
                        margin-bottom: 20px;
                        text-align: center;
                        box-shadow: 0 10px 25px rgba(0, 0, 0, 0.3);'>
                <div style='font-size: 2.2rem; margin-bottom: 4px;'>🚀</div>
                <h3 style='color: #F8FAFC; margin: 0; font-size: 1.15rem; font-weight: 800;'>NextHire AI</h3>
                <p style='color: #93C5FD; margin: 2px 0 0 0; font-size: 0.78rem; font-weight: 600;'>AI Career Assistant v2.0</p>
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
        ]

        for label, page_key in menu_items:
            is_active = (curr_page == page_key) or (curr_page == f"resume_{page_key}")
            if st.button(label, key=f"sb_nav_{page_key}", use_container_width=True, type="primary" if is_active else "secondary"):
                st.session_state["current_page"] = page_key
                st.rerun()

        st.write("")
        theme_mode = st.session_state.get("theme_mode", "dark")
        sb_theme_btn = "☀️ Light Theme" if theme_mode == "dark" else "🌙 Dark Theme"
        if st.button(sb_theme_btn, key="btn_sb_toggle_theme", use_container_width=True):
            st.session_state["theme_mode"] = "light" if theme_mode == "dark" else "dark"
            st.rerun()

        st.divider()

        render_html(
            """
            <div style='background: #0F172A; border: 1px solid #334155; border-radius: 12px; padding: 12px; text-align: center; color: white;'>
                <p style='margin: 0; font-size: 0.75rem; color: #94A3B8;'>Architected & Developed by</p>
                <p style='margin: 2px 0 0 0; font-size: 0.85rem; font-weight: 800; color: #60A5FA;'>Santosh Kumar Kolagani</p>
            </div>
            """
        )

    # ---------------------------------------------------------
    # TOP HEADER NAVIGATION BAR
    # ---------------------------------------------------------
    c_logo, c_dev, c_step, c_user, c_theme = st.columns([1.1, 2.3, 1.6, 1.2, 1.0])

    with c_logo:
        if st.button("🚀 NextHire AI", key="nav_logo_home", use_container_width=True):
            st.session_state["current_page"] = "home"
            st.rerun()

    with c_dev:
        # HIGH-CONTRAST GLOWING DEVELOPER BADGE FOR SANTOSH KUMAR KOLAGANI
        render_html(
            """
            <div style='text-align: center; padding-top: 2px;'>
                <div style='background: linear-gradient(135deg, #FFFFFF 0%, #F8FAFC 100%);
                            border: 2px solid #2563EB;
                            box-shadow: 0 4px 18px rgba(37, 99, 235, 0.35);
                            border-radius: 25px;
                            padding: 5px 14px;
                            display: inline-flex;
                            align-items: center;
                            justify-content: center;
                            gap: 8px;
                            white-space: nowrap;'>
                    <span style='background: linear-gradient(135deg, #2563EB 0%, #1D4ED8 100%); width: 22px; height: 22px; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-size: 0.72rem; color: white; font-weight: bold;'>✨</span>
                    <span style='font-size: 0.8rem; font-weight: 700; color: #0F172A; letter-spacing: 0.2px;'>
                        Developed by <b style='color: #2563EB; text-transform: uppercase; font-weight: 800;'>Santosh Kumar Kolagani</b>
                    </span>
                </div>
            </div>
            """
        )

    with c_step:
        render_html(
            f"""
            <div style='text-align: center; background: #F1F5F9; border: 1px solid #CBD5E1; border-radius: 20px; padding: 5px 14px; margin-top: 2px;'>
                <span style='color: #475569; font-size: 0.8rem; font-weight: 600;'>Section:</span>
                <span style='color: #2563EB; font-size: 0.85rem; font-weight: 700; margin-left: 4px;'>{curr_step_name}</span>
            </div>
            """
        )

    with c_user:
        render_html(
            f"""
            <div style='text-align: right; padding-top: 4px;'>
                <span style='background: #F8FAFC; border: 1px solid #CBD5E1; color: #0F172A; padding: 5px 12px; border-radius: 14px; font-size: 0.82rem; font-weight: 700; display: inline-block; white-space: nowrap;'>
                    {display_user}
                </span>
            </div>
            """
        )

    with c_theme:
        theme_mode = st.session_state.get("theme_mode", "dark")
        top_theme_btn = "☀️ Light" if theme_mode == "dark" else "🌙 Dark"
        if st.button(top_theme_btn, key="btn_top_toggle_theme", use_container_width=True):
            st.session_state["theme_mode"] = "light" if theme_mode == "dark" else "dark"
            st.rerun()

    st.divider()