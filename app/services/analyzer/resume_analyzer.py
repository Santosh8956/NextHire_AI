"""
===========================================================
Project     : NextHire AI
File        : resume_analyzer.py
Author      : Santosh Kolagani

Purpose:
    ATS Resume Strength Evaluation Engine & Actionable Redirection Generator.
===========================================================
"""

import json
import re
from app.config.constants import ACTION_VERBS


def analyze_resume_strength(resume_dict: dict, api_key: str = "") -> dict:
    """
    Evaluates resume ATS strength and generates structured improvement items
    with direct redirection metadata.
    """
    personal = resume_dict.get("personal_info", {})
    summary = personal.get("summary", "")
    exp_list = resume_dict.get("experience", [])
    proj_list = resume_dict.get("projects", [])
    skills_list = resume_dict.get("skills", [])
    job_target = resume_dict.get("job_target", {})
    job_desc = job_target.get("job_description", "")

    strengths = []
    structured_improvements = []
    missing_keywords = []

    # Base scores
    ats_score = 75
    quality_score = 70
    format_score = 80

    # 1. Check Contact Info
    has_email = bool(personal.get("email"))
    has_phone = bool(personal.get("phone"))
    has_linkedin = bool(personal.get("linkedin"))
    has_github = bool(personal.get("github"))

    if has_email and has_phone:
        ats_score += 10
        strengths.append("Complete contact details provided (Name, Email, Phone).")
    else:
        structured_improvements.append({
            "id": "contact_info",
            "issue": "Missing vital contact details (Email or Phone)",
            "recommendation": "Provide valid email and phone number in your header.",
            "category": "Personal Info",
            "target_page": "data_collection",
            "editor_focus": "personal",
            "button_label": "✏️ Fix Contact Info"
        })

    if not (has_linkedin or has_github):
        structured_improvements.append({
            "id": "online_profiles",
            "issue": "Missing LinkedIn or GitHub profile links",
            "recommendation": "Add your LinkedIn or GitHub portfolio URL to boost recruiter responses by 40%.",
            "category": "Online Presence",
            "target_page": "data_collection",
            "editor_focus": "personal",
            "button_label": "🌐 Add Online Profiles"
        })

    # 2. Check Professional Summary
    if summary and len(summary.split()) >= 25:
        quality_score += 10
        strengths.append("Well-crafted professional summary.")
    else:
        structured_improvements.append({
            "id": "summary_length",
            "issue": "Professional summary is too short or missing",
            "recommendation": "Craft a 3-4 sentence professional summary highlighting target role skills.",
            "category": "Professional Summary",
            "target_page": "resume_editor",
            "editor_focus": "summary",
            "button_label": "📝 Generate AI Summary"
        })

    # 3. Check Bullet Points (Action Verbs & Metrics)
    all_exp_bullets = []
    for exp in exp_list:
        all_exp_bullets.extend(exp.get("bullet_points", []))

    all_proj_bullets = []
    for proj in proj_list:
        all_proj_bullets.extend(proj.get("bullet_points", []))

    all_bullets = all_exp_bullets + all_proj_bullets

    strong_verb_count = 0
    metric_count = 0

    for b in all_bullets:
        words = b.strip().split()
        if words and words[0].capitalize() in ACTION_VERBS:
            strong_verb_count += 1
        if any(char.isdigit() for char in b):
            metric_count += 1

    if strong_verb_count >= 3:
        quality_score += 10
        strengths.append(f"Strong action verbs detected in {strong_verb_count} bullet points.")
    else:
        structured_improvements.append({
            "id": "action_verbs",
            "issue": "Bullet points lack strong initial action verbs",
            "recommendation": "Start bullet points with impactful verbs like 'Architected', 'Spearheaded', 'Optimized'.",
            "category": "Work Experience",
            "target_page": "resume_editor",
            "editor_focus": "experience",
            "button_label": "💼 Enhance Experience Bullets"
        })

    if metric_count >= 2:
        quality_score += 10
        strengths.append(f"Quantifiable metrics present in {metric_count} project/experience bullets.")
    else:
        structured_improvements.append({
            "id": "project_metrics",
            "issue": "Add more project & experience metric details (%, $, scale)",
            "recommendation": "Include quantifiable results (e.g. 'improved efficiency by 30%', 'scaled to 10k users').",
            "category": "Key Projects",
            "target_page": "resume_editor",
            "editor_focus": "projects",
            "button_label": "🚀 Add Project Metrics"
        })

    # 4. Job Description Keyword Matching
    if job_desc:
        jd_words = set(re.findall(r'\b[A-Za-z]{3,15}\b', job_desc.lower()))
        resume_text = json.dumps(resume_dict).lower()
        target_keywords = {"python", "sql", "aws", "docker", "machine learning", "api", "git", "nlp", "pandas", "tableau", "react", "agile"}
        jd_tech_keywords = target_keywords.intersection(jd_words)

        for kw in jd_tech_keywords:
            if kw not in resume_text:
                missing_keywords.append(kw.capitalize())

        if missing_keywords:
            structured_improvements.append({
                "id": "missing_keywords",
                "issue": f"Missing key job terms: {', '.join(missing_keywords[:4])}",
                "recommendation": "Incorporate missing target keywords into your technical skills or project descriptions.",
                "category": "ATS Keywords",
                "target_page": "data_collection",
                "editor_focus": "job_tailoring",
                "button_label": "🎯 Tailor ATS Keywords"
            })
        else:
            ats_score += 10
            strengths.append("High ATS keyword alignment with target job description.")
    else:
        structured_improvements.append({
            "id": "target_job",
            "issue": "No target job description specified for ATS tailoring",
            "recommendation": "Paste a target job posting to get custom ATS keyword scoring and optimization.",
            "category": "Job Alignment",
            "target_page": "data_collection",
            "editor_focus": "job_tailoring",
            "button_label": "🎯 Paste Target Job Description"
        })

    # Ensure score caps
    ats_score = min(100, ats_score)
    quality_score = min(100, quality_score)
    format_score = min(100, format_score)
    overall_score = int((ats_score * 0.4) + (quality_score * 0.4) + (format_score * 0.2))

    return {
        "overall_score": overall_score,
        "ats_compatibility_score": ats_score,
        "content_quality_score": quality_score,
        "formatting_score": format_score,
        "strengths": strengths,
        "improvements": structured_improvements,
        "missing_keywords": missing_keywords,
        "actionable_suggestions": [imp["recommendation"] for imp in structured_improvements]
    }
