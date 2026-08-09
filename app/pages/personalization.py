"""
===========================================================
Project     : NextHire AI
File        : personalization.py
Author      : Santosh Kolagani

Purpose:
    Screen 5 – Personalization: Target Job Role, Target Company & Job Description inputs
    with AI Company Online Resource intelligence and redirection to Template Gallery.
===========================================================
"""

import streamlit as st
from app.components.navbar import render_navbar
from app.services.parser.resume_parser import extract_text_from_pdf, parse_resume_content


COMPANY_KNOWLEDGE = {
    "google": "Core Focus: Scalable distributed systems, AI/ML, cloud architecture, clean code, data structures & algorithms, innovation.",
    "microsoft": "Core Focus: Azure cloud services, enterprise software, AI integration, collaboration, C#/.NET, Python, customer success.",
    "amazon": "Core Focus: AWS cloud infrastructure, customer obsession, ownership, scalable microservices, operational excellence, high performance.",
    "meta": "Core Focus: Large scale infrastructure, PyTorch, AI research, web platforms (React), data analytics, move fast culture.",
    "nvidia": "Core Focus: GPU computing, CUDA, deep learning, computer vision, AI hardware acceleration, high performance computing.",
    "accenture": "Core Focus: Digital transformation, IT consulting, cloud migration, enterprise architecture, client management.",
    "deloitte": "Core Focus: Technology consulting, data analytics, cyber security, risk management, strategy execution."
}


def _generate_company_insights(company: str, role: str, api_key: str) -> str:
    """Fetches AI company insights and target role keywords."""
    company_clean = company.strip().lower()
    known_info = COMPANY_KNOWLEDGE.get(company_clean, f"Core Focus: Industry best practices for {company}, domain expertise, and technical excellence.")

    if api_key and len(api_key) > 10:
        try:
            genai.configure(api_key=api_key)
            model = genai.GenerativeModel("gemini-1.5-flash")
            prompt = (
                f"Act as a top career strategist. Provide a concise target job description and key ATS keywords for the role '{role}' at the company '{company}'.\n"
                f"Include key skills, technologies, core competencies, and corporate values expected by {company}.\n"
                f"Format as bullet points under: Key Requirements, Technical Stack, and Core Competencies."
            )
            response = model.generate_content(prompt)
            if response and response.text:
                return response.text.strip()
        except Exception:
            pass

    return (
        f"🎯 Target Company ({company}) & Role ({role}) Alignment Insights:\n\n"
        f"• {known_info}\n"
        f"• Expected Technical Stack: Python, Cloud Systems, SQL, API Integration, Data Structures.\n"
        f"• Expected Soft Skills: Problem Solving, Team Collaboration, Analytical Thinking, Leadership."
    )


