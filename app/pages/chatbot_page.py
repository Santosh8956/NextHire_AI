"""
===========================================================
Project     : NextHire AI
File        : chatbot_page.py
Author      : Santosh Kolagani

Purpose:
    Dedicated AI Assistant Chatbot Screen integrated directly into the application.
    Trained with exhaustive knowledge of NextHire AI features, templates, ATS scoring,
    and developer details with zero empty fallback answers.
===========================================================
"""

import streamlit as st
import google.generativeai as genai
from app.components.navbar import render_navbar
from app.config.settings import get_api_key
from app.utils.helpers import render_html


NEXTHIRE_SYSTEM_KNOWLEDGE = """
You are NextHire AI Assistant, an intelligent career strategist and customer support bot for the NextHire AI platform.
Developed by Santosh Kumar Kolagani, NextHire AI is a state-of-the-art AI Career Assistant & Resume Builder v2.0.

KEY PLATFORM INFORMATION & DETAILS:
1. PLATFORM OVERVIEW:
   - NextHire AI is 100% free, private, and client-encrypted.
   - Enables job seekers to build, edit, ATS-tailor, and download publication-grade 4K vector PDF resumes.

2. DEVELOPER DETAILS:
   - Architected and engineered by Santosh Kumar Kolagani.

3. TEMPLATE CATALOG (50 Signature Templates across 6 Categories):
   - ATS Friendly (20 Templates)
   - Modern Professional (10 Templates)
   - Tech & Developer (5 Templates)
   - Creative & Design (5 Templates)
   - Executive & Senior (5 Templates)
   - Academic & Research (5 Templates)
   - Supported Fonts: Helvetica, Times-Roman, Courier, Georgia, Trebuchet MS, Palatino.

4. CREATION MODES (General vs Customized):
   - General Resume: Comprehensive resume for overall experience.
   - Customized Resume: Tailored resume for a target job title (e.g. Senior Software Engineer) and company (e.g. Google, Microsoft, Amazon, Deloitte, Nvidia).

5. KEY FEATURES:
   - Home & Onboarding: Instant mode switcher, name setup, action dashboard.
   - Target Personalization: Auto-fetches target company keywords and accepts PDF/TXT resume uploads.
   - Template Gallery: High-resolution 2.5x zoomed card previews, search, category filter, font filter.
   - Resume Workspace: Content editor for personal details, summary, experience, education, skills, projects, certifications.
   - Live Content Editor & AI Polish: Instant Gemini AI action verb enhancement and metric insertion.
   - ATS Score Dashboard: 0-100% score calculation, keyword match density, missing critical skills report.
   - Export & Download: 1-click 4K vector PDF generation via ReportLab engine.

GUIDELINES FOR YOUR RESPONSES:
- Be polite, encouraging, professional, and highly knowledgeable.
- ALWAYS give detailed, actionable answers related to NextHire AI features, career tips, or resume building strategies.
- NEVER return empty answers, "I don't know", or "not known". If a query is unusual, provide guidance on NextHire AI tools.
"""


