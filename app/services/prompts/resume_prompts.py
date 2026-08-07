"""
===========================================================
Project     : NextHire AI
File        : resume_prompts.py
Author      : Santosh Kolagani

Purpose:
    System and user prompts for Gemini AI resume generation.
===========================================================
"""

SUMMARY_PROMPT_TEMPLATE = """
You are an expert ATS Resume Specialist and Career Coach.
Generate a compelling 3-4 sentence professional summary based on the following candidate profile.

Candidate Profile:
- Name: {full_name}
- Target Role: {target_role}
- Target Company: {target_company}
- Key Skills: {skills}
- Career Experience/Education Highlights: {highlights}
- Job Description Context: {job_description}

Guidelines:
1. Use strong action-oriented, professional language.
2. Incorporate key industry keywords relevant to {target_role}.
3. Highlight metrics, strengths, and candidate potential.
4. Do NOT use first-person pronouns like "I" or "My". Use direct professional tone.
5. Return ONLY the final professional summary text without markdown labels or commentary.
"""

BULLET_IMPROVER_PROMPT_TEMPLATE = """
You are an ATS Resume Optimizer. Enhance the following resume bullet point to make it more impactful, quantifiable, and ATS-friendly.

Original Bullet Point:
"{original_bullet}"

Context (Role/Project):
"{context}"

Job Description Keywords to include if relevant:
"{job_keywords}"

Instructions:
1. Start with a powerful action verb (e.g., Architected, Engineered, Spearheaded, Optimized).
2. Include quantifiable outcomes or percentage metrics where logical (estimate realistic metrics if none present).
3. Align keywords with ATS standards.
4. Return ONLY a JSON object with this exact structure:
{{
    "enhanced_bullet": "The newly enhanced bullet point text...",
    "action_verb_used": "Action verb used",
    "improvement_reason": "Brief 1-sentence explanation of what changed"
}}
"""

RESUME_ANALYSIS_PROMPT_TEMPLATE = """
You are a Senior Technical Recruiter and ATS Evaluation Engine.
Analyze the following resume against the target job role and description.

Candidate Resume Data:
{resume_text}

Target Job Role: {target_role}
Target Job Description:
{job_description}

Perform a rigorous evaluation and return a JSON object with exact keys:
{{
    "overall_score": 85,
    "ats_compatibility_score": 88,
    "content_quality_score": 82,
    "formatting_score": 85,
    "strengths": [
        "Strong use of quantifiable action verbs in project descriptions.",
        "Clear alignment with core python and data science requirements."
    ],
    "improvements": [
        "Missing explicitly required keyword: 'Docker'",
        "Experience section lacks measurable business impact metrics."
    ],
    "missing_keywords": [
        "Docker", "AWS", "Kubernetes"
    ],
    "actionable_suggestions": [
        "Add a certification or project demonstrating containerization skills.",
        "Quantify project achievements with specific percentages or scale."
    ]
}}
Ensure overall_score is between 0 and 100 based on realistic ATS standards. Return valid JSON ONLY.
"""