def show_personalization():
    """Renders Screen 5 – Personalization supporting both fresh creation and PDF/TXT upload."""
    render_navbar()

    theme_mode = st.session_state.get("theme_mode", "dark")
    is_dark = (theme_mode == "dark")

    # Mode Check & Switcher
    curr_choice = st.session_state.get("resume_type_choice", "Personalized Resume")
    if curr_choice == "General Resume":
        st.session_state["resume_type_choice"] = "Personalized Resume"

    col1, col2, col3 = st.columns([1, 2.8, 1])

    with col2:
        c_pers_hdr, c_pers_sw = st.columns([3, 1.2])
        with c_pers_hdr:
            render_html(
                f"""
                <div style='text-align: left; margin-bottom: 20px;'>
                    <h1 style='color: {"#60A5FA" if is_dark else "#1E3A8A"}; font-size: 2.1rem; font-weight: 700; margin: 0 0 6px 0;'>🎯 Target Job Personalization</h1>
                    <p style='color: {"#94A3B8" if is_dark else "#64748B"}; font-size: 0.98rem; margin: 0;'>Provide target job role & company parameters for maximum ATS keyword match.</p>
                </div>
                """
            )
        with c_pers_sw:
            st.write("")
            if st.button("🔄 Switch to General", key="btn_pers_switch_gen", use_container_width=True):
                st.session_state["resume_type_choice"] = "General Resume"
                st.session_state["home_step"] = 3
                st.session_state["current_page"] = "home"
                st.rerun()

        if "resume_data" not in st.session_state or not st.session_state["resume_data"]:
            st.session_state["resume_data"] = SAMPLE_RESUME_DATA.copy()

        resume = st.session_state["resume_data"]
        job_target = resume.setdefault("job_target", {})

        target_role = st.text_input(
            "Target Job Role / Title *",
            value=job_target.get("job_title", ""),
            placeholder="e.g. Senior Software Engineer / Data Scientist / AI Developer",
            key="pers_role_input"
        )

        target_company = st.text_input(
            "Target Company Name",
            value=job_target.get("company_name", ""),
            placeholder="e.g. Google / Microsoft / Amazon / Deloitte",
            key="pers_company_input"
        )

        # AI Company Resources Generator Button
        if st.button("🌐 Fetch AI Company & Target Role Keywords", use_container_width=True, key="btn_fetch_insights"):
            if not target_role:
                st.warning("Please enter a Target Job Role first!")
            else:
                api_key = get_api_key()
                with st.spinner("Fetching company intelligence & target ATS keywords..."):
                    insights = _generate_company_insights(
                        target_company if target_company else "Top Tech Enterprise",
                        target_role,
                        api_key=api_key
                    )
                    job_target["job_description"] = insights
                    st.success("🎉 Target company & role insights generated below!")

        job_desc = st.text_area(
            "Job Description & Target ATS Keywords",
            value=job_target.get("job_description", ""),
            height=160,
            placeholder="Paste job posting details or click the button above to auto-generate target company keywords...",
            key="pers_desc_textarea"
        )

        st.write("")
        st.divider()

        # ---------------------------------------------------------
        # UPLOAD EXISTING RESUME (PDF/TXT) OPTION IN PERSONALIZATION
        # ---------------------------------------------------------
        render_html(
            f"""
            <div style='background: {"#1E293B" if is_dark else "#F0FDF4"}; border: 1.5px solid {"#16A34A" if is_dark else "#BBF7D0"}; border-radius: 12px; padding: 18px; margin-bottom: 15px;'>
                <h4 style='color: {"#4ADE80" if is_dark else "#15803D"}; margin: 0 0 6px 0;'>📄 Upload Existing Resume PDF/TXT for Target Tailoring</h4>
                <p style='color: {"#CBD5E1" if is_dark else "#334155"}; font-size: 0.88rem; margin: 0;'>Optional: Upload your current resume file to parse details while applying target job parameters.</p>
            </div>
            """
        )

        uploaded_pers_pdf = st.file_uploader("Upload Existing Resume File (PDF/TXT):", type=["pdf", "txt"], key="pers_pdf_upload")
        if uploaded_pers_pdf is not None:
            file_bytes = uploaded_pers_pdf.read()
            if uploaded_pers_pdf.name.endswith(".pdf"):
                extracted_text = extract_text_from_pdf(file_bytes)
            else:
                extracted_text = file_bytes.decode("utf-8", errors="ignore")

            if extracted_text:
                parsed_data = parse_resume_content(extracted_text)
                parsed_data["job_target"] = {
                    "job_title": target_role.strip() if target_role.strip() else "Software Developer",
                    "company_name": target_company.strip(),
                    "job_description": job_desc.strip(),
                    "personalized_mode": True
                }
                st.session_state["resume_data"] = parsed_data
                st.session_state["pers_resume_parsed"] = True
                st.success("🎉 Existing resume uploaded & target parameters applied!")

        if st.session_state.get("pers_resume_parsed"):
            c_p_def, c_p_sel = st.columns(2)
            with c_p_def:
                if st.button("📄 Continue with Default Template", use_container_width=True, key="btn_pers_tpl_default"):
                    st.session_state["selected_template"] = "ats_1"
                    st.session_state["current_page"] = "data_collection"
                    st.rerun()
            with c_p_sel:
                if st.button("🎨 Select New Template", type="primary", use_container_width=True, key="btn_pers_tpl_select"):
                    st.session_state["current_page"] = "template_selection"
                    st.rerun()

        st.write("")
        st.divider()

        # Action Buttons: Back, Skip Personalization, Save & Continue
        c_b, c_sk, c_s = st.columns([1, 1.2, 1.2])

        with c_b:
            if st.button("⬅️ Back", use_container_width=True, key="btn_pers_back"):
                st.session_state["current_page"] = "home"
                st.rerun()

        with c_sk:
            if st.button("⏭️ Skip Personalization", use_container_width=True, key="btn_pers_skip"):
                job_target["job_title"] = job_target.get("job_title", "Software Developer")
                job_target["personalized_mode"] = True
                st.session_state["resume_data"] = resume
                st.session_state["current_page"] = "template_selection"
                st.rerun()

        with c_s:
            if st.button("Save & Continue ➡️", type="primary", use_container_width=True, key="btn_pers_save"):
                job_target["job_title"] = target_role if target_role.strip() else "Software Developer"
                job_target["company_name"] = target_company.strip()
                job_target["job_description"] = job_desc.strip()
                job_target["personalized_mode"] = True
                st.session_state["resume_data"] = resume
                st.session_state["current_page"] = "template_selection"
                st.rerun()
                st.rerun()