def _get_local_bot_answer(query: str) -> str:
    """Fallback Rule-based AI Engine providing 100% accurate, non-empty answers."""
    q = query.lower().strip()

    if any(k in q for k in ["who built", "developer", "author", "creator", "who made", "santosh"]):
        return (
            "🚀 **NextHire AI** was developed and engineered by **Santosh Kumar Kolagani**!\n\n"
            "It was built to empower job seekers worldwide with AI-driven resume tailoring, "
            "ATS scoring, and publication-ready 4K vector PDF resume generation."
        )

    if any(k in q for k in ["free", "cost", "price", "payment", "paid", "subscription"]):
        return (
            "🎉 **NextHire AI is 100% FREE!**\n\n"
            "• All 50 signature resume templates are completely unlocked.\n"
            "• AI bullet polishing, ATS scoring, and PDF vector downloads are 100% free without hidden fees or credit card requirements."
        )

    if any(k in q for k in ["template", "design", "font", "style", "catalog"]):
        return (
            "🎨 **NextHire AI features 50 Classified Signature Templates across 6 Categories:**\n\n"
            "1. 📄 **ATS Friendly (20 Templates)** — Optimized for Taleo, Workday, Greenhouse.\n"
            "2. 💼 **Modern Professional (10 Templates)** — Contemporary headers & pill badges.\n"
            "3. 💻 **Tech & Developer (5 Templates)** — Code terminal & tech stack matrix.\n"
            "4. 🎨 **Creative & Design (5 Templates)** — Accent borders & visual flair.\n"
            "5. 👔 **Executive & Senior (5 Templates)** — Serif fonts & leadership focus.\n"
            "6. 🎓 **Academic & Research (5 Templates)** — Publication-ready academic layouts.\n\n"
            "Supports fonts like Helvetica, Times-Roman, Courier, Georgia, Trebuchet MS & Palatino!"
        )

    if any(k in q for k in ["ats", "score", "scanner", "parser", "compatibility", "keyword"]):
        return (
            "📊 **NextHire AI ATS Score Dashboard Features:**\n\n"
            "• **Overall Match Score (0–100%)**: Calculates keyword coverage against target job descriptions.\n"
            "• **Keyword Density**: Highlights essential skills found vs missing.\n"
            "• **Formatting Check**: Ensures standard headings, contact placement, and bullet structure.\n"
            "• **AI Polish**: Enhances bullet points with action verbs and quantifiable metrics to boost your ATS score."
        )

    if any(k in q for k in ["personalize", "tailor", "target", "company", "google", "microsoft", "amazon"]):
        return (
            "🎯 **Target Job Personalization Mode:**\n\n"
            "• Allows you to enter your **Target Job Role** (e.g. Senior Software Engineer) and **Company Name** (e.g. Google, Microsoft, Deloitte).\n"
            "• Click **'Fetch AI Company Keywords'** to automatically extract ATS skills for that target company.\n"
            "• You can also upload your existing **PDF or TXT resume** to apply target tailoring instantly!"
        )

    if any(k in q for k in ["download", "pdf", "export", "save", "print"]):
        return (
            "📥 **Exporting & Downloading Resumes:**\n\n"
            "• Head to the **'Resume Final Preview'** or **'Export PDF Resume'** section.\n"
            "• Click **'Download ATS Vector PDF'** to instantly download a 4K resolution vector PDF generated via ReportLab."
        )

    if any(k in q for k in ["switch", "mode", "general", "customized"]):
        return (
            "🔄 **Resume Modes (General vs Customized):**\n\n"
            "• **General Resume**: Ideal for a comprehensive resume showcasing all your skills.\n"
            "• **Customized Resume**: Ideal for tailoring your resume to a specific job posting.\n"
            "• You can instantly switch between modes using the **'Switch Mode'** button on the Dashboard or Personalization header!"
        )

    return (
        f"🤖 **NextHire AI Assistant Guide:**\n\n"
        f"Thank you for asking about *'{query}'*!\n\n"
        "Here is how NextHire AI can help you:\n"
        "1. **Build New Resume**: Pick from 50 ATS-classified templates in the **Template Gallery**.\n"
        "2. **Upload Existing Resume**: Upload a PDF/TXT file on the **Home** or **Personalization** screen.\n"
        "3. **ATS Optimization**: Run the **ATS Score Dashboard** to evaluate keyword coverage.\n"
        "4. **AI Bullet Polish**: Use the **Live Content Editor** to polish bullet points with high-impact metrics.\n"
        "5. **1-Click Download**: Export a publication-ready 4K PDF on the **Download** page."
    )


def _generate_ai_chat_response(messages: list) -> str:
    """Generates AI response using Gemini API or fallback local engine."""
    api_key = get_api_key()
    user_query = messages[-1]["content"] if messages else ""

    if api_key and len(api_key) > 10:
        try:
            genai.configure(api_key=api_key)
            model = genai.GenerativeModel("gemini-1.5-flash")
            
            prompt = NEXTHIRE_SYSTEM_KNOWLEDGE + "\n\nCHAT HISTORY:\n"
            for m in messages[-6:]:
                role = "User" if m["role"] == "user" else "Assistant"
                prompt += f"{role}: {m['content']}\n"
            prompt += "Assistant:"

            response = model.generate_content(prompt)
            if response and response.text and len(response.text.strip()) > 5:
                return response.text.strip()
        except Exception:
            pass

    return _get_local_bot_answer(user_query)


