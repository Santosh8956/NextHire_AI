"""
===========================================================
Project     : NextHire AI
File        : constants.py
Author      : Santosh Kolagani

Purpose:
    Global constants, template catalog (16 layout styles),
    and sample resume data.
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
        ("ats_21", "ATS Compact Timeline", "Timeline ATS", "Clean vertical timeline structure optimized for ATS parsing.", "#1E3A8A", "Helvetica"),
        ("ats_22", "ATS Sidebar Compact", "Sidebar ATS", "Two-column sidebar structure with clear text hierarchy.", "#334155", "Helvetica")
    ]
    build_section("ATS Friendly", ats_names)

    # 2. Modern Professional
    modern_names = [
        ("modern_1", "Modern Teal Professional", "Popular", "Vibrant teal headers with crisp modern alignment.", "#0D9488", "Helvetica"),
        ("modern_2", "Professional Emerald", "Recommended", "Sophisticated emerald green accents for business leads.", "#059669", "Helvetica"),
        ("modern_3", "Sapphire Executive Pro", "Sleek", "Deep blue accents with refined line spacing for engineers.", "#2563EB", "Helvetica"),
        ("modern_4", "Modern Slate Clean", "Elegant", "Subtle slate grey contrast with skill pill formatting.", "#475569", "Helvetica"),
        ("modern_5", "Modern Indigo Shift", "Pro Choice", "Clean indigo side accent bar with sharp section titles.", "#4F46E5", "Helvetica"),
        ("modern_6", "Modern Cyan Edge", "Fresh", "Bright cyan accents tailored for product & tech management.", "#0891B2", "Helvetica"),
        ("modern_7", "Modern Rose Minimal", "Stylized", "Soft rose red header accent with balanced margin spacing.", "#E11D48", "Helvetica"),
        ("modern_8", "Modern Amber Accent", "Warm Tone", "Warm amber highlights suitable for consulting & strategy.", "#D97706", "Helvetica"),
        ("modern_9", "Modern Violet Split", "Modern", "Rich violet header divider with distinct typography hierarchy.", "#7C3AED", "Helvetica"),
        ("modern_10", "Modern Steel Gray", "Corporate", "Monochromatic dark steel theme for corporate environments.", "#334155", "Helvetica"),
        ("modern_11", "Modern Cobalt Blue", "Sharp", "High contrast cobalt blue styling for executive summaries.", "#1D4ED8", "Helvetica"),
        ("modern_12", "Modern Forest Green", "Natural", "Deep forest green headers for sustainability & agriculture leads.", "#15803D", "Helvetica"),
        ("modern_13", "Modern Plum Elegance", "Distinct", "Deep plum purple headers with refined bullet styling.", "#7E22CE", "Helvetica"),
        ("modern_14", "Modern Charcoal Pro", "Dark Modern", "Modern dark charcoal theme for high-impact resumes.", "#1F2937", "Helvetica"),
        ("modern_15", "Modern Deep Crimson", "Bold Accent", "Bold crimson header line for energetic professionals.", "#B91C1C", "Helvetica"),
        ("modern_16", "Modern Ocean Mist", "Clean Slate", "Refreshing sky blue theme with wide structural margins.", "#0284C7", "Helvetica"),
        ("modern_17", "Modern Terracotta", "Warm Earth", "Terracotta rust accent designed for architecture & design leads.", "#C2410C", "Helvetica"),
        ("modern_18", "Modern Midnight Blue", "Midnight", "Rich dark midnight blue header banner for senior leads.", "#1E1B4B", "Helvetica"),
        ("modern_19", "Modern Mint Crisp", "Crisp", "Mint green highlights ideal for wellness, biotech & healthcare.", "#059669", "Helvetica"),
        ("modern_20", "Modern Titanium Silver", "Minimal", "Sleek silver-gray theme with compact bullet styling.", "#475569", "Helvetica"),
        ("modern_21", "Modern Boxed Gradient", "Gradient Card", "Rounded card containers with gradient accent rules.", "#0D9488", "Helvetica"),
        ("modern_22", "Modern Split Column", "Two Column", "Balanced two-column modern layout for senior engineers.", "#4F46E5", "Helvetica")
    ]
    build_section("Modern Professional", modern_names)

    # 3. Tech & Developer
    tech_names = [
        ("tech_1", "Minimalist Tech Indigo", "Dev Choice", "High-density developer layout putting skills & projects front.", "#4F46E5", "Helvetica"),
        ("tech_2", "Terminal Tech Developer", "Coder Special", "Monospace-inspired headers for backend & DevOps engineers.", "#1E1E2E", "Courier"),
        ("tech_3", "Full-Stack Engineer", "Full Stack", "Emphasizes tech stack tags, GitHub repositories & system metrics.", "#0891B2", "Helvetica"),
        ("tech_4", "Cyber Security & Cloud", "Security", "Crisp tech layout highlighting certifications & system architecture.", "#7C3AED", "Helvetica"),
        ("tech_5", "DevOps Infrastructure", "DevOps", "Courier monospace styling tailored for SRE & CI/CD pipeline pros.", "#059669", "Courier"),
        ("tech_6", "Data Engineering Lead", "Data Eng", "Highlights Big Data, Spark, Kafka, and data pipeline achievements.", "#2563EB", "Helvetica"),
        ("tech_7", "Backend Microservices", "Backend", "Monospace code block styling for Go, Java, and Python devs.", "#0F172A", "Courier"),
        ("tech_8", "Frontend React Developer", "Frontend", "Clean layout highlighting UI frameworks, TypeScript & performance.", "#0284C7", "Helvetica"),
        ("tech_9", "AI / ML Researcher", "AI / ML", "Highlights machine learning models, PyTorch, and paper links.", "#4338CA", "Helvetica"),
        ("tech_10", "Mobile iOS / Android", "Mobile Dev", "Tailored for Swift, Kotlin, and Flutter mobile developers.", "#D97706", "Helvetica"),
        ("tech_11", "System Architect", "Architect", "High-density layout for Enterprise System Architects.", "#1E293B", "Courier"),
        ("tech_12", "Cloud Solutions AWS", "Cloud Pro", "Highlights AWS, Azure, GCP certifications and architecture.", "#2563EB", "Helvetica"),
        ("tech_13", "Open Source Contributor", "Open Source", "Emphasizes GitHub stars, pull requests, and OSS libraries.", "#16A34A", "Courier"),
        ("tech_14", "Database Specialist", "DBA", "Highlights SQL performance tuning, Postgres, and database scaling.", "#0D9488", "Helvetica"),
        ("tech_15", "QA Automation Tester", "QA Eng", "Focuses on Selenium, Cypress, PyTest, and automation frameworks.", "#4F46E5", "Helvetica"),
        ("tech_16", "Embedded Systems C++", "Embedded", "Monospace layout for C/C++, IoT, and hardware developers.", "#374151", "Courier"),
        ("tech_17", "Game Developer Tech", "Gamedev", "Tailored for Unreal Engine, Unity, C#, and 3D graphics devs.", "#9333EA", "Helvetica"),
        ("tech_18", "Blockchain Engineer", "Web3", "Monospace layout for Smart Contracts, Solidity, and Rust devs.", "#2563EB", "Courier"),
        ("tech_19", "Tech Lead Manager", "Tech Lead", "Balances technical architecture with team leadership metrics.", "#1E1B4B", "Helvetica"),
        ("tech_20", "Hacker Code Minimal", "Terminal", "Ultra-clean dark terminal format for cybersecurity experts.", "#0F766E", "Courier"),
        ("tech_21", "Developer Sidebar Code", "Dev Sidebar", "Left monospace sidebar for tech stack and repositories.", "#1E1E2E", "Courier"),
        ("tech_22", "System Microservices Grid", "Grid Tech", "Grid layout organizing service endpoints and projects.", "#0891B2", "Helvetica")
    ]
    build_section("Tech & Developer", tech_names)

    # 4. Creative & Design
    creative_names = [
        ("creative_1", "Creative Violet Accent", "Creative", "Vibrant violet headers for UI/UX designers & marketers.", "#8B5CF6", "Helvetica"),
        ("creative_2", "Coral Modern Designer", "Warm Accent", "Warm coral accents with clear section hierarchy.", "#F97316", "Helvetica"),
        ("creative_3", "Crimson Bold Creative", "Bold", "Bold red header bars for media professionals & PMs.", "#DC2626", "Helvetica"),
        ("creative_4", "Amber Gold Modern", "Stylish", "Golden amber highlights suited for creative direction.", "#D97706", "Helvetica"),
        ("creative_5", "Creative Magenta Accent", "Magenta", "Vibrant magenta styling for brand strategists & content creators.", "#C026D3", "Helvetica"),
        ("creative_6", "Creative Electric Blue", "Electric", "Bright electric blue headers for digital product designers.", "#06B6D4", "Helvetica"),
        ("creative_7", "Creative Soft Rose", "Soft Rose", "Elegant soft rose accents for fashion & lifestyle leads.", "#F43F5E", "Helvetica"),
        ("creative_8", "Creative Emerald Fresh", "Fresh Green", "Refreshing emerald theme for eco brands & creative agencies.", "#10B981", "Helvetica"),
        ("creative_9", "Creative Sunset Purple", "Sunset", "Warm sunset purple header for motion graphics & video editors.", "#9333EA", "Helvetica"),
        ("creative_10", "Creative Mint Splash", "Minty", "Cool mint headers for copywriters, editors & UX researchers.", "#14B8A6", "Helvetica"),
        ("creative_11", "Creative Peach Warm", "Warm Peach", "Warm peach theme tailored for interior design & event planners.", "#F97316", "Helvetica"),
        ("creative_12", "Creative Royal Indigo", "Royal Blue", "Deep royal indigo layout for creative leads & art directors.", "#6366F1", "Helvetica"),
        ("creative_13", "Creative Graphite Studio", "Studio Dark", "Sleek graphite theme for studio photographers & animators.", "#374151", "Helvetica"),
        ("creative_14", "Creative Solar Yellow", "Solar Gold", "High energy solar yellow highlights for marketing directors.", "#EAB308", "Helvetica"),
        ("creative_15", "Creative Neon Lime", "Vibrant Lime", "Edgy lime green highlights for game designers & digital artists.", "#84CC16", "Helvetica"),
        ("creative_16", "Creative Deep Fuchsia", "Fuchsia", "Bold fuchsia headers for PR managers & social media leads.", "#D946EF", "Helvetica"),
        ("creative_17", "Creative Nordic Minimal", "Nordic", "Clean Scandinavian minimalism with subtle gray accents.", "#64748B", "Helvetica"),
        ("creative_18", "Creative Studio Crimson", "Crimson Red", "High impact crimson headers for creative agency directors.", "#E11D48", "Helvetica"),
        ("creative_19", "Creative Ocean Wave", "Aqua Blue", "Refreshing ocean aqua style for 3D artists & UI designers.", "#0284C7", "Helvetica"),
        ("creative_20", "Creative Vintage Chic", "Vintage", "Classic serif typography with warm sepia undertones.", "#B45309", "Times-Roman"),
        ("creative_21", "Creative Portfolio Column", "Portfolio", "Sidebar layout showcasing design portfolio links & skills.", "#8B5CF6", "Helvetica"),
        ("creative_22", "Creative Gradient Banner", "Gradient Art", "Multi-color top header for brand directors & artists.", "#C026D3", "Helvetica")
    ]
    build_section("Creative & Design", creative_names)

    # 5. Executive & Senior
    executive_names = [
        ("executive_1", "Executive Leadership Gold", "Senior Lead", "Authoritative header styling with elegant serif fonts.", "#B45309", "Times-Roman"),
        ("executive_2", "Corporate Director Navy", "Director", "Commanding navy header with spacious entry spacing.", "#1E3A8A", "Times-Roman"),
        ("executive_3", "Boardroom Elite Serif", "Boardroom", "Classic serif typography with refined divider rules.", "#334155", "Times-Roman"),
        ("executive_4", "Prime Enterprise Lead", "Enterprise", "Deep charcoal accents with structured achievements section.", "#111827", "Helvetica"),
        ("executive_5", "Chief Technology Officer", "CTO Choice", "High level layout balancing technical strategy & organization size.", "#1E1B4B", "Helvetica"),
        ("executive_6", "Chief Executive Officer", "CEO Standard", "Authoritative executive layout focusing on P&L and company scale.", "#0F172A", "Times-Roman"),
        ("executive_7", "Chief Financial Officer", "CFO Standard", "Formal serif layout for financial stewards & treasurers.", "#1E293B", "Times-Roman"),
        ("executive_8", "Vice President Operations", "VP Ops", "Highlights multi-department leadership, scale & efficiency.", "#047857", "Helvetica"),
        ("executive_9", "Senior Strategy Consultant", "Strategy", "Tailored for McKinsey/BCG/Bain management consultants.", "#4338CA", "Times-Roman"),
        ("executive_10", "Managing Director", "MD Level", "Commanding cobalt blue layout for investment directors.", "#1D4ED8", "Times-Roman"),
        ("executive_11", "Global Head of Product", "Head of Prod", "Focuses on product portfolio vision, ARR & global teams.", "#0369A1", "Helvetica"),
        ("executive_12", "General Counsel Legal", "General Counsel", "Formal legal layout for chief legal officers & partners.", "#312E81", "Times-Roman"),
        ("executive_13", "Partner Investment Banking", "PE / VC Partner", "Highlights M&A transactions, portfolio growth & capital allocation.", "#0F766E", "Times-Roman"),
        ("executive_14", "Principal Architect", "Principal", "Refined layout for Distinguished Engineers & Fellows.", "#475569", "Helvetica"),
        ("executive_15", "Senior Director Marketing", "CMO Level", "Emphasizes brand growth, customer acquisition & revenue.", "#7E22CE", "Times-Roman"),
        ("executive_16", "Executive Chair Leader", "Chairman", "Prestigious layout for advisory board chairs & trustees.", "#1E3E62", "Times-Roman"),
        ("executive_17", "Founder & Startup CEO", "Founder", "Highlights venture funding raised, team growth & traction.", "#2563EB", "Helvetica"),
        ("executive_18", "Global Enterprise Director", "Global Dir", "Highlights international operations & multi-country teams.", "#059669", "Times-Roman"),
        ("executive_19", "Senior Vice President Sales", "SVP Sales", "Focuses on ARR growth, enterprise deal size & sales teams.", "#B91C1C", "Times-Roman"),
        ("executive_20", "Senior Advisor Executive", "Advisor", "Refined layout for executive mentors, board members & advisors.", "#374151", "Times-Roman"),
        ("executive_21", "Executive Dual Rule", "Dual Rule", "Prestigious double-rule header with gold accent font.", "#B45309", "Times-Roman"),
        ("executive_22", "Executive Boxed Lead", "Boxed Exec", "Enclosed executive summary card with board achievements.", "#1E3A8A", "Times-Roman")
    ]
    build_section("Executive & Senior", executive_names)

    # 6. Academic & Research
    academic_names = [
        ("academic_1", "Academic Standard CV", "Academic CV", "Comprehensive academic layout prioritizing research & education.", "#1E293B", "Times-Roman"),
        ("academic_2", "Research Scholar", "Research", "Structured format emphasizing thesis projects & publications.", "#15803D", "Times-Roman"),
        ("academic_3", "University Fellow", "University", "Clean layout for teaching assistants, scholars & researchers.", "#0369A1", "Helvetica"),
        ("academic_4", "Scientific PhD Centric", "Scientific", "Formal design optimized for scientific grants & doctorates.", "#4338CA", "Times-Roman"),
        ("academic_5", "Postdoctoral Researcher", "Postdoc", "Highlights lab research, peer-reviewed journals & grants.", "#334155", "Times-Roman"),
        ("academic_6", "Medical Researcher CV", "Medical Scholar", "Tailored for clinical trials, PubMed citations & medical CVs.", "#0891B2", "Times-Roman"),
        ("academic_7", "Professor & Faculty Lead", "Professor", "Formal layout for tenured professors & department heads.", "#1E3A8A", "Times-Roman"),
        ("academic_8", "Data Science Fellow", "Data Fellow", "Combines academic research metrics with computational ML skills.", "#2563EB", "Helvetica"),
        ("academic_9", "Bio-Engineering Scholar", "Biotech", "Highlights laboratory patents, research trials & publications.", "#047857", "Times-Roman"),
        ("academic_10", "Clinical Research Lead", "Clinical CV", "Focuses on trial protocols, regulatory submissions & research.", "#0F766E", "Times-Roman"),
        ("academic_11", "Humanities & Literature", "Humanities", "Traditional elegant typography for liberal arts & literature.", "#78350F", "Times-Roman"),
        ("academic_12", "Economics & Policy Scholar", "Economics", "Highlights econometric models, policy papers & citations.", "#1E1B4B", "Times-Roman"),
        ("academic_13", "Physics & Astronomy Fellow", "Physics", "Tailored for astrophysics, quantum computing & lab papers.", "#312E81", "Times-Roman"),
        ("academic_14", "Computer Science Scholar", "CS Scholar", "Highlights algorithms research, IEEE papers & conference talks.", "#4F46E5", "Helvetica"),
        ("academic_15", "Environmental Researcher", "Environmental", "Highlights climate research, field studies & grant projects.", "#16A34A", "Times-Roman"),
        ("academic_16", "Institutional Dean CV", "Dean Level", "Formal multi-page academic CV for college deans & provosts.", "#0F172A", "Times-Roman"),
        ("academic_17", "Graduate Research Scholar", "Grad Student", "Clean layout for master's and PhD graduate applicants.", "#0284C7", "Helvetica"),
        ("academic_18", "Fulbright Scholar Format", "Fulbright", "Prestigious academic layout for global scholarship candidates.", "#B45309", "Times-Roman"),
        ("academic_19", "Scientific Grant Scholar", "Grant Proposal", "Highlights research funding, NSF/NIH grants & lab team size.", "#4338CA", "Times-Roman"),
        ("academic_20", "Academic Library Scholar", "Archival CV", "Formal layout for archivists, researchers & bibliographers.", "#374151", "Times-Roman"),
        ("academic_21", "Academic Formal Serif", "Formal Serif", "Traditional dual-rule serif CV layout for research fellows.", "#1E293B", "Times-Roman"),
        ("academic_22", "Academic Timeline CV", "Research Timeline", "Chronological research timeline format for scientific papers.", "#15803D", "Times-Roman")
    ]
    build_section("Academic & Research", academic_names)

    return templates

TEMPLATES = _generate_templates()

SAMPLE_RESUME_DATA = {
    "personal_info": {
        "full_name": "Santosh Kolagani",
        "email": "santosh.kolagani@example.com",
        "phone": "+91 98765 43210",
        "location": "Rajahmundry, AP, India",
        "linkedin": "linkedin.com/in/santoshkolagani",
        "github": "github.com/santoshkolagani",
        "portfolio": "santoshkolagani.dev",
        "summary": "Motivated Computer Science & Engineering (Data Science) undergraduate with expertise in AI/ML model deployment, full-stack Python web applications, and data analytics. Adept at building scalable web tools using Streamlit and machine learning framework."
    },
    "education": [
        {
            "degree": "B.Tech in Computer Science & Engineering (Data Science)",
            "field_of_study": "Data Science & AI",
            "institution": "GIET College of Engineering",
            "location": "Rajahmundry, AP",
            "start_year": "2022",
            "end_year": "2026",
            "grade": "CGPA: 8.7 / 10",
            "achievements": "Lead Developer for Academic Major Projects; Active Member of Data Science Club."
        }
    ],
    "experience": [
        {
            "job_title": "AI / Machine Learning Intern",
            "company": "TechSolutions Innovations",
            "location": "Hyderabad, AP (Remote)",
            "start_date": "Jun 2024",
            "end_date": "Aug 2024",
            "is_current": False,
            "bullet_points": [
                "Developed NLP text processing pipelines using Python and Gemini API, improving document categorization accuracy by 24%.",
                "Built interactive web dashboards using Streamlit to display real-time predictive analytics models.",
                "Collaborated with senior software engineers to deploy backend REST endpoints and optimize database queries."
            ]
        }
    ],
    "projects": [
        {
            "title": "NextHire AI - Resume Builder & Analysis Engine",
            "technologies": "Python, Streamlit, Google Gemini API, ReportLab, Pydantic",
            "link": "github.com/santoshkolagani/nexthire-ai",
            "description": "An intelligent AI-powered platform for resume creation, ATS scoring, content enhancement, and PDF export.",
            "bullet_points": [
                "Architected a modular web application with multi-template rendering and dynamic ATS strength scoring engine.",
                "Integrated Gemini LLM prompts for automatic bullet-point enhancement, impact verb suggestions, and section rewrites.",
                "Engineered automated PDF export engine delivering 100% ATS-compliant single and multi-page layouts."
            ]
        },
        {
            "title": "Predictive Customer Churn Analytics",
            "technologies": "Python, Scikit-Learn, Pandas, Streamlit, Plotly",
            "link": "github.com/santoshkolagani/churn-prediction",
            "description": "Machine learning system evaluating telecom customer retention metrics.",
            "bullet_points": [
                "Trained Random Forest and XGBoost classifiers on 10,000+ customer records, achieving an 89% ROC-AUC score.",
                "Created interactive feature importance visualizations to help non-technical stakeholders identify high-risk accounts."
            ]
        }
    ],
    "skills": [
        {
            "category_name": "Programming Languages",
            "skills": ["Python", "SQL", "JavaScript", "HTML/CSS"]
        },
        {
            "category_name": "AI / Machine Learning",
            "skills": ["Gemini API", "Scikit-Learn", "Pandas", "NumPy", "NLP", "Prompt Engineering"]
        },
        {
            "category_name": "Frameworks & Tools",
            "skills": ["Streamlit", "ReportLab", "Git & GitHub", "REST APIs", "VS Code"]
        }
    ],
    "certifications": [
        {
            "name": "Google Data Analytics Professional Certificate",
            "issuing_organization": "Coursera / Google",
            "issue_date": "2024",
            "credential_url": "coursera.org/verify/example"
        },
        {
            "name": "Python for Data Science & AI",
            "issuing_organization": "IBM",
            "issue_date": "2023",
            "credential_url": "ibm.com/verify/example"
        }
    ],
    "job_target": {
        "job_title": "Junior Data Scientist / AI Developer",
        "company_name": "NextGen Analytics",
        "job_description": "Looking for a Junior Data Scientist with strong Python skills, experience in NLP, LLM integrations, Streamlit dashboard development, and database querying. Candidate will build end-to-end AI applications and deploy ML models.",
        "personalized_mode": True
    }
}

ACTION_VERBS = [
    "Architected", "Engineered", "Developed", "Designed", "Implemented",
    "Optimized", "Spearheaded", "Accelerated", "Automated", "Integrated",
    "Formulated", "Pioneered", "Transformed", "Maximized", "Generated",
    "Streamlined", "Deployed", "Built", "Created", "Directed"
]
