"""
===========================================================
Project     : NextHire AI
File        : resume_parser.py
Author      : Santosh Kolagani

Purpose:
    Overleaf-style Resume Import & Parser Engine for PDF/TXT/JSON resumes.
===========================================================
"""

import re
import json
import io


def extract_text_from_pdf(file_bytes: bytes) -> str:
    """Extracts raw text from PDF file bytes using pypdf."""
    try:
        import pypdf
        reader = pypdf.PdfReader(io.BytesIO(file_bytes))
        text_lines = []
        for page in reader.pages:
            t = page.extract_text()
            if t:
                text_lines.append(t)
        return "\n".join(text_lines)
    except Exception as e:
        print(f"[Resume Parser Warning] pypdf extraction error: {e}")
        return ""


def parse_resume_content(text: str) -> dict:
    """
    Parses raw resume text into structured ResumeData dictionary.
    """
    lines = [line.strip() for line in text.split("\n") if line.strip()]
    full_text = "\n".join(lines)

    # 1. Extract Contact Info
    email_match = re.search(r'[\w\.-]+@[\w\.-]+\.\w+', full_text)
    phone_match = re.search(r'(\+?\d{1,3}[-.\s]?)?\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}', full_text)
    linkedin_match = re.search(r'linkedin\.com/in/[\w-]+', full_text, re.IGNORECASE)
    github_match = re.search(r'github\.com/[\w-]+', full_text, re.IGNORECASE)

    email = email_match.group(0) if email_match else ""
    phone = phone_match.group(0) if phone_match else ""
    linkedin = linkedin_match.group(0) if linkedin_match else ""
    github = github_match.group(0) if github_match else ""

    # Name is typically the first prominent line
    name = lines[0] if lines else "Candidate Name"
    if "@" in name or "http" in name:
        name = "Candidate Profile"

    # 2. Extract Sections
    summary = ""
    skills = []
    experience = []
    education = []
    projects = []

    # Section Headers Detection
    section_chunks = re.split(r'\n(?=[A-Z\s]{4,20}\n)', full_text)

    for chunk in section_chunks:
        chunk_lines = [l for l in chunk.split("\n") if l]
        if not chunk_lines:
            continue

        header = chunk_lines[0].upper()

        if "SUMMARY" in header or "PROFILE" in header or "OBJECTIVE" in header:
            summary = " ".join(chunk_lines[1:])
        elif "SKILL" in header:
            skill_text = " ".join(chunk_lines[1:])
            # Split by commas or bullets
            raw_skills = re.split(r'[,|•·\n]', skill_text)
            clean_skills = [s.strip() for s in raw_skills if len(s.strip()) > 1]
            if clean_skills:
                skills.append({
                    "category_name": "Technical & Industry Skills",
                    "skills": clean_skills[:12]
                })
        elif "EXPERIENCE" in header or "WORK" in header or "EMPLOYMENT" in header:
            exp_bullets = [l.strip("•-· ") for l in chunk_lines[1:] if len(l.strip()) > 5]
            experience.append({
                "job_title": chunk_lines[1] if len(chunk_lines) > 1 else "Professional Role",
                "company": "Organization",
                "start_date": "2022",
                "end_date": "Present",
                "bullet_points": exp_bullets[:4] if exp_bullets else ["Led key initiatives and project deliverables."]
            })
        elif "EDUCATION" in header or "ACADEMIC" in header:
            education.append({
                "degree": chunk_lines[1] if len(chunk_lines) > 1 else "Degree",
                "institution": chunk_lines[2] if len(chunk_lines) > 2 else "University",
                "start_year": "2020",
                "end_year": "2024",
                "grade": ""
            })
        elif "PROJECT" in header:
            proj_bullets = [l.strip("•-· ") for l in chunk_lines[1:] if len(l.strip()) > 5]
            projects.append({
                "title": chunk_lines[1] if len(chunk_lines) > 1 else "Key Project",
                "technologies": "Python, SQL, APIs",
                "description": "Project developed to optimize workflows.",
                "bullet_points": proj_bullets[:3] if proj_bullets else ["Architected solution for core system."]
            })

    # Default fallbacks if empty
    if not summary:
        summary = full_text[:250].replace("\n", " ")
    if not skills:
        skills = [{"category_name": "Core Skills", "skills": ["Python", "Data Analysis", "Project Management", "Git"]}]
    if not education:
        education = [{"degree": "Bachelor of Technology", "institution": "University / College", "start_year": "2020", "end_year": "2024"}]
    if not experience:
        experience = [{
            "job_title": "Software Engineer / Professional",
            "company": "Technology Solutions",
            "start_date": "2023",
            "end_date": "Present",
            "bullet_points": ["Executed technical deliverables and collaborated with cross-functional teams."]
        }]

    return {
        "personal_info": {
            "full_name": name,
            "email": email,
            "phone": phone,
            "location": "Location",
            "linkedin": linkedin,
            "github": github,
            "portfolio": "",
            "summary": summary
        },
        "education": education,
        "experience": experience,
        "projects": projects if projects else [{
            "title": "NextHire AI Implementation",
            "technologies": "Python, Streamlit",
            "description": "AI-powered resume optimization application.",
            "bullet_points": ["Designed modular system architecture and user-centric workflow."]
        }],
        "skills": skills,
        "certifications": [],
        "job_target": {
            "job_title": "Target Role",
            "company_name": "Target Company",
            "job_description": "Target job description for ATS tailoring."
        }
    }
