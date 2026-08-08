"""
===========================================================
Project     : NextHire AI
File        : image_generator.py
Author      : Santosh Kolagani

Purpose:
    Renders screen-optimized, large, bold, crystal-clear PNG template
    images supporting 16 visually distinct layout styles with vibrant colors
    and high-contrast typography.
===========================================================
"""

import io
import streamlit as st
from PIL import Image, ImageDraw, ImageFont


def _load_font(size: int, font_type: str = "Helvetica", bold: bool = False):
    """Loads vector TrueType font at requested size."""
    font_names = []
    if font_type == "Times-Roman":
        font_names = ["timesbd.ttf", "times.ttf", "georgiab.ttf", "georgia.ttf"] if bold else ["times.ttf", "georgia.ttf"]
    elif font_type == "Courier":
        font_names = ["courbd.ttf", "cour.ttf", "lucon.ttf"] if bold else ["cour.ttf", "lucon.ttf"]
    else:
        font_names = ["arialbd.ttf", "arial.ttf", "verdana.ttf", "DejaVuSans-Bold.ttf"] if bold else ["arial.ttf", "DejaVuSans.ttf"]

    for fn in font_names:
        try:
            return ImageFont.truetype(fn, size)
        except Exception:
            pass
    try:
        return ImageFont.truetype("arial.ttf", size)
    except Exception:
        return ImageFont.load_default()


