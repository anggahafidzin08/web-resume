"""
Navigation component for the web resume application.
Provides consistent navigation across all pages.
"""

import streamlit as st


def render_navigation(active_page: str = "Home"):
    """
    Render the main navigation sidebar.
    
    Args:
        active_page: Name of the currently active page
    """
    with st.sidebar:
        # Profile section
        st.markdown("### 👤 Angga Putra Hafidzin")
        st.markdown("**Data Engineer**")
        st.divider()
        
        # Navigation links
        pages = {
            "Home": "🏠 Home",
            "Resume": "📄 Resume",
            "Portfolio": "💼 Portfolio",
            "Contact": "📧 Contact"
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
            "[📧 Email](mailto:anggaputrahafidzin@gmail.com)"
        )
        st.markdown(
            "[💼 LinkedIn](https://linkedin.com/in/anggaph)"
        )
        st.markdown(
            "[🐙 GitHub](https://github.com/anggahafdz08)"
        )
        
        # Contact CTA
        st.divider()
        if st.button("📩 Get in Touch", use_container_width=True):
            st.session_state.current_page = "Contact"
            st.rerun()


def render_mobile_nav():
    """
    Render mobile-friendly top navigation.
    Shows when screen width is small.
    """
    # Create columns for mobile nav
    cols = st.columns(4)
    
    pages = ["Home", "Resume", "Portfolio", "Contact"]
    icons = ["🏠", "📄", "💼", "📧"]
    
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
