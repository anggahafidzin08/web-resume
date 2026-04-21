"""
Page components for the web resume application.
"""

from .home import render_home
from .resume import render_resume
from .portfolio import render_portfolio
from .project_detail import render_project_detail
from .contact import render_contact

__all__ = [
    'render_home',
    'render_resume',
    'render_portfolio',
    'render_project_detail',
    'render_contact'
]
