"""
===========================================================
Project     : NextHire AI
File        : navbar.py
Author      : Santosh Kolagani

Purpose:
    Sleek top navigation bar with glowing developer credit badge for Santosh Kumar Kolagani,
    section step indicator, and candidate profile badge.
===========================================================
"""

import streamlit as st
from app.utils.helpers import render_html


def render_navbar():
    """
    Renders sleek top navigation bar with unique glowing developer credit badge.
    """
    curr_page = st.session_state.get("current_page", "home")
    user_name = st.session_state.get("user_name", "Candidate")

    # Step label mapping
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

    # Top Navigation Row
    c_brand, c_step, c_user = st.columns([2.1, 1.8, 1.6])

    with c_brand:
        b1, b2 = st.columns([1, 1.8])
        with b1:
            if st.button("🚀 NextHire AI", key="nav_logo_home"):
                st.session_state["current_page"] = "home"
                st.rerun()
        with b2:
            # UNIQUE GLOWING DEVELOPER CREDIT BADGE FOR SANTOSH KUMAR KOLAGANI
            render_html(
                """
                <div style='padding-top: 4px;'>
                    <div style='background: linear-gradient(135deg, #0F172A 0%, #1E3A8A 50%, #2563EB 100%);
                                border: 1.5px solid #60A5FA;
                                box-shadow: 0 4px 14px rgba(37, 99, 235, 0.35);
                                border-radius: 20px;
                                padding: 5px 14px;
                                display: inline-flex;
                                align-items: center;
                                gap: 6px;
                                color: #F8FAFC;'>
                        <span style='font-size: 0.9rem;'>✨</span>
                        <span style='font-size: 0.78rem; font-weight: 700; letter-spacing: 0.3px; color: #FFFFFF;'>
                            Developed by <b style='color: #60A5FA; text-transform: uppercase;'>Santosh Kumar Kolagani</b>
                        </span>
                    </div>
                </div>
                """
            )

    with c_step:
        render_html(
            f"""
            <div style='text-align: center; background: #F1F5F9; border: 1px solid #E2E8F0; border-radius: 20px; padding: 6px 16px; margin-top: 2px;'>
                <span style='color: #475569; font-size: 0.85rem; font-weight: 600;'>Section:</span>
                <span style='color: #2563EB; font-size: 0.9rem; font-weight: 700; margin-left: 6px;'>{curr_step_name}</span>
            </div>
            """
        )

    with c_user:
        u_str = f"👤 {user_name}" if (user_name and user_name != "Candidate") else "👤 Guest Candidate"
        render_html(
            f"""
            <div style='text-align: right; padding-top: 6px;'>
                <span style='background: #F8FAFC; border: 1px solid #CBD5E1; color: #0F172A; padding: 4px 12px; border-radius: 12px; font-size: 0.85rem; font-weight: 700; display: inline-block;'>
                    {u_str}
                </span>
            </div>
            """
        )

    st.divider()