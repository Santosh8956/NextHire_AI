"""
===========================================================
Project     : NextHire AI
File        : navbar.py
Author      : Santosh Kolagani

Purpose:
    Interactive Navigation Bar supporting multi-page workflow.
===========================================================
"""

import streamlit as st
from app.config.settings import get_api_key


def render_navbar():
    """
    Renders top navigation bar with step status and navigation buttons.
    """
    # Quick API key input expander in top bar
    with st.expander("🔑 Gemini API Settings (Optional for offline fallback)", expanded=False):
        c1, c2 = st.columns([3, 1])
        with c1:
            key_val = st.text_input(
                "Enter Gemini API Key:",
                value=st.session_state.get("api_key", ""),
                type="password",
                help="Leave blank to use intelligent offline fallback engine."
            )
            if key_val != st.session_state.get("api_key", ""):
                st.session_state["api_key"] = key_val
        with c2:
            if st.button("Load Sample Data 🚀"):
                from app.config.constants import SAMPLE_RESUME_DATA
                st.session_state["resume_data"] = SAMPLE_RESUME_DATA
                st.session_state["current_page"] = "data_collection"
                st.success("Sample resume data loaded!")
                st.rerun()

    # Step progress header
    c_logo, c_nav1, c_nav2, c_nav3, c_nav4, c_nav5, c_nav6 = st.columns([2, 1.2, 1.2, 1.2, 1.2, 1.2, 1.2])

    with c_logo:
        st.markdown("### 🚀 **NextHire AI**")

    curr = st.session_state.get("current_page", "home")

    def page_btn(col, label, page_name, icon):
        with col:
            is_active = (curr == page_name)
            btn_type = "primary" if is_active else "secondary"
            if st.button(f"{icon} {label}", type=btn_type, use_container_width=True, key=f"nav_{page_name}"):
                st.session_state["current_page"] = page_name
                st.rerun()

    page_btn(c_nav1, "Home", "home", "🏠")
    page_btn(c_nav2, "Data", "data_collection", "📝")
    page_btn(c_nav3, "Templates", "template_selection", "🎨")
    page_btn(c_nav4, "Editor", "resume_editor", "✍️")
    page_btn(c_nav5, "Analysis", "resume_analysis", "📊")
    page_btn(c_nav6, "Download", "download", "📥")

    st.divider()