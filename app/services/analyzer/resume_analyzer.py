"""
===========================================================
Project     : NextHire AI
File        : resume_analyzer.py
Author      : Santosh Kolagani

Purpose:
    High-Accuracy ATS Resume Strength Evaluation Engine & Dynamic NLP Keyword Matcher.
===========================================================
"""

import json
import re
from app.config.constants import ACTION_VERBS

# Comprehensive Master Skill Catalog for Domain & Technical Matching
MASTER_SKILL_CATALOG = {
    # Tech & Software
    "python", "sql", "javascript", "typescript", "java", "c++", "c#", "golang", "ruby", "php",
    "html", "css", "react", "angular", "vue", "node.js", "express", "django", "flask", "fastapi",
    "spring boot", "git", "github", "docker", "kubernetes", "aws", "azure", "gcp", "ci/cd",
    "devops", "microservices", "rest api", "graphql", "postgresql", "mysql", "mongodb", "redis",
    
    # AI & Data Science
    "machine learning", "deep learning", "artificial intelligence", "nlp", "natural language processing",
    "computer vision", "tensorflow", "pytorch", "scikit-learn", "pandas", "numpy", "data analysis",
    "data engineering", "data visualization", "tableau", "power bi", "big data", "spark", "hadoop",
    "llm", "gemini", "prompt engineering", "neural networks", "predictive modeling",

    # Business & Domain
    "project management", "agile", "scrum", "jira", "product management", "business analysis",
    "stakeholder management", "strategic planning", "cross-functional", "leadership", "communication",
    "problem solving", "customer success", "salesforce", "seo", "content marketing",
    "financial modeling", "accounting", "compliance", "risk management", "operations", "kpis"
}

STOP_WORDS = {
    "and", "the", "for", "with", "that", "this", "from", "you", "your", "have", "are",
    "will", "can", "all", "our", "work", "team", "years", "role", "job", "ability",
    "experience", "skills", "knowledge", "required", "responsible", "working", "must",
    "strong", "using", "used", "etc", "such", "well", "good", "great", "high", "new",
    "building", "seeking", "looking", "candidate", "position", "company", "opportunity",
    "about", "across", "after", "again", "also", "been", "before", "being", "between",
    "both", "came", "come", "could", "each", "even", "every", "first", "into", "just",
    "like", "make", "many", "more", "most", "much", "must", "over", "same", "some",
    "than", "then", "them", "these", "they", "time", "very", "want", "were", "what",
    "when", "where", "which", "while", "who", "whom", "why", "would"
}


def extract_job_keywords(job_desc: str, job_title: str = "") -> set:
    """
    Dynamically extracts relevant technical, domain, and skill keywords (1-gram to 3-gram)
    from a target job description or job title.
    """
    extracted = set()
    text_clean = job_desc.lower() if job_desc else job_title.lower()

    if not text_clean.strip():
        return extracted

    # 1. Match against Master Skill Catalog
    for skill in MASTER_SKILL_CATALOG:
        if re.search(r'\b' + re.escape(skill) + r'\b', text_clean):
            extracted.add(skill)

    # 2. Extract capitalized/technical n-grams dynamically from raw text
    words = re.findall(r'\b[a-zA-Z0-9\+\#\.\-]{2,20}\b', text_clean)
    filtered_words = [w for w in words if w not in STOP_WORDS and not w.isdigit()]

    for w in filtered_words:
        if len(w) >= 3 and w not in STOP_WORDS:
            extracted.add(w)

    return extracted


