"""
===========================================================
Project     : NextHire AI
File        : data_collection.py
Author      : Santosh Kolagani

Purpose:
    Screen 6 – Resume Workspace: Clean, organized workspace with full flexibility to remove
    any or all Education, Experience, Projects, Skills, and Certification items.
===========================================================
"""

import streamlit as st
from app.components.navbar import render_navbar
from app.config.constants import SAMPLE_RESUME_DATA
from app.services.generator.resume_generator import generate_summary
from app.services.parser.resume_parser import extract_text_from_pdf, parse_resume_content
from app.config.settings import get_api_key
from app.utils.helpers import render_html


def _get_resume():
    if "resume_data" not in st.session_state or not st.session_state["resume_data"]:
        st.session_state["resume_data"] = SAMPLE_RESUME_DATA.copy()
    return st.session_state["resume_data"]


def show_data_collection():
    """Renders Screen 6 – Resume Workspace with full item removal flexibility."""
    render_navbar()

    render_html(
        """
        <div style='text-align: center; margin-bottom: 20px;'>
            <h1 style='color: #1E3A8A; font-size: 2.2rem; font-weight: 700;'>Resume Workspace</h1>
            <p style='color: #64748B; font-size: 1.05rem;'>Fill out or edit your details. You can add or remove any section items to suit your experience background.</p>
        </div>
        """
    )

    # ---------------------------------------------------------
    # NEXTHIRE SMART FEATURE: Import Existing Resume (PDF/TXT)
    # ---------------------------------------------------------
    with st.expander("⚡ NextHire Smart Feature: Import Existing Resume (PDF / TXT)", expanded=False):
        c_up, c_btn = st.columns([3, 1])
        with c_up:
            uploaded_file = st.file_uploader(
                "Upload existing resume to auto-fill sections:",
                type=["pdf", "txt"],
                key="workspace_resume_upload"
            )
        with c_btn:
            st.write("")
            st.write("")
            if uploaded_file is not None:
                if st.button("🚀 Parse & Fill", type="primary", use_container_width=True):
                    with st.spinner("Extracting content..."):
                        file_bytes = uploaded_file.read()
                        if uploaded_file.name.endswith(".pdf"):
                            extracted_text = extract_text_from_pdf(file_bytes)
                        else:
                            extracted_text = file_bytes.decode("utf-8", errors="ignore")

                        if extracted_text:
                            parsed_data = parse_resume_content(extracted_text)
                            st.session_state["resume_data"] = parsed_data
                            st.success("🎉 Resume parsed successfully into workspace!")
                            st.rerun()

    resume = _get_resume()
    personal = resume.setdefault("personal_info", {})
    education = resume.setdefault("education", [])
    experience = resume.setdefault("experience", [])
    projects = resume.setdefault("projects", [])
    skills = resume.setdefault("skills", [])
    certs = resume.setdefault("certifications", [])
    job_target = resume.setdefault("job_target", {})

    st.markdown("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")

    # ---------------------------------------------------------
    # SECTION 1: Personal Details
    # ---------------------------------------------------------
    with st.expander("👤 Personal Details", expanded=True):
        c1, c2 = st.columns(2)
        with c1:
            personal["full_name"] = st.text_input("Full Name *", value=personal.get("full_name", ""), key="ws_name")
            personal["email"] = st.text_input("Email Address *", value=personal.get("email", ""), key="ws_email")
            personal["phone"] = st.text_input("Phone Number *", value=personal.get("phone", ""), key="ws_phone")
        with c2:
            personal["location"] = st.text_input("Location (City, State/Country)", value=personal.get("location", ""), key="ws_loc")
            personal["linkedin"] = st.text_input("LinkedIn Profile URL", value=personal.get("linkedin", ""), key="ws_link")
            personal["portfolio"] = st.text_input("GitHub / Portfolio URL", value=personal.get("portfolio", ""), key="ws_port")

    # ---------------------------------------------------------
    # SECTION 2: Education (Fully Removable)
    # ---------------------------------------------------------
    with st.expander("🎓 Education", expanded=False):
        if not education:
            st.info("ℹ️ No education entries added yet. (Click '➕ Add Education' below to add one)")
        else:
            for idx, edu in enumerate(education):
                c_hdr, c_rem = st.columns([3, 1])
                with c_hdr:
                    st.markdown(f"#### Education #{idx+1}")
                with c_rem:
                    if st.button("🗑️ Remove Education", key=f"btn_rem_edu_{idx}", use_container_width=True):
                        education.pop(idx)
                        st.rerun()

                e1, e2 = st.columns(2)
                with e1:
                    edu["degree"] = st.text_input(f"Degree / Qualification #{idx+1}", value=edu.get("degree", ""), key=f"ws_edu_deg_{idx}")
                    edu["field_of_study"] = st.text_input(f"Field of Study / Major #{idx+1}", value=edu.get("field_of_study", ""), key=f"ws_edu_f_{idx}")
                    edu["institution"] = st.text_input(f"College / University #{idx+1}", value=edu.get("institution", ""), key=f"ws_edu_i_{idx}")
                with e2:
                    edu["start_year"] = st.text_input(f"Start Year #{idx+1}", value=edu.get("start_year", ""), key=f"ws_edu_sy_{idx}")
                    edu["end_year"] = st.text_input(f"End Year #{idx+1}", value=edu.get("end_year", ""), key=f"ws_edu_ey_{idx}")
                    edu["grade"] = st.text_input(f"GPA / Grade #{idx+1}", value=edu.get("grade", ""), key=f"ws_edu_g_{idx}")
                st.divider()

        st.write("")
        if st.button("➕ Add Education", key="btn_add_edu"):
            education.append({"degree": "", "field_of_study": "", "institution": "", "start_year": "", "end_year": "", "grade": ""})
            st.rerun()

    # ---------------------------------------------------------
    # SECTION 3: Skills (Fully Removable)
    # ---------------------------------------------------------
    with st.expander("💡 Skills", expanded=False):
        if not skills:
            st.info("ℹ️ No skill categories added yet. (Click '➕ Add Skill Category' below to add one)")
        else:
            for idx, sk in enumerate(skills):
                s1, s2, s3 = st.columns([1.5, 2.5, 1])
                with s1:
                    sk["category_name"] = st.text_input(f"Skill Category #{idx+1}", value=sk.get("category_name", ""), key=f"ws_sk_cat_{idx}")
                with s2:
                    sk_str = ", ".join(sk.get("skills", []))
                    new_sk_str = st.text_input(f"Skills (Comma separated) #{idx+1}", value=sk_str, key=f"ws_sk_val_{idx}")
                    sk["skills"] = [item.strip() for item in new_sk_str.split(",") if item.strip()]
                with s3:
                    st.write("")
                    st.write("")
                    if st.button("🗑️ Remove", key=f"btn_rem_sk_{idx}", use_container_width=True):
                        skills.pop(idx)
                        st.rerun()

        st.write("")
        if st.button("➕ Add Skill Category", key="btn_add_sk"):
            skills.append({"category_name": "", "skills": []})
            st.rerun()

    # ---------------------------------------------------------
    # SECTION 4: Projects (Fully Removable)
    # ---------------------------------------------------------
    with st.expander("🚀 Projects", expanded=False):
        if not projects:
            st.info("ℹ️ No project entries added yet. (Click '➕ Add Project' below to add one)")
        else:
            for idx, proj in enumerate(projects):
                p_hdr, p_rem = st.columns([3, 1])
                with p_hdr:
                    st.markdown(f"#### Project #{idx+1}: {proj.get('title', 'New Project')}")
                with p_rem:
                    if st.button("🗑️ Remove Project", key=f"btn_rem_proj_{idx}", use_container_width=True):
                        projects.pop(idx)
                        st.rerun()

                proj["title"] = st.text_input(f"Project Title #{idx+1}", value=proj.get("title", ""), key=f"ws_proj_t_{idx}")
                proj["description"] = st.text_area(f"Description #{idx+1}", value=proj.get("description", ""), height=80, key=f"ws_proj_d_{idx}")
                proj["technologies"] = st.text_input(f"Technologies Used #{idx+1}", value=proj.get("technologies", ""), key=f"ws_proj_tech_{idx}")
                proj["achievement"] = st.text_input(f"Key Achievement (Optional) #{idx+1}", value=proj.get("achievement", ""), key=f"ws_proj_ach_{idx}")

                st.divider()

        st.write("")
        if st.button("➕ Add Project", key="btn_add_proj", type="secondary"):
            projects.append({
                "title": "",
                "description": "",
                "technologies": "",
                "achievement": "",
                "bullet_points": []
            })
            st.rerun()

    # ---------------------------------------------------------
    # SECTION 5: Experience (Fully Removable - Optional for Freshers / Students)
    # ---------------------------------------------------------
    with st.expander("💼 Experience (Optional)", expanded=False):
        if not experience:
            st.info("ℹ️ No work experience entries added. (Freshers & Students can skip this section)")
        else:
            for idx, exp in enumerate(experience):
                x_hdr, x_rem = st.columns([3, 1])
                with x_hdr:
                    st.markdown(f"#### Role #{idx+1}: {exp.get('job_title', 'Job Title')}")
                with x_rem:
                    if st.button("🗑️ Remove Experience", key=f"btn_rem_exp_{idx}", use_container_width=True):
                        experience.pop(idx)
                        st.rerun()

                x1, x2 = st.columns(2)
                with x1:
                    exp["job_title"] = st.text_input(f"Job Title #{idx+1}", value=exp.get("job_title", ""), key=f"ws_exp_t_{idx}")
                    exp["company"] = st.text_input(f"Company #{idx+1}", value=exp.get("company", ""), key=f"ws_exp_c_{idx}")
                with x2:
                    exp["start_date"] = st.text_input(f"Start Date #{idx+1}", value=exp.get("start_date", ""), key=f"ws_exp_sd_{idx}")
                    exp["end_date"] = st.text_input(f"End Date #{idx+1}", value=exp.get("end_date", ""), key=f"ws_exp_ed_{idx}")

                bullets = exp.get("bullet_points", [""])
                b_text = "\n".join(bullets)
                new_b_text = st.text_area(f"Key Accomplishments (One per line) #{idx+1}", value=b_text, height=100, key=f"ws_exp_b_{idx}")
                exp["bullet_points"] = [line.strip() for line in new_b_text.split("\n") if line.strip()]
                st.divider()

        st.write("")
        if st.button("➕ Add Experience", key="btn_add_exp"):
            experience.append({"job_title": "", "company": "", "location": "", "start_date": "", "end_date": "", "bullet_points": [""]})
            st.rerun()

    # ---------------------------------------------------------
    # SECTION 6: Certifications (Fully Removable)
    # ---------------------------------------------------------
    with st.expander("📜 Certifications (Optional)", expanded=False):
        if not certs:
            st.info("ℹ️ No certifications added. (Optional section)")
        else:
            for idx, c in enumerate(certs):
                c1, c2, c3, c4 = st.columns([2, 2, 2, 1])
                with c1:
                    c["name"] = st.text_input(f"Certificate Name #{idx+1}", value=c.get("name", ""), key=f"ws_cert_n_{idx}")
                with c2:
                    c["issuing_organization"] = st.text_input(f"Issuer #{idx+1}", value=c.get("issuing_organization", ""), key=f"ws_cert_i_{idx}")
                with c3:
                    c["issue_date"] = st.text_input(f"Issue Date / Year #{idx+1}", value=c.get("issue_date", ""), key=f"ws_cert_d_{idx}")
                with c4:
                    st.write("")
                    st.write("")
                    if st.button("🗑️ Remove", key=f"btn_rem_cert_{idx}", use_container_width=True):
                        certs.pop(idx)
                        st.rerun()

        st.write("")
        if st.button("➕ Add Certification", key="btn_add_cert"):
            certs.append({"name": "", "issuing_organization": "", "issue_date": ""})
            st.rerun()

    # ---------------------------------------------------------
    # SECTION 7: Career Goal
    # ---------------------------------------------------------
    with st.expander("🎯 Career Goal", expanded=False):
        summary_val = st.text_area(
            "Professional Summary / Career Objective",
            value=personal.get("summary", ""),
            height=120,
            key="ws_summary_input"
        )
        personal["summary"] = summary_val

        if st.button("✨ AI Generate Career Goal Summary", type="primary", key="btn_ai_gen_summary"):
            api_key = get_api_key()
            with st.spinner("Generating summary..."):
                gen_summary = generate_summary(personal, job_target, skills, api_key=api_key)
                personal["summary"] = gen_summary
                st.success("Generated!")
                st.rerun()

    st.markdown("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    st.write("")

    # Sequential Back & Continue Navigation
    col_l, col_r = st.columns([1, 1])
    with col_l:
        if st.button("⬅️ Back to Template", use_container_width=True, key="btn_ws_back"):
            st.session_state["current_page"] = "template_selection"
            st.rerun()
    with col_r:
        if st.button("Continue to Review ➡️", type="primary", use_container_width=True, key="btn_ws_continue"):
            st.session_state["resume_data"] = resume
            st.session_state["current_page"] = "review"
            st.rerun()
