"""
===========================================================
Project     : NextHire AI
File        : constants.py
Author      : Santosh Kolagani

Purpose:
    Global constants, template catalog (16 layout styles),
    and clean empty initial resume data dictionary.
===========================================================
"""

TEMPLATE_CATEGORIES = [
    "ATS Friendly",
    "Modern Professional",
    "Tech & Developer",
    "Creative & Design",
    "Executive & Senior",
    "Academic & Research",
    "All Templates"
]

LAYOUT_STYLES = [
    "header_banner",     # 1. Full-width primary color top header banner
    "left_accent",       # 2. Thick vertical accent bar on left side
    "split_header",      # 3. Left: Name & Title, Right: Shaded Contact Box
    "centered_minimal",  # 4. Centered candidate header with classic divider lines
    "code_terminal",     # 5. Monospace theme with code comments & bracketed tags
    "executive_serif",   # 6. Elegant serif typography with double rule lines
    "modern_pills",      # 7. Section title background pill blocks & skill badges
    "border_frame",      # 8. Full-page outer theme border with framed header
    "sidebar_column",    # 9. Left sidebar column for contact & skills, right for experience
    "top_accent_bar",    # 10. Thick top horizontal bar with floating header card
    "minimal_divider",   # 11. Clean typography with colored dot indicators
    "compact_grid",      # 12. High-density boxed grid for skills and experience
    "creative_gradient", # 13. Dual-color top accent bar with stylized headers
    "classic_boxed",     # 14. Rounded background cards for experience items
    "timeline_style",    # 15. Vertical timeline line for work experience items
    "academic_formal"    # 16. Formal academic layout with dual top/bottom rules
]