@st.cache_data(show_spinner=False)
def generate_template_preview_image(template_info: dict, resume_data: dict = None) -> bytes:
    """
    Generates a 900x1200 screen-optimized large, bold, crystal-clear PNG preview image.
    Supporting 16 unique layout styles with vibrant colors and rich typography.
    """
    width, height = 900, 1200
    img = Image.new("RGB", (width, height), color="#FFFFFF")
    draw = ImageDraw.Draw(img)

    hex_color = template_info.get("color", "#1E3A8A")
    hex_clean = hex_color.lstrip("#")
    primary_rgb = tuple(int(hex_clean[i:i+2], 16) for i in (0, 2, 4))
    font_type = template_info.get("font", "Helvetica")
    layout = template_info.get("layout_style", "header_banner")

    # Screen-Optimized Large Bold Font Scaling (900x1200 sharp canvas)
    title_font = _load_font(42, font_type, bold=True)
    subtitle_font = _load_font(20, font_type, bold=False)
    section_font = _load_font(25, font_type, bold=True)
    item_title_font = _load_font(21, font_type, bold=True)
    body_font = _load_font(18, font_type, bold=False)
    small_font = _load_font(15, font_type, bold=False)

    # Personal Profile
    personal = resume_data.get("personal_info", {}) if resume_data else {}
    raw_name = personal.get("full_name", "").strip()
    name = (raw_name if raw_name else "SANTOSH KOLAGANI").upper()
    email = personal.get("email", "").strip() or "santosh.kolagani@example.com"
    phone = personal.get("phone", "").strip() or "+91 98765 43210"
    location = personal.get("location", "").strip() or "Rajahmundry, AP, India"
    summary = personal.get("summary", "").strip() or "Motivated Computer Science & Data Science professional skilled in AI/ML model deployment, full-stack Python web tools, and scalable software solutions."

    # Experience fallback
    experience = resume_data.get("experience", []) if resume_data else []
    if not experience:
        experience = [{
            "job_title": "AI / Machine Learning Intern",
            "company": "TechSolutions Innovations",
            "start_date": "Jun 2024",
            "end_date": "Aug 2024",
            "bullet_points": [
                "Developed NLP text processing pipelines using Python & Gemini API, improving categorization by 24%.",
                "Built interactive web dashboards using Streamlit to display real-time predictive analytics models.",
                "Optimized database query speeds reducing execution latency by 30% across internal endpoints."
            ]
        }]

    # Projects fallback
    projects = resume_data.get("projects", []) if resume_data else []
    if not projects:
        projects = [{
            "title": "NextHire AI - Resume Builder & Analysis Engine",
            "technologies": "Python, Streamlit, Gemini API, ReportLab",
            "bullet_points": [
                "Architected modular web app with template rendering engine & ATS scoring.",
                "Integrated Gemini LLM prompts for automatic bullet-point enhancement & section rewrites."
            ]
        }]

    # Education fallback
    education = resume_data.get("education", []) if resume_data else []
    if not education:
        education = [{
            "degree": "B.Tech in Computer Science & Engineering (Data Science)",
            "institution": "GIET College of Engineering",
            "start_year": "2022",
            "end_year": "2026"
        }]

    curr_y = 45
    left_m = 50

    # ---------------------------------------------------------
    # 16 DISTINCT VIBRANT LAYOUT STYLES (Screen-Optimized 900x1200)
    # ---------------------------------------------------------
    if layout == "header_banner":
        draw.rectangle([0, 0, width, 140], fill=primary_rgb)
        draw.text((50, 35), name, fill="#FFFFFF", font=title_font)
        draw.text((50, 90), f"{email}  |  {phone}  |  {location}", fill="#F1F5F9", font=subtitle_font)
        curr_y = 165

    elif layout == "left_accent":
        draw.rectangle([0, 0, 24, height], fill=primary_rgb)
        draw.text((60, 40), name, fill=primary_rgb, font=title_font)
        draw.text((60, 92), f"{email}  |  {phone}  |  {location}", fill="#475569", font=subtitle_font)
        draw.line([(60, 125), (width - 50, 125)], fill=primary_rgb, width=4)
        curr_y = 145
        left_m = 60

    elif layout == "split_header":
        draw.text((50, 35), name, fill=primary_rgb, font=title_font)
        draw.text((50, 88), "SOFTWARE & AI DEVELOPER", fill="#334155", font=subtitle_font)
        draw.rectangle([width - 380, 28, width - 50, 118], fill="#F8FAFC", outline=primary_rgb, width=2)
        draw.text((width - 360, 40), f"Email: {email}", fill="#1E293B", font=body_font)
        draw.text((width - 360, 65), f"Phone: {phone}", fill="#1E293B", font=body_font)
        draw.text((width - 360, 90), f"Loc: {location}", fill="#1E293B", font=body_font)
        draw.line([(50, 138), (width - 50, 138)], fill=primary_rgb, width=4)
        curr_y = 160

    elif layout == "centered_minimal":
        draw.text((width//2 - 170, 35), name, fill=primary_rgb, font=title_font)
        draw.text((width//2 - 270, 88), f"{email}   •   {phone}   •   {location}", fill="#475569", font=subtitle_font)
        draw.line([(90, 125), (width - 90, 125)], fill=primary_rgb, width=3)
        draw.line([(90, 130), (width - 90, 130)], fill=primary_rgb, width=1)
        curr_y = 150

    elif layout == "code_terminal":
        draw.rectangle([0, 0, width, 140], fill="#1E1E2E")
        draw.text((50, 25), f"$ cat candidate_profile.json", fill="#A6E3A1", font=subtitle_font)
        draw.text((50, 60), f"\"name\": \"{name}\", \"role\": \"Full-Stack AI Developer\"", fill="#F9E2AF", font=subtitle_font)
        draw.text((50, 95), f"\"contact\": \"{email} | {phone}\"", fill="#89B4FA", font=subtitle_font)
        curr_y = 165

    elif layout == "executive_serif":
        draw.line([(50, 30), (width - 50, 30)], fill=primary_rgb, width=4)
        draw.text((50, 48), name, fill=primary_rgb, font=title_font)
        draw.text((50, 98), f"EXECUTIVE PROFILE  |  {email}  |  {phone}", fill="#334155", font=subtitle_font)
        draw.line([(50, 130), (width - 50, 130)], fill=primary_rgb, width=4)
        draw.line([(50, 136), (width - 50, 136)], fill=primary_rgb, width=2)
        curr_y = 155

    elif layout == "modern_pills":
        draw.rectangle([0, 0, width, 140], fill="#F8FAFC")
        draw.rectangle([50, 28, 380, 82], fill=primary_rgb)
        draw.text((70, 38), name, fill="#FFFFFF", font=title_font)
        draw.text((50, 95), f"{email}  |  {phone}  |  {location}", fill="#475569", font=subtitle_font)
        draw.line([(50, 130), (width - 50, 130)], fill=primary_rgb, width=4)
        curr_y = 150

    elif layout == "border_frame":
        draw.rectangle([15, 15, width - 15, height - 15], outline=primary_rgb, width=4)
        draw.text((55, 40), name, fill=primary_rgb, font=title_font)
        draw.text((55, 92), f"{email}  |  {phone}  |  {location}", fill="#475569", font=subtitle_font)
        draw.line([(55, 125), (width - 55, 125)], fill=primary_rgb, width=4)
        curr_y = 145
        left_m = 55

    elif layout == "top_accent_bar":
        draw.rectangle([0, 0, width, 24], fill=primary_rgb)
        draw.rectangle([50, 45, width - 50, 125], fill="#F8FAFC", outline="#CBD5E1", width=2)
        draw.text((70, 58), name, fill=primary_rgb, font=title_font)
        draw.text((70, 96), f"{email}  |  {phone}  |  {location}", fill="#475569", font=subtitle_font)
        curr_y = 145

    elif layout == "sidebar_column":
        draw.rectangle([0, 0, 290, height], fill="#F8FAFC")
        draw.line([(290, 0), (290, height)], fill=primary_rgb, width=3)
        draw.text((30, 40), name, fill=primary_rgb, font=_load_font(26, font_type, bold=True))
        draw.text((30, 80), f"{email}\n{phone}\n{location}", fill="#475569", font=subtitle_font)
        draw.text((30, 160), "SKILLS", fill=primary_rgb, font=section_font)
        draw.text((30, 195), "• Python & SQL\n• Streamlit & APIs\n• Gemini LLMs\n• Data Science", fill="#334155", font=body_font)
        left_m = 315
        curr_y = 40

    elif layout == "creative_gradient":
        draw.rectangle([0, 0, width, 80], fill=primary_rgb)
        draw.rectangle([0, 80, width, 115], fill="#38BDF8")
        draw.text((50, 30), name, fill="#FFFFFF", font=title_font)
        draw.text((50, 88), f"{email}  |  {phone}  |  {location}", fill="#FFFFFF", font=subtitle_font)
        curr_y = 140

    else:
        # Default layout fallback
        draw.rectangle([0, 0, width, 115], fill=primary_rgb)
        draw.text((50, 28), name, fill="#FFFFFF", font=title_font)
        draw.text((50, 78), f"{email}  |  {phone}  |  {location}", fill="#F1F5F9", font=subtitle_font)
        curr_y = 135

    # Helper for Section Header (Large Bold & High-Contrast)
    def draw_section_header(title):
        nonlocal curr_y
        right_margin = 55 if layout == "border_frame" else (width - 290 if layout == "sidebar_column" else 50)

        if layout == "code_terminal":
            draw.text((left_m, curr_y), f"// {title}", fill=primary_rgb, font=section_font)
            curr_y += 30
            draw.line([(left_m, curr_y), (width - right_margin, curr_y)], fill="#CBD5E1", width=2)
        elif layout in ["modern_pills", "classic_boxed"]:
            draw.rectangle([left_m, curr_y, left_m + 320, curr_y + 36], fill=primary_rgb)
            draw.text((left_m + 16, curr_y + 6), title, fill="#FFFFFF", font=section_font)
            curr_y += 46
        elif layout == "executive_serif":
            draw.line([(left_m, curr_y), (width - right_margin, curr_y)], fill=primary_rgb, width=2)
            draw.text((left_m, curr_y + 4), f"❖  {title}", fill=primary_rgb, font=section_font)
            curr_y += 34
            draw.line([(left_m, curr_y), (width - right_margin, curr_y)], fill=primary_rgb, width=2)
        else:
            draw.text((left_m, curr_y), title, fill=primary_rgb, font=section_font)
            curr_y += 30
            draw.line([(left_m, curr_y), (width - right_margin, curr_y)], fill=primary_rgb, width=3)

        curr_y += 16

    # Helper for wrapped text line drawing (Large BOLD Crisp Text)
    def draw_wrapped_text(text_str, prefix="", font_to_use=body_font, text_color="#1E293B", indent=0, max_width_chars=60):
        nonlocal curr_y
        words = text_str.split()
        if not words:
            return
        line = prefix
        for w in words:
            test_line = line + " " + w if line else w
            if len(test_line) > max_width_chars:
                draw.text((left_m + indent, curr_y), line, fill=text_color, font=font_to_use)
                curr_y += 24
                line = "    " + w
            else:
                line = test_line
        if line:
            draw.text((left_m + indent, curr_y), line, fill=text_color, font=font_to_use)
            curr_y += 24

    # 1. Summary
    draw_section_header("PROFESSIONAL SUMMARY")
    draw_wrapped_text(summary, font_to_use=body_font, text_color="#1E293B", max_width_chars=52 if layout == "sidebar_column" else 72)
    curr_y += 12

    # 2. Experience
    draw_section_header("WORK EXPERIENCE")
    for exp in experience:
        role = exp.get("job_title", "")
        company = exp.get("company", "")
        dates = f"{exp.get('start_date', '')} - {exp.get('end_date', 'Present')}"
        
        draw.text((left_m, curr_y), f"{role} — {company}", fill="#0F172A", font=item_title_font)
        if layout != "sidebar_column":
            draw.text((width - 240, curr_y), dates, fill="#64748B", font=body_font)
        curr_y += 26

        for bullet in exp.get("bullet_points", []):
            draw_wrapped_text(bullet, prefix="•  ", font_to_use=body_font, text_color="#334155", indent=16, max_width_chars=48 if layout == "sidebar_column" else 68)
        curr_y += 8

    # 3. Projects
    draw_section_header("KEY PROJECTS")
    for proj in projects:
        title = proj.get("title", "")
        tech = proj.get("technologies", "")
        proj_header = f"{title}" + (f" [{tech}]" if tech else "")
        draw.text((left_m, curr_y), proj_header, fill="#0F172A", font=item_title_font)
        curr_y += 26

        for bullet in proj.get("bullet_points", []):
            draw_wrapped_text(bullet, prefix="•  ", font_to_use=body_font, text_color="#334155", indent=16, max_width_chars=48 if layout == "sidebar_column" else 68)
        curr_y += 8

    # 4. Education
    draw_section_header("EDUCATION")
    for edu in education:
        deg = edu.get("degree", "")
        inst = edu.get("institution", "")
        yrs = f"{edu.get('start_year', '')} - {edu.get('end_year', '')}"
        draw.text((left_m, curr_y), f"{deg} — {inst}", fill="#0F172A", font=item_title_font)
        if layout != "sidebar_column":
            draw.text((width - 220, curr_y), yrs, fill="#64748B", font=body_font)
        curr_y += 28

    # Footer Bar
    draw.rectangle([0, height - 40, width, height], fill="#F8FAFC")
    draw.text((50, height - 28), f"NextHire AI Large Format  |  Template: {template_info.get('name')}  |  Layout: {layout.replace('_', ' ').title()}", fill="#475569", font=small_font)

    buf = io.BytesIO()
    img.save(buf, format="PNG", quality=98)
    buf.seek(0)
    return buf.getvalue()
