"""
===========================================================
Project     : NextHire AI
File        : cards.py
Author      : Santosh Kolagani

Purpose:
Reusable card components used throughout the application.

Responsibilities:
- Statistics Cards
- Feature Cards
- Template Cards
- AI Insight Cards
===========================================================
"""

# ==========================================================
# Imports
# ==========================================================

import streamlit as st


# ==========================================================
# Statistics Card
# ==========================================================

def stats_card(
    title: str,
    value: str,
    icon: str = "📊"
):
    """
    Display a statistics card.
    """

    st.metric(
        label=f"{icon} {title}",
        value=value
    )


# ==========================================================
# Feature Card
# ==========================================================

def feature_card(
    title: str,
    description: str,
    icon: str = "✨"
):
    """
    Display a feature card.
    """

    with st.container(border=True):

        st.markdown(f"## {icon}")

        st.subheader(title)

        st.write(description)


# ==========================================================
# Resume Template Card
# ==========================================================

def template_card(
    template_name: str,
    description: str
):
    """
    Display a resume template card.
    """

    with st.container(border=True):

        st.subheader(template_name)

        st.write(description)

        st.button(
            "Use Template",
            key=f"template_{template_name}",
            use_container_width=True
        )


# ==========================================================
# AI Insight Card
# ==========================================================

def ai_insight_card(
    title: str,
    message: str
):
    """
    Display AI recommendations.
    """

    with st.container(border=True):

        st.subheader(f"💡 {title}")

        st.info(message)


# ==========================================================
# Success Card
# ==========================================================

def success_card(message: str):
    """
    Display success message.
    """

    st.success(message)


# ==========================================================
# Warning Card
# ==========================================================

def warning_card(message: str):
    """
    Display warning message.
    """

    st.warning(message)


# ==========================================================
# Error Card
# ==========================================================

def error_card(message: str):
    """
    Display error message.
    """

    st.error(message)