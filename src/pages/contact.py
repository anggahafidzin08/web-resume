"""
Contact page with contact form and information.
"""

import streamlit as st
from src.components import (
    render_contact_form,
    render_contact_info,
    render_social_links
)


def render_contact():
    """
    Render the contact page.
    """
    # Page header
    st.markdown(
        f"""
        <div style="
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            padding: 40px 20px;
            border-radius: 20px;
            text-align: center;
            color: white;
            margin-bottom: 30px;
        ">
            <h1 style="font-size: 42px; margin-bottom: 10px;">
                📧 Contact
            </h1>
            <p style="font-size: 18px; opacity: 0.9;">
                Let's start a conversation
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )
    
    # Two column layout
    col1, col2 = st.columns([2, 1])
    
    with col1:
        # Contact form
        render_contact_form()
    
    with col2:
        # Contact information
        render_contact_info()
        
        st.divider()
        
        # Social links
        render_social_links()
    
    st.divider()
    
    # FAQ Section
    st.markdown("### ❓ Frequently Asked Questions")
    
    faq_cols = st.columns(2)
    
    with faq_cols[0]:
        with st.expander("**What's your typical response time?**"):
            st.markdown(
                """
                I typically respond within 24-48 hours during business days. 
                For urgent matters, please mention it in your message subject.
                """
            )
        
        with st.expander("**Are you available for freelance work?**"):
            st.markdown(
                """
                Yes! I'm open to freelance projects and consulting opportunities. 
                Please provide details about your project in the contact form.
                """
            )
    
    with faq_cols[1]:
        with st.expander("**What types of projects do you work on?**"):
            st.markdown(
                """
                I specialize in web applications, data visualization, 
                and Python-based solutions. Open to discussing various project types.
                """
            )
        
        with st.expander("**Do you work remotely?**"):
            st.markdown(
                """
                Yes, I'm comfortable working remotely with teams worldwide. 
                Available for video calls and asynchronous collaboration.
                """
            )
    
    # Map/Location section (optional)
    st.divider()
    
    st.markdown("### 📍 Location")
    
    st.markdown(
        """
        <div style="
            background-color: #F3F4F6;
            padding: 30px;
            border-radius: 15px;
            text-align: center;
        ">
            <p style="font-size: 18px; color: #1F2937;">
                🇮🇩 Based in Indonesia
            </p>
            <p style="color: #6B7280; margin-top: 10px;">
                Available for remote work worldwide
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )
    
    # Final CTA
    st.markdown("")
    st.markdown(
        """
        <div style="
            text-align: center;
            padding: 30px;
        ">
            <h3 style="color: #2563EB;">
                💡 Prefer email?
            </h3>
            <p style="color: #6B7280;">
                Send me a direct email at 
                <a href="mailto:anggaputrahafidzin@gmail.com" style="color: #2563EB;">
                    anggaputrahafidzin@gmail.com
                </a>
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )
