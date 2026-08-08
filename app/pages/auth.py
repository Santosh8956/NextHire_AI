"""
===========================================================
Project     : NextHire AI
File        : auth.py
Author      : Santosh Kolagani

Purpose:
    Login & Sign Up Page for NextHire AI supporting user authentication,
    registration, and quick guest access.
===========================================================
"""

import streamlit as st
from app.components.navbar import render_navbar
from app.utils.helpers import render_html


def show_auth():
    """Renders Login & Sign Up Page."""
    render_navbar()

    col1, col2, col3 = st.columns([1, 2.2, 1])

    with col2:
        render_html(
            """
            <div style='text-align: center; margin-bottom: 25px;'>
                <div style='font-size: 3rem; margin-bottom: 5px;'>🚀</div>
                <h1 style='color: #1E3A8A; font-size: 2.2rem; font-weight: 700; margin: 0;'>Welcome to NextHire AI</h1>
                <p style='color: #64748B; font-size: 1.05rem; margin-top: 5px;'>Sign in to your account or register to save and manage your AI resumes.</p>
            </div>
            """
        )

        tab_login, tab_signup = st.tabs(["🔑 Log In", "📝 Sign Up / Register"])

        # ---------------------------------------------------------
        # TAB 1: LOG IN
        # ---------------------------------------------------------
        with tab_login:
            with st.form("login_form"):
                email = st.text_input("Email Address", placeholder="name@example.com", key="login_email")
                password = st.text_input("Password", type="password", placeholder="••••••••", key="login_pass")
                login_btn = st.form_submit_button("Log In 🔓", type="primary", use_container_width=True)

                if login_btn:
                    if email and password:
                        st.session_state["authenticated"] = True
                        st.session_state["user_email"] = email
                        # Extract name from email if not set
                        name_part = email.split("@")[0].replace(".", " ").title()
                        st.session_state["user_name"] = name_part
                        
                        resume_data = st.session_state.get("resume_data", {})
                        personal = resume_data.setdefault("personal_info", {})
                        if not personal.get("full_name"):
                            personal["full_name"] = name_part
                            personal["email"] = email

                        st.success(f"Welcome back, {name_part}!")
                        st.session_state["current_page"] = "home"
                        st.rerun()
                    else:
                        st.error("Please enter both email and password.")

            st.write("")
            st.markdown("---")
            if st.button("⚡ Continue as Guest (No Registration Required)", use_container_width=True, key="btn_guest_access"):
                st.session_state["authenticated"] = True
                st.session_state["user_name"] = "Guest Candidate"
                st.session_state["current_page"] = "home"
                st.rerun()

        # ---------------------------------------------------------
        # TAB 2: SIGN UP / REGISTER
        # ---------------------------------------------------------
        with tab_signup:
            with st.form("signup_form"):
                full_name = st.text_input("Full Name", placeholder="Santosh Kolagani", key="signup_name")
                email = st.text_input("Email Address", placeholder="santosh@example.com", key="signup_email")
                password = st.text_input("Password", type="password", placeholder="••••••••", key="signup_pass")
                confirm_pass = st.text_input("Confirm Password", type="password", placeholder="••••••••", key="signup_confirm")
                signup_btn = st.form_submit_button("Create Account 🚀", type="primary", use_container_width=True)

                if signup_btn:
                    if not full_name or not email or not password:
                        st.error("Please fill in all required fields.")
                    elif password != confirm_pass:
                        st.error("Passwords do not match.")
                    else:
                        st.session_state["authenticated"] = True
                        st.session_state["user_name"] = full_name
                        st.session_state["user_email"] = email

                        resume_data = st.session_state.get("resume_data", {})
                        personal = resume_data.setdefault("personal_info", {})
                        personal["full_name"] = full_name
                        personal["email"] = email

                        st.success("Account created successfully!")
                        st.session_state["current_page"] = "home"
                        st.rerun()
