"""
===========================================================
Project     : NextHire AI
File        : buttons.py
Author      : Santosh Kolagani

Purpose:
Reusable button components for the entire application.

Responsibilities:
- Primary Button
- Secondary Button
- Outline Button
- Success Button
- Danger Button
- Disabled Button
===========================================================
"""

# ==========================================================
# Imports
# ==========================================================

import streamlit as st


# ==========================================================
# Primary Button
# ==========================================================

def primary_button(
    label: str,
    key: str = None,
    use_container_width: bool = True
) -> bool:
    """
    Primary Call-To-Action Button.
    """

    return st.button(
        label,
        key=key,
        type="primary",
        use_container_width=use_container_width
    )


# ==========================================================
# Secondary Button
# ==========================================================

def secondary_button(
    label: str,
    key: str = None,
    use_container_width: bool = True
) -> bool:
    """
    Standard Secondary Button.
    """

    return st.button(
        label,
        key=key,
        use_container_width=use_container_width
    )


# ==========================================================
# Outline Button
# ==========================================================

def outline_button(
    label: str,
    key: str = None,
    use_container_width: bool = True
) -> bool:
    """
    Outline Button.
    """

    return st.button(
        label,
        key=key,
        use_container_width=use_container_width
    )


# ==========================================================
# Success Button
# ==========================================================

def success_button(
    label: str,
    key: str = None,
    use_container_width: bool = True
) -> bool:
    """
    Success Action Button.
    """

    return st.button(
        f"✅ {label}",
        key=key,
        use_container_width=use_container_width
    )


# ==========================================================
# Danger Button
# ==========================================================

def danger_button(
    label: str,
    key: str = None,
    use_container_width: bool = True
) -> bool:
    """
    Danger Action Button.
    """

    return st.button(
        f"❌ {label}",
        key=key,
        use_container_width=use_container_width
    )


# ==========================================================
# Disabled Button
# ==========================================================

def disabled_button(
    label: str,
    use_container_width: bool = True
):
    """
    Disabled Button.
    """

    st.button(
        label,
        disabled=True,
        use_container_width=use_container_width
    )