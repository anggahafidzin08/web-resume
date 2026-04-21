"""
Project detail page for displaying individual project information.
"""

import streamlit as st
from src.utils.data_loader import (
    get_project_by_slug,
    load_project_content,
    get_all_projects
)
import markdown


def render_project_detail():
    """
    Render the project detail page.
    """
    # Get selected project from session state
    project_slug = st.session_state.get("selected_project")
    
    if not project_slug:
        st.warning("No project selected. Please select a project from the portfolio.")
        if st.button("← Back to Portfolio"):
            st.session_state.current_page = "Portfolio"
            st.rerun()
        return
    
    # Load project data
    project = get_project_by_slug(project_slug)
    
    if not project:
        st.error(f"Project '{project_slug}' not found.")
        if st.button("← Back to Portfolio"):
            st.session_state.current_page = "Portfolio"
            st.rerun()
        return
    
    # Project header
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
                {project.get('title', 'Project')}
            </h1>
            <p style="font-size: 20px; opacity: 0.9; font-style: italic;">
                {project.get('subtitle', '')}
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )

    # Back button
    if st.button("← Back to Portfolio"):
        st.session_state.current_page = "Portfolio"
        st.rerun()

    # Quick info bar
    info_cols = st.columns(4)

    with info_cols[0]:
        st.markdown(f"**📁 Category**")
        st.markdown(project.get("category", "N/A"))

    with info_cols[1]:
        st.markdown(f"**👤 Role**")
        st.markdown(project.get("role", "N/A"))

    with info_cols[2]:
        st.markdown(f"**👥 Team**")
        st.markdown(f"{project.get('team_size', 1)} person(s)")

    with info_cols[3]:
        st.markdown(f"**📅 Timeline**")
        start = project.get("start_date", "")
        end = project.get("end_date", "")
        st.markdown(f"{start} - {end}")

    st.divider()

    # Main content - two columns
    col1, col2 = st.columns([2, 1])

    with col1:
        # Project image/hero
        st.markdown("### 🖼️ Project Overview")

        project_image = project.get("image")
        if project_image:
            st.image(project_image, use_container_width=True)
        else:
            st.markdown(
                f"""
                <div style="
                    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                    height: 300px;
                    border-radius: 15px;
                    display: flex;
                    align-items: center;
                    justify-content: center;
                    color: white;
                    font-size: 72px;
                    margin-bottom: 20px;
                ">
                    📁
                </div>
                """,
                unsafe_allow_html=True
            )
        
        # Description
        st.markdown("### 📝 Description")
        st.markdown(project.get("long_description", project.get("description", "")))
        
        # Problem & Solution
        st.markdown("")
        problem_col, solution_col = st.columns(2)
        
        with problem_col:
            st.markdown("### ❌ Problem")
            st.markdown(project.get("problem", "N/A"))
        
        with solution_col:
            st.markdown("### ✅ Solution")
            st.markdown(project.get("solution", "N/A"))
    
    with col2:
        # Technologies
        st.markdown("### 🛠️ Technologies")
        technologies = project.get("technologies", [])
        
        for tech in technologies:
            st.markdown(f"`{tech}`")
        
        st.markdown("")
        
        # Project links
        st.markdown("### 🔗 Links")
        links = project.get("links", {})
        
        if links.get("live"):
            st.markdown(f"[🌐 Live Demo]({links.get('live')})")
        
        if links.get("github"):
            st.markdown(f"[🐙 Source Code]({links.get('github')})")
        
        if links.get("case_study"):
            st.markdown(f"[📖 Case Study]({links.get('case_study')})")
        
        st.markdown("")
        
        # Status badge
        status = project.get("status", "unknown")
        status_emoji = {"completed": "✅", "in_progress": "🔄", "planned": "📋"}.get(status, "❓")
        
        st.markdown(f"**Status:** {status_emoji} {status.title()}")
    
    st.divider()
    
    # Challenges & Solutions
    st.markdown("### 🧩 Challenges & Solutions")
    
    challenges = project.get("challenges", [])
    
    if challenges:
        for i, challenge in enumerate(challenges):
            with st.expander(f"**Challenge {i+1}:** {challenge.get('challenge', 'N/A')}", expanded=False):
                st.markdown(f"**Solution:** {challenge.get('solution', 'N/A')}")
    else:
        st.info("No challenges documented for this project.")
    
    st.divider()
    
    # Results & Impact
    st.markdown("### 📊 Results & Impact")
    
    results = project.get("results", [])
    
    if results:
        for result in results:
            st.markdown(f"✅ {result}")
    else:
        st.info("No results documented for this project.")
    
    st.divider()
    
    # Gallery section
    st.markdown("### 🖼️ Project Gallery")

    gallery = project.get("gallery", [])

    if gallery:
        for img_path in gallery:
            st.image(img_path, use_container_width=False)
    else:
        st.info("No gallery images available.")
    
    st.divider()
    
    # Related projects
    st.markdown("### 🔗 Related Projects")
    
    all_projects = get_all_projects()
    current_category = project.get("category")
    
    # Find related projects (same category, excluding current)
    related = [
        p for p in all_projects
        if p.get("category") == current_category and p.get("slug") != project_slug
    ][:3]
    
    if related:
        related_cols = st.columns(3)
        
        for i, col in enumerate(related_cols):
            if i < len(related):
                rel_project = related[i]
                
                with col:
                    st.markdown(f"**{rel_project.get('title', 'Project')}**")
                    st.markdown(f"*{rel_project.get('subtitle', '')}*")
                    
                    if st.button(
                        "View →",
                        key=f"related_{rel_project.get('slug', i)}",
                        use_container_width=True
                    ):
                        st.session_state.selected_project = rel_project.get("slug")
                        st.rerun()
    else:
        st.info("No related projects found.")
    
    # Bottom CTA
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
                Like what you see?
            </h2>
            <p style="font-size: 18px; opacity: 0.95;">
                Let's discuss how I can help bring your project to life
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )
