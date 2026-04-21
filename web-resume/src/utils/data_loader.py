"""
Data loading utilities for the web resume application.
Handles loading and caching of JSON data files.
"""

import json
import os
from pathlib import Path
from functools import lru_cache


# Base directory for data files (project root is parent of src)
PROJECT_ROOT = Path(__file__).parent.parent.parent
DATA_DIR = PROJECT_ROOT / "data"
CONTENT_DIR = PROJECT_ROOT / "content"


@lru_cache(maxsize=None)
def load_resume_data() -> dict:
    """
    Load resume data from JSON file.
    Uses LRU cache to avoid repeated file reads.
    
    Returns:
        dict: Resume data structure
    """
    resume_file = DATA_DIR / "resume.json"
    
    if not resume_file.exists():
        raise FileNotFoundError(f"Resume data file not found: {resume_file}")
    
    with open(resume_file, 'r', encoding='utf-8') as f:
        return json.load(f)


@lru_cache(maxsize=None)
def load_projects_data() -> dict:
    """
    Load projects data from JSON file.
    Uses LRU cache to avoid repeated file reads.
    
    Returns:
        dict: Projects data structure with 'projects' key
    """
    projects_file = DATA_DIR / "projects.json"
    
    if not projects_file.exists():
        raise FileNotFoundError(f"Projects data file not found: {projects_file}")
    
    with open(projects_file, 'r', encoding='utf-8') as f:
        return json.load(f)


def get_project_by_slug(slug: str) -> dict | None:
    """
    Get a specific project by its slug.
    
    Args:
        slug: Project slug identifier
        
    Returns:
        dict or None: Project data if found, None otherwise
    """
    projects_data = load_projects_data()
    projects = projects_data.get("projects", [])
    
    for project in projects:
        if project.get("slug") == slug:
            return project
    
    return None


def get_featured_projects(limit: int = 3) -> list:
    """
    Get featured projects for homepage display.
    
    Args:
        limit: Maximum number of projects to return
        
    Returns:
        list: List of featured project dictionaries
    """
    projects_data = load_projects_data()
    projects = projects_data.get("projects", [])
    
    # Filter featured projects and sort by order
    featured = [p for p in projects if p.get("featured", False)]
    featured.sort(key=lambda x: x.get("order", 999))
    
    return featured[:limit]


def get_all_projects() -> list:
    """
    Get all projects sorted by order.
    
    Returns:
        list: List of all project dictionaries
    """
    projects_data = load_projects_data()
    projects = projects_data.get("projects", [])
    
    # Sort by order field
    projects.sort(key=lambda x: x.get("order", 999))
    
    return projects


def load_project_content(slug: str) -> str:
    """
    Load detailed project content from markdown file.
    
    Args:
        slug: Project slug identifier
        
    Returns:
        str: Markdown content or empty string if not found
    """
    content_file = CONTENT_DIR / "projects" / f"{slug}.md"
    
    if not content_file.exists():
        return ""
    
    with open(content_file, 'r', encoding='utf-8') as f:
        return f.read()


def get_unique_technologies() -> list:
    """
    Get list of all unique technologies used across projects.
    
    Returns:
        list: Sorted list of unique technology names
    """
    projects = get_all_projects()
    technologies = set()
    
    for project in projects:
        techs = project.get("technologies", [])
        technologies.update(techs)
    
    return sorted(list(technologies))


def get_project_categories() -> list:
    """
    Get list of all unique project categories.
    
    Returns:
        list: Sorted list of unique category names
    """
    projects = get_all_projects()
    categories = set()
    
    for project in projects:
        category = project.get("category")
        if category:
            categories.add(category)
    
    return sorted(list(categories))


def filter_projects(
    technologies: list | None = None,
    category: str | None = None,
    search_query: str | None = None
) -> list:
    """
    Filter projects by technologies, category, and search query.
    
    Args:
        technologies: List of technology names to filter by
        category: Category to filter by
        search_query: Search query to match against title and description
        
    Returns:
        list: Filtered list of projects
    """
    projects = get_all_projects()
    
    # Filter by technologies
    if technologies:
        projects = [
            p for p in projects
            if any(tech in p.get("technologies", []) for tech in technologies)
        ]
    
    # Filter by category
    if category:
        projects = [
            p for p in projects
            if p.get("category") == category
        ]
    
    # Filter by search query
    if search_query:
        query = search_query.lower()
        projects = [
            p for p in projects
            if (query in p.get("title", "").lower() or
                query in p.get("description", "").lower() or
                query in p.get("subtitle", "").lower())
        ]
    
    return projects
