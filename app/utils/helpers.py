"""
===========================================================
Project     : NextHire AI
File        : helpers.py
Author      : Santosh Kolagani

Purpose:
    Bulletproof HTML renderer for Streamlit that completely strips all
    leading indentation from every line, ensuring Markdown NEVER renders code blocks.
===========================================================
"""

import streamlit as st


def render_html(html_str: str):
    """
    Strips leading whitespace from every line of HTML and renders it in Streamlit.
    Guarantees no line starts with 4+ spaces so Markdown will NEVER create a code block.
    """
    clean_lines = [line.lstrip() for line in html_str.splitlines()]
    clean_html = "\n".join(clean_lines).strip()
    st.markdown(clean_html, unsafe_allow_html=True)
