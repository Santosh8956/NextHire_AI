"""
===========================================================
Project     : NextHire AI
File        : chatbot.py
Author      : Santosh Kolagani

Purpose:
    Floating AI Chatbot Widget rendered at bottom-right corner across all pages.
    Trained with full knowledge about NextHire AI features, templates, ATS scoring,
    and developer details, providing zero empty fallback answers.
===========================================================
"""

import streamlit as st
import google.generativeai as genai
from app.config.settings import get_api_key
from app.utils.helpers import render_html


# Exhaustive System Prompt & Knowledge Base for NextHire AI
NEXTHIRE_SYSTEM_KNOWLEDGE = """
You are NextHire AI Assistant, an intelligent career strategist and customer support bot for the NextHire AI platform.
Developed by Santosh Kumar Kolagani, NextHire AI is a state-of-the-art AI Career Assistant & Resume Builder v2.0.

KEY PLATFORM INFORMATION & DETAILS:
1. PLATFORM OVERVIEW:
   - NextHire AI is 100% free, private, and encrypted. No credit card or mandatory account creation required.
   - It empowers job seekers to create, edit, ATS-optimize, and export publication-ready 4K ATS vector PDF resumes.

2. DEVELOPER DETAILS:
   - Developed and engineered by Santosh Kumar Kolagani.

3. TEMPLATE CATALOG (50 Signature Templates across 6 Categories):
   - ATS Friendly (20 Templates): Maximum parser compatibility, clean single & double column layouts.
   - Modern Professional (10 Templates): Sleek header banners, pill badges, contemporary typography.
   - Tech & Developer (5 Templates): Code terminal themes, technical skill matrix focus.
   - Creative & Design (5 Templates): Vibrant accent borders, portfolio-ready styling.
   - Executive & Senior (5 Templates): Elegant serif typography, executive summary focus.
   - Academic & Research (5 Templates): Scholarly publications, thesis & grant formatting.
   - Supported Fonts: Helvetica, Times-Roman, Courier, Georgia, Trebuchet MS, Palatino.

4. CREATION MODES (General vs Customized):
   - General Resume: Versatile resume highlighting overall experience, projects, and skills.
   - Customized Resume: Tailors bullets, summary, and keywords for a specific target job title (e.g. Data Scientist) and company (e.g. Google, Microsoft, Amazon, Deloitte, Nvidia).

5. KEY FEATURES & PAGES:
   - Home & Onboarding: Instant mode switcher, name personalization, quick action dashboard.
   - Target Personalization: Auto-fetches company keywords using Gemini AI and accepts existing resume PDF/TXT uploads.
   - Template Gallery: High-resolution 2.5x zoomed card previews, search, category filter, font filter, and layout views.
   - Resume Workspace: Full content editing for personal details, summary, experience, education, skills, projects, certifications, custom sections.
   - Content Editor & AI Polish: Instant AI bullet point polishing, action verb enhancement, and grammar fixes.
   - ATS Score Dashboard: 0-100% score rating, keyword density analysis, missing skills report, and score improvement roadmap.
   - Export & Download: 1-click 4K vector PDF generation via ReportLab engine.

GUIDELINES FOR YOUR RESPONSES:
- Be polite, encouraging, professional, and highly knowledgeable.
- ALWAYS give helpful, detailed answers related to NextHire AI features, career tips, or resume building strategies.
- NEVER return empty answers, "I don't know", or "not known". If a query is unusual, explain how NextHire AI tools can solve career challenges.
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


def render_floating_chatbot():
    """Renders sleek floating chatbot widget at bottom-right corner across all pages."""
    theme_mode = st.session_state.get("theme_mode", "dark")
    is_dark = (theme_mode == "dark")

    if "chatbot_open" not in st.session_state:
        st.session_state["chatbot_open"] = False
    if "chatbot_messages" not in st.session_state:
        st.session_state["chatbot_messages"] = [
            {
                "role": "assistant",
                "content": "👋 **Hi! I'm NextHire AI Assistant.** Ask me anything about creating resumes, ATS scores, 50 templates, or platform features!"
            }
        ]

    bot_open = st.session_state["chatbot_open"]

    # Styled Floating Trigger Button & Chat Container in Bottom Right
    hdr_bg = "#0F172A" if is_dark else "#1E3A8A"

    col_void, col_bot = st.columns([3.5, 1.2])
    with col_bot:
        if not bot_open:
            if st.button("💬 Chatbot 🤖", key="btn_toggle_float_bot", type="primary", use_container_width=True):
                st.session_state["chatbot_open"] = True
                st.rerun()
        else:
            render_html(
                f"""
                <div style='background: {hdr_bg}; border: 2px solid #38BDF8; border-radius: 16px 16px 0 0; padding: 12px 16px; color: white;'>
                    <div style='display: flex; justify-content: space-between; align-items: center;'>
                        <div style='display: flex; align-items: center; gap: 8px;'>
                            <span style='font-size: 1.3rem;'>🤖</span>
                            <div>
                                <h4 style='margin: 0; color: #F8FAFC; font-size: 1rem; font-weight: 700;'>NextHire AI Assistant</h4>
                                <span style='color: #4ADE80; font-size: 0.75rem; font-weight: 600;'>Online • Ready to Answer</span>
                            </div>
                        </div>
                    </div>
                </div>
                """
            )

            if st.button("❌ Close Chatbot", key="btn_close_float_bot", use_container_width=True):
                st.session_state["chatbot_open"] = False
                st.rerun()

            # Chat History Container
            chat_container = st.container(height=260)
            with chat_container:
                for msg in st.session_state["chatbot_messages"]:
                    with st.chat_message(msg["role"]):
                        st.markdown(msg["content"])

            # Quick Suggestion Chips
            st.caption("Quick Questions:")
            q1, q2 = st.columns(2)
            with q1:
                if st.button("🚀 How to build?", key="btn_sq_build", use_container_width=True):
                    _process_user_chat_input("How do I create a resume on NextHire AI?")
            with q2:
                if st.button("🎨 50 Templates?", key="btn_sq_tpl", use_container_width=True):
                    _process_user_chat_input("Tell me about the 50 resume templates")

            # Chat Input Form
            with st.form("nxt_bot_form", clear_on_submit=True):
                user_text = st.text_input("Ask a question about NextHire AI...", key="nxt_bot_input_field", placeholder="e.g. How does ATS scoring work?")
                submit_chat = st.form_submit_button("Send 📩", type="primary", use_container_width=True)

                if submit_chat and user_text.strip():
                    _process_user_chat_input(user_text.strip())

    # Add Launcher to Sidebar as well for easy access
    with st.sidebar:
        st.markdown("---")
        if st.button("🤖 Launch AI Chatbot Widget", key="btn_sidebar_launch_bot", use_container_width=True):
            st.session_state["chatbot_open"] = not st.session_state["chatbot_open"]
            st.rerun()


def _process_user_chat_input(prompt_text: str):
    """Processes chat input and appends assistant response."""
    st.session_state["chatbot_messages"].append({"role": "user", "content": prompt_text})
    ai_reply = _generate_ai_chat_response(st.session_state["chatbot_messages"])
    st.session_state["chatbot_messages"].append({"role": "assistant", "content": ai_reply})
    st.rerun()