def analyze_resume_strength(resume_dict: dict, api_key: str = "") -> dict:
    """
    Evaluates resume ATS strength with ground-up accuracy based on candidate data,
    dynamic job description keyword coverage, content quality, and format compliance.
    """
    personal = resume_dict.get("personal_info", {})
    summary = personal.get("summary", "").strip()
    exp_list = resume_dict.get("experience", [])
    proj_list = resume_dict.get("projects", [])
    skills_list = resume_dict.get("skills", [])
    education_list = resume_dict.get("education", [])
    job_target = resume_dict.get("job_target", {})
    job_desc = job_target.get("job_description", "").strip()
    job_title = job_target.get("job_title", "").strip()

    strengths = []
    structured_improvements = []

    # Flatten candidate text for keyword searching
    resume_full_text = json.dumps(resume_dict).lower()

    # ---------------------------------------------------------
    # 1. GROUND-UP ATS KEYWORD SCORE (40% Weight)
    # ---------------------------------------------------------
    target_keywords = extract_job_keywords(job_desc, job_title)
    matched_keywords = []
    missing_keywords = []

    if target_keywords:
        for kw in sorted(target_keywords):
            if re.search(r'\b' + re.escape(kw) + r'\b', resume_full_text):
                matched_keywords.append(kw.title())
            else:
                missing_keywords.append(kw.title())

        match_ratio = len(matched_keywords) / max(1, len(target_keywords))
        ats_score = int(match_ratio * 100)

        if match_ratio >= 0.70:
            strengths.append(f"High ATS Keyword Match: {len(matched_keywords)} / {len(target_keywords)} key target terms identified.")
        elif match_ratio >= 0.40:
            strengths.append(f"Moderate ATS Keyword Match ({len(matched_keywords)} terms matched).")
        else:
            structured_improvements.append({
                "id": "ats_keywords",
                "issue": f"Low ATS Keyword Alignment ({len(matched_keywords)} / {len(target_keywords)} matched)",
                "recommendation": f"Incorporate missing target terms like {', '.join(missing_keywords[:4])} into your skills or projects.",
                "category": "ATS Keywords",
                "target_page": "data_collection",
                "editor_focus": "job_tailoring",
                "button_label": "🎯 Tailor ATS Keywords"
            })
    else:
        # Fallback if no Job Description or Target Role was specified
        num_skills = len(skills_list)
        if num_skills >= 8:
            ats_score = 85
            strengths.append(f"Robust skills inventory with {num_skills} listed skills.")
        elif num_skills >= 4:
            ats_score = 65
            strengths.append(f"Solid foundational skills list ({num_skills} skills).")
        elif num_skills > 0:
            ats_score = 45
            structured_improvements.append({
                "id": "skills_count",
                "issue": "Skills list is brief (only " + str(num_skills) + " skills)",
                "recommendation": "Add 4+ domain or technical skills to improve ATS keyword scanning.",
                "category": "Skills",
                "target_page": "data_collection",
                "editor_focus": "skills",
                "button_label": "💡 Add More Skills"
            })
        else:
            ats_score = 25
            structured_improvements.append({
                "id": "skills_missing",
                "issue": "No technical or core skills listed",
                "recommendation": "Add relevant hard & soft skills to enable ATS parser indexing.",
                "category": "Skills",
                "target_page": "data_collection",
                "editor_focus": "skills",
                "button_label": "💡 Add Skills List"
            })

        structured_improvements.append({
            "id": "target_job",
            "issue": "No target job description specified for precision ATS tailoring",
            "recommendation": "Paste a target job description in the Details Workspace to get exact ATS keyword matching.",
            "category": "Job Alignment",
            "target_page": "data_collection",
            "editor_focus": "job_tailoring",
            "button_label": "🎯 Paste Job Description"
        })

    # ---------------------------------------------------------
    # 2. GROUND-UP CONTENT QUALITY SCORE (30% Weight)
    # ---------------------------------------------------------
    header_pts = 0
    if personal.get("full_name"):
        header_pts += 5
    if personal.get("email"):
        header_pts += 5
    if personal.get("phone"):
        header_pts += 5
    if personal.get("location") or personal.get("linkedin") or personal.get("github"):
        header_pts += 5

    if header_pts == 20:
        strengths.append("Complete header contact details provided (Name, Email, Phone, Location/Links).")
    else:
        structured_improvements.append({
            "id": "contact_info",
            "issue": "Header contact details incomplete",
            "recommendation": "Provide email, phone number, and location in your contact header.",
            "category": "Personal Info",
            "target_page": "data_collection",
            "editor_focus": "personal",
            "button_label": "✏️ Fix Contact Info"
        })

    summary_words = len(summary.split()) if summary else 0
    summary_pts = 0
    if summary_words >= 25:
        summary_pts = 20
        strengths.append("Well-structured professional summary (25+ words).")
    elif summary_words >= 15:
        summary_pts = 10
    else:
        structured_improvements.append({
            "id": "summary_length",
            "issue": "Professional summary is missing or brief",
            "recommendation": "Write a 3-4 sentence professional summary highlighting your career achievements.",
            "category": "Professional Summary",
            "target_page": "resume_editor",
            "editor_focus": "summary",
            "button_label": "📝 Generate AI Summary"
        })

    # Experience & Bullets Evaluation
    all_bullets = []
    for exp in exp_list:
        all_bullets.extend(exp.get("bullet_points", []))
    for proj in proj_list:
        all_bullets.extend(proj.get("bullet_points", []))

    exp_pts = 0
    if exp_list:
        exp_pts += 10

    strong_verb_count = 0
    metric_count = 0

    for b in all_bullets:
        b_clean = b.strip()
        words = b_clean.split()
        if words and words[0].capitalize() in ACTION_VERBS:
            strong_verb_count += 1
        if re.search(r'\d+%|\$\d+|\b\d+\b|\d+k|\d+x', b_clean, re.IGNORECASE):
            metric_count += 1

    if strong_verb_count >= 3:
        exp_pts += 15
        strengths.append(f"Impactful action verbs present in {strong_verb_count} bullet points.")
    elif strong_verb_count > 0:
        exp_pts += 8
    else:
        structured_improvements.append({
            "id": "action_verbs",
            "issue": "Bullets lack initial action verbs",
            "recommendation": "Start work experience bullets with action verbs like 'Spearheaded', 'Architected', 'Optimized'.",
            "category": "Work Experience",
            "target_page": "resume_editor",
            "editor_focus": "experience",
            "button_label": "💼 Enhance Bullets"
        })

    if metric_count >= 2:
        exp_pts += 10
        strengths.append(f"Quantifiable metrics present in {metric_count} experience/project bullets.")
    elif metric_count == 1:
        exp_pts += 5
    else:
        structured_improvements.append({
            "id": "project_metrics",
            "issue": "Missing quantifiable metrics (%, $, numbers, multipliers)",
            "recommendation": "Add quantifiable achievements (e.g., 'improved query speed by 35%', 'managed $50k budget').",
            "category": "Work Impact",
            "target_page": "resume_editor",
            "editor_focus": "projects",
            "button_label": "🚀 Add Quantifiable Metrics"
        })

    proj_pts = 15 if proj_list else 0
    if not proj_list:
        structured_improvements.append({
            "id": "projects_section",
            "issue": "No key projects listed",
            "recommendation": "Add 1-2 featured projects to demonstrate technical hands-on capability.",
            "category": "Projects",
            "target_page": "data_collection",
            "editor_focus": "projects",
            "button_label": "🛠️ Add Key Projects"
        })

    edu_pts = 10 if education_list else 0
    if not education_list:
        structured_improvements.append({
            "id": "education_section",
            "issue": "No education background provided",
            "recommendation": "Specify degree title, institution, and completion year.",
            "category": "Education",
            "target_page": "data_collection",
            "editor_focus": "education",
            "button_label": "🎓 Add Education"
        })

    quality_score = min(100, header_pts + summary_pts + exp_pts + proj_pts + edu_pts)

    # ---------------------------------------------------------
    # 3. GROUND-UP ATS FORMAT & STRUCTURE COMPLIANCE (30% Weight)
    # ---------------------------------------------------------
    section_pts = 0
    if personal.get("full_name"):
        section_pts += 10
    if summary:
        section_pts += 10
    if exp_list:
        section_pts += 10
    if education_list:
        section_pts += 10
    if skills_list:
        section_pts += 10

    total_bullets = len(all_bullets)
    if 3 <= total_bullets <= 18:
        bullet_pts = 30
        strengths.append(f"Optimal ATS bullet point density ({total_bullets} bullets).")
    elif total_bullets > 0:
        bullet_pts = 15
    else:
        bullet_pts = 0

    font_pts = 20  # NextHire templates use ATS-compliant Helvetica, Times-Roman, Courier

    format_score = min(100, section_pts + bullet_pts + font_pts)

    # ---------------------------------------------------------
    # 4. COMPOSITE OVERALL SCORE & BOUNDS
    # ---------------------------------------------------------
    overall_score = int(round((ats_score * 0.40) + (quality_score * 0.30) + (format_score * 0.30)))

    # Ensure bounds [0, 100]
    ats_score = max(0, min(100, ats_score))
    quality_score = max(0, min(100, quality_score))
    format_score = max(0, min(100, format_score))
    overall_score = max(0, min(100, overall_score))

    return {
        "overall_score": overall_score,
        "ats_compatibility_score": ats_score,
        "content_quality_score": quality_score,
        "formatting_score": format_score,
        "strengths": strengths,
        "improvements": structured_improvements,
        "matched_keywords": matched_keywords,
        "missing_keywords": missing_keywords,
        "actionable_suggestions": [imp["recommendation"] for imp in structured_improvements]
    }

