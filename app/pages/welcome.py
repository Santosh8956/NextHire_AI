"""
===========================================================
Project     : NextHire AI
File        : welcome.py
Author      : Santosh Kolagani

Purpose:
    Screen 2 – AI Welcome: Friendly AI intro screen with sequential Back & Continue navigation.
===========================================================
"""

import streamlit as st
from app.components.navbar import render_navbar
from app.utils.helpers import render_html


def show_ai_welcome():
    """Renders Screen 2 – AI Welcome."""
    render_navbar()

    user_name = st.session_state.get("user_name", "Friend")

    col1, col2, col3 = st.columns([1, 2.2, 1])

    with col2:
        render_html(
            f"""
            <div style='background: linear-gradient(135deg, #0F172A 0%, #1E293B 100%); 
                        border: 2px solid #3B82F6; 
                        border-radius: 20px; 
                        padding: 35px 30px; 
                        text-align: center; 
                        box-shadow: 0 20px 40px rgba(0, 0, 0, 0.3);'>
                <div style='font-size: 3.5rem; margin-bottom: 12px;'>👋</div>
                <h1 style='color: #F8FAFC; font-size: 2.2rem; margin-bottom: 8px; font-weight: 700;'>
                    Hello, {user_name}!
                </h1>
                <h3 style='color: #60A5FA; font-size: 1.3rem; margin-bottom: 18px; font-weight: 500;'>
                    I'm NextHire AI.
                </h3>
                <p style='color: #94A3B8; font-size: 1.1rem; line-height: 1.6; margin-bottom: 22px;'>
                    I'll help you build a professional, ATS-optimized resume using AI.<br>
                    The process takes only a few minutes.
                </p>
                <div style='background: #1E3A8A; border-radius: 12px; padding: 10px 18px; margin-bottom: 15px; display: inline-block;'>
                    <span style='color: #E0F2FE; font-size: 1.05rem; font-weight: 600;'>🚀 Let's begin!</span>
                </div>
            </div>
            """
        )

        st.write("")
        st.write("")

        c_back, c_next = st.columns([1, 1])
        with c_back:
            if st.button("⬅️ Back", use_container_width=True, key="btn_welcome_back"):
                st.session_state["current_page"] = "home"
                st.rerun()
        with c_next:
            if st.button("Continue ➡️", type="primary", use_container_width=True, key="btn_welcome_continue"):
                st.session_state["current_page"] = "resume_type"
                st.rerun()
