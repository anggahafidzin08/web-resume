"""
Reusable UI components for the web resume application.
"""

from .navigation import (
    render_navigation,
    render_mobile_nav,
    get_current_page,
    set_page
)

from .project_card import (
    render_project_card,
    render_project_card_compact
)

from .skill_bar import (
    render_skill_bar,
    render_skill_tag,
    render_skill_group
)

from .timeline_item import (
    render_timeline_item,
    render_experience_item,
    render_education_item
)

from .contact_form import (
    render_contact_form,
    render_contact_info,
    render_social_links
)

__all__ = [
    'render_navigation',
    'render_mobile_nav',
    'get_current_page',
    'set_page',
    'render_project_card',
    'render_project_card_compact',
    'render_skill_bar',
    'render_skill_tag',
    'render_skill_group',
    'render_timeline_item',
    'render_experience_item',
    'render_education_item',
    'render_contact_form',
    'render_contact_info',
    'render_social_links'
]
