"""
===========================================================
Project     : NextHire AI
File        : navbar.py
Author      : Santosh Kolagani

Purpose:
    Ultra-clean 4-column SaaS top navigation bar with high-contrast glowing developer credit
    badge for Santosh Kumar Kolagani, zero column overlap, step indicator, and profile badge.
===========================================================
"""

import streamlit as st
from app.utils.helpers import render_html


def render_navbar():
    """
    Renders ultra-clean top navigation bar with non-overlapping developer credit badge.
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

    # Dedicated 4-Column Layout (Zero Merging / Zero Overlap)
    c_logo, c_dev, c_step, c_user = st.columns([1.1, 2.6, 1.8, 1.5])

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

    st.divider()