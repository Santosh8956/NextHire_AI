"""
===========================================================
Project     : NextHire AI
File        : data_collection.py
Author      : Santosh Kolagani

Purpose:
    Interactive Multi-Tab Data Collection Form with NextHire Smart Feature
    Existing Resume Import (PDF/TXT) and Profile Editing.
===========================================================
"""

import streamlit as st
from app.components.navbar import render_navbar
from app.config.constants import SAMPLE_RESUME_DATA
from app.services.generator.resume_generator import generate_summary
from app.services.parser.resume_parser import extract_text_from_pdf, parse_resume_content
from app.config.settings import get_api_key


def _get_resume():
    if "resume_data" not in st.session_state or not st.session_state["resume_data"]:
        st.session_state["resume_data"] = SAMPLE_RESUME_DATA.copy()
    return st.session_state["resume_data"]


def show_data_collection():
    """Renders data collection form with NextHire Smart Feature resume upload & 5 structured tabs."""
    render_navbar()

    st.markdown("## 📝 Step 1: Candidate Profile & Existing Resume Editor")
    st.caption("Upload your existing resume (PDF/TXT) to auto-extract details, or fill out/edit your career profile manually.")

    # ---------------------------------------------------------
    # NEXTHIRE SMART FEATURE: Import & Edit Existing Resume
    # ---------------------------------------------------------
    with st.expander("⚡ NextHire Smart Feature: Upload & Import Existing Resume (PDF / TXT)", expanded=True):
        c_up, c_btn = st.columns([3, 1])
        with c_up:
            uploaded_file = st.file_uploader(
                "Drag & drop your existing resume file here:",
                type=["pdf", "txt"],
                help="Supported formats: PDF, TXT. Automatically extracts contact info, summary, experience, education, and skills."
            )
        with c_btn:
            st.write("")
            st.write("")
            if uploaded_file is not None:
                if st.button("🚀 Parse & Edit Resume", type="primary", use_container_width=True):
                    with st.spinner("Extracting resume content..."):
                        file_bytes = uploaded_file.read()
                        if uploaded_file.name.endswith(".pdf"):
                            extracted_text = extract_text_from_pdf(file_bytes)
                        else:
                            extracted_text = file_bytes.decode("utf-8", errors="ignore")

                        if extracted_text:
                            parsed_data = parse_resume_content(extracted_text)
                            st.session_state["resume_data"] = parsed_data
                            st.success("🎉 Existing resume parsed successfully! Profile updated below.")
                            st.rerun()
                        else:
                            st.error("Could not extract text from uploaded file. Please verify file content.")

    st.divider()

    resume = _get_resume()
    personal = resume.setdefault("personal_info", {})
    education = resume.setdefault("education", [])
    experience = resume.setdefault("experience", [])
    projects = resume.setdefault("projects", [])
    skills = resume.setdefault("skills", [])
    certs = resume.setdefault("certifications", [])
    job_target = resume.setdefault("job_target", {})

    tab1, tab2, tab3, tab4, tab5 = st.tabs([
        "👤 Personal Info",
        "🎓 Education",
        "💼 Experience",
        "🚀 Projects & Skills",
        "🎯 Job Tailoring & Certs"
    ])

    # ---------------------------------------------------------
    # TAB 1: Personal Info
    # ---------------------------------------------------------
    with tab1:
        st.subheader("Personal & Contact Details")
        c1, c2 = st.columns(2)
        with c1:
            personal["full_name"] = st.text_input("Full Name *", value=personal.get("full_name", ""))
            personal["email"] = st.text_input("Email Address *", value=personal.get("email", ""))
            personal["phone"] = st.text_input("Phone Number *", value=personal.get("phone", ""))
            personal["location"] = st.text_input("Location (City, State/Country)", value=personal.get("location", ""))
        with c2:
            personal["linkedin"] = st.text_input("LinkedIn Profile URL", value=personal.get("linkedin", ""))
            personal["github"] = st.text_input("GitHub / Portfolio URL", value=personal.get("github", ""))
            personal["portfolio"] = st.text_input("Personal Website", value=personal.get("portfolio", ""))

        st.subheader("Professional Summary")
        summary_val = st.text_area("Summary Statement", value=personal.get("summary", ""), height=100, help="Brief overview of your qualifications and goals.")
        personal["summary"] = summary_val

        col_sum1, col_sum2 = st.columns([2, 1])
        with col_sum2:
            if st.button("✨ AI Generate Summary", type="primary", use_container_width=True):
                api_key = get_api_key()
                with st.spinner("Crafting AI Professional Summary..."):
                    generated = generate_summary(personal, job_target, skills, api_key=api_key)
                    personal["summary"] = generated
                    st.success("Summary generated successfully!")
                    st.rerun()

    # ---------------------------------------------------------
    # TAB 2: Education
    # ---------------------------------------------------------
    with tab2:
        st.subheader("Education History")
        if not education:
            education.append({"degree": "", "field_of_study": "", "institution": "", "start_year": "", "end_year": "", "grade": ""})

        for idx, edu in enumerate(education):
            with st.expander(f"Education #{idx+1}: {edu.get('degree', 'New Degree')}", expanded=True):
                e1, e2 = st.columns(2)
                with e1:
                    edu["degree"] = st.text_input(f"Degree / Qualification #{idx+1}", value=edu.get("degree", ""), key=f"edu_deg_{idx}")
                    edu["field_of_study"] = st.text_input(f"Field of Study / Branch #{idx+1}", value=edu.get("field_of_study", ""), key=f"edu_f_{idx}")
                    edu["institution"] = st.text_input(f"College / University #{idx+1}", value=edu.get("institution", ""), key=f"edu_i_{idx}")
                with e2:
                    edu["start_year"] = st.text_input(f"Start Year #{idx+1}", value=edu.get("start_year", ""), key=f"edu_sy_{idx}")
                    edu["end_year"] = st.text_input(f"End Year #{idx+1}", value=edu.get("end_year", ""), key=f"edu_ey_{idx}")
                    edu["grade"] = st.text_input(f"GPA / Percentage #{idx+1}", value=edu.get("grade", ""), key=f"edu_g_{idx}")

        c_add, c_rem = st.columns([1, 1])
        with c_add:
            if st.button("➕ Add Another Education"):
                education.append({"degree": "", "field_of_study": "", "institution": "", "start_year": "", "end_year": "", "grade": ""})
                st.rerun()

    # ---------------------------------------------------------
    # TAB 3: Experience
    # ---------------------------------------------------------
    with tab3:
        st.subheader("Work & Internship Experience")
        if not experience:
            experience.append({"job_title": "", "company": "", "location": "", "start_date": "", "end_date": "", "bullet_points": [""]})

        for idx, exp in enumerate(experience):
            with st.expander(f"Experience #{idx+1}: {exp.get('job_title', 'Role')} at {exp.get('company', 'Company')}", expanded=True):
                x1, x2 = st.columns(2)
                with x1:
                    exp["job_title"] = st.text_input(f"Job Title / Role #{idx+1}", value=exp.get("job_title", ""), key=f"exp_t_{idx}")
                    exp["company"] = st.text_input(f"Company / Organization #{idx+1}", value=exp.get("company", ""), key=f"exp_c_{idx}")
                with x2:
                    exp["start_date"] = st.text_input(f"Start Date #{idx+1}", value=exp.get("start_date", ""), key=f"exp_sd_{idx}")
                    exp["end_date"] = st.text_input(f"End Date #{idx+1}", value=exp.get("end_date", ""), key=f"exp_ed_{idx}")

                bullets = exp.get("bullet_points", [""])
                b_text = "\n".join(bullets)
                new_b_text = st.text_area(f"Key Accomplishments (One per line) #{idx+1}", value=b_text, height=100, key=f"exp_b_{idx}")
                exp["bullet_points"] = [line.strip() for line in new_b_text.split("\n") if line.strip()]

        if st.button("➕ Add Work Experience"):
            experience.append({"job_title": "", "company": "", "location": "", "start_date": "", "end_date": "", "bullet_points": [""]})
            st.rerun()

    # ---------------------------------------------------------
    # TAB 4: Projects & Skills
    # ---------------------------------------------------------
    with tab4:
        st.subheader("Featured Projects")
        if not projects:
            projects.append({"title": "", "technologies": "", "description": "", "bullet_points": [""]})

        for idx, proj in enumerate(projects):
            with st.expander(f"Project #{idx+1}: {proj.get('title', 'Project Title')}", expanded=True):
                p1, p2 = st.columns(2)
                with p1:
                    proj["title"] = st.text_input(f"Project Title #{idx+1}", value=proj.get("title", ""), key=f"proj_t_{idx}")
                    proj["technologies"] = st.text_input(f"Tech Stack #{idx+1}", value=proj.get("technologies", ""), key=f"proj_tech_{idx}")
                with p2:
                    proj["description"] = st.text_input(f"Short Description #{idx+1}", value=proj.get("description", ""), key=f"proj_d_{idx}")

                bullets = proj.get("bullet_points", [""])
                b_text = "\n".join(bullets)
                new_b_text = st.text_area(f"Project Highlights (One per line) #{idx+1}", value=b_text, height=100, key=f"proj_b_{idx}")
                proj["bullet_points"] = [line.strip() for line in new_b_text.split("\n") if line.strip()]

        if st.button("➕ Add Project"):
            projects.append({"title": "", "technologies": "", "description": "", "bullet_points": [""]})
            st.rerun()

        st.divider()
        st.subheader("Technical & Soft Skills")
        if not skills:
            skills.extend([
                {"category_name": "Programming Languages", "skills": ["Python", "SQL", "JavaScript"]},
                {"category_name": "Frameworks & Tools", "skills": ["Streamlit", "Git", "REST APIs"]}
            ])

        for idx, sk in enumerate(skills):
            s1, s2 = st.columns([1, 2])
            with s1:
                sk["category_name"] = st.text_input(f"Category #{idx+1}", value=sk.get("category_name", ""), key=f"sk_cat_{idx}")
            with s2:
                sk_str = ", ".join(sk.get("skills", []))
                new_sk_str = st.text_input(f"Skills (Comma separated) #{idx+1}", value=sk_str, key=f"sk_val_{idx}")
                sk["skills"] = [item.strip() for item in new_sk_str.split(",") if item.strip()]

    # ---------------------------------------------------------
    # TAB 5: Job Tailoring & Certifications
    # ---------------------------------------------------------
    with tab5:
        st.subheader("Job Application Details (For AI Personalization)")
        job_target["job_title"] = st.text_input("Target Job Title", value=job_target.get("job_title", ""), placeholder="e.g. Data Scientist / Software Engineer")
        job_target["company_name"] = st.text_input("Target Company Name", value=job_target.get("company_name", ""), placeholder="e.g. Google / Microsoft")
        job_target["job_description"] = st.text_area("Target Job Description (Paste here)", value=job_target.get("job_description", ""), height=150, help="Paste job posting text here for ATS optimization.")

        st.divider()
        st.subheader("Certifications & Achievements")
        if not certs:
            certs.append({"name": "", "issuing_organization": "", "issue_date": ""})

        for idx, c in enumerate(certs):
            c1, c2, c3 = st.columns(3)
            with c1:
                c["name"] = st.text_input(f"Certificate Name #{idx+1}", value=c.get("name", ""), key=f"cert_n_{idx}")
            with c2:
                c["issuing_organization"] = st.text_input(f"Issuer #{idx+1}", value=c.get("issuing_organization", ""), key=f"cert_i_{idx}")
            with c3:
                c["issue_date"] = st.text_input(f"Year / Date #{idx+1}", value=c.get("issue_date", ""), key=f"cert_d_{idx}")

    st.write("")
    st.divider()

    # Next step footer action
    col_l, col_r = st.columns([3, 1])
    with col_r:
        if st.button("Proceed to Template Selection ➡️", type="primary", use_container_width=True):
            st.session_state["resume_data"] = resume
            st.session_state["current_page"] = "template_selection"
            st.rerun()
