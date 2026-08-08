"""
===========================================================
Project     : NextHire AI
File        : settings.py
Author      : Santosh Kolagani

Purpose:
    Configuration parameters and integrated Gemini API key management.
===========================================================
"""

import os
import streamlit as st
from dotenv import load_dotenv

load_dotenv()

# Read Gemini API Key from environment or Streamlit secrets safely
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY", "")
DEFAULT_MODEL = "gemini-1.5-flash"


def get_api_key():
    """Retrieve integrated Gemini API key seamlessly from session, env, or secrets."""
    if "api_key" in st.session_state and st.session_state["api_key"]:
        return st.session_state["api_key"]
    
    env_key = os.getenv("GEMINI_API_KEY")
    if env_key:
        return env_key
        
    try:
        if hasattr(st, "secrets") and "GEMINI_API_KEY" in st.secrets:
            return st.secrets["GEMINI_API_KEY"]
    except Exception:
        pass
        
    return GEMINI_API_KEY
