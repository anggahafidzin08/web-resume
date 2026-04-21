"""
Project card component for displaying project previews.
"""

import streamlit as st
from PIL import Image, ImageOps


def render_project_card(
    title: str,
    subtitle: str,
    description: str,
    technologies: list,
    image: str = None,
    on_click: callable = None,
    key: str = None
):
    """
    Render a project card with image, title, description, and tech tags.
    
    Args:
        title: Project title
        subtitle: Project subtitle/tagline
        description: Brief project description
        technologies: List of technology names
        image: Path to project image (optional)
        on_click: Callback function when card is clicked
        key: Unique key for the component
    """
    # Create a container for the card
    with st.container():
        # Image section
        if image:
            try:
                st.image(image, use_container_width=True)
            except Exception:
                # Placeholder if image not found
                st.markdown(
                    f"""
                    <div style="
                        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                        height: 200px;
                        border-radius: 10px 10px 0 0;
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
        else:
            st.markdown(
                f"""
                <div style="
                    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                    height: 200px;
                    border-radius: 10px 10px 0 0;
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
        
        # Content section
        st.markdown(f"### {title}")
        if subtitle:
            st.markdown(f"*{subtitle}*")
        
        st.markdown(description)
        
        # Technology tags
        if technologies:
            st.markdown("**Technologies:**")
            cols = st.columns(min(len(technologies), 3))
            for i, tech in enumerate(technologies[:6]):  # Show max 6 technologies
                with cols[i % len(cols)]:
                    st.markdown(f"`{tech}`")
        
        # View project button
        if on_click:
            if st.button("View Project →", key=f"view_{key}", use_container_width=True):
                on_click()


def render_project_card_compact(
    title: str,
    description: str,
    technologies: list,
    image: str = None,
    key: str = None,
    image_width: int = 500,
    image_height: int = 200,
):
    """
    Render a compact project card for grid layouts.

    Args:
        title: Project title
        description: Brief description
        technologies: List of technology names
        image: Path to project image (optional, shown as thumbnail)
        key: Unique key for the component
    """
    with st.container():
        if image:
            try:
                # Try to open and resize/crop the image to the exact size
                img = Image.open(image)
                img = ImageOps.exif_transpose(img)
                img = ImageOps.fit(img, (image_width, image_height), Image.LANCZOS)
                st.image(img, width=image_width)
            except Exception:
                # Fallback: let Streamlit handle the image (works for URLs)
                try:
                    st.image(image, width=image_width)
                except Exception:
                    st.markdown(
                        f"""
                        <div style="
                            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                            height: {image_height}px;
                            border-radius: 10px 10px 0 0;
                            display: flex;
                            align-items: center;
                            justify-content: center;
                            color: white;
                            font-size: 36px;
                        ">
                            📁
                        </div>
                        """,
                        unsafe_allow_html=True
                    )
        else:
            st.markdown(
                f"""
                <div style="
                    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                    height: 100px;
                    border-radius: 10px 10px 0 0;
                    display: flex;
                    align-items: center;
                    justify-content: center;
                    color: white;
                    font-size: 36px;
                ">
                    📁
                </div>
                """,
                unsafe_allow_html=True
            )
        
        # Content
        st.markdown(f"#### {title}")
        st.markdown(description[:100] + "..." if len(description) > 100 else description)
        
        # Tech tags (compact)
        if technologies:
            tech_str = " • ".join(technologies[:3])
            st.markdown(f"*{tech_str}*")
