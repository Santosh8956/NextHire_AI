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
from app.config.constants import SAMPLE_RESUME_DATA
from app.config.settings import get_api_key
from app.utils.helpers import render_html
import google.generativeai as genai


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
    """Renders Screen 5 – Personalization redirecting directly to Template Gallery."""
    render_navbar()

    # Guard check: If General Resume was selected, skip automatically to workspace
    if st.session_state.get("resume_type_choice") == "General Resume":
        st.session_state["current_page"] = "data_collection"
        st.rerun()

    col1, col2, col3 = st.columns([1, 2.8, 1])

    with col2:
        render_html(
            """
            <div style='text-align: center; margin-bottom: 25px;'>
                <h1 style='color: #1E3A8A; font-size: 2.2rem; font-weight: 700;'>🎯 Target Job Personalization</h1>
                <p style='color: #64748B; font-size: 1.05rem;'>Provide your target job role & company details. AI will customize keywords and bullet points using company intelligence.</p>
            </div>
            """
        )

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
            height=180,
            placeholder="Paste job posting details or click the button above to auto-generate target company keywords...",
            key="pers_desc_textarea"
        )

        st.write("")
        st.divider()

        # Action Buttons: Back, Skip Personalization, Save & Continue
        c_b, c_sk, c_s = st.columns([1, 1.2, 1.2])

        with c_b:
            if st.button("⬅️ Back", use_container_width=True, key="btn_pers_back"):
                st.session_state["current_page"] = "home"
                st.rerun()

        with c_sk:
            # REQUIREMENT: Skip button redirects directly to Template Gallery
            if st.button("⏭️ Skip Personalization", use_container_width=True, key="btn_pers_skip"):
                job_target["job_title"] = job_target.get("job_title", "Software Developer")
                st.session_state["resume_data"] = resume
                st.session_state["current_page"] = "template_selection"
                st.rerun()

        with c_s:
            # REQUIREMENT: Save & Continue redirects directly to Template Gallery
            if st.button("Save & Continue ➡️", type="primary", use_container_width=True, key="btn_pers_save"):
                job_target["job_title"] = target_role if target_role.strip() else "Software Developer"
                job_target["company_name"] = target_company.strip()
                job_target["job_description"] = job_desc.strip()
                st.session_state["resume_data"] = resume
                st.session_state["current_page"] = "template_selection"
                st.rerun()
