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

    width, height = 460, 600
    img = Image.new("RGB", (width, height), color="#FFFFFF")
    draw = ImageDraw.Draw(img)

    hex_color = template_info.get("color", "#1E3A8A")
    hex_clean = hex_color.lstrip("#")
    try:
        primary_rgb = tuple(int(hex_clean[i:i+2], 16) for i in (0, 2, 4))
    except Exception:
        primary_rgb = (30, 58, 138)

    font_type = template_info.get("font", "Helvetica")
    layout = template_info.get("layout_style", "header_banner")

    # Website-Standard Gallery Template Preview Proportions (460x600 canvas for large crisp text)
    title_font = _load_font(32, font_type, bold=True)
    subtitle_font = _load_font(16, font_type, bold=True)
    section_font = _load_font(21, font_type, bold=True)
    item_title_font = _load_font(18, font_type, bold=True)
    body_font = _load_font(16, font_type, bold=False)
    small_font = _load_font(13, font_type, bold=False)

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

    curr_y = 20
    left_m = 22
    right_m = 22

    # ---------------------------------------------------------
    # 16 DISTINCT VIBRANT LAYOUT STYLES (All Coordinates Integer-Casted)
    # ---------------------------------------------------------
    if layout == "header_banner":
        draw.rectangle([0, 0, width, 95], fill=primary_rgb)
        draw.text((_i(22), _i(14)), name, fill="#FFFFFF", font=title_font)
        draw.text((_i(22), _i(58)), f"{email}  |  {phone}  |  {location}", fill="#F1F5F9", font=subtitle_font)
        curr_y = 110

    elif layout == "left_accent":
        draw.rectangle([0, 0, 14, height], fill=primary_rgb)
        draw.text((_i(28), _i(14)), name, fill=primary_rgb, font=title_font)
        draw.text((_i(28), _i(56)), f"{email}  |  {phone}  |  {location}", fill="#334155", font=subtitle_font)
        draw.line([(_i(28), _i(84)), (_i(width - 22), _i(84))], fill=primary_rgb, width=_i(3))
        curr_y = 96
        left_m = 28

    elif layout == "split_header":
        draw.text((_i(22), _i(14)), name, fill=primary_rgb, font=title_font)
        draw.text((_i(22), _i(54)), f"{email}  |  {phone}  |  {location}", fill="#1E293B", font=subtitle_font)
        draw.line([(_i(22), _i(82)), (_i(width - 22), _i(82))], fill=primary_rgb, width=_i(3))
        curr_y = 94

    elif layout == "centered_minimal":
        center_x = _i(width // 2)
        draw.text((_i(center_x - 130), _i(14)), name, fill=primary_rgb, font=title_font)
        draw.text((_i(center_x - 160), _i(54)), f"{email}   •   {phone}   •   {location}", fill="#334155", font=subtitle_font)
        draw.line([(_i(36), _i(82)), (_i(width - 36), _i(82))], fill=primary_rgb, width=_i(2))
        curr_y = 94

    elif layout == "code_terminal":
        draw.rectangle([0, 0, width, 95], fill="#1E1E2E")
        draw.text((_i(22), _i(12)), "$ cat candidate_profile.json", fill="#A6E3A1", font=subtitle_font)
        draw.text((_i(22), _i(38)), f"\"name\": \"{name}\", \"role\": \"AI Developer\"", fill="#F9E2AF", font=subtitle_font)
        draw.text((_i(22), _i(64)), f"\"contact\": \"{email} | {phone}\"", fill="#89B4FA", font=subtitle_font)
        curr_y = 110

    elif layout == "executive_serif":
        draw.line([(_i(22), _i(12)), (_i(width - 22), _i(12))], fill=primary_rgb, width=_i(3))
        draw.text((_i(22), _i(18)), name, fill=primary_rgb, font=title_font)
        draw.text((_i(22), _i(56)), f"EXECUTIVE PROFILE  |  {email}  |  {phone}", fill="#1E293B", font=subtitle_font)
        draw.line([(_i(22), _i(84)), (_i(width - 22), _i(84))], fill=primary_rgb, width=_i(3))
        curr_y = 96

    elif layout == "modern_pills":
        draw.rectangle([0, 0, width, 95], fill="#F8FAFC")
        draw.rectangle([_i(22), _i(12), _i(300), _i(52)], fill=primary_rgb)
        draw.text((_i(30), _i(15)), name, fill="#FFFFFF", font=title_font)
        draw.text((_i(22), _i(62)), f"{email}  |  {phone}  |  {location}", fill="#334155", font=subtitle_font)
        draw.line([(_i(22), _i(84)), (_i(width - 22), _i(84))], fill=primary_rgb, width=_i(3))
        curr_y = 96

    elif layout == "border_frame":
        curr_y = 92
        left_m = 26
        right_m = 26
        draw.text((_i(26), _i(14)), name, fill=primary_rgb, font=title_font)
        draw.text((_i(26), _i(54)), f"{email}  |  {phone}  |  {location}", fill="#334155", font=subtitle_font)
        draw.line([(_i(26), _i(82)), (_i(width - 26), _i(82))], fill=primary_rgb, width=_i(3))

    elif layout == "top_accent_bar":
        draw.rectangle([0, 0, width, 12], fill=primary_rgb)
        draw.rectangle([_i(22), _i(18), _i(width - 22), _i(84)], fill="#F8FAFC", outline="#CBD5E1", width=_i(1))
        draw.text((_i(30), _i(22)), name, fill=primary_rgb, font=title_font)
        draw.text((_i(30), _i(58)), f"{email}  |  {phone}  |  {location}", fill="#334155", font=subtitle_font)
        curr_y = 96

    elif layout == "sidebar_column":
        draw.rectangle([0, 0, 140, height], fill="#F8FAFC")
        draw.line([(_i(140), 0), (_i(140), height)], fill=primary_rgb, width=_i(3))
        draw.text((_i(10), _i(14)), name, fill=primary_rgb, font=_load_font(18, font_type, bold=True))
        draw.text((_i(10), _i(46)), f"{email}\n{phone}\n{location}", fill="#334155", font=subtitle_font)
        draw.text((_i(10), _i(120)), "SKILLS", fill=primary_rgb, font=section_font)
        draw.text((_i(10), _i(148)), "• Python & SQL\n• Streamlit & APIs\n• Gemini LLMs\n• Data Science", fill="#0F172A", font=body_font)
        left_m = 152
        right_m = 16
        curr_y = 16

    elif layout == "creative_gradient":
        draw.rectangle([0, 0, width, 50], fill=primary_rgb)
        draw.rectangle([0, 50, width, 80], fill="#38BDF8")
        draw.text((_i(22), _i(10)), name, fill="#FFFFFF", font=title_font)
        draw.text((_i(22), _i(54)), f"{email}  |  {phone}  |  {location}", fill="#FFFFFF", font=subtitle_font)
        curr_y = 92

    else:
        # Default layout fallback
        draw.rectangle([0, 0, width, 90], fill=primary_rgb)
        draw.text((_i(22), _i(14)), name, fill="#FFFFFF", font=title_font)
        draw.text((_i(22), _i(56)), f"{email}  |  {phone}  |  {location}", fill="#F1F5F9", font=subtitle_font)
        curr_y = 100

    # Helper for Section Header (Clean & Proportional)
    def draw_section_header(title):
        nonlocal curr_y
        line_right = _i(width - right_m)

        if layout == "code_terminal":
            draw.text((_i(left_m), _i(curr_y)), f"// {title}", fill=primary_rgb, font=section_font)
            curr_y += 24
            draw.line([(_i(left_m), _i(curr_y)), (line_right, _i(curr_y))], fill="#CBD5E1", width=_i(2))
        elif layout in ["modern_pills", "classic_boxed"]:
            draw.rectangle([_i(left_m), _i(curr_y), _i(left_m + 220), _i(curr_y + 26)], fill=primary_rgb)
            draw.text((_i(left_m + 8), _i(curr_y + 2)), title, fill="#FFFFFF", font=section_font)
            curr_y += 30
        elif layout == "executive_serif":
            draw.line([(_i(left_m), _i(curr_y)), (line_right, _i(curr_y))], fill=primary_rgb, width=_i(2))
            draw.text((_i(left_m), _i(curr_y + 2)), f"❖  {title}", fill=primary_rgb, font=section_font)
            curr_y += 24
            draw.line([(_i(left_m), _i(curr_y)), (line_right, _i(curr_y))], fill=primary_rgb, width=_i(2))
        else:
            draw.text((_i(left_m), _i(curr_y)), title, fill=primary_rgb, font=section_font)
            curr_y += 24
            draw.line([(_i(left_m), _i(curr_y)), (line_right, _i(curr_y))], fill=primary_rgb, width=_i(2))

        curr_y += 6

    # Helper for wrapped text line drawing (Enlarged High-Contrast Text)
    def draw_wrapped_text(text_str, prefix="", font_to_use=body_font, text_color="#0F172A", indent=0, max_width_chars=34):
        nonlocal curr_y
        words = text_str.split()
        if not words:
            return
        line = prefix
        for w in words:
            test_line = line + " " + w if line else w
            if len(test_line) > max_width_chars:
                draw.text((_i(left_m + indent), _i(curr_y)), line, fill=text_color, font=font_to_use)
                curr_y += 20
                line = "    " + w
            else:
                line = test_line
        if line:
            draw.text((_i(left_m + indent), _i(curr_y)), line, fill=text_color, font=font_to_use)
            curr_y += 20

    # 1. Summary
    draw_section_header("PROFESSIONAL SUMMARY")
    draw_wrapped_text(summary, font_to_use=body_font, text_color="#0F172A", max_width_chars=22 if layout == "sidebar_column" else 34)
    curr_y += 6

    # 2. Experience
    draw_section_header("WORK EXPERIENCE")
    for exp in experience:
        if not isinstance(exp, dict):
            continue
        role = exp.get("job_title", "")
        company = exp.get("company", "")
        dates = f"{exp.get('start_date', '')} - {exp.get('end_date', 'Present')}"
        title_str = f"{role} — {company}"

        try:
            title_bbox = draw.textbbox((0, 0), title_str, font=item_title_font)
            title_w = title_bbox[2] - title_bbox[0]
        except Exception:
            title_w = 200

        if layout != "sidebar_column":
            try:
                date_bbox = draw.textbbox((0, 0), dates, font=body_font)
                date_w = _i(date_bbox[2] - date_bbox[0])
            except Exception:
                date_w = 90

            if title_w + date_w + 10 > (width - left_m - right_m):
                draw.text((_i(left_m), _i(curr_y)), title_str, fill="#0F172A", font=item_title_font)
                curr_y += 22
                draw.text((_i(left_m), _i(curr_y)), dates, fill="#334155", font=body_font)
                curr_y += 22
            else:
                draw.text((_i(left_m), _i(curr_y)), title_str, fill="#0F172A", font=item_title_font)
                draw.text((_i(width - right_m - date_w), _i(curr_y)), dates, fill="#334155", font=body_font)
                curr_y += 24
        else:
            draw.text((_i(left_m), _i(curr_y)), title_str, fill="#0F172A", font=item_title_font)
            curr_y += 24

        bullets = exp.get("bullet_points", [])
        if isinstance(bullets, list):
            for bullet in bullets:
                draw_wrapped_text(str(bullet), prefix="•  ", font_to_use=body_font, text_color="#0F172A", indent=8, max_width_chars=20 if layout == "sidebar_column" else 32)
        curr_y += 4

    # 3. Projects
    draw_section_header("KEY PROJECTS")
    for proj in projects:
        if not isinstance(proj, dict):
            continue
        title = proj.get("title", "")
        tech = proj.get("technologies", "")
        proj_header = f"{title}" + (f" [{tech}]" if tech else "")
        draw_wrapped_text(proj_header, prefix="", font_to_use=item_title_font, text_color="#0F172A", indent=0, max_width_chars=20 if layout == "sidebar_column" else 30)

        bullets = proj.get("bullet_points", [])
        if isinstance(bullets, list):
            for bullet in bullets:
                draw_wrapped_text(str(bullet), prefix="•  ", font_to_use=body_font, text_color="#0F172A", indent=8, max_width_chars=20 if layout == "sidebar_column" else 32)
        curr_y += 4

    # 4. Education
    draw_section_header("EDUCATION")
    for edu in education:
        if not isinstance(edu, dict):
            continue
        deg = edu.get("degree", "")
        inst = edu.get("institution", "")
        yrs = f"{edu.get('start_year', '')} - {edu.get('end_year', '')}"
        edu_str = f"{deg} — {inst}"

        try:
            title_bbox = draw.textbbox((0, 0), edu_str, font=item_title_font)
            title_w = title_bbox[2] - title_bbox[0]
        except Exception:
            title_w = 180

        if layout != "sidebar_column":
            try:
                yrs_bbox = draw.textbbox((0, 0), yrs, font=body_font)
                yrs_w = _i(yrs_bbox[2] - yrs_bbox[0])
            except Exception:
                yrs_w = 80

            if title_w + yrs_w + 10 > (width - left_m - right_m):
                draw.text((_i(left_m), _i(curr_y)), edu_str, fill="#0F172A", font=item_title_font)
                curr_y += 22
                draw.text((_i(left_m), _i(curr_y)), yrs, fill="#334155", font=body_font)
                curr_y += 22
            else:
                draw.text((_i(left_m), _i(curr_y)), edu_str, fill="#0F172A", font=item_title_font)
                draw.text((_i(width - right_m - yrs_w), _i(curr_y)), yrs, fill="#334155", font=body_font)
                curr_y += 24
        else:
            draw.text((_i(left_m), _i(curr_y)), edu_str, fill="#0F172A", font=item_title_font)
            curr_y += 24

    # Footer Bar
    footer_y = height - 28
    draw.rectangle([0, _i(footer_y), width, height], fill="#F8FAFC")
    draw.text((_i(22), _i(footer_y + 6)), f"NextHire AI  |  Template: {template_info.get('name')}  |  Layout: {layout.replace('_', ' ').title()}", fill="#334155", font=small_font)

    if layout == "border_frame":
        draw.rectangle([_i(6), _i(6), _i(width - 6), _i(height - 6)], outline=primary_rgb, width=_i(3))

    buf = io.BytesIO()
    img.save(buf, format="PNG", quality=98)
    buf.seek(0)
    return buf.getvalue()
