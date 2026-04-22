"""
Web Resume Application - Main Entry Point
A multi-page web application showcasing professional resume and portfolio.
"""

import streamlit as st
from src.pages import (
    render_home,
    render_resume,
    render_portfolio,
    render_project_detail
)
from src.components import render_navigation


# Page configuration
st.set_page_config(
    page_title="Angga Putra Hafidzin - Data Engineer & Analyst",
    page_icon="👨‍💻",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'https://github.com/yourusername/web-resume',
        'Report a bug': "https://github.com/yourusername/web-resume/issues",
        'About': "# Web Resume\nThis is a professional portfolio built with Streamlit."
    }
)

# Custom CSS for modern styling
st.markdown(
    """
    <style>
    /* Main container styling */
    .stApp {
        background-color: #F9FAFB;
    }
    
    /* Header styling */
    h1, h2, h3, h4, h5, h6 {
        font-family: 'Segoe UI', sans-serif;
        color: #1F2937;
    }
    
    /* Button styling */
    .stButton>button {
        border-radius: 10px;
        font-weight: 600;
        transition: all 0.3s ease;
    }
    
    .stButton>button:hover {
        transform: translateY(-2px);
        box-shadow: 0 4px 8px rgba(0,0,0,0.1);
    }
    
    /* Card styling */
    .stContainer {
        border-radius: 15px;
        padding: 20px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.05);
    }
    
    /* Sidebar styling */
    section[data-testid="stSidebar"] {
        background-color: #FFFFFF;
    }
    
    /* Metric styling */
    [data-testid="stMetricValue"] {
        font-size: 24px;
        color: #2563EB;
    }
    
    /* Hide Streamlit branding */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    </style>
    """,
    unsafe_allow_html=True
)

# Initialize session state
if "current_page" not in st.session_state:
    st.session_state.current_page = "Home"
if "selected_project" not in st.session_state:
    st.session_state.selected_project = None


def main():
    """
    Main application function.
    """
    # Render sidebar navigation
    render_navigation(active_page=st.session_state.current_page)
    
    # Main content area
    current_page = st.session_state.current_page
    
    # Route to appropriate page
    if current_page == "Home":
        render_home()
    elif current_page == "Resume":
        render_resume()
    elif current_page == "Portfolio":
        render_portfolio()
    elif current_page == "Project Detail":
        render_project_detail()
    else:
        # Default to home
        render_home()
    
    # Footer
    st.markdown("")
    st.divider()
    st.markdown(
        """
        <div style="
            text-align: center;
            color: #6B7280;
            padding: 20px;
            font-size: 14px;
        ">
            <p>
                © 2026 Angga Putra Hafidzin. Built with ❤️ using 
                <a href="https://streamlit.io" target="_blank" style="color: #2563EB;">Streamlit</a>
            </p>
            <p>
                <a href="https://github.com/anggahafidzin08/web-resume" target="_blank" style="color: #2563EB;">
                    View Source Code
                </a>
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )


if __name__ == "__main__":
    main()