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
    Generates a 900x1200 high-resolution, large-font, high-contrast A4 PNG preview.
    Generates a 700x990 high-resolution, large-font, high-contrast A4 PNG preview.
    Guarantees 100% integer coordinate math so Pillow never raises float exceptions.
    """
    def _i(val):
        """Helper to guarantee integer casting for all Pillow coordinates."""
        return int(round(float(val)))

    max_canvas_height = 3600
    width = 600
    img = Image.new("RGB", (width, max_canvas_height), color="#FFFFFF")
    draw = ImageDraw.Draw(img)

    hex_color = template_info.get("color", "#1E3A8A")
    hex_clean = hex_color.lstrip("#")
    try:
        primary_rgb = tuple(int(hex_clean[i:i+2], 16) for i in (0, 2, 4))
    except Exception:
        primary_rgb = (30, 58, 138)

    font_type = template_info.get("font", "Helvetica")
    layout = template_info.get("layout_style", "header_banner")

    # Ultra-Large Typography for Direct 24px+ Browser Screen Visibility (600px Canvas)
    title_font = _load_font(86, font_type, bold=True)
    subtitle_font = _load_font(36, font_type, bold=True)
    section_font = _load_font(60, font_type, bold=True)
    item_title_font = _load_font(48, font_type, bold=True)
    body_font = _load_font(42, font_type, bold=False)
    small_font = _load_font(30, font_type, bold=False)

    # Personal Profile
    personal = resume_data.get("personal_info", {}) if isinstance(resume_data, dict) else {}
    raw_name = personal.get("full_name", "").strip() if isinstance(personal, dict) else ""
    name = (raw_name if raw_name else "SANTOSH KOLAGANI").upper()
    email = (personal.get("email", "").strip() if isinstance(personal, dict) else "") or "santosh.kolagani@example.com"
    phone = (personal.get("phone", "").strip() if isinstance(personal, dict) else "") or "+91 98765 43210"
    location = (personal.get("location", "").strip() if isinstance(personal, dict) else "") or "Rajahmundry, AP, India"
    summary = (personal.get("summary", "").strip() if isinstance(resume_data, dict) else "") or "Motivated Computer Science & Data Science professional skilled in AI/ML model deployment, full-stack Python web tools, and scalable software solutions."

    # Experience fallback
    experience = resume_data.get("experience", []) if isinstance(resume_data, dict) else []
    if not experience or not isinstance(experience, list):
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
    projects = resume_data.get("projects", []) if isinstance(resume_data, dict) else []
    if not projects or not isinstance(projects, list):
        projects = [{
            "title": "NextHire AI - Resume Builder & Analysis Engine",
            "technologies": "Python, Streamlit, Gemini API, ReportLab",
            "bullet_points": [
                "Architected modular web app with template rendering engine & ATS scoring.",
                "Integrated Gemini LLM prompts for automatic bullet-point enhancement & section rewrites."
            ]
        }]

    # Education fallback
    education = resume_data.get("education", []) if isinstance(resume_data, dict) else []
    if not education or not isinstance(education, list):
        education = [{
            "degree": "B.Tech in Computer Science & Engineering (Data Science)",
            "institution": "GIET College of Engineering",
            "start_year": "2022",
            "end_year": "2026"
        }]

    curr_y = 36
    left_m = 36
    right_m = 36

    # ---------------------------------------------------------
    # 16 DISTINCT VIBRANT LAYOUT STYLES (All Coordinates Integer-Casted)
    # ---------------------------------------------------------
    if layout == "header_banner":
        draw.rectangle([0, 0, width, 220], fill=primary_rgb)
        draw.text((_i(36), _i(28)), name, fill="#FFFFFF", font=title_font)
        draw.text((_i(36), _i(140)), f"{email}  |  {phone}  |  {location}", fill="#F1F5F9", font=subtitle_font)
        curr_y = 250

    elif layout == "left_accent":
        draw.rectangle([0, 0, 28, max_canvas_height], fill=primary_rgb)
        draw.text((_i(48), _i(28)), name, fill=primary_rgb, font=title_font)
        draw.text((_i(48), _i(135)), f"{email}  |  {phone}  |  {location}", fill="#334155", font=subtitle_font)
        draw.line([(_i(48), _i(190)), (_i(width - 36), _i(190))], fill=primary_rgb, width=_i(5))
        curr_y = 220
        left_m = 48

    elif layout == "split_header":
        draw.text((_i(36), _i(24)), name, fill=primary_rgb, font=title_font)
        draw.text((_i(36), _i(130)), f"{email}  |  {phone}  |  {location}", fill="#1E293B", font=subtitle_font)
        draw.line([(_i(36), _i(185)), (_i(width - 36), _i(185))], fill=primary_rgb, width=_i(5))
        curr_y = 215

    elif layout == "centered_minimal":
        center_x = _i(width // 2)
        draw.text((_i(center_x - 220), _i(24)), name, fill=primary_rgb, font=title_font)
        draw.text((_i(center_x - 260), _i(130)), f"{email}   •   {phone}", fill="#334155", font=subtitle_font)
        draw.line([(_i(50), _i(185)), (_i(width - 50), _i(185))], fill=primary_rgb, width=_i(4))
        curr_y = 215

    elif layout == "code_terminal":
        draw.rectangle([0, 0, width, 220], fill="#1E1E2E")
        draw.text((_i(36), _i(22)), "$ cat candidate_profile.json", fill="#A6E3A1", font=subtitle_font)
        draw.text((_i(36), _i(80)), f"\"name\": \"{name}\", \"role\": \"AI Developer\"", fill="#F9E2AF", font=subtitle_font)
        draw.text((_i(36), _i(140)), f"\"contact\": \"{email} | {phone}\"", fill="#89B4FA", font=subtitle_font)
        curr_y = 250

    elif layout == "executive_serif":
        draw.line([(_i(36), _i(24)), (_i(width - 36), _i(24))], fill=primary_rgb, width=_i(5))
        draw.text((_i(36), _i(38)), name, fill=primary_rgb, font=title_font)
        draw.text((_i(36), _i(140)), f"EXECUTIVE PROFILE  |  {email}  |  {phone}", fill="#1E293B", font=subtitle_font)
        draw.line([(_i(36), _i(195)), (_i(width - 36), _i(195))], fill=primary_rgb, width=_i(5))
        curr_y = 225

    elif layout == "modern_pills":
        draw.rectangle([0, 0, width, 220], fill="#F8FAFC")
        draw.rectangle([_i(36), _i(24), _i(540), _i(120)], fill=primary_rgb)
        draw.text((_i(50), _i(32)), name, fill="#FFFFFF", font=title_font)
        draw.text((_i(36), _i(145)), f"{email}  |  {phone}  |  {location}", fill="#334155", font=subtitle_font)
        draw.line([(_i(36), _i(195)), (_i(width - 36), _i(195))], fill=primary_rgb, width=_i(5))
        curr_y = 225

    elif layout == "border_frame":
        curr_y = 210
        left_m = 45
        right_m = 45
        draw.text((_i(45), _i(28)), name, fill=primary_rgb, font=title_font)
        draw.text((_i(45), _i(135)), f"{email}  |  {phone}  |  {location}", fill="#334155", font=subtitle_font)
        draw.line([(_i(45), _i(190)), (_i(width - 45), _i(190))], fill=primary_rgb, width=_i(5))

    elif layout == "top_accent_bar":
        draw.rectangle([0, 0, width, 32], fill=primary_rgb)
        draw.rectangle([_i(36), _i(48), _i(width - 36), _i(195)], fill="#F8FAFC", outline="#CBD5E1", width=_i(2))
        draw.text((_i(50), _i(60)), name, fill=primary_rgb, font=title_font)
        draw.text((_i(50), _i(145)), f"{email}  |  {phone}  |  {location}", fill="#334155", font=subtitle_font)
        curr_y = 225

    elif layout == "sidebar_column":
        draw.rectangle([0, 0, 240, max_canvas_height], fill="#F8FAFC")
        draw.line([(_i(240), 0), (_i(240), max_canvas_height)], fill=primary_rgb, width=_i(5))
        draw.text((_i(16), _i(24)), name, fill=primary_rgb, font=_load_font(42, font_type, bold=True))
        draw.text((_i(16), _i(120)), f"{email}\n{phone}\n{location}", fill="#334155", font=subtitle_font)
        draw.text((_i(16), _i(280)), "SKILLS", fill=primary_rgb, font=section_font)
        draw.text((_i(16), _i(360)), "• Python & SQL\n• Streamlit & APIs\n• Gemini LLMs\n• Data Science", fill="#0F172A", font=body_font)
        left_m = 260
        right_m = 20
        curr_y = 28

    elif layout == "creative_gradient":
        draw.rectangle([0, 0, width, 120], fill=primary_rgb)
        draw.rectangle([0, 120, width, 185], fill="#38BDF8")
        draw.text((_i(36), _i(24)), name, fill="#FFFFFF", font=title_font)
        draw.text((_i(36), _i(135)), f"{email}  |  {phone}  |  {location}", fill="#FFFFFF", font=subtitle_font)
        curr_y = 215

    else:
        # Default layout fallback
        draw.rectangle([0, 0, width, 210], fill=primary_rgb)
        draw.text((_i(36), _i(24)), name, fill="#FFFFFF", font=title_font)
        draw.text((_i(36), _i(135)), f"{email}  |  {phone}  |  {location}", fill="#F1F5F9", font=subtitle_font)
        curr_y = 230

    # Helper for Section Header (Clean & Proportional)
    def draw_section_header(title):
        nonlocal curr_y
        line_right = _i(width - right_m)

        if layout == "code_terminal":
            draw.text((_i(left_m), _i(curr_y)), f"// {title}", fill=primary_rgb, font=section_font)
            curr_y += 66
            draw.line([(_i(left_m), _i(curr_y)), (line_right, _i(curr_y))], fill="#CBD5E1", width=_i(3))
        elif layout in ["modern_pills", "classic_boxed"]:
            draw.rectangle([_i(left_m), _i(curr_y), _i(left_m + 500), _i(curr_y + 72)], fill=primary_rgb)
            draw.text((_i(left_m + 20), _i(curr_y + 6)), title, fill="#FFFFFF", font=section_font)
            curr_y += 84
        elif layout == "executive_serif":
            draw.line([(_i(left_m), _i(curr_y)), (line_right, _i(curr_y))], fill=primary_rgb, width=_i(3))
            draw.text((_i(left_m), _i(curr_y + 8)), f"❖  {title}", fill=primary_rgb, font=section_font)
            curr_y += 70
            draw.line([(_i(left_m), _i(curr_y)), (line_right, _i(curr_y))], fill=primary_rgb, width=_i(3))
        else:
            draw.text((_i(left_m), _i(curr_y)), title, fill=primary_rgb, font=section_font)
            curr_y += 66
            draw.line([(_i(left_m), _i(curr_y)), (line_right, _i(curr_y))], fill=primary_rgb, width=_i(4))

        curr_y += 24

    # Helper for wrapped text line drawing (Enlarged High-Contrast Text)
    def draw_wrapped_text(text_str, prefix="", font_to_use=body_font, text_color="#0F172A", indent=0, max_width_chars=24):
        nonlocal curr_y
        words = text_str.split()
        if not words:
            return
        line = prefix
        for w in words:
            test_line = line + " " + w if line else w
            if len(test_line) > max_width_chars:
                draw.text((_i(left_m + indent), _i(curr_y)), line, fill=text_color, font=font_to_use)
                curr_y += 54
                line = "    " + w
            else:
                line = test_line
        if line:
            draw.text((_i(left_m + indent), _i(curr_y)), line, fill=text_color, font=font_to_use)
            curr_y += 54

    # 1. Summary
    draw_section_header("PROFESSIONAL SUMMARY")
    draw_wrapped_text(summary, font_to_use=body_font, text_color="#0F172A", max_width_chars=14 if layout == "sidebar_column" else 24)
    curr_y += 20

    # 2. Experience
    draw_section_header("WORK EXPERIENCE")
    for exp in experience:
        if not isinstance(exp, dict):
            continue
        role = exp.get("job_title", "")
        company = exp.get("company", "")
        dates = f"{exp.get('start_date', '')} - {exp.get('end_date', 'Present')}"

        draw.text((_i(left_m), _i(curr_y)), f"{role}", fill="#0F172A", font=item_title_font)
        curr_y += 54
        draw.text((_i(left_m), _i(curr_y)), f"{company}  |  {dates}", fill="#334155", font=body_font)
        curr_y += 56

        bullets = exp.get("bullet_points", [])
        if isinstance(bullets, list):
            for bullet in bullets:
                draw_wrapped_text(str(bullet), prefix="•  ", font_to_use=body_font, text_color="#0F172A", indent=18, max_width_chars=14 if layout == "sidebar_column" else 22)
        curr_y += 18

    # 3. Projects
    draw_section_header("KEY PROJECTS")
    for proj in projects:
        if not isinstance(proj, dict):
            continue
        title = proj.get("title", "")
        tech = proj.get("technologies", "")
        proj_header = f"{title}" + (f" [{tech}]" if tech else "")
        draw_wrapped_text(proj_header, prefix="", font_to_use=item_title_font, text_color="#0F172A", indent=0, max_width_chars=14 if layout == "sidebar_column" else 22)

        bullets = proj.get("bullet_points", [])
        if isinstance(bullets, list):
            for bullet in bullets:
                draw_wrapped_text(str(bullet), prefix="•  ", font_to_use=body_font, text_color="#0F172A", indent=18, max_width_chars=14 if layout == "sidebar_column" else 22)
        curr_y += 18

    # 4. Education
    draw_section_header("EDUCATION")
    for edu in education:
        if not isinstance(edu, dict):
            continue
        deg = edu.get("degree", "")
        inst = edu.get("institution", "")
        yrs = f"{edu.get('start_year', '')} - {edu.get('end_year', '')}"

        draw.text((_i(left_m), _i(curr_y)), f"{deg}", fill="#0F172A", font=item_title_font)
        curr_y += 54
        draw.text((_i(left_m), _i(curr_y)), f"{inst}  |  {yrs}", fill="#334155", font=body_font)
        curr_y += 56

    # Footer Bar
    footer_y = curr_y + 24
    draw.rectangle([0, _i(footer_y), width, _i(footer_y + 60)], fill="#F8FAFC")
    draw.text((_i(36), _i(footer_y + 16)), f"NextHire AI Preview  |  Template: {template_info.get('name')}  |  Layout: {layout.replace('_', ' ').title()}", fill="#334155", font=small_font)

    total_h = max(1400, _i(footer_y + 60))

    if layout == "border_frame":
        draw.rectangle([_i(16), _i(16), _i(width - 16), _i(total_h - 16)], outline=primary_rgb, width=_i(6))

    full_resume_img = img.crop((0, 0, width, total_h))

    buf = io.BytesIO()
    full_resume_img.save(buf, format="PNG", quality=98)
    buf.seek(0)
    return buf.getvalue()
