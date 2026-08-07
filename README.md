# 🚀 NextHire AI - AI-Powered Resume Builder & ATS Analyzer

**NextHire AI** is an intelligent, user-centric web application designed to help students, fresh graduates, and professionals create high-quality, ATS-optimized resumes. Powered by Google Gemini AI and ReportLab, NextHire AI offers job-specific resume tailoring, real-time ATS strength scoring, interactive bullet point enhancement, and instant PDF export.

---

## ✨ Features

- 👤 **Interactive Profile Collector**: 5-tab data collection form for Personal Info, Education, Experience, Projects, Skills, Certifications, and Job Target.
- 🎨 **Multi-Template Support**: Choose from 4 ATS-friendly templates (Classic ATS, Modern Professional, Minimalist Tech, Executive Corporate).
- 🤖 **AI Professional Summary Generator**: Crafts 3-4 sentence role-aligned summaries using Gemini API or intelligent offline fallback.
- ✍️ **AI Bullet Point Polish**: Enhances project and experience bullet points with strong action verbs and quantitative metrics.
- 📊 **ATS Resume Analysis Dashboard**: Provides an overall score (0–100), ATS compatibility percentage, missing keyword detector, and actionable suggestions.
- 📥 **One-Click PDF Export**: Renders publication-ready PDF resumes directly from Python.

---

## 📁 Repository Structure

```
NextHire_AI/
├── app/
│   ├── main.py                     # Entry point & Streamlit router
│   ├── components/                 # UI components (Navbar, Header, Footer)
│   ├── config/                     # Constants, sample data, and API settings
│   ├── models/                     # Data schemas (Pydantic models)
│   ├── pages/                      # 5-step application pages
│   │   ├── home.py                 # Landing page
│   │   ├── data_collection.py      # Candidate profile form
│   │   ├── template_selection.py   # Template picker
│   │   ├── resume_editor.py        # Live editor & AI polish
│   │   ├── resume_analysis.py      # ATS score breakdown
│   │   └── download.py             # PDF download page
│   ├── services/                   # AI & ATS business logic
│   │   ├── generator/              # Gemini summary & bullet generator
│   │   ├── analyzer/               # ATS score engine & keyword matcher
│   │   └── prompts/                # Structured prompt templates
│   ├── styles/                     # Custom CSS styles
│   └── utils/                      # PDF export engine (ReportLab)
├── documents/
│   └── SRS_NextHire_AI.md          # Software Requirements Specification
└── requirements.txt                # Project Python dependencies
```

---

## 🚀 Quickstart & Installation Guide

### 1. Prerequisites
Ensure you have Python 3.9+ installed.

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Launch NextHire AI
From the project root directory (`c:\NextHire_AI`), run:
```bash
streamlit run app/main.py
```

### 4. Optional: Configure Gemini API Key
- Enter your API Key in the top navigation drawer in the app, or create a `.env` file in the root directory:
```env
GEMINI_API_KEY=your_google_gemini_api_key_here
```
*(Note: If no API key is provided, NextHire AI operates seamlessly using its offline fallback engine).*

---

## 👨‍💻 Author

**Santosh Kumar Kolagani**  
*B.Tech - Computer Science & Engineering (Data Science)*  
*GIET College of Engineering*  
AI Based Project: **NextHire AI**
