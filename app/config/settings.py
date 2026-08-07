"""
===========================================================
Project     : NextHire AI
File        : settings.py
Author      : Santosh Kolagani

Purpose:
    Configuration parameters and Gemini API key management.
===========================================================
"""

import os
from dotenv import load_dotenv

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY", "")
DEFAULT_MODEL = "gemini-1.5-flash"


def get_api_key():
    """Retrieve Gemini API key from Streamlit session state or environment."""
    import streamlit as st
    if "api_key" in st.session_state and st.session_state["api_key"]:
        return st.session_state["api_key"]
    return os.getenv("GEMINI_API_KEY", "")
