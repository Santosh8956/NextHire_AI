"""
===========================================================
Project     : NextHire AI
File        : resume_analysis.py
Author      : Santosh Kolagani

Purpose:
    ATS Resume Strength Evaluation Dashboard with Interactive Direct
    Redirection, Return to Preview Hub, and Return to Workspace Edit options.
===========================================================
"""

import streamlit as st
from app.components.navbar import render_navbar
from app.services.analyzer.resume_analyzer import analyze_resume_strength
from app.config.settings import get_api_key
from app.utils.image_generator import generate_template_preview_image
from app.config.constants import TEMPLATES
from app.utils.helpers import render_html


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
        render_html(
            f"""
            <div style='background: #0F172A; border: 2px solid {color}; padding: 16px; border-radius: 12px; text-align: center; color: white;'>
                <h3 style='color: #94A3B8; font-size: 0.85rem; margin: 0;'>OVERALL RESUME SCORE</h3>
                <h1 style='color: {color}; font-size: 2.8rem; margin: 5px 0;'>{overall} / 100</h1>
            </div>
            """
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

        render_html(
            f"""
            <div style='background-color: #0F172A; border: 2px solid {t_info.get("color", "#2563EB")}; padding: 18px; border-radius: 12px; margin-bottom: 20px; color: white;'>
                <div style='display: flex; justify-content: space-between; align-items: center;'>
                    <h3 style='margin: 0; color: #F8FAFC;'>👁️ FINAL RESUME LOOK PREVIEW ({t_info.get('name')})</h3>
                    <span style='background: {t_info.get("color")}; color: white; padding: 4px 12px; border-radius: 12px; font-weight: bold;'>
                        {t_info.get('layout_style', 'default').replace('_', ' ').title()}
                    </span>
                </div>
            </div>
            """
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
            render_html(
                f"""
                <div style='background: #F0FDF4; border-left: 4px solid #16A34A; padding: 12px; border-radius: 6px; margin-bottom: 10px; color: #166534;'>
                    ✔️ <b>{s}</b>
                </div>
                """
            )

        st.markdown("### 🎯 ATS Keyword Match Breakdown")
        matched_kws = analysis.get("matched_keywords", [])
        missing_kws = analysis.get("missing_keywords", [])

        if matched_kws:
            st.markdown("**Matched Target Keywords:**")
            matched_html = " ".join([f"<span style='background: #DCFCE7; color: #15803D; padding: 4px 10px; border-radius: 12px; font-weight: 600; font-size: 0.85rem; display: inline-block; margin: 3px;'>✓ {kw}</span>" for kw in matched_kws])
            render_html(f"<div style='margin-bottom: 14px;'>{matched_html}</div>")

        if missing_kws:
            st.markdown("**Missing Target Keywords (Add to Boost Score):**")
            missing_html = " ".join([f"<span style='background: #FEE2E2; color: #991B1B; padding: 4px 10px; border-radius: 12px; font-weight: 600; font-size: 0.85rem; display: inline-block; margin: 3px;'>⚠️ {kw}</span>" for kw in missing_kws[:12]])
            render_html(f"<div style='margin-bottom: 14px;'>{missing_html}</div>")
        elif not matched_kws and not missing_kws:
            st.info("Paste a Target Job Description in the Details Workspace to unlock full target keyword matching!")

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
                    render_html(
                        f"""
                        <div style='background: #FEF2F2; border-left: 4px solid #DC2626; padding: 12px 16px; border-radius: 8px 8px 0 0; margin-top: 10px;'>
                            <div style='display: flex; justify-content: space-between; align-items: center;'>
                                <span style='color: #991B1B; font-weight: bold;'>❌ {imp.get('issue')}</span>
                                <span style='background: #FEE2E2; color: #991B1B; padding: 2px 8px; border-radius: 6px; font-size: 0.75rem;'>{imp.get('category')}</span>
                            </div>
                            <p style='color: #7F1D1D; font-size: 0.85rem; margin-top: 6px; margin-bottom: 0;'>💡 <i>{imp.get('recommendation')}</i></p>
                        </div>
                        """
                    )
                    
                    btn_label = imp.get("button_label", "➡️ Fix Issue in Editor")
                    target_p = imp.get("target_page", "resume_editor")
                    focus_sec = imp.get("editor_focus", "summary")

                    if st.button(btn_label, key=f"fix_btn_{idx}", use_container_width=True, type="primary"):
                        st.session_state["return_to_page"] = "resume_analysis"
                        st.session_state["current_page"] = target_p
                        st.session_state["editor_focus"] = focus_sec
                        st.rerun()

                    st.write("")

    st.write("")
    st.divider()

    # Bottom Navigation Action Bar with BOTH Return to Final Preview Hub and Return to Workspace Edit options
    col_nav1, col_nav2, col_nav3, col_nav4 = st.columns([1.2, 1.2, 1.3, 1.3])

    with col_nav1:
        if st.button("⬅️ Return to Final Preview Hub", use_container_width=True):
            ret_p = st.session_state.pop("return_to_page", "preview")
            st.session_state["current_page"] = ret_p
            st.rerun()

    with col_nav2:
        if st.button("✍️ Return to Workspace Edit", use_container_width=True):
            st.session_state["current_page"] = "data_collection"
            st.rerun()

    with col_nav3:
        if st.button("👁️ Preview Resume Final Look", use_container_width=True):
            st.session_state["show_analysis_preview"] = not st.session_state.get("show_analysis_preview", False)
            st.rerun()

    with col_nav4:
        if st.button("Proceed to Download PDF 📥", type="primary", use_container_width=True):
            st.session_state["current_page"] = "download"
            st.rerun()
