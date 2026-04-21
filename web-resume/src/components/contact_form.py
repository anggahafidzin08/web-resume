"""
Contact form component with validation.
"""

import streamlit as st
from src.utils.validators import validate_contact_form, sanitize_text


def render_contact_form(on_submit: callable = None):
    """
    Render a contact form with validation.
    
    Args:
        on_submit: Callback function when form is submitted successfully
        
    Returns:
        bool: True if form was submitted successfully, False otherwise
    """
    st.markdown("### Send Me a Message")
    st.markdown("Fill out the form below and I'll get back to you as soon as possible.")
    
    # Initialize session state for form
    if "form_submitted" not in st.session_state:
        st.session_state.form_submitted = False
    if "form_errors" not in st.session_state:
        st.session_state.form_errors = {}
    
    # Show success message if form was submitted
    if st.session_state.form_submitted:
        st.success("✅ Thank you for your message! I'll get back to you soon.")
        if st.button("Send Another Message"):
            st.session_state.form_submitted = False
            st.session_state.form_errors = {}
            st.rerun()
        return True
    
    with st.form(key="contact_form", clear_on_submit=False):
        # Name field
        name = st.text_input(
            "Name *",
            placeholder="Your full name",
            help="Please enter your full name"
        )
        
        # Email field
        email = st.text_input(
            "Email *",
            placeholder="your.email@example.com",
            help="Please enter a valid email address"
        )
        
        # Subject field
        subject = st.text_input(
            "Subject *",
            placeholder="What is this regarding?",
            help="Brief subject for your message"
        )
        
        # Message field
        message = st.text_area(
            "Message *",
            placeholder="Your message here...",
            help="Please enter at least 20 characters",
            height=150
        )
        
        # Submit button
        submit_button = st.form_submit_button(
            "📧 Send Message",
            use_container_width=True
        )
        
        if submit_button:
            # Sanitize inputs
            name = sanitize_text(name)
            email = sanitize_text(email)
            subject = sanitize_text(subject)
            message = sanitize_text(message)
            
            # Validate form
            is_valid, errors = validate_contact_form(name, email, subject, message)
            
            if is_valid:
                # Store submission data (in real app, send to backend)
                st.session_state.form_submitted = True
                st.session_state.form_data = {
                    "name": name,
                    "email": email,
                    "subject": subject,
                    "message": message
                }
                
                # Call callback if provided
                if on_submit:
                    on_submit(st.session_state.form_data)
                
                st.rerun()
            else:
                # Store errors
                st.session_state.form_errors = errors
    
    # Display errors
    if st.session_state.form_errors:
        st.error("❌ Please correct the following errors:")
        if "name" in st.session_state.form_errors:
            st.error(f"• **Name:** {st.session_state.form_errors['name']}")
        if "email" in st.session_state.form_errors:
            st.error(f"• **Email:** {st.session_state.form_errors['email']}")
        if "subject" in st.session_state.form_errors:
            st.error(f"• **Subject:** {st.session_state.form_errors['subject']}")
        if "message" in st.session_state.form_errors:
            st.error(f"• **Message:** {st.session_state.form_errors['message']}")
    
    return False


def render_contact_info():
    """
    Render contact information section.
    """
    st.markdown("### Contact Information")
    st.markdown("Feel free to reach out through any of these channels:")
    
    # Email
    st.markdown("**📧 Email**")
    st.markdown("[anggaputrahafidzin@gmail.com](mailto:anggaputrahafidzin@gmail.com)")
    st.markdown("")
    
    # Phone
    st.markdown("**📱 Phone**")
    st.markdown("+62 XXX XXX XXXX")
    st.markdown("")
    
    # Location
    st.markdown("**📍 Location**")
    st.markdown("Indonesia")
    st.markdown("")
    
    # Availability
    st.info("💡 **Available for opportunities** - I'm currently open to new roles and projects!")


def render_social_links():
    """
    Render social media links.
    """
    st.markdown("### Connect With Me")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown(
            "[💼 LinkedIn](https://linkedin.com/in/yourprofile)"
        )
    
    with col2:
        st.markdown(
            "[🐙 GitHub](https://github.com/yourusername)"
        )
    
    with col3:
        st.markdown(
            "[🌐 Website](https://yourwebsite.com)"
        )