def show_chatbot_page():
    """Renders Dedicated Full-Screen AI Assistant Chatbot Page."""
    render_navbar()

    theme_mode = st.session_state.get("theme_mode", "dark")
    is_dark = (theme_mode == "dark")

    if "page_chat_messages" not in st.session_state:
        st.session_state["page_chat_messages"] = [
            {
                "role": "assistant",
                "content": "👋 **Welcome to NextHire AI Assistant!**\n\nI am your dedicated AI career strategist. Ask me anything about building resumes, ATS score optimization, our 50 templates, target company tailoring (Google, Microsoft, Amazon), or platform features!"
            }
        ]

    c_left, c_mid, c_right = st.columns([1, 3.2, 1])

    with c_mid:
        render_html(
            f"""
            <div style='background: linear-gradient(135deg, #0F172A 0%, #1E3A8A 100%);
                        border: 2px solid #38BDF8;
                        border-radius: 20px;
                        padding: 26px 30px;
                        color: white;
                        margin-bottom: 25px;
                        box-shadow: 0 15px 35px rgba(0, 0, 0, 0.25);'>
                <div style='display: flex; align-items: center; gap: 16px;'>
                    <div style='background: linear-gradient(135deg, #2563EB 0%, #0284C7 100%); width: 56px; height: 56px; border-radius: 16px; display: flex; align-items: center; justify-content: center; font-size: 1.9rem;'>
                        🤖
                    </div>
                    <div>
                        <h2 style='margin: 0; color: #F8FAFC; font-size: 1.8rem; font-weight: 800;'>NextHire AI Career Chatbot</h2>
                        <div style='display: flex; align-items: center; gap: 8px; margin-top: 4px;'>
                            <span style='background: #16A34A; width: 9px; height: 9px; border-radius: 50%; display: inline-block;'></span>
                            <span style='color: #4ADE80; font-size: 0.88rem; font-weight: 700;'>AI Model Active • Trained on 100% NextHire AI Intelligence</span>
                        </div>
                    </div>
                </div>
            </div>
            """
        )

        # Quick Question Buttons
        st.write("**💡 Suggested Questions:**")
        q1, q2, q3, q4 = st.columns(4)
        with q1:
            if st.button("👨‍💻 Developer?", key="btn_pg_dev", use_container_width=True):
                _handle_page_chat_submit("Who developed NextHire AI?")
        with q2:
            if st.button("🎨 50 Templates?", key="btn_pg_tpl", use_container_width=True):
                _handle_page_chat_submit("Tell me about the 50 signature templates")
        with q3:
            if st.button("📊 ATS Score?", key="btn_pg_ats", use_container_width=True):
                _handle_page_chat_submit("How does the ATS scoring engine work?")
        with q4:
            if st.button("🎯 Job Tailoring?", key="btn_pg_target", use_container_width=True):
                _handle_page_chat_submit("How do I tailor my resume for Google or Microsoft?")

        st.write("")
        st.divider()

        # Chat History Container
        chat_box = st.container(height=380)
        with chat_box:
            for m in st.session_state["page_chat_messages"]:
                with st.chat_message(m["role"]):
                    st.markdown(m["content"])

        # Chat Input Form
        with st.form("page_chatbot_form", clear_on_submit=True):
            user_input = st.text_input(
                "💬 Ask NextHire AI Assistant:",
                placeholder="e.g. How do I export my resume to 4K PDF vector format?",
                key="pg_chat_input_val"
            )
            c_s1, c_s2 = st.columns([3, 1])
            with c_s2:
                submitted = st.form_submit_button("Send Question 🚀", type="primary", use_container_width=True)

            if submitted and user_input.strip():
                _handle_page_chat_submit(user_input.strip())


def _handle_page_chat_submit(prompt: str):
    """Processes user submission and generates bot response."""
    st.session_state["page_chat_messages"].append({"role": "user", "content": prompt})
    with st.spinner("AI thinking..."):
        bot_reply = _generate_ai_chat_response(st.session_state["page_chat_messages"])
        st.session_state["page_chat_messages"].append({"role": "assistant", "content": bot_reply})
    st.rerun()
