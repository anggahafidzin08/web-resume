"""
Navigation component for the web resume application.
Provides consistent navigation across all pages.
"""

import streamlit as st

from src.utils.data_loader import load_resume_data


def render_navigation(active_page: str = "Home"):
    """
    Render the main navigation sidebar.
    
    Args:
        active_page: Name of the currently active page
    """
    resume_data = load_resume_data()
    personal = resume_data.get("personal", {})
    with st.sidebar:
        # Profile section
        st.markdown("### 👤 " + personal.get("name", "Angga Putra Hafidzin"))
        st.markdown("**" + personal.get("title", "Data Engineer") + "**")
        st.divider()
        
        # Navigation links
        pages = {
            "Home": "🏠 Home",
            "Resume": "📄 Resume",
            "Portfolio": "💼 Portfolio"
        }
        
        st.markdown("### Navigation")
        
        for page_key, page_label in pages.items():
            if page_key == active_page:
                st.button(
                    page_label,
                    key=f"nav_{page_key}",
                    use_container_width=True,
                    type="primary"
                )
            else:
                if st.button(
                    page_label,
                    key=f"nav_{page_key}",
                    use_container_width=True
                ):
                    # Navigate to the selected page
                    st.session_state.current_page = page_key
                    st.rerun()
        
        st.divider()
        
        # Social links
        st.markdown("### Connect")
        st.markdown(
            f"[📧 Email](mailto:{personal.get('email', 'anggaputrahafidzin@gmail.com')})"
        )
        st.markdown(
            f"[💼 LinkedIn]({personal.get('linkedin', 'anggaph')})"
        )
        st.markdown(
            f"[🐙 GitHub]({personal.get('github', 'anggahafdz08')})"
        )


def render_mobile_nav():
    """
    Render mobile-friendly top navigation.
    Shows when screen width is small.
    """
    # Create columns for mobile nav
    cols = st.columns(4)
    
    pages = ["Home", "Resume", "Portfolio"]
    icons = ["🏠", "📄", "💼"]
    
    for i, (page, icon) in enumerate(zip(pages, icons)):
        with cols[i]:
            if page == st.session_state.get("current_page", "Home"):
                if st.button(f"{icon}", key=f"mobile_{page}", use_container_width=True):
                    st.session_state.current_page = page
                    st.rerun()


def get_current_page() -> str:
    """
    Get the current active page from session state.
    
    Returns:
        str: Current page name
    """
    return st.session_state.get("current_page", "Home")


def set_page(page_name: str):
    """
    Set the current page in session state.
    
    Args:
        page_name: Name of the page to navigate to
    """
    st.session_state.current_page = page_name
