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
    Generates a 900x1200 screen-optimized, large-font, high-contrast complete A4 page PNG preview.
    Supporting 16 unique layout styles with vibrant colors and bold typography.
    """
    width, height = 900, 1200
    img = Image.new("RGB", (width, height), color="#FFFFFF")
    draw = ImageDraw.Draw(img)

    hex_color = template_info.get("color", "#1E3A8A")
    hex_clean = hex_color.lstrip("#")
    primary_rgb = tuple(int(hex_clean[i:i+2], 16) for i in (0, 2, 4))
    font_type = template_info.get("font", "Helvetica")
    layout = template_info.get("layout_style", "header_banner")

    # High-Visibility Large Typography for Clear Previews (900x1200 canvas)
    title_font = _load_font(44, font_type, bold=True)
    subtitle_font = _load_font(18, font_type, bold=False)
    section_font = _load_font(24, font_type, bold=True)
    item_title_font = _load_font(20, font_type, bold=True)
    body_font = _load_font(16, font_type, bold=False)
    small_font = _load_font(14, font_type, bold=False)

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

    curr_y = 42
    left_m = 45
    right_m = 45

    # ---------------------------------------------------------
    # 16 DISTINCT VIBRANT LAYOUT STYLES (900x1200 Large Page View)
    # ---------------------------------------------------------
    if layout == "header_banner":
        draw.rectangle([0, 0, width, 140], fill=primary_rgb)
        draw.text((45, 30), name, fill="#FFFFFF", font=title_font)
        draw.text((45, 92), f"{email}  |  {phone}  |  {location}", fill="#F1F5F9", font=subtitle_font)
        curr_y = 160

    elif layout == "left_accent":
        draw.rectangle([0, 0, 24, height], fill=primary_rgb)
        draw.text((55, 34), name, fill=primary_rgb, font=title_font)
        draw.text((55, 92), f"{email}  |  {phone}  |  {location}", fill="#334155", font=subtitle_font)
        draw.line([(55, 125), (width - 45, 125)], fill=primary_rgb, width=3)
        curr_y = 145
        left_m = 55

    elif layout == "split_header":
        draw.text((45, 30), name, fill=primary_rgb, font=title_font)
        draw.text((45, 84), "SOFTWARE & AI DEVELOPER", fill="#1E293B", font=subtitle_font)
        draw.rectangle([width - 380, 20, width - 45, 118], fill="#F8FAFC", outline=primary_rgb, width=2)
        draw.text((width - 365, 30), f"Email: {email}", fill="#0F172A", font=body_font)
        draw.text((width - 365, 58), f"Phone: {phone}", fill="#0F172A", font=body_font)
        draw.text((width - 365, 86), f"Loc: {location}", fill="#0F172A", font=body_font)
        draw.line([(45, 132), (width - 45, 132)], fill=primary_rgb, width=3)
        curr_y = 150

    elif layout == "centered_minimal":
        draw.text((width//2 - 180, 30), name, fill=primary_rgb, font=title_font)
        draw.text((width//2 - 260, 84), f"{email}   •   {phone}   •   {location}", fill="#334155", font=subtitle_font)
        draw.line([(70, 120), (width - 70, 120)], fill=primary_rgb, width=2)
        draw.line([(70, 124), (width - 70, 124)], fill=primary_rgb, width=1)
        curr_y = 145

    elif layout == "code_terminal":
        draw.rectangle([0, 0, width, 140], fill="#1E1E2E")
        draw.text((45, 22), f"$ cat candidate_profile.json", fill="#A6E3A1", font=subtitle_font)
        draw.text((45, 58), f"\"name\": \"{name}\", \"role\": \"Full-Stack AI Developer\"", fill="#F9E2AF", font=subtitle_font)
        draw.text((45, 94), f"\"contact\": \"{email} | {phone}\"", fill="#89B4FA", font=subtitle_font)
        curr_y = 160

    elif layout == "executive_serif":
        draw.line([(45, 25), (width - 45, 25)], fill=primary_rgb, width=3)
        draw.text((45, 40), name, fill=primary_rgb, font=title_font)
        draw.text((45, 94), f"EXECUTIVE PROFILE  |  {email}  |  {phone}", fill="#1E293B", font=subtitle_font)
        draw.line([(45, 128), (width - 45, 128)], fill=primary_rgb, width=3)
        draw.line([(45, 134), (width - 45, 134)], fill=primary_rgb, width=1)
        curr_y = 150

    elif layout == "modern_pills":
        draw.rectangle([0, 0, width, 140], fill="#F8FAFC")
        draw.rectangle([45, 22, 400, 78], fill=primary_rgb)
        draw.text((60, 30), name, fill="#FFFFFF", font=title_font)
        draw.text((45, 94), f"{email}  |  {phone}  |  {location}", fill="#334155", font=subtitle_font)
        draw.line([(45, 130), (width - 45, 130)], fill=primary_rgb, width=3)
        curr_y = 148

    elif layout == "border_frame":
        draw.rectangle([12, 12, width - 12, height - 12], outline=primary_rgb, width=3)
        draw.text((48, 32), name, fill=primary_rgb, font=title_font)
        draw.text((48, 86), f"{email}  |  {phone}  |  {location}", fill="#334155", font=subtitle_font)
        draw.line([(48, 120), (width - 48, 120)], fill=primary_rgb, width=3)
        curr_y = 140
        left_m = 48
        right_m = 48

    elif layout == "top_accent_bar":
        draw.rectangle([0, 0, width, 22], fill=primary_rgb)
        draw.rectangle([45, 38, width - 45, 125], fill="#F8FAFC", outline="#CBD5E1", width=2)
        draw.text((60, 48), name, fill=primary_rgb, font=title_font)
        draw.text((60, 92), f"{email}  |  {phone}  |  {location}", fill="#334155", font=subtitle_font)
        curr_y = 145

    elif layout == "sidebar_column":
        draw.rectangle([0, 0, 270, height], fill="#F8FAFC")
        draw.line([(270, 0), (270, height)], fill=primary_rgb, width=3)
        draw.text((25, 32), name, fill=primary_rgb, font=_load_font(24, font_type, bold=True))
        draw.text((25, 78), f"{email}\n{phone}\n{location}", fill="#334155", font=subtitle_font)
        draw.text((25, 160), "SKILLS", fill=primary_rgb, font=section_font)
        draw.text((25, 196), "• Python & SQL\n• Streamlit & APIs\n• Gemini LLMs\n• Data Science", fill="#0F172A", font=body_font)
        left_m = 290
        right_m = 35
        curr_y = 32

    elif layout == "creative_gradient":
        draw.rectangle([0, 0, width, 82], fill=primary_rgb)
        draw.rectangle([0, 82, width, 118], fill="#38BDF8")
        draw.text((45, 24), name, fill="#FFFFFF", font=title_font)
        draw.text((45, 88), f"{email}  |  {phone}  |  {location}", fill="#FFFFFF", font=subtitle_font)
        curr_y = 142

    else:
        # Default layout fallback
        draw.rectangle([0, 0, width, 130], fill=primary_rgb)
        draw.text((45, 26), name, fill="#FFFFFF", font=title_font)
        draw.text((45, 82), f"{email}  |  {phone}  |  {location}", fill="#F1F5F9", font=subtitle_font)
        curr_y = 148

    # Helper for Section Header (Clean & Proportional)
    def draw_section_header(title):
        nonlocal curr_y
        line_right = width - right_m

        if layout == "code_terminal":
            draw.text((left_m, curr_y), f"// {title}", fill=primary_rgb, font=section_font)
            curr_y += 30
            draw.line([(left_m, curr_y), (line_right, curr_y)], fill="#CBD5E1", width=1)
        elif layout in ["modern_pills", "classic_boxed"]:
            draw.rectangle([left_m, curr_y, left_m + 310, curr_y + 34], fill=primary_rgb)
            draw.text((left_m + 14, curr_y + 4), title, fill="#FFFFFF", font=section_font)
            curr_y += 42
        elif layout == "executive_serif":
            draw.line([(left_m, curr_y), (line_right, curr_y)], fill=primary_rgb, width=1)
            draw.text((left_m, curr_y + 4), f"❖  {title}", fill=primary_rgb, font=section_font)
            curr_y += 32
            draw.line([(left_m, curr_y), (line_right, curr_y)], fill=primary_rgb, width=1)
        else:
            draw.text((left_m, curr_y), title, fill=primary_rgb, font=section_font)
            curr_y += 30
            draw.line([(left_m, curr_y), (line_right, curr_y)], fill=primary_rgb, width=2)

        curr_y += 14

    # Helper for wrapped text line drawing (Bold High-Contrast Text)
    def draw_wrapped_text(text_str, prefix="", font_to_use=body_font, text_color="#0F172A", indent=0, max_width_chars=60):
        nonlocal curr_y
        words = text_str.split()
        if not words:
            return
        line = prefix
        for w in words:
            test_line = line + " " + w if line else w
            if len(test_line) > max_width_chars:
                draw.text((left_m + indent, curr_y), line, fill=text_color, font=font_to_use)
                curr_y += 22
                line = "    " + w
            else:
                line = test_line
        if line:
            draw.text((left_m + indent, curr_y), line, fill=text_color, font=font_to_use)
            curr_y += 22

    # 1. Summary
    draw_section_header("PROFESSIONAL SUMMARY")
    draw_wrapped_text(summary, font_to_use=body_font, text_color="#0F172A", max_width_chars=40 if layout == "sidebar_column" else 64)
    curr_y += 10

    # 2. Experience
    draw_section_header("WORK EXPERIENCE")
    for exp in experience:
        role = exp.get("job_title", "")
        company = exp.get("company", "")
        dates = f"{exp.get('start_date', '')} - {exp.get('end_date', 'Present')}"
        
        # Role & Company title
        title_str = f"{role} — {company}"
        draw.text((left_m, curr_y), title_str, fill="#0F172A", font=item_title_font)
        
        # Right-aligned dates with guaranteed zero collision
        if layout != "sidebar_column":
            try:
                date_bbox = draw.textbbox((0, 0), dates, font=body_font)
                date_w = date_bbox[2] - date_bbox[0]
            except Exception:
                date_w = 130
            draw.text((width - right_m - date_w, curr_y), dates, fill="#475569", font=body_font)
            
        curr_y += 25

        for bullet in exp.get("bullet_points", []):
            draw_wrapped_text(bullet, prefix="•  ", font_to_use=body_font, text_color="#1E293B", indent=14, max_width_chars=38 if layout == "sidebar_column" else 60)
        curr_y += 8

    # 3. Projects
    draw_section_header("KEY PROJECTS")
    for proj in projects:
        title = proj.get("title", "")
        tech = proj.get("technologies", "")
        proj_header = f"{title}" + (f" [{tech}]" if tech else "")
        draw.text((left_m, curr_y), proj_header, fill="#0F172A", font=item_title_font)
        curr_y += 25

        for bullet in proj.get("bullet_points", []):
            draw_wrapped_text(bullet, prefix="•  ", font_to_use=body_font, text_color="#1E293B", indent=14, max_width_chars=38 if layout == "sidebar_column" else 60)
        curr_y += 8

    # 4. Education
    draw_section_header("EDUCATION")
    for edu in education:
        deg = edu.get("degree", "")
        inst = edu.get("institution", "")
        yrs = f"{edu.get('start_year', '')} - {edu.get('end_year', '')}"
        draw.text((left_m, curr_y), f"{deg} — {inst}", fill="#0F172A", font=item_title_font)
        if layout != "sidebar_column":
            try:
                yrs_bbox = draw.textbbox((0, 0), yrs, font=body_font)
                yrs_w = yrs_bbox[2] - yrs_bbox[0]
            except Exception:
                yrs_w = 100
            draw.text((width - right_m - yrs_w, curr_y), yrs, fill="#475569", font=body_font)
        curr_y += 26

    # Footer Bar
    draw.rectangle([0, height - 36, width, height], fill="#F8FAFC")
    draw.text((45, height - 25), f"NextHire AI Resume Preview  |  Template: {template_info.get('name')}  |  Layout: {layout.replace('_', ' ').title()}", fill="#475569", font=small_font)

    buf = io.BytesIO()
    img.save(buf, format="PNG", quality=95)
    buf.seek(0)
    return buf.getvalue()


