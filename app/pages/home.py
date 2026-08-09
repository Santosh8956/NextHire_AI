"""
===========================================================
Project     : NextHire AI
File        : home.py
Author      : Santosh Kolagani

Purpose:
    Screen 1 & Dashboard: Welcomes user with Get Started button, unique modern AI Architect name onboarding,
    General vs Customized selection (redirecting Customized directly to personalization),
    and unique Dashboard with custom template routing logic.
===========================================================
"""

import streamlit as st
from app.components.navbar import render_navbar
from app.services.parser.resume_parser import extract_text_from_pdf, parse_resume_content
from app.utils.helpers import render_html


def show_home():
    """Renders Welcome Onboarding Flow & Unique NextHire Dashboard."""
    render_navbar()

    theme_mode = st.session_state.get("theme_mode", "dark")
    is_dark = (theme_mode == "dark")

    # Onboarding Step State (1: Welcome, 2: Name Prompt, 3: General vs Customized, 4: Dashboard)
    if "home_step" not in st.session_state:
        st.session_state["home_step"] = 1
    if "user_name" not in st.session_state:
        st.session_state["user_name"] = ""

    home_step = st.session_state.get("home_step", 1)
    user_name = st.session_state.get("user_name", "")

    # ---------------------------------------------------------
    # STEP 1: WELCOME TO NEXTHIRE AI & GET STARTED BUTTON
    # ---------------------------------------------------------
    if home_step == 1:
        render_html(
            """
            <div style='background: linear-gradient(135deg, #0F172A 0%, #1E3A8A 100%);
                        border: 2px solid #3B82F6;
                        border-radius: 20px;
                        padding: 38px 30px;
                        text-align: center;
                        color: white;
                        margin-bottom: 25px;
                        box-shadow: 0 15px 35px rgba(0, 0, 0, 0.25);'>
                <div style='font-size: 3.8rem; margin-bottom: 8px;'>🚀</div>
                <h1 style='color: #F8FAFC; font-size: 2.8rem; font-weight: 800; margin: 0 0 6px 0;'>Welcome to NextHire AI</h1>
                <p style='color: #93C5FD; font-size: 1.3rem; font-weight: 600; margin: 0 0 15px 0;'>Your Intelligent AI Career Assistant</p>
                <p style='color: #E2E8F0; font-size: 1.05rem; max-width: 750px; margin: 0 auto; line-height: 1.6;'>
                    Craft high-impact, ATS-optimized resumes tailored for top career opportunities using advanced AI content polishing and high-resolution classified templates.
                </p>
            </div>
            """
        )

        # Theme-aware styles for feature highlight cards
        c1_bg = "#1E293B" if is_dark else "#F0F9FF"
        c1_border = "#0284C7" if is_dark else "#BAE6FD"
        c1_title = "#38BDF8" if is_dark else "#0369A1"
        c1_sub = "#94A3B8" if is_dark else "#334155"

        c2_bg = "#1E293B" if is_dark else "#FAF5FF"
        c2_border = "#9333EA" if is_dark else "#E9D5FF"
        c2_title = "#C084FC" if is_dark else "#6B21A8"
        c2_sub = "#94A3B8" if is_dark else "#334155"

        c3_bg = "#1E293B" if is_dark else "#F0FDF4"
        c3_border = "#16A34A" if is_dark else "#BBF7D0"
        c3_title = "#4ADE80" if is_dark else "#15803D"
        c3_sub = "#94A3B8" if is_dark else "#334155"

        c4_bg = "#1E293B" if is_dark else "#FFF7ED"
        c4_border = "#EA580C" if is_dark else "#FED7AA"
        c4_title = "#FB923C" if is_dark else "#C2410C"
        c4_sub = "#94A3B8" if is_dark else "#334155"

        # Feature Highlights Grid
        f1, f2, f3, f4 = st.columns(4)

        with f1:
            render_html(
                f"""
                <div style='background: {c1_bg}; border: 1.5px solid {c1_border}; border-left: 4px solid {c1_title}; border-radius: 14px; padding: 20px 16px; min-height: 195px; height: 100%; box-sizing: border-box;'>
                    <div style='font-size: 1.8rem; margin-bottom: 6px;'>🎯</div>
                    <h4 style='color: {c1_title}; margin: 0 0 6px 0; font-size: 1.05rem;'>ATS Scoring Engine</h4>
                    <p style='color: {c1_sub}; font-size: 0.83rem; margin: 0; line-height: 1.45;'>Evaluate keyword coverage & ATS compatibility instantly.</p>
                </div>
                """
            )

        with f2:
            render_html(
                f"""
                <div style='background: {c2_bg}; border: 1.5px solid {c2_border}; border-left: 4px solid {c2_title}; border-radius: 14px; padding: 20px 16px; min-height: 195px; height: 100%; box-sizing: border-box;'>
                    <div style='font-size: 1.8rem; margin-bottom: 6px;'>🤖</div>
                    <h4 style='color: {c2_title}; margin: 0 0 6px 0; font-size: 1.05rem;'>AI Content Polish</h4>
                    <p style='color: {c2_sub}; font-size: 0.83rem; margin: 0; line-height: 1.45;'>Enhance bullet points with action verbs & performance metrics.</p>
                </div>
                """
            )

        with f3:
            render_html(
                f"""
                <div style='background: {c3_bg}; border: 1.5px solid {c3_border}; border-left: 4px solid {c3_title}; border-radius: 14px; padding: 20px 16px; min-height: 195px; height: 100%; box-sizing: border-box;'>
                    <div style='font-size: 1.8rem; margin-bottom: 6px;'>🎨</div>
                    <h4 style='color: {c3_title}; margin: 0 0 6px 0; font-size: 1.05rem;'>Signature HD Templates</h4>
                    <p style='color: {c3_sub}; font-size: 0.83rem; margin: 0; line-height: 1.45;'>Classified designs across ATS, Modern, Tech & Executive layouts.</p>
                </div>
                """
            )

        with f4:
            render_html(
                f"""
                <div style='background: {c4_bg}; border: 1.5px solid {c4_border}; border-left: 4px solid {c4_title}; border-radius: 14px; padding: 20px 16px; min-height: 195px; height: 100%; box-sizing: border-box;'>
                    <div style='font-size: 1.8rem; margin-bottom: 6px;'>📥</div>
                    <h4 style='color: {c4_title}; margin: 0 0 6px 0; font-size: 1.05rem;'>Instant PDF Export</h4>
                    <p style='color: {c4_sub}; font-size: 0.83rem; margin: 0; line-height: 1.45;'>Publication-ready vector PDF document export in 1-click.</p>
                </div>
                """
            )

        st.write("")
        st.write("")

        c1, c2, c3 = st.columns([1, 2, 1])
        with c2:
            if st.button("🚀 Get Started", type="primary", use_container_width=True, key="btn_home_get_started"):
                st.session_state["home_step"] = 2
                st.rerun()

    # ---------------------------------------------------------
    # STEP 2: ULTRA-MODERN CONVERSATIONAL AI RESUME ARCHITECT ONBOARDING
    # ---------------------------------------------------------
    elif home_step == 2:
        render_html(
            """
            <div style='background: linear-gradient(135deg, #0F172A 0%, #1E293B 100%);
                        border: 2px solid #38BDF8;
                        border-radius: 24px;
                        padding: 32px 36px;
                        margin-bottom: 25px;
                        box-shadow: 0 20px 45px rgba(0, 0, 0, 0.35);'>
                <div style='display: flex; align-items: center; gap: 16px; margin-bottom: 20px;'>
                    <div style='background: linear-gradient(135deg, #2563EB 0%, #0284C7 100%);
                                width: 54px; height: 54px; border-radius: 16px; display: flex; align-items: center; justify-content: center; font-size: 1.8rem; color: white; box-shadow: 0 0 20px rgba(56, 189, 248, 0.6);'>
                        🤖
                    </div>
                    <div>
                        <h3 style='margin: 0; color: #F8FAFC; font-size: 1.4rem; font-weight: 800; letter-spacing: -0.3px;'>NextHire AI Resume Architect</h3>
                        <div style='display: flex; align-items: center; gap: 8px; margin-top: 4px;'>
                            <span style='background: #16A34A; width: 8px; height: 8px; border-radius: 50%; display: inline-block;'></span>
                            <span style='color: #4ADE80; font-size: 0.85rem; font-weight: 700; text-transform: uppercase; letter-spacing: 0.5px;'>AI Model Active • Personalizing Your Session</span>
                        </div>
                    </div>
                </div>
                <div style='background: rgba(30, 41, 59, 0.8); border-left: 4px solid #38BDF8; padding: 20px 24px; border-radius: 14px; margin-bottom: 15px;'>
                    <p style='color: #F1F5F9; font-size: 1.15rem; margin: 0 0 10px 0; line-height: 1.6; font-weight: 500;'>
                        👋 <b>Welcome!</b> I'm NextHire AI, your personal resume architect and ATS strategy partner.
                    </p>
                    <p style='color: #94A3B8; font-size: 1rem; margin: 0; line-height: 1.55;'>
                        I analyze target job postings, enhance experience bullets with high-impact action metrics, and generate publication-ready 4K ATS vector resumes.
                        <b>To get started on your personalized resume, what should I call you?</b>
                    </p>
                </div>
            </div>
            """
        )

        with st.form("interactive_name_form"):
            entered_name = st.text_input(
                "👤 Enter Your Full Name:",
                value=user_name,
                placeholder="e.g. Santosh Kumar Kolagani",
                help="Your name will be placed at the top of your resume and personalized greetings."
            )

            preview_greeting = entered_name.strip() if entered_name.strip() else "Future Industry Leader"
            render_html(
                f"""
                <div style='background: #F0F9FF; border: 1.5px dashed #0284C7; border-radius: 12px; padding: 12px 18px; margin: 14px 0;'>
                    <p style='color: #0369A1; font-size: 0.95rem; margin: 0;'>
                        ✨ Live Greeting Preview: <b>"Welcome aboard, {preview_greeting}! Let's craft your high-impact resume."</b>
                    </p>
                </div>
                """
            )

            c1, c2 = st.columns([1, 1])
            with c1:
                if st.form_submit_button("🚀 Save Name & Start Building ➡️", type="primary", use_container_width=True):
                    if entered_name.strip():
                        st.session_state["user_name"] = entered_name.strip()
                        resume = st.session_state.get("resume_data", {})
                        personal = resume.setdefault("personal_info", {})
                        personal["full_name"] = entered_name.strip()
                        st.session_state["home_step"] = 3
                        st.rerun()
                    else:
                        st.warning("Please enter your name to proceed!")

        st.write("")
        render_html(
            """
            <div style='display: flex; justify-content: center; gap: 24px; color: #94A3B8; font-size: 0.88rem;'>
                <span>🔒 <b>100% Private & Encrypted</b></span>
                <span>⚡ <b>Instant Setup</b></span>
                <span>🎯 <b>ATS Tailored</b></span>
            </div>
            """
        )

    # ---------------------------------------------------------
    # STEP 3: GENERAL RESUME vs CUSTOMIZED RESUME (Direct Personalization Redirection)
    # ---------------------------------------------------------
    elif home_step == 3:
        render_html(
            f"""
            <div style='background: #F0FDF4; border-left: 5px solid #16A34A; border-radius: 12px; padding: 22px 25px; margin-bottom: 25px;'>
                <h3 style='color: #15803D; margin-top: 0; font-size: 1.4rem;'>Nice to meet you, {user_name}! 🚀</h3>
                <p style='color: #334155; font-size: 1.1rem; margin-bottom: 0;'>
                    <b>What brings you here today?</b> Please choose what you would like to create:
                </p>
            </div>
            """
        )

        col_gen, col_cust = st.columns(2)

        with col_gen:
            render_html(
                """
                <div style='background: #FFFFFF; border: 2px solid #2563EB; border-radius: 16px; padding: 25px; text-align: center; height: 100%;'>
                    <div style='font-size: 3rem; margin-bottom: 10px;'>📄</div>
                    <h3 style='color: #1E3A8A; margin: 0 0 10px 0;'>General Resume</h3>
                    <p style='color: #64748B; font-size: 0.95rem; line-height: 1.5; margin-bottom: 20px;'>
                        Create a versatile, clean resume showcasing your complete skills, education, projects, and career background.
                    </p>
                </div>
                """
            )
            st.write("")
            if st.button("🚀 General Resume", type="primary", use_container_width=True, key="btn_select_general"):
                st.session_state["resume_type_choice"] = "General Resume"
                st.session_state["home_step"] = 4
                st.rerun()

        with col_cust:
            render_html(
                """
                <div style='background: #FFFFFF; border: 2px solid #16A34A; border-radius: 16px; padding: 25px; text-align: center; height: 100%;'>
                    <div style='font-size: 3rem; margin-bottom: 10px;'>🎯</div>
                    <h3 style='color: #166534; margin: 0 0 10px 0;'>Customized Resume</h3>
                    <p style='color: #64748B; font-size: 0.95rem; line-height: 1.5; margin-bottom: 20px;'>
                        Tailor your resume specifically for a target job role, company, and job description for maximum ATS keyword match.
                    </p>
                </div>
                """
            )
            st.write("")
            if st.button("🎯 Customized Resume", type="primary", use_container_width=True, key="btn_select_customized"):
                st.session_state["resume_type_choice"] = "Personalized Resume"
                st.session_state["current_page"] = "personalization"
                st.rerun()

    # ---------------------------------------------------------
    # STEP 4: UNIQUE, USER-FRIENDLY DASHBOARD WITH SPECIFIED ROUTING
    # ---------------------------------------------------------
    elif home_step == 4:
        rtype = st.session_state.get("resume_type_choice", "General Resume")

        c_dash_hdr, c_dash_sw = st.columns([3.2, 1.2])
        with c_dash_hdr:
            render_html(
                f"""
                <div style='background: linear-gradient(135deg, #0F172A 0%, #1E3A8A 100%);
                            border: 2px solid #3B82F6;
                            border-radius: 16px;
                            padding: 22px 26px;
                            color: white;
                            margin-bottom: 20px;'>
                    <h2 style='margin: 0; color: #F8FAFC; font-size: 1.8rem;'>👋 Dashboard — Welcome, {user_name}!</h2>
                    <p style='margin: 6px 0 0 0; color: #93C5FD; font-size: 0.98rem;'>
                        Active Resume Mode: <b style="color: #60A5FA;">{rtype}</b>
                    </p>
                </div>
                """
            )
        with c_dash_sw:
            st.write("")
            if st.button("🔄 Switch Mode (Gen / Custom)", key="btn_dash_switch_mode", use_container_width=True):
                st.session_state["home_step"] = 3
                st.rerun()

        # Quick Action Row
        c_act1, c_act2 = st.columns(2)

        with c_act1:
            render_html(
                """
                <div style='background: #F0F9FF; border: 2px solid #0284C7; border-radius: 12px; padding: 18px;'>
                    <h4 style='color: #0369A1; margin: 0 0 6px 0;'>🚀 Build New Resume</h4>
                    <p style='color: #334155; font-size: 0.85rem; margin-bottom: 12px;'>Choose a template style first, then proceed directly to details workspace.</p>
                </div>
                """
            )
            st.write("")
            if st.button("🚀 Start Building New Resume", type="primary", use_container_width=True, key="dash_btn_new"):
                st.session_state["from_flow"] = "build_new"
                st.session_state["current_page"] = "template_selection"
                st.rerun()

        with c_act2:
            render_html(
                """
                <div style='background: #F0FDF4; border: 2px solid #16A34A; border-radius: 12px; padding: 18px;'>
                    <h4 style='color: #15803D; margin: 0 0 6px 0;'>📄 Edit Existing Resume (Upload PDF/TXT)</h4>
                    <p style='color: #334155; font-size: 0.85rem; margin-bottom: 12px;'>Upload your resume file to parse and edit details.</p>
                </div>
                """
            )
            st.write("")
            uploaded_pdf = st.file_uploader("Upload PDF/TXT file:", type=["pdf", "txt"], key="dash_pdf_upload")
            if uploaded_pdf is not None:
                file_bytes = uploaded_pdf.read()
                if uploaded_pdf.name.endswith(".pdf"):
                    extracted_text = extract_text_from_pdf(file_bytes)
                else:
                    extracted_text = file_bytes.decode("utf-8", errors="ignore")

                if extracted_text:
                    parsed_data = parse_resume_content(extracted_text)
                    st.session_state["resume_data"] = parsed_data
                    st.session_state["edit_resume_parsed"] = True
                    st.success("🎉 Existing resume parsed successfully!")

            if st.session_state.get("edit_resume_parsed"):
                render_html(
                    """
                    <div style='background: #FFFBEB; border: 1.5px solid #FCD34D; border-radius: 10px; padding: 14px; margin-top: 10px;'>
                        <p style='color: #92400E; font-weight: 700; margin: 0 0 8px 0; font-size: 0.95rem;'>
                            💡 How would you like to choose the template style for your imported resume?
                        </p>
                    </div>
                    """
                )
                c_tpl_default, c_tpl_select = st.columns(2)
                with c_tpl_default:
                    if st.button("📄 Continue with Default Template", use_container_width=True, key="btn_tpl_default"):
                        st.session_state["selected_template"] = "ats_1"
                        st.session_state["current_page"] = "data_collection"
                        st.rerun()
                with c_tpl_select:
                    if st.button("🎨 Select New Template", type="primary", use_container_width=True, key="btn_tpl_select"):
                        st.session_state["from_flow"] = "edit_existing"
                        st.session_state["current_page"] = "template_selection"
                        st.rerun()

        st.write("")
        st.divider()

        # ---------------------------------------------------------
        # UNIQUE REDIRECTION CARDS GRID (Direct Feature Navigation)
        # ---------------------------------------------------------
        st.markdown("### ⚡ Quick Feature Redirections")
        st.caption("Click any feature card below to navigate directly:")

        grid_card_bg = "#1E293B" if is_dark else "#FFFFFF"
        grid_card_border = "#334155" if is_dark else "#E2E8F0"
        grid_body_sub = "#94A3B8" if is_dark else "#64748B"

        grid1, grid2, grid3 = st.columns(3)

        with grid1:
            render_html(
                f"""
                <div style='background: {grid_card_bg}; border: 1.5px solid {grid_card_border}; border-radius: 12px; padding: 18px;'>
                    <h4 style='color: {"#60A5FA" if is_dark else "#1E3A8A"}; margin: 0 0 6px 0;'>📊 ATS Score & Analysis</h4>
                    <p style='color: {grid_body_sub}; font-size: 0.85rem; margin: 0;'>Evaluate ATS compatibility score, formatting checks & missing keywords.</p>
                </div>
                """
            )
            st.write("")
            if st.button("📊 View ATS Score & Analysis", use_container_width=True, key="dash_redir_ats"):
                st.session_state["current_page"] = "resume_analysis"
                st.rerun()

        with grid2:
            render_html(
                f"""
                <div style='background: {grid_card_bg}; border: 1.5px solid {grid_card_border}; border-radius: 12px; padding: 18px;'>
                    <h4 style='color: {"#2DD4BF" if is_dark else "#0D9488"}; margin: 0 0 6px 0;'>✍️ Content Editor & AI Polish</h4>
                    <p style='color: {grid_body_sub}; font-size: 0.85rem; margin: 0;'>Side-by-side live editor to enhance bullet points with action verbs.</p>
                </div>
                """
            )
            st.write("")
            if st.button("✍️ Open Content Editor", use_container_width=True, key="dash_redir_editor"):
                st.session_state["current_page"] = "resume_editor"
                st.rerun()

        with grid3:
            render_html(
                f"""
                <div style='background: {grid_card_bg}; border: 1.5px solid {grid_card_border}; border-radius: 12px; padding: 18px;'>
                    <h4 style='color: {"#C084FC" if is_dark else "#7C3AED"}; margin: 0 0 6px 0;'>🎨 Signature Template Gallery</h4>
                    <p style='color: {grid_body_sub}; font-size: 0.85rem; margin: 0;'>Browse high-resolution preview cards across classified template styles.</p>
                </div>
                """
            )
            st.write("")
            if st.button("🎨 Open Template Gallery", use_container_width=True, key="dash_redir_tmpl"):
                st.session_state["current_page"] = "template_selection"
                st.rerun()

        st.write("")
        grid4, grid5, grid6 = st.columns(3)

        with grid4:
            render_html(
                f"""
                <div style='background: {grid_card_bg}; border: 1.5px solid {grid_card_border}; border-radius: 12px; padding: 18px;'>
                    <h4 style='color: {"#38BDF8" if is_dark else "#2563EB"}; margin: 0 0 6px 0;'>📝 Resume Workspace</h4>
                    <p style='color: {grid_body_sub}; font-size: 0.85rem; margin: 0;'>Clean workspace sections: Personal, Education, Skills, Projects, Experience.</p>
                </div>
                """
            )
            st.write("")
            if st.button("📝 Open Workspace", use_container_width=True, key="dash_redir_ws"):
                st.session_state["current_page"] = "data_collection"
                st.rerun()

        with grid5:
            render_html(
                f"""
                <div style='background: {grid_card_bg}; border: 1.5px solid {grid_card_border}; border-radius: 12px; padding: 18px;'>
                    <h4 style='color: {"#FBBF24" if is_dark else "#D97706"}; margin: 0 0 6px 0;'>🎯 Target Job Personalization</h4>
                    <p style='color: {grid_body_sub}; font-size: 0.85rem; margin: 0;'>Customize target job role, company name, and job posting requirements.</p>
                </div>
                """
            )
            st.write("")
            if st.button("🎯 Target Personalization", use_container_width=True, key="dash_redir_pers"):
                st.session_state["current_page"] = "personalization"
                st.rerun()

        with grid6:
            render_html(
                f"""
                <div style='background: {grid_card_bg}; border: 1.5px solid {grid_card_border}; border-radius: 12px; padding: 18px;'>
                    <h4 style='color: {"#34D399" if is_dark else "#059669"}; margin: 0 0 6px 0;'>📥 Export PDF Resume</h4>
                    <p style='color: {grid_body_sub}; font-size: 0.85rem; margin: 0;'>Inspect final high-resolution document preview and download ATS PDF.</p>
                </div>
                """
            )
            st.write("")
            if st.button("📥 Export & Download PDF", use_container_width=True, key="dash_redir_dl"):
                st.session_state["current_page"] = "download"
                st.rerun()

    st.write("")
    st.divider()

    render_html(
        f"""
        <div style='text-align: center; color: {"#94A3B8" if is_dark else "#64748B"}; font-size: 0.88rem;'>
            NextHire AI Resume Builder & ATS Platform • Developed by <b>Santosh Kumar Kolagani</b>
        </div>
        """
    )