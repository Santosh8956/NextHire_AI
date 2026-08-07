"""
===========================================================
Project     : NextHire AI
File        : pdf_generator.py
Author      : Santosh Kolagani

Purpose:
    PDF Export Engine using ReportLab supporting 16 visually distinct
    layout styles across all templates.
===========================================================
"""

import io
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, HRFlowable, Table, TableStyle
)
from app.config.constants import TEMPLATES


def generate_resume_pdf(resume_data: dict, template_id: str = "ats_1") -> bytes:
    """
    Generates a PDF byte buffer for the resume based on the selected template layout style.
    """
    buffer = io.BytesIO()
    
    doc = SimpleDocTemplate(
        buffer,
        pagesize=letter,
        leftMargin=36,
        rightMargin=36,
        topMargin=36,
        bottomMargin=36
    )
    
    if template_id in TEMPLATES:
        template_info = TEMPLATES[template_id]
    else:
        template_info = list(TEMPLATES.values())[0]

    hex_color = template_info.get("color", "#1E3A8A")
    primary_color = colors.HexColor(hex_color)
    dark_text = colors.HexColor("#1F2937")
    muted_text = colors.HexColor("#4B5563")

    layout = template_info.get("layout_style", "header_banner")
    font_base = template_info.get("font", "Helvetica")

    if font_base == "Times-Roman" or layout in ["executive_serif", "academic_formal"]:
        font_base = "Times-Roman"
        font_bold = "Times-Bold"
        font_oblique = "Times-Italic"
    elif font_base == "Courier" or layout == "code_terminal":
        font_base = "Courier"
        font_bold = "Courier-Bold"
        font_oblique = "Courier-Oblique"
    else:
        font_base = "Helvetica"
        font_bold = "Helvetica-Bold"
        font_oblique = "Helvetica-Oblique"

    styles = getSampleStyleSheet()
    align_choice = 'CENTER' if layout in ['centered_minimal', 'academic_formal'] else 'LEFT'

    title_style = ParagraphStyle(
        'DocTitle',
        parent=styles['Normal'],
        fontName=font_bold,
        fontSize=20,
        leading=24,
        alignment=0 if align_choice == 'LEFT' else 1,
        textColor=primary_color,
        spaceAfter=4
    )

    subtitle_style = ParagraphStyle(
        'DocSubtitle',
        parent=styles['Normal'],
        fontName=font_base,
        fontSize=9,
        leading=12,
        alignment=0 if align_choice == 'LEFT' else 1,
        textColor=muted_text,
        spaceAfter=8
    )

    section_heading_style = ParagraphStyle(
        'SectionHeading',
        parent=styles['Normal'],
        fontName=font_bold,
        fontSize=11,
        leading=14,
        textColor=primary_color if layout not in ["modern_pills", "classic_boxed"] else colors.white,
        spaceBefore=8,
        spaceAfter=4
    )

    item_title_style = ParagraphStyle(
        'ItemTitle',
        parent=styles['Normal'],
        fontName=font_bold,
        fontSize=9.5,
        leading=12.5,
        textColor=dark_text
    )

    item_subtitle_style = ParagraphStyle(
        'ItemSubtitle',
        parent=styles['Normal'],
        fontName=font_oblique,
        fontSize=9,
        leading=12,
        textColor=muted_text
    )

    body_style = ParagraphStyle(
        'BodyText',
        parent=styles['Normal'],
        fontName=font_base,
        fontSize=9,
        leading=12,
        textColor=dark_text
    )

    bullet_style = ParagraphStyle(
        'BulletText',
        parent=styles['Normal'],
        fontName=font_base,
        fontSize=9,
        leading=12,
        leftIndent=12,
        textColor=dark_text,
        spaceAfter=2
    )

    story = []

    # ---------------------------------------------------------
    # Header Layout Rendering
    # ---------------------------------------------------------
    personal = resume_data.get("personal_info", {})
    name = personal.get("full_name", "Your Name")

    contacts = []
    if personal.get("email"): contacts.append(personal['email'])
    if personal.get("phone"): contacts.append(personal['phone'])
    if personal.get("location"): contacts.append(personal['location'])
    if personal.get("linkedin"): contacts.append(personal['linkedin'])
    if personal.get("github"): contacts.append(personal['github'])
    contact_line = "  |  ".join(contacts)

    if layout == "split_header":
        left_p = Paragraph(f"<b>{name.upper()}</b><br/><font color='{hex_color}'><b>SENIOR CANDIDATE PROFILE</b></font>", title_style)
        right_p = Paragraph(contact_line.replace(" | ", "<br/>"), subtitle_style)
        head_table = Table([[left_p, right_p]], colWidths=[4.2*inch, 2.8*inch])
        head_table.setStyle(TableStyle([
            ('BACKGROUND', (1, 0), (1, 0), colors.HexColor("#F8FAFC")),
            ('PADDING', (1, 0), (1, 0), 8),
            ('ALIGN', (1, 0), (1, 0), 'RIGHT'),
            ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ]))
        story.append(head_table)
        story.append(Spacer(1, 6))

    elif layout in ["header_banner", "creative_gradient"]:
        banner_p = Paragraph(f"<font color='white'><b>{name.upper()}</b></font><br/><font color='#E2E8F0'>{contact_line}</font>", ParagraphStyle('Banner', parent=title_style, textColor=colors.white, alignment=1))
        banner_table = Table([[banner_p]], colWidths=[7.0*inch])
        banner_table.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, -1), primary_color),
            ('TOPPADDING', (0, 0), (-1, -1), 12),
            ('BOTTOMPADDING', (0, 0), (-1, -1), 12),
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ]))
        story.append(banner_table)
        story.append(Spacer(1, 8))

    else:
        story.append(Paragraph(f"<b>{name.upper()}</b>", title_style))
        story.append(Paragraph(contact_line, subtitle_style))
        story.append(HRFlowable(width="100%", thickness=1.5, color=primary_color, spaceAfter=8))

    # Helper for Section Title
    def append_section_heading(title_text):
        if layout == "code_terminal":
            story.append(Paragraph(f"<b>// {title_text}</b>", section_heading_style))
            story.append(HRFlowable(width="100%", thickness=1, color=colors.HexColor("#CBD5E1"), spaceAfter=4))
        elif layout in ["executive_serif", "academic_formal"]:
            story.append(HRFlowable(width="100%", thickness=1, color=primary_color, spaceBefore=6, spaceAfter=2))
            story.append(Paragraph(f"<b>❖  {title_text}</b>", section_heading_style))
            story.append(HRFlowable(width="100%", thickness=1, color=primary_color, spaceAfter=4))
        elif layout in ["modern_pills", "classic_boxed"]:
            pill_p = Paragraph(f"<b>{title_text}</b>", section_heading_style)
            pill_table = Table([[pill_p]], colWidths=[7.0*inch])
            pill_table.setStyle(TableStyle([
                ('BACKGROUND', (0, 0), (-1, -1), primary_color),
                ('TOPPADDING', (0, 0), (-1, -1), 3),
                ('BOTTOMPADDING', (0, 0), (-1, -1), 3),
                ('LEFTPADDING', (0, 0), (-1, -1), 6),
            ]))
            story.append(pill_table)
            story.append(Spacer(1, 4))
        else:
            story.append(Paragraph(f"<b>{title_text}</b>", section_heading_style))
            story.append(HRFlowable(width="100%", thickness=1, color=primary_color, spaceAfter=4))

    # 2. Professional Summary
    summary = personal.get("summary", "")
    if summary:
        append_section_heading("PROFESSIONAL SUMMARY")
        story.append(Paragraph(summary, body_style))
        story.append(Spacer(1, 4))

    # 3. Technical Skills
    skills_cat = resume_data.get("skills", [])
    if skills_cat:
        append_section_heading("TECHNICAL SKILLS")
        skill_lines = []
        for cat in skills_cat:
            cat_name = cat.get("category_name", "Skills")
            sk_list = ", ".join(cat.get("skills", []))
            if sk_list:
                skill_lines.append(f"<b>{cat_name}:</b> {sk_list}")
        if skill_lines:
            story.append(Paragraph("<br/>".join(skill_lines), body_style))
            story.append(Spacer(1, 4))

    # 4. Work Experience
    experience = resume_data.get("experience", [])
    if experience:
        append_section_heading("WORK EXPERIENCE")
        for exp in experience:
            job_title = exp.get("job_title", "")
            company = exp.get("company", "")
            dates = f"{exp.get('start_date', '')} - {exp.get('end_date', 'Present')}"
            loc = exp.get("location", "")
            
            left_text = f"<b>{job_title}</b> — <i>{company}</i>"
            right_text = f"{dates} | {loc}" if loc else dates
            
            header_table = Table(
                [[Paragraph(left_text, item_title_style), Paragraph(right_text, item_subtitle_style)]],
                colWidths=[4.3*inch, 2.7*inch]
            )
            header_table.setStyle(TableStyle([
                ('ALIGN', (1, 0), (1, 0), 'RIGHT'),
                ('VALIGN', (0, 0), (-1, -1), 'TOP'),
                ('LEFTPADDING', (0, 0), (-1, -1), 0),
                ('RIGHTPADDING', (0, 0), (-1, -1), 0),
                ('BOTTOMPADDING', (0, 0), (-1, -1), 2),
            ]))
            story.append(header_table)

            for bullet in exp.get("bullet_points", []):
                if bullet.strip():
                    story.append(Paragraph(f"• {bullet.strip()}", bullet_style))
            story.append(Spacer(1, 3))

    # 5. Projects
    projects = resume_data.get("projects", [])
    if projects:
        append_section_heading("KEY PROJECTS")
        for proj in projects:
            p_title = proj.get("title", "")
            p_tech = proj.get("technologies", "")
            p_desc = proj.get("description", "")
            
            p_header = f"<b>{p_title}</b>"
            if p_tech:
                p_header += f" <font color='{hex_color}'>[{p_tech}]</font>"

            story.append(Paragraph(p_header, item_title_style))
            if p_desc:
                story.append(Paragraph(p_desc, body_style))

            for bullet in proj.get("bullet_points", []):
                if bullet.strip():
                    story.append(Paragraph(f"• {bullet.strip()}", bullet_style))
            story.append(Spacer(1, 3))

    # 6. Education
    education = resume_data.get("education", [])
    if education:
        append_section_heading("EDUCATION")
        for edu in education:
            degree = edu.get("degree", "")
            inst = edu.get("institution", "")
            years = f"{edu.get('start_year', '')} - {edu.get('end_year', '')}"
            grade = edu.get("grade", "")
            
            left_text = f"<b>{degree}</b> — {inst}"
            right_text = f"{years} {f'({grade})' if grade else ''}"
            
            edu_table = Table(
                [[Paragraph(left_text, item_title_style), Paragraph(right_text, item_subtitle_style)]],
                colWidths=[4.5*inch, 2.5*inch]
            )
            edu_table.setStyle(TableStyle([
                ('ALIGN', (1, 0), (1, 0), 'RIGHT'),
                ('VALIGN', (0, 0), (-1, -1), 'TOP'),
                ('LEFTPADDING', (0, 0), (-1, -1), 0),
                ('RIGHTPADDING', (0, 0), (-1, -1), 0),
                ('BOTTOMPADDING', (0, 0), (-1, -1), 2),
            ]))
            story.append(edu_table)
            story.append(Spacer(1, 3))

    # 7. Certifications
    certs = resume_data.get("certifications", [])
    if certs:
        append_section_heading("CERTIFICATIONS")
        cert_lines = []
        for c in certs:
            name = c.get("name", "")
            org = c.get("issuing_organization", "")
            yr = c.get("issue_date", "")
            if name:
                cert_lines.append(f"• <b>{name}</b> — {org} ({yr})" if org else f"• <b>{name}</b>")
        if cert_lines:
            story.append(Paragraph("<br/>".join(cert_lines), body_style))

    # Build PDF document
    doc.build(story)
    
    buffer.seek(0)
    return buffer.getvalue()
