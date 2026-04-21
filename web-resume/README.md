# Web Resume Portfolio - Angga Putra Hafidzin

A modern, interactive web-based resume and portfolio application built with Streamlit. This application provides a comprehensive view of professional experience, skills, and project portfolio in an engaging, multi-page format.

![Status](https://img.shields.io/badge/status-active-success)
![Python](https://img.shields.io/badge/python-3.8+-blue)
![Streamlit](https://img.shields.io/badge/streamlit-1.32+-red)
![License](https://img.shields.io/badge/license-MIT-green)

## ✨ Features

### 🏠 Home Page

- Professional hero section with introduction
- Quick stats overview (experience, projects, skills)
- Featured projects showcase
- Call-to-action sections

### 📄 Resume Page

- Complete professional information
- Work experience timeline
- Education history
- Skills visualization (technical & soft skills)
- Certifications and awards
- PDF download option

### 💼 Portfolio Page

- Interactive project gallery
- Advanced filtering by technology
- Category-based organization
- Search functionality
- Compact project cards

### 📁 Project Detail Pages

- Comprehensive project descriptions
- Problem & solution breakdowns
- Technology stack display
- Challenges & solutions documentation
- Results and impact metrics
- Project gallery
- Related projects suggestions

### 📧 Contact Page

- Contact form with validation
- Direct contact information
- Social media links
- FAQ section
- Availability status

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- pip package manager

### Installation

1. **Clone or navigate to the project directory:**

   ```bash
   cd "d:\Personal Document\Curriculum Vitae\web-resume"
   ```

2. **Create a virtual environment (recommended):**

   ```bash
   python -m venv .venv
   ```

3. **Activate the virtual environment:**
   - Windows:
     ```bash
     .venv\Scripts\activate
     ```
   - macOS/Linux:
     ```bash
     source .venv/bin/activate
     ```

4. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

5. **Run the application:**

   ```bash
   streamlit run app.py
   ```

6. **Open your browser:**
   The application will open at `http://localhost:8501`

## 📁 Project Structure

```
web-resume/
├── app.py                          # Main application entry point
├── requirements.txt                # Python dependencies
├── README.md                       # Project documentation
├── .streamlit/
│   └── config.toml                # Streamlit configuration
├── src/
│   ├── __init__.py
│   ├── pages/                     # Page components
│   │   ├── __init__.py
│   │   ├── home.py               # Home page
│   │   ├── resume.py             # Resume page
│   │   ├── portfolio.py          # Portfolio overview
│   │   ├── project_detail.py     # Individual project view
│   │   └── contact.py            # Contact page
│   ├── components/                # Reusable UI components
│   │   ├── __init__.py
│   │   ├── navigation.py         # Sidebar navigation
│   │   ├── project_card.py       # Project card components
│   │   ├── skill_bar.py          # Skill visualization
│   │   ├── timeline_item.py      # Experience/education items
│   │   └── contact_form.py       # Contact form with validation
│   └── utils/                     # Utility functions
│       ├── __init__.py
│       ├── data_loader.py        # Data loading and caching
│       └── validators.py         # Form validation
├── data/
│   ├── resume.json               # Resume data structure
│   └── projects.json             # Projects metadata
├── content/
│   └── projects/                 # Detailed project markdown files
│       ├── web-resume-portfolio.md
│       ├── data-analysis-dashboard.md
│       └── ...
└── assets/
    ├── images/                   # Images and graphics
    │   ├── profile.jpg
    │   └── projects/
    └── documents/                # Downloadable files
        └── CV-AnggaPutra-Hafidzin.pdf
```

## 🛠️ Technology Stack

- **Frontend Framework:** Streamlit 1.32+
- **Programming Language:** Python 3.8+
- **Data Format:** JSON
- **Styling:** Custom CSS + Streamlit theming
- **Form Validation:** Custom validators
- **Markdown Processing:** Python markdown library

## 📊 Data Configuration

### Resume Data (`data/resume.json`)

The resume data is stored in a structured JSON format. Update the following sections:

```json
{
  "personal": {
    "name": "Your Name",
    "title": "Your Title",
    "email": "your.email@example.com",
    "phone": "+62 XXX XXX XXXX",
    "location": "City, Country",
    "linkedin": "linkedin.com/in/yourprofile",
    "github": "github.com/yourusername"
  },
  "summary": "Your professional summary...",
  "experience": [...],
  "education": [...],
  "skills": {...},
  "certifications": [...],
  "awards": [...]
}
```

### Projects Data (`data/projects.json`)

Each project includes:

```json
{
  "id": "project-001",
  "slug": "project-name",
  "title": "Project Title",
  "subtitle": "Brief tagline",
  "category": "Web Application",
  "description": "Short description",
  "long_description": "Detailed description",
  "technologies": ["Python", "Streamlit"],
  "role": "Developer",
  "team_size": 1,
  "start_date": "2024-01",
  "end_date": "2024-03",
  "status": "completed",
  "featured": true,
  "links": {
    "live": "https://...",
    "github": "https://..."
  }
}
```

## 🎨 Customization

### Theme Colors

Edit `.streamlit/config.toml` to customize colors:

```toml
[theme]
primaryColor = "#2563EB"
backgroundColor = "#FFFFFF"
secondaryBackgroundColor = "#F3F4F6"
textColor = "#1F2937"
font = "sans serif"
```

### Adding New Projects

1. Add project metadata to `data/projects.json`
2. Create detailed content in `content/projects/project-slug.md`
3. Add images to `assets/images/projects/`
4. Restart the application

### Adding Custom CSS

Add custom styles in `app.py` within the `st.markdown()` CSS block or create a separate `styles/custom.css` file.

## 🧪 Testing

### Manual Testing Checklist

- [ ] All navigation links work correctly
- [ ] Resume information displays accurately
- [ ] Project filtering works as expected
- [ ] Contact form validates input properly
- [ ] Responsive design works on mobile/tablet
- [ ] All images load correctly
- [ ] PDF download works (when implemented)
- [ ] No console errors in browser

### Running the App

```bash
# Development mode
streamlit run app.py

# Production mode (if deploying)
streamlit run app.py --server.headless true --server.port 8501
```

## 🚀 Deployment

### Deploy to Streamlit Cloud

1. **Push your code to GitHub**

2. **Go to [share.streamlit.io](https://share.streamlit.io)**

3. **Connect your repository**

4. **Configure deployment:**
   - Main file path: `app.py`
   - Python version: 3.10+
   - Install command: `pip install -r requirements.txt`

5. **Deploy!**

### Alternative Hosting Options

- **Hugging Face Spaces** - Free hosting with Streamlit support
- **VPS/Dedicated Server** - Full control with Docker
- **Heroku** - Easy deployment (requires Procfile)

## 📝 Content Updates

### Updating Personal Information

Edit `data/resume.json` and update the `personal` section with your actual information from your CV.

### Updating Projects

1. Edit `data/projects.json` to add/modify projects
2. Update corresponding markdown files in `content/projects/`
3. Add project images to `assets/images/projects/`

### Adding Images

Place images in the appropriate folders:

- Profile photo: `assets/images/profile.jpg`
- Project images: `assets/images/projects/`
- Company logos: `assets/images/companies/`

## 🔧 Troubleshooting

### Common Issues

**Issue: App won't start**

```bash
# Check Python version
python --version

# Reinstall dependencies
pip install -r requirements.txt --force-reinstall
```

**Issue: Data not loading**

- Verify JSON files are valid (use JSONLint)
- Check file paths are correct
- Restart Streamlit server

**Issue: Images not displaying**

- Verify image paths in JSON files
- Ensure images exist in the specified locations
- Check file extensions match

**Issue: Styling not applying**

- Clear browser cache
- Check CSS syntax
- Restart Streamlit with `Ctrl+C` and rerun

## 📄 License

This project is open source and available under the MIT License.

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📞 Support

For questions or issues:

- Email: anggaputrahafidzin@gmail.com
- GitHub Issues: [Create an issue](https://github.com/yourusername/web-resume/issues)

## 🙏 Acknowledgments

- Built with [Streamlit](https://streamlit.io/)
- Inspired by modern portfolio designs
- Part of the PRD implementation plan

---

**Last Updated:** April 4, 2026  
**Version:** 1.0.0  
**Author:** Angga Putra Hafidzin
