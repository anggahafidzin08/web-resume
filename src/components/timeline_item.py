"""
Timeline item component for experience and education sections.
"""

import streamlit as st


def render_timeline_item(
    title: str,
    subtitle: str,
    date_range: str,
    location: str | None = None,
    description: list | None = None,
    technologies: list | None = None,
    icon: str = "💼",
    logo: str | None = None
):
    """
    Render a timeline item for experience or education.
    
    Args:
        title: Main title (company or institution name)
        subtitle: Subtitle (position or degree)
        date_range: Date range string
        location: Location (optional)
        description: List of description bullet points
        technologies: List of technologies used
        icon: Icon emoji for the timeline item
    """
    # Create a container with left border for timeline effect
    with st.container():
        col1, col2 = st.columns([1, 20], vertical_alignment="center")
        
        with col1:
            try:
                if logo:
                    st.image(logo, width="stretch", )
            except Exception:
                st.markdown(f"### {icon}")
        
        with col2:
            st.markdown(f"### {title}")
            
            # Date and location
            date_location = []
            if date_range:
                date_location.append(f" | 📅 {date_range}")
            if location:
                date_location.append(f"📍 {location}")
            
            st.markdown(f"**{subtitle}        {" | ".join(date_location)}**")
    with st.container():
        # Description bullet points
        if description:
            for point in description:
                st.markdown(f"• {point}")
        
        # Technologies
        if technologies:
            st.markdown("*Technologies:*")
            tech_cols = st.columns(min(len(technologies), 4))
            for i, tech in enumerate(technologies):
                with tech_cols[i % len(tech_cols)]:
                    st.markdown(f"`{tech}`")
        
        st.divider()


def render_experience_item(experience: dict):
    """
    Render a work experience item from resume data.
    
    Args:
        experience: Experience dictionary from resume.json
    """
    # Format date range
    start_date = experience.get("start_date", "")
    end_date = "Present" if experience.get("current", False) else experience.get("end_date", "")
    date_range = f"{start_date} - {end_date}"
    
    render_timeline_item(
        title=experience.get("company", "Company"),
        subtitle=experience.get("position", "Position"),
        date_range=date_range,
        location=experience.get("location"),
        description=experience.get("description", []),
        technologies=experience.get("technologies", []),
        icon="💼",
        logo=experience.get("logo", None)
    )


def render_education_item(education: dict):
    """
    Render an education item from resume data.
    
    Args:
        education: Education dictionary from resume.json
    """
    # Format date range
    start_date = education.get("start_date", "")
    end_date = education.get("end_date", "")
    date_range = f"{start_date} - {end_date}"
    
    # Build description
    description = []
    if education.get("gpa"):
        description.append(f"GPA: {education.get('gpa')}")
    
    achievements = education.get("achievements", [])
    if achievements:
        description.extend(achievements)
    
    render_timeline_item(
        title=education.get("institution", "Institution"),
        subtitle=f"{education.get('degree', '')} in {education.get('field', '')}",
        date_range=date_range,
        location=education.get("location"),
        description=description if description else None,
        logo=education.get("logo", None),
        icon="🎓"
    )
