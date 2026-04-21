"""
Home page component for the web resume application.
Main landing page with hero section, featured projects, and quick stats.
"""

import streamlit as st
import base64
from pathlib import Path
from src.utils.data_loader import (
    load_resume_data,
    get_featured_projects,
    get_all_projects
)
from src.components import (
    render_skill_bar,
    render_skill_tag,
    render_project_card
)


def render_home():
    """
    Render the home/landing page.
    """
    # Load data
    resume_data = load_resume_data()
    featured_projects = get_featured_projects(limit=3)
    all_projects = get_all_projects()
    
    personal = resume_data.get("personal", {})
    summary = resume_data.get("summary", "")
    skills = resume_data.get("skills", {})
    
    # Hero Section (with optional profile image)
    profile_img = personal.get("profile_image")
    with st.container():
        # enforce a 1:5 column width ratio for profile image and hero
        hcol1, hcol2 = st.columns([1, 5])
        with hcol1:
            if profile_img:
                try:
                    # Read image file and embed as base64 so we can control sizing via CSS
                    img_path = Path(profile_img)
                    if not img_path.is_file():
                        img_path = Path.cwd() / profile_img
                    img_bytes = img_path.read_bytes()
                    ext = img_path.suffix.lower().lstrip('.') or 'png'
                    mime = 'jpeg' if ext in ('jpg', 'jpeg') else ext
                    b64 = base64.b64encode(img_bytes).decode()
                    img_src = f"data:image/{mime};base64,{b64}"

                    # Render image to fully cover the available hero height using object-fit:cover
                    st.markdown(
                        f"""
                        <div style="height:260px;border-radius:12px;overflow:hidden;">
                            <img src="{img_src}" style="width:100%;height:100%;object-fit:cover;display:block;" />
                        </div>
                        """,
                        unsafe_allow_html=True,
                    )
                except Exception:
                    # fallback to emoji if image fails
                    st.markdown("<div style='font-size:72px;text-align:center;'>👋</div>", unsafe_allow_html=True)
            else:
                st.markdown("<div style='font-size:72px;text-align:center;'>👋</div>", unsafe_allow_html=True)
        with hcol2:
            st.markdown(
                f"""
                <div style="
                    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                    padding: 20px;
                    min-height: 260px;
                    display: flex;
                    flex-direction: column;
                    justify-content: center;
                    border-radius: 20px;
                    text-align: center;
                    color: white;
                    margin-bottom: 40px;
                ">
                    <h1 style="font-size: 48px; margin-bottom: 10px;">
                        👋 Hi, I'm {personal.get('name', 'Angga Putra Hafidzin')}
                    </h1>
                    <h2 style="font-size: 24px; font-weight: 300; opacity: 0.9;">
                        {personal.get('title', 'Tech Role')}
                    </h2>
                    <p style="font-size: 18px; margin-top: 20px; opacity: 0.95;">
                        Building innovative solutions through code
                    </p>
                </div>
                """,
                unsafe_allow_html=True
            )
    
    # Quick Stats
    st.markdown("### 📊 Quick Stats")
    stats_cols = st.columns(4)
    
    # Calculate stats
    years_exp = personal.get("experience_years", 0)
    total_projects = len(all_projects)
    total_skills = len(skills.get("technical", []))
    total_certs = len(resume_data.get("certifications", []))
    
    with stats_cols[0]:
        st.metric("Years Experience", f"{years_exp}+", "Growing")
    with stats_cols[1]:
        st.metric("Projects Completed", str(total_projects), "Active")
    with stats_cols[2]:
        st.metric("Technical Skills", str(total_skills), "Diverse")
    with stats_cols[3]:
        st.metric("Certifications", str(total_certs), "Verified")
    
    st.divider()
    
    # Two column layout
    col1, col2 = st.columns([2, 1])
    
    with col1:
        # About Section
        st.markdown("### 👨‍💻 About Me")
        st.markdown(summary)
        
        # CTA Buttons
        st.markdown("")
        cta_cols = st.columns(2)
        
        with cta_cols[0]:
            if st.button("📄 View Resume", use_container_width=True, type="primary"):
                st.session_state.current_page = "Resume"
                st.rerun()
        
        with cta_cols[1]:
            if st.button("💼 View Portfolio", use_container_width=True):
                st.session_state.current_page = "Portfolio"
                st.rerun()
    
    with col2:
        # Top Skills
        st.markdown("### 🚀 Top Skills")
        technical_skills = skills.get("technical", [])[:5]
        
        for skill in technical_skills:
            render_skill_bar(
                skill.get("name", "Skill"),
                skill.get("level", 50)
            )
    
    st.divider()
    
    # Featured Projects
    st.markdown("### ⭐ Featured Projects")
    st.markdown("Here are some of my recent works that showcase my skills and expertise.")
    
    if featured_projects:
        for i, project in enumerate(featured_projects):
            with st.container():
                # Create a card-like container
                st.markdown(
                    f"""
                    <div style="
                        background-color: white;
                        padding: 20px;
                        border-radius: 10px;
                        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
                        margin: 20px 0;
                    ">
                    </div>
                    """,
                    unsafe_allow_html=True
                )
                
                # Project content
                col_img, col_content = st.columns([1, 2])
                
                with col_img:
                    # Placeholder gradient instead of image
                    st.markdown(
                        f"""
                        <div style="
                            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                            height: 150px;
                            border-radius: 10px;
                            display: flex;
                            align-items: center;
                            justify-content: center;
                            color: white;
                            font-size: 48px;
                        ">
                            📁
                        </div>
                        """,
                        unsafe_allow_html=True
                    )
                
                with col_content:
                    st.markdown(f"#### {project.get('title', 'Project')}")
                    st.markdown(f"*{project.get('subtitle', '')}*")
                    st.markdown(project.get('description', ''))
                    
                    # Technologies
                    technologies = project.get("technologies", [])
                    if technologies:
                        st.markdown("**Technologies:**")
                        tech_cols = st.columns(min(len(technologies), 4))
                        for idx, tech in enumerate(technologies[:4]):
                            with tech_cols[idx % len(tech_cols)]:
                                st.markdown(f"`{tech}`")
                    
                    # View button
                    if st.button(
                        "View Project →",
                        key=f"featured_{project.get('slug', i)}",
                        type="secondary"
                    ):
                        st.session_state.selected_project = project.get("slug")
                        st.session_state.current_page = "Project Detail"
                        st.rerun()
                
                st.divider()
    else:
        st.info("No featured projects available yet.")
    
    # View all projects link
    st.markdown("")
    if st.button("📂 View All Projects →", use_container_width=True):
        st.session_state.current_page = "Portfolio"
        st.rerun()
    
    # Call to Action Section
    st.markdown("")
    st.markdown(
        """
        <div style="
            background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
            padding: 40px 20px;
            border-radius: 20px;
            text-align: center;
            color: white;
            margin-top: 40px;
        ">
            <h2 style="font-size: 32px; margin-bottom: 15px;">
                Let's Work Together
            </h2>
            <p style="font-size: 18px; margin-bottom: 25px; opacity: 0.95;">
                I'm always interested in hearing about new projects and opportunities.
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )
    
    contact_cols = st.columns(2)
    with contact_cols[0]:
        if st.button("📧 Get in Touch", use_container_width=True, type="primary"):
            st.session_state.current_page = "Contact"
            st.rerun()
    
    with contact_cols[1]:
        if st.button("📥 Download CV", use_container_width=True):
            # Note: In production, this would link to actual PDF file
            st.info("CV download feature coming soon!")
