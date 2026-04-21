"""
Portfolio overview page with project grid and filtering.
"""

import streamlit as st
from src.utils.data_loader import (
    get_all_projects,
    get_unique_technologies,
    get_project_categories,
    filter_projects
)
from src.components import render_project_card_compact


def render_portfolio():
    """
    Render the portfolio overview page with filtering capabilities.
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
                💼 Portfolio
            </h1>
            <p style="font-size: 18px; opacity: 0.9;">
                Explore my projects and case studies
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )
    
    # Get all data
    all_projects = get_all_projects()
    technologies = get_unique_technologies()
    categories = get_project_categories()
    
    # Filters section
    st.markdown("### 🔍 Filter Projects")
    
    filter_col1, filter_col2, filter_col3 = st.columns(3)
    
    with filter_col1:
        # Technology filter
        selected_techs = st.multiselect(
            "Technologies",
            options=technologies,
            default=[],
            help="Filter by technologies used"
        )
    
    with filter_col2:
        # Category filter
        selected_category = st.selectbox(
            "Category",
            options=["All"] + categories,
            index=0,
            help="Filter by project category"
        )
    
    with filter_col3:
        # Search
        search_query = st.text_input(
            "Search",
            placeholder="Search projects...",
            help="Search by title or description"
        )
    
    # Apply filters
    category = None if selected_category == "All" else selected_category
    
    filtered_projects = filter_projects(
        technologies=selected_techs if selected_techs else None,
        category=category,
        search_query=search_query if search_query else None
    )
    
    # Display results count
    st.markdown(f"**📊 Showing {len(filtered_projects)} of {len(all_projects)} projects**")
    
    st.divider()
    
    # Projects grid
    if filtered_projects:
        # Display projects in grid
        for i in range(0, len(filtered_projects), 3):
            cols = st.columns(3)
            
            for j, col in enumerate(cols):
                project_idx = i + j
                if project_idx < len(filtered_projects):
                    project = filtered_projects[project_idx]
                    
                    with col:
                        # Compact project card
                        render_project_card_compact(
                            title=project.get("title", "Project"),
                            description=project.get("description", ""),
                            technologies=project.get("technologies", [])[:3],
                            image=project.get("image"),
                            key=project.get("slug", project_idx)
                        )
                        
                        # View button
                        if st.button(
                            "View Details →",
                            key=f"view_{project.get('slug', project_idx)}",
                            use_container_width=True
                        ):
                            st.session_state.selected_project = project.get("slug")
                            st.session_state.current_page = "Project Detail"
                            st.rerun()
    else:
        # No projects found
        st.warning("🔍 No projects found matching your filters. Try adjusting your search criteria.")
        
        # Reset filters button
        if st.button("Reset Filters"):
            st.session_state.filter_techs = []
            st.session_state.filter_category = "All"
            st.session_state.filter_search = ""
            st.rerun()
    
    # Bottom CTA
    st.divider()
    st.markdown("")
    
    cta_cols = st.columns(2)
    
    with cta_cols[0]:
        st.markdown(
            """
            ### 🚀 Interested in working together?
            I'm always open to discussing new projects and opportunities.
            """
        )
        
        if st.button("📧 Get in Touch", use_container_width=True, type="primary"):
            st.session_state.current_page = "Contact"
            st.rerun()
    
    with cta_cols[1]:
        st.markdown(
            """
            ### 💻 Want to see the code?
            Check out my GitHub for open source projects and contributions.
            """
        )
        
        if st.button("🐙 View GitHub", use_container_width=True):
            # Open GitHub in new tab
            st.markdown("[Visit GitHub →](https://github.com/yourusername)")
