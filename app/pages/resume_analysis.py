"""
===========================================================
Project     : NextHire AI
File        : resume_analysis.py
Author      : Santosh Kolagani

Purpose:
    ATS Resume Strength Evaluation Dashboard with Interactive Direct
    Redirection and Inline "Preview Resume Final Look" Feature.
===========================================================
"""

import streamlit as st
from app.components.navbar import render_navbar
from app.services.analyzer.resume_analyzer import analyze_resume_strength
from app.config.settings import get_api_key
from app.utils.image_generator import generate_template_preview_image
from app.config.constants import TEMPLATES


def show_resume_analysis():
    """Renders ATS Score Dashboard with direct redirection & Final Look Resume Preview."""
    render_navbar()

    st.markdown("## 📊 Step 4: ATS Resume Strength & Optimization Dashboard")
    st.caption("AI-powered evaluation checking ATS compatibility, keyword coverage, and content impact. Click any improvement area below to jump directly to the editor.")

    resume = st.session_state.get("resume_data", {})
    if not resume:
        st.warning("No resume data found.")
        return

    api_key = get_api_key()

    with st.spinner("Analyzing resume against ATS standards..."):
        analysis = analyze_resume_strength(resume, api_key=api_key)
        resume["analysis"] = analysis
        st.session_state["resume_data"] = resume

    overall = analysis.get("overall_score", 80)
    ats = analysis.get("ats_compatibility_score", 80)
    quality = analysis.get("content_quality_score", 80)
    fmt = analysis.get("formatting_score", 80)

    # Score Metrics Cards
    c1, c2, c3, c4 = st.columns(4)
    with c1:
        color = "#16A34A" if overall >= 80 else ("#D97706" if overall >= 65 else "#DC2626")
        st.markdown(
            f"""
            <div style='background: #0F172A; border: 2px solid {color}; padding: 16px; border-radius: 12px; text-align: center; color: white;'>
                <h3 style='color: #94A3B8; font-size: 0.85rem; margin: 0;'>OVERALL RESUME SCORE</h3>
                <h1 style='color: {color}; font-size: 2.8rem; margin: 5px 0;'>{overall} / 100</h1>
            </div>
            """,
            unsafe_allow_html=True
        )
    with c2:
        st.metric("ATS Compatibility", f"{ats}%")
    with c3:
        st.metric("Content Quality", f"{quality}%")
    with c4:
        st.metric("Formatting & Structure", f"{fmt}%")

    st.write("")
    st.divider()

    # ---------------------------------------------------------
    # INLINE FINAL LOOK RESUME PREVIEW DRAWER
    # ---------------------------------------------------------
    if st.session_state.get("show_analysis_preview"):
        selected_template = st.session_state.get("selected_template", "ats_1")
        if selected_template not in TEMPLATES:
            selected_template = "ats_1"
        t_info = TEMPLATES.get(selected_template, list(TEMPLATES.values())[0])

        st.markdown(
            f"""
            <div style='background-color: #0F172A; border: 2px solid {t_info.get("color", "#2563EB")}; padding: 18px; border-radius: 12px; margin-bottom: 20px; color: white;'>
                <div style='display: flex; justify-content: space-between; align-items: center;'>
                    <h3 style='margin: 0; color: #F8FAFC;'>👁️ FINAL RESUME LOOK PREVIEW ({t_info.get('name')})</h3>
                    <span style='background: {t_info.get("color")}; color: white; padding: 4px 12px; border-radius: 12px; font-weight: bold;'>
                        {t_info.get('layout_style', 'default').replace('_', ' ').title()}
                    </span>
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

        try:
            preview_png = generate_template_preview_image(t_info, resume_data=resume)
            st.image(
                preview_png,
                caption=f"Final Look Document Render — {t_info.get('name')}",
                use_container_width=True
            )
        except Exception as e:
            st.error(f"Error loading preview image: {e}")

        if st.button("❌ Close Preview Drawer", key="close_analysis_preview_btn", use_container_width=True):
            st.session_state["show_analysis_preview"] = False
            st.rerun()

        st.divider()

    col_l, col_r = st.columns([1, 1])

    # ---------------------------------------------------------
    # LEFT COLUMN: Strengths & Missing Keywords
    # ---------------------------------------------------------
    with col_l:
        st.markdown("### ✅ Resume Strengths")
        for s in analysis.get("strengths", []):
            st.markdown(
                f"""
                <div style='background: #F0FDF4; border-left: 4px solid #16A34A; padding: 12px; border-radius: 6px; margin-bottom: 10px; color: #166534;'>
                    ✔️ <b>{s}</b>
                </div>
                """,
                unsafe_allow_html=True
            )

        st.markdown("### 🔑 Missing Job Keywords")
        keywords = analysis.get("missing_keywords", [])
        if keywords:
            for kw in keywords:
                st.markdown(
                    f"""
                    <div style='background: #FFFBEB; border-left: 4px solid #D97706; padding: 10px; border-radius: 6px; margin-bottom: 8px; color: #92400E;'>
                        ⚠️ Missing Target Keyword: <b>{kw}</b>
                    </div>
                    """,
                    unsafe_allow_html=True
                )
        else:
            st.info("No critical missing keywords detected!")

    # ---------------------------------------------------------
    # RIGHT COLUMN: Interactive Areas for Improvement with Redirect Buttons
    # ---------------------------------------------------------
    with col_r:
        st.markdown("### ⚠️ Areas for Improvement (Click to Fix)")
        st.caption("Click any item below to jump directly to that section in the editor:")

        improvements = analysis.get("improvements", [])
        if not improvements:
            st.success("🎉 Excellent! No critical improvement areas detected.")
        else:
            for idx, imp in enumerate(improvements):
                with st.container():
                    st.markdown(
                        f"""
                        <div style='background: #FEF2F2; border-left: 4px solid #DC2626; padding: 12px 16px; border-radius: 8px 8px 0 0; margin-top: 10px;'>
                            <div style='display: flex; justify-content: space-between; align-items: center;'>
                                <span style='color: #991B1B; font-weight: bold;'>❌ {imp.get('issue')}</span>
                                <span style='background: #FEE2E2; color: #991B1B; padding: 2px 8px; border-radius: 6px; font-size: 0.75rem;'>{imp.get('category')}</span>
                            </div>
                            <p style='color: #7F1D1D; font-size: 0.85rem; margin-top: 6px; margin-bottom: 0;'>💡 <i>{imp.get('recommendation')}</i></p>
                        </div>
                        """,
                        unsafe_allow_html=True
                    )
                    
                    btn_label = imp.get("button_label", "➡️ Fix Issue in Editor")
                    target_p = imp.get("target_page", "resume_editor")
                    focus_sec = imp.get("editor_focus", "summary")

                    if st.button(btn_label, key=f"fix_btn_{idx}", use_container_width=True, type="primary"):
                        st.session_state["current_page"] = target_p
                        st.session_state["editor_focus"] = focus_sec
                        st.rerun()

                    st.write("")

    st.write("")
    st.divider()

    # Bottom Navigation Action Bar with Preview Resume Final Look Button
    col_nav1, col_nav2, col_nav3 = st.columns([1.2, 1.5, 1.5])

    with col_nav1:
        if st.button("⬅️ Back to Editor", use_container_width=True):
            st.session_state["current_page"] = "resume_editor"
            st.rerun()

    with col_nav2:
        if st.button("👁️ Preview Resume Final Look", use_container_width=True):
            st.session_state["show_analysis_preview"] = not st.session_state.get("show_analysis_preview", False)
            st.rerun()

    with col_nav3:
        if st.button("Proceed to Download PDF 📥", type="primary", use_container_width=True):
            st.session_state["current_page"] = "download"
            st.rerun()
