"""
Data loading utilities
"""
from .data_loader import (
    load_resume_data,
    load_projects_data,
    get_project_by_slug,
    get_featured_projects,
    get_all_projects,
    load_project_content,
    get_unique_technologies,
    get_project_categories,
    filter_projects
)

__all__ = [
    'load_resume_data',
    'load_projects_data',
    'get_project_by_slug',
    'get_featured_projects',
    'get_all_projects',
    'load_project_content',
    'get_unique_technologies',
    'get_project_categories',
    'filter_projects'
]
