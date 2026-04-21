"""
Validation utilities for the web resume application.
Handles form validation and data sanitization.
"""

import re
from typing import Tuple


def validate_email(email: str) -> Tuple[bool, str]:
    """
    Validate email address format.
    
    Args:
        email: Email address to validate
        
    Returns:
        Tuple[bool, str]: (is_valid, error_message)
    """
    if not email or not email.strip():
        return False, "Email is required"
    
    email = email.strip()
    
    # Basic email regex pattern
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    
    if not re.match(pattern, email):
        return False, "Please enter a valid email address"
    
    if len(email) > 254:
        return False, "Email address is too long"
    
    return True, ""


def validate_phone(phone: str) -> Tuple[bool, str]:
    """
    Validate phone number format (international format).
    
    Args:
        phone: Phone number to validate
        
    Returns:
        Tuple[bool, str]: (is_valid, error_message)
    """
    if not phone or not phone.strip():
        return False, "Phone number is required"
    
    phone = phone.strip()
    
    # Remove common separators
    cleaned = re.sub(r'[\s\-\(\)\.]', '', phone)
    
    # Check if it starts with + and has digits
    if not re.match(r'^\+?\d{10,15}$', cleaned):
        return False, "Please enter a valid phone number (10-15 digits)"
    
    return True, ""


def validate_name(name: str, field_name: str = "Name") -> Tuple[bool, str]:
    """
    Validate name field.
    
    Args:
        name: Name to validate
        field_name: Name of the field for error messages
        
    Returns:
        Tuple[bool, str]: (is_valid, error_message)
    """
    if not name or not name.strip():
        return False, f"{field_name} is required"
    
    name = name.strip()
    
    if len(name) < 2:
        return False, f"{field_name} must be at least 2 characters long"
    
    if len(name) > 100:
        return False, f"{field_name} is too long"
    
    # Check for mostly alphanumeric characters
    if not re.match(r'^[\w\s\-\'\.\,]+$', name):
        return False, f"{field_name} contains invalid characters"
    
    return True, ""


def validate_message(message: str, min_length: int = 20) -> Tuple[bool, str]:
    """
    Validate message field (e.g., contact form message).
    
    Args:
        message: Message to validate
        min_length: Minimum required length
        
    Returns:
        Tuple[bool, str]: (is_valid, error_message)
    """
    if not message or not message.strip():
        return False, "Message is required"
    
    message = message.strip()
    
    if len(message) < min_length:
        return False, f"Message must be at least {min_length} characters long"
    
    if len(message) > 5000:
        return False, "Message is too long (maximum 5000 characters)"
    
    return True, ""


def validate_subject(subject: str) -> Tuple[bool, str]:
    """
    Validate subject field.
    
    Args:
        subject: Subject to validate
        
    Returns:
        Tuple[bool, str]: (is_valid, error_message)
    """
    if not subject or not subject.strip():
        return False, "Subject is required"
    
    subject = subject.strip()
    
    if len(subject) < 3:
        return False, "Subject must be at least 3 characters long"
    
    if len(subject) > 200:
        return False, "Subject is too long (maximum 200 characters)"
    
    return True, ""


def validate_contact_form(
    name: str,
    email: str,
    subject: str,
    message: str
) -> Tuple[bool, dict]:
    """
    Validate complete contact form.
    
    Args:
        name: Name field value
        email: Email field value
        subject: Subject field value
        message: Message field value
        
    Returns:
        Tuple[bool, dict]: (is_valid, errors_dict)
    """
    errors = {}
    
    # Validate name
    is_valid, error = validate_name(name, "Name")
    if not is_valid:
        errors["name"] = error
    
    # Validate email
    is_valid, error = validate_email(email)
    if not is_valid:
        errors["email"] = error
    
    # Validate subject
    is_valid, error = validate_subject(subject)
    if not is_valid:
        errors["subject"] = error
    
    # Validate message
    is_valid, error = validate_message(message)
    if not is_valid:
        errors["message"] = error
    
    return len(errors) == 0, errors


def sanitize_text(text: str) -> str:
    """
    Sanitize text input by removing potentially harmful characters.
    
    Args:
        text: Text to sanitize
        
    Returns:
        str: Sanitized text
    """
    if not text:
        return ""
    
    # Remove null bytes
    text = text.replace('\x00', '')
    
    # Strip leading/trailing whitespace
    text = text.strip()
    
    # Normalize line endings
    text = text.replace('\r\n', '\n').replace('\r', '\n')
    
    return text


def validate_url(url: str) -> Tuple[bool, str]:
    """
    Validate URL format.
    
    Args:
        url: URL to validate
        
    Returns:
        Tuple[bool, str]: (is_valid, error_message)
    """
    if not url or not url.strip():
        return True, ""  # Empty URL is valid (optional field)
    
    url = url.strip()
    
    # Basic URL pattern
    pattern = r'^https?://[^\s]+$'
    
    if not re.match(pattern, url):
        return False, "Please enter a valid URL (must start with http:// or https://)"
    
    return True, ""


def validate_date(date_str: str) -> Tuple[bool, str]:
    """
    Validate date string format (YYYY-MM or YYYY-MM-DD).
    
    Args:
        date_str: Date string to validate
        
    Returns:
        Tuple[bool, str]: (is_valid, error_message)
    """
    if not date_str or not date_str.strip():
        return False, "Date is required"
    
    date_str = date_str.strip()
    
    # Pattern for YYYY-MM or YYYY-MM-DD
    pattern = r'^\d{4}-\d{2}(-\d{2})?$'
    
    if not re.match(pattern, date_str):
        return False, "Please use YYYY-MM or YYYY-MM-DD format"
    
    return True, ""
