"""
===========================================================
Project     : NextHire AI
File        : resume_generator.py
Author      : Santosh Kolagani

Purpose:
    AI Service for Summary Generation and Bullet Point Enhancement
    (Supports Gemini API with Rule-Based Offline Fallback).
===========================================================
"""

import json
import random
import google.generativeai as genai
from app.services.prompts.resume_prompts import (
    SUMMARY_PROMPT_TEMPLATE,
    BULLET_IMPROVER_PROMPT_TEMPLATE
)
from app.config.constants import ACTION_VERBS


def _fallback_summary(full_name: str, target_role: str, skills_str: str) -> str:
    """Generates a professional fallback summary when API key is unavailable."""
    role = target_role if target_role else "Software & Data Engineering Professional"
    skills = skills_str if skills_str else "Python, Data Analysis, and Modern Software Frameworks"
    
    return (
        f"Results-driven and detail-oriented {role} with strong expertise in {skills}. "
        f"Demonstrated ability to design, build, and optimize scalable solutions with clean architecture and modern development standards. "
        f"Eager to contribute technical skills, analytical problem-solving, and innovative ideas to deliver high-impact results."
    )


def _fallback_enhance_bullet(bullet: str) -> str:
    """Enhances a bullet point with action verbs and metrics fallback."""
    if not bullet.strip():
        return bullet
        
    words = bullet.strip().split()
    first_word = words[0].capitalize()
    
    # If doesn't start with strong verb, pick one
    if first_word not in ACTION_VERBS:
        verb = random.choice(ACTION_VERBS[:10])
        bullet = f"{verb} {bullet[0].lower()}{bullet[1:]}"
        
    # Append impact metric if missing numbers
    if not any(char.isdigit() for char in bullet):
        metric_additions = [
            ", improving processing efficiency by 25%.",
            ", reducing average execution time by 30%.",
            ", ensuring 99.9% uptime and reliable performance.",
            ", increasing user engagement metrics by 20%."
        ]
        bullet = bullet.rstrip(".") + random.choice(metric_additions)
        
    return bullet


def generate_summary(personal_info: dict, job_target: dict, skills_list: list, api_key: str = "") -> str:
    """
    Generates an AI-crafted professional summary using Gemini API or fallback engine.
    """
    full_name = personal_info.get("full_name", "Professional")
    target_role = job_target.get("job_title", "Software Professional")
    target_company = job_target.get("company_name", "Leading Enterprise")
    job_desc = job_target.get("job_description", "")
    
    skills_flat = []
    for cat in skills_list:
        if isinstance(cat, dict):
            skills_flat.extend(cat.get("skills", []))
        elif hasattr(cat, "skills"):
            skills_flat.extend(cat.skills)
    skills_str = ", ".join(skills_flat[:8])

    if not api_key:
        return _fallback_summary(full_name, target_role, skills_str)

    try:
        genai.configure(api_key=api_key)
        model = genai.GenerativeModel("gemini-1.5-flash")
        
        prompt = SUMMARY_PROMPT_TEMPLATE.format(
            full_name=full_name,
            target_role=target_role,
            target_company=target_company,
            skills=skills_str,
            highlights=f"Background in {skills_str}",
            job_description=job_desc if job_desc else "Standard industry expectations"
        )
        
        response = model.generate_content(prompt)
        if response and response.text:
            return response.text.strip()
    except Exception as e:
        print(f"[AI Generator Warning] Fallback used due to Gemini API call: {e}")

    return _fallback_summary(full_name, target_role, skills_str)


def enhance_bullet_point(bullet: str, context: str = "", job_keywords: str = "", api_key: str = "") -> dict:
    """
    Enhances a single bullet point using Gemini API or fallback engine.
    """
    if not api_key:
        enhanced = _fallback_enhance_bullet(bullet)
        return {
            "enhanced_bullet": enhanced,
            "action_verb_used": enhanced.split()[0] if enhanced else "",
            "improvement_reason": "Optimized with action verb and quantitative impact metric."
        }

    try:
        genai.configure(api_key=api_key)
        model = genai.GenerativeModel("gemini-1.5-flash")
        
        prompt = BULLET_IMPROVER_PROMPT_TEMPLATE.format(
            original_bullet=bullet,
            context=context,
            job_keywords=job_keywords
        )
        
        response = model.generate_content(prompt)
        if response and response.text:
            text = response.text.strip()
            # Clean json block formatting if returned
            if text.startswith("```json"):
                text = text[7:]
            if text.endswith("```"):
                text = text[:-3]
            res_json = json.loads(text)
            return res_json
    except Exception as e:
        print(f"[Bullet Enhancer Warning] Fallback used: {e}")

    enhanced = _fallback_enhance_bullet(bullet)
    return {
        "enhanced_bullet": enhanced,
        "action_verb_used": enhanced.split()[0] if enhanced else "",
        "improvement_reason": "Enhanced with action verb and performance metric."
    }