def _generate_templates():
    templates = {}

    def build_section(category, name_tuples):
        for idx, (tid, name, tag, desc, color, font) in enumerate(name_tuples):
            layout = LAYOUT_STYLES[idx % len(LAYOUT_STYLES)]
            templates[tid] = {
                "id": tid,
                "name": name,
                "category": category,
                "tag": tag,
                "description": desc,
                "color": color,
                "font": font,
                "layout_style": layout
            }

    # 1. ATS Friendly
    ats_names = [
        ("ats_1", "Classic ATS Single-Column", "ATS Standard", "Clean single-column format 100% readable by ATS software.", "#1E3A8A", "Helvetica"),
        ("ats_2", "ATS High Density Compact", "High Density", "Space-optimized single-page layout for dense work history.", "#334155", "Helvetica"),
        ("ats_3", "ATS Clean Minimalist", "Minimalist", "Distraction-free typography with clear section dividers.", "#0F172A", "Helvetica"),
        ("ats_4", "ATS Corporate Analyst", "Analyst Choice", "Traditional corporate layout tailored for finance & analytics.", "#0369A1", "Helvetica"),
        ("ats_5", "ATS Federal Standard", "Government", "Standard serif layout tailored for federal & public sector applications.", "#172554", "Times-Roman"),
        ("ats_6", "ATS Healthcare Professional", "Healthcare", "Clean layout emphasizing medical certifications & patient care.", "#0891B2", "Helvetica"),
        ("ats_7", "ATS Finance & Banking", "Banking", "Conservative format highlighting numerical impact & financial compliance.", "#1E293B", "Times-Roman"),
        ("ats_8", "ATS Operations Manager", "Operations", "Structured format focusing on process optimization & KPIs.", "#047857", "Helvetica"),
        ("ats_9", "ATS Legal & Compliance", "Legal", "Formal typography for legal counsel, compliance & policy roles.", "#312E81", "Times-Roman"),
        ("ats_10", "ATS Supply Chain Pro", "Logistics", "Highlights logistics, procurement, and vendor metrics.", "#1F2937", "Helvetica"),
        ("ats_11", "ATS Sales & Account Exec", "Sales Pro", "Emphasizes revenue targets, client acquisition & quota performance.", "#1D4ED8", "Helvetica"),
        ("ats_12", "ATS Marketing Strategist", "Marketing", "Balances campaign metrics, SEO skills & audience growth.", "#4338CA", "Helvetica"),
        ("ats_13", "ATS Human Resources", "HR Standard", "Clean layout for talent acquisition & HR operations.", "#0F766E", "Helvetica"),
        ("ats_14", "ATS Mechanical Engineer", "Engineering", "High-density technical layout for CAD & manufacturing pros.", "#374151", "Courier"),
        ("ats_15", "ATS Civil & Structure", "Civil Eng", "Structured for project budgets, site management & engineering.", "#1E3E62", "Times-Roman"),
        ("ats_16", "ATS Quality Assurance", "QA Standard", "Highlights test coverage, bug metrics & compliance.", "#0369A1", "Helvetica"),
        ("ats_17", "ATS Customer Success", "Client Success", "Focuses on retention metrics, CSAT scores & onboarding.", "#0284C7", "Helvetica"),
        ("ats_18", "ATS Project Management", "PMP Choice", "Tailored for Scrum Masters, PMPs, and Agile project managers.", "#1E293B", "Helvetica"),
        ("ats_19", "ATS Data Analyst Clean", "Data Analyst", "Highlights SQL, Python, Tableau dashboards & quantitative metrics.", "#047857", "Helvetica"),
        ("ats_20", "ATS General Graduate", "Fresh Grad", "Starter layout for students & fresh university graduates.", "#2563EB", "Helvetica"),
    ]
    build_section("ATS Friendly", ats_names)

    # 2. Modern Professional
    modern_names = [
        ("mod_1", "Modern Corporate Indigo", "Modern Top", "Contemporary header layout with soft indigo section titles.", "#2563EB", "Helvetica"),
        ("mod_2", "Modern Minimal Emerald", "Eco Clean", "Subtle green accents for sustainability & modern management roles.", "#059669", "Helvetica"),
        ("mod_3", "Modern Slate Executive", "Slate Pro", "Sleek slate gray design with refined border dividers.", "#475569", "Helvetica"),
        ("mod_4", "Modern Executive Teal", "Teal Accent", "Teal highlight headers for product managers & team leads.", "#0D9488", "Helvetica"),
        ("mod_5", "Modern Crimson Leader", "Executive", "Bold red top border for senior directors & VP candidates.", "#991B1B", "Helvetica"),
    ]
    build_section("Modern Professional", modern_names)

    # 3. Tech & Developer
    tech_names = [
        ("tech_1", "Full Stack Developer Dark", "Dev Choice", "Clean dark headers tailored for software engineers & architects.", "#0F172A", "Courier"),
        ("tech_2", "Data Scientist Analytics", "AI & ML", "Emphasizes technical skills, ML frameworks & research papers.", "#1E3A8A", "Helvetica"),
        ("tech_3", "DevOps & Cloud Engineer", "Cloud Ready", "Highlights AWS, Docker, Kubernetes & CI/CD pipeline accomplishments.", "#0369A1", "Courier"),
        ("tech_4", "Cybersecurity Specialist", "Security", "Focused layout for SOC analysts, penetration testers & CISSPs.", "#15803D", "Courier"),
        ("tech_5", "Mobile App Developer", "iOS/Android", "Displays app store achievements, Swift, Kotlin & Flutter skills.", "#7C3AED", "Helvetica"),
    ]
    build_section("Tech & Developer", tech_names)

    return templates

TEMPLATES = _generate_templates()

# Clean Initial Empty Resume Data Dictionary (No Default Pre-filled Sample Text)
SAMPLE_RESUME_DATA = {
    "personal_info": {
        "full_name": "",
        "email": "",
        "phone": "",
        "location": "",
        "linkedin": "",
        "github": "",
        "portfolio": "",
        "summary": ""
    },
    "education": [],
    "experience": [],
    "projects": [],
    "skills": [],
    "certifications": [],
    "job_target": {
        "job_title": "",
        "company_name": "",
        "job_description": "",
        "personalized_mode": False
    }
}

ACTION_VERBS = [
    "Architected", "Engineered", "Developed", "Designed", "Implemented",
    "Optimized", "Spearheaded", "Accelerated", "Automated", "Integrated",
    "Formulated", "Pioneered", "Transformed", "Maximized", "Generated",
    "Streamlined", "Deployed", "Built", "Created", "Directed"
]
