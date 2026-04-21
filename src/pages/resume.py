"""
Resume page component displaying comprehensive CV information.
"""

import streamlit as st
from src.utils.data_loader import load_resume_data
from src.components import (
    render_skill_bar,
    render_skill_tag,
    render_experience_item,
    render_education_item
)


def render_resume():
    """
    Render the resume/CV page.
    """
    # Load resume data
    resume_data = load_resume_data()
    
    personal = resume_data.get("personal", {})
    summary = resume_data.get("summary", "")
    experience = resume_data.get("experience", [])
    education = resume_data.get("education", [])
    skills = resume_data.get("skills", {})
    certifications = resume_data.get("certifications", [])
    awards = resume_data.get("awards", [])
    
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
                📄 Resume
            </h1>
            <p style="font-size: 18px; opacity: 0.9;">
                Comprehensive overview of my professional journey
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )
    
    # Personal Information Section
    st.markdown("### 👤 Personal Information")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown(f"**📧 Email:**")
        st.markdown(f"[{personal.get('email', 'N/A')}](mailto:{personal.get('email', '')})")
        
        st.markdown(f"**📱 Phone:**")
        st.markdown(f"[{personal.get('phone', 'N/A')}](https://wa.me/{personal.get('phone', '').replace('+', '').replace(' ', '')})")
    
    with col2:
        st.markdown(f"**📍 Location:**")
        st.markdown(personal.get('location', 'N/A'))
        
        st.markdown(f"**🌐 Website:**")
        st.markdown(f"[{personal.get('website', 'N/A')}](https://{personal.get('website', '')})")
    
    # Social links
    st.markdown("")
    social_cols = st.columns(3)
    
    with social_cols[0]:
        st.markdown(f"**💼 LinkedIn:**")
        linkedin = personal.get('linkedin', '')
        if linkedin:
            st.markdown(f"[View Profile](https://{linkedin})")
    
    with social_cols[1]:
        st.markdown(f"**🐙 GitHub:**")
        github = personal.get('github', '')
        if github:
            st.markdown(f"[View Profile](https://{github})")
    
    with social_cols[2]:
        st.markdown(f"**🌐 Portfolio:**")
        website = personal.get('website', '')
        if website:
            st.markdown(f"[Visit Website](https://{website})")
    
    st.divider()
    
    # Professional Summary
    st.markdown("### 📝 Professional Summary")
    st.markdown(summary)
    
    st.divider()
    
    # Work Experience
    st.markdown("### Work Experience")
    
    if experience:
        for exp in experience:
            render_experience_item(exp)
    else:
        st.info("No work experience listed yet.")
    
    st.divider()
    
    # Education
    st.markdown("### 🎓 Education")
    
    if education:
        for edu in education:
            render_education_item(edu)
    else:
        st.info("No education information listed yet.")
    
    st.divider()
    
    # Certifications
    st.markdown("### 📜 Certifications")
    
    if certifications:
        for cert in certifications:
            with st.container():
                col1, col2 = st.columns([3, 1])
                
                with col1:
                    st.markdown(f"**{cert.get('name', 'Certification')}**")
                    st.markdown(f"{cert.get('issuer', 'Organization')}")
                
                with col2:
                    st.markdown(f"📅 {cert.get('date', 'N/A')}")
                
                # Credential link
                cert_url = cert.get('url', '')
                if cert_url:
                    st.markdown(f"[View Credential]({cert_url})")
                
                st.divider()
    else:
        st.info("No certifications listed yet.")
        
    # Skills Section
    st.markdown("### 🚀 Skills")
    
    # Technical Skills
    technical_skills = skills.get("technical", [])
    if technical_skills:
        st.markdown("#### Technical Skills")
        tech_cols = st.columns(2)
        
        for i, skill in enumerate(technical_skills):
            with tech_cols[i % 2]:
                render_skill_bar(
                    skill.get("name", "Skill"),
                    skill.get("level", 50)
                )
    
    # Soft Skills
    soft_skills = skills.get("soft", [])
    if soft_skills:
        st.markdown("")
        st.markdown("#### Soft Skills")
        render_skill_tag([skill.get("name", skill) if isinstance(skill, dict) else skill for skill in soft_skills])
    
    # Languages
    languages = skills.get("languages", [])
    if languages:
        st.markdown("")
        st.markdown("#### Languages")
        for lang in languages:
            col1, col2 = st.columns([2, 1])
            with col1:
                st.markdown(f"**{lang.get('name', 'Language')}**")
            with col2:
                st.markdown(f"*{lang.get('proficiency', 'N/A')}*")
    
    st.divider()
    
    
    # Awards
    st.markdown("### 🏆 Awards & Honors")
    
    if awards:
        for award in awards:
            with st.container():
                col1, col2 = st.columns([3, 1])
                
                with col1:
                    st.markdown(f"**{award.get('name', 'Award')}**")
                    st.markdown(f"{award.get('issuer', 'Organization')}")
                    if award.get('description'):
                        st.markdown(f"*{award.get('description')}*")
                
                with col2:
                    st.markdown(f"📅 {award.get('date', 'N/A')}")
                
                st.divider()
    else:
        st.info("No awards listed yet.")
    
    # Download CV Section
    st.markdown("")
    st.markdown(
        """
        <div style="
            background-color: #EFF6FF;
            padding: 30px;
            border-radius: 15px;
            text-align: center;
            border: 2px solid #2563EB;
        ">
            <h3 style="color: #2563EB; margin-bottom: 15px;">
                📥 Download Full CV
            </h3>
            <p style="color: #6B7280; margin-bottom: 20px;">
                Get a PDF version of my complete resume for offline viewing
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )
    
    download_cols = st.columns(3)
    with download_cols[1]:
        if st.button("📄 Download PDF", use_container_width=True, type="primary"):
            # Note: In production, this would download the actual PDF file
            st.info("PDF download feature coming soon! The CV file will be available in the assets/documents folder.")
