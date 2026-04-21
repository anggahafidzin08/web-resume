"""
Skill bar component for visualizing skill levels.
"""

import streamlit as st


def render_skill_bar(skill_name: str, level: int, max_level: int = 100):
    """
    Render a skill bar with percentage visualization.
    
    Args:
        skill_name: Name of the skill
        level: Current skill level (0-100)
        max_level: Maximum level (default 100)
    """
    percentage = min(100, (level / max_level) * 100)
    
    # Color based on proficiency
    if percentage >= 80:
        color = "#10B981"  # Green - Expert
    elif percentage >= 60:
        color = "#3B82F6"  # Blue - Proficient
    elif percentage >= 40:
        color = "#F59E0B"  # Amber - Intermediate
    else:
        color = "#EF4444"  # Red - Beginner
    
    st.markdown(
        f"""
        <div style="margin: 10px 0;">
            <div style="display: flex; justify-content: space-between; margin-bottom: 5px;">
                <span style="font-weight: 600; color: #1F2937;">{skill_name}</span>
                <span style="color: #6B7280;">{level}%</span>
            </div>
            <div style="
                background-color: #E5E7EB;
                border-radius: 10px;
                height: 10px;
                overflow: hidden;
            ">
                <div style="
                    background: linear-gradient(90deg, {color} 0%, {color} {percentage}%, #E5E7EB {percentage}%, #E5E7EB 100%);
                    height: 100%;
                    border-radius: 10px;
                    transition: width 0.3s ease;
                "></div>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )


def render_skill_tag(skills: list):
    """
    Render skills as tags/badges in a horizontal row.

    Args:
        skills: List of skill names
    """
    tags_html = "".join([
        f"""<span style="
            display: inline-block;
            background-color: #EFF6FF;
            color: #2563EB;
            padding: 5px 12px;
            border-radius: 20px;
            margin: 4px;
            font-size: 14px;
            font-weight: 500;
        ">{name}</span>"""
        for name in skills
    ])

    st.markdown(
        f"""
        <div style="display: flex; flex-wrap: wrap; gap: 4px;">
            {tags_html}
        </div>
        """,
        unsafe_allow_html=True
    )


def render_skill_group(skills: list, group_name: str = "Skills"):
    """
    Render a group of skills as tags.
    
    Args:
        skills: List of skill names or skill dicts
        group_name: Group title
    """
    if skills:
        st.markdown(f"**{group_name}**")
        for skill in skills:
            if isinstance(skill, dict):
                render_skill_tag(skill.get("name", ""))
            else:
                render_skill_tag(skill)
        st.markdown("")  # Add spacing
