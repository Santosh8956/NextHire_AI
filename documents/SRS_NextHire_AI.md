# Software Requirements Specification (SRS)

# NextHire AI

## AI-Powered Resume Builder with Intelligent Resume Strength Analysis and Personalized Resume Generation

---

## Version

Version 1.0

---

## Prepared By

Santosh Kolagani

B.Tech - Computer Science & Engineering (Data Science)

GIET College of Engineering

---

## Project Type

Academic Major Project

---

## Document Purpose

This Software Requirements Specification (SRS) defines the functional and non-functional requirements of the NextHire AI system. The document serves as the primary reference for designing, developing, testing, deploying, and maintaining the application throughout the project lifecycle.

---

## Date

(To be updated during final submission)

# 2. Project Overview

NextHire AI is an intelligent AI-powered resume builder designed to simplify resume creation while improving resume quality through artificial intelligence.

Unlike conventional resume builders that only collect user information and generate a static resume, NextHire AI provides an interactive experience where users can create professional resumes, personalize them for specific job applications, analyze resume strength, edit content, regenerate selected sections using AI, and maintain multiple resume versions without repeatedly entering their information.

The system is designed with a user-first philosophy where artificial intelligence assists users rather than replacing their decisions. Every recommendation remains optional, allowing users to maintain full control over their resume content.

# 3. Problem Statement

Many existing resume builders require users to manually write professional summaries, optimize resumes for Applicant Tracking Systems (ATS), and repeatedly create new resumes for different companies.

Most available platforms either provide limited customization, require premium subscriptions for advanced AI features, or overwhelm users with lengthy forms and complex workflows.

Students and fresh graduates often struggle to create professional resumes due to limited writing experience and lack of knowledge about industry expectations.

NextHire AI aims to solve these challenges by providing an intelligent, user-friendly, and accessible resume-building platform that combines AI assistance with complete user control.

# 4. Objectives

The primary objectives of NextHire AI are:

- Simplify resume creation for students and professionals.
- Generate professional resume content using AI.
- Allow users to personalize resumes for specific job applications.
- Provide intelligent Resume Strength Analysis.
- Enable live editing before downloading.
- Support AI-powered regeneration of selected resume sections.
- Allow users to create multiple resume versions from a single career profile.
- Offer a clean, modern, and beginner-friendly user experience.

# 5. Scope

NextHire AI is an AI-powered resume builder designed to help students, fresh graduates, and professionals create high-quality resumes with minimal effort.

The application enables users to build professional resumes by providing structured career information through a simple and user-friendly interface. Users can create either a general resume for future opportunities or a personalized resume tailored to a specific job role and company.

The system provides multiple resume templates, AI-powered content generation, Resume Strength Analysis, editable resume previews, AI-assisted content improvement, resume version management, and PDF export.

Version 1 of NextHire AI focuses on delivering a complete resume-building experience from data collection to resume generation, editing, analysis, optimization, and download. Features such as user authentication, cloud synchronization, cover letter generation, interview preparation, and resume sharing are outside the scope of Version 1 and are planned for future releases.

# 6. Target Users

NextHire AI is designed for users who want to create professional resumes quickly and efficiently.

The primary target users include:

- Students creating their first resume.
- Fresh graduates applying for internships or full-time jobs.
- Job seekers looking to improve their existing resumes.
- Professionals applying for different companies using personalized resumes.
- Individuals preparing resumes for future career opportunities.
- Career changers updating their resumes for new industries.

# 7. Functional Requirements

The system shall provide the following functionalities:

## User Interaction

- Display an interactive landing page.
- Introduce the application through an AI welcome screen.
- Allow users to choose between creating a General Resume or a Job-Specific Resume.

## Data Collection

- Collect personal information.
- Collect education details.
- Collect technical, soft, and non-technical skills.
- Collect project details.
- Collect internship and work experience.
- Collect certifications.
- Collect optional career goals and job preferences.

## Resume Templates

- Display multiple resume templates.
- Allow template search and filtering.
- Allow users to preview templates before selection.

## AI Resume Generation

- Generate a professional summary.
- Improve project descriptions.
- Improve experience descriptions.
- Organize skills professionally.
- Optimize content for ATS compatibility.

## Resume Editing

- Allow users to edit any section of the resume.
- Support live preview while editing.

## Resume Analysis

- Generate a Resume Strength Score.
- Display strengths and improvement areas.
- Provide AI-generated suggestions.

## AI Regeneration

- Improve selected sections.
- Regenerate selected sections.
- Regenerate the entire resume.

## Resume Management

- Create multiple resume versions using the same career profile.
- Allow template switching without re-entering data.

## Export

- Export the final resume as a PDF.

# 8. Non-Functional Requirements

The system should satisfy the following quality requirements:

## Usability

- The interface should be simple and beginner-friendly.
- Users should be able to navigate the application easily.
- Data collection should be minimal and well-organized.

## Performance

- Resume generation should complete within a reasonable time.
- Resume analysis should provide quick feedback.

## Reliability

- The system should generate consistent and professional resumes.
- User-entered information should remain accurate throughout the session.

## Security

- Personalization should remain optional.
- User data should not be shared without permission.

## Maintainability

- The project should follow a modular architecture.
- The codebase should be easy to understand and extend.

## Compatibility

- The application should run on Windows, macOS, and Linux.
- It should support modern web browsers after deployment.

## Cost

- The project should use free and open-source technologies wherever possible.

# 9. System Workflow

NextHire AI follows a structured and user-centric workflow that simplifies the resume-building process while leveraging Artificial Intelligence to improve resume quality. The application is designed to guide users step by step, ensuring they remain in control of their resume throughout the process.

The workflow consists of the following stages:

## Step 1: Landing Page

The user visits the NextHire AI website and is introduced to the platform through a modern landing page.

Available options include:

- Get Started
- View Demo Resume

---

## Step 2: AI Welcome Screen

The AI assistant welcomes the user and briefly explains how NextHire AI works.

The user proceeds by clicking:

- Continue

---

## Step 3: Resume Purpose Selection

The user chooses one of the following options:

- Create a General Resume (for future opportunities)
- Create a Personalized Resume (for a specific job)

If the user selects **Personalized Resume**, they may optionally provide:

- Job Role
- Company Name
- Job Description (Paste or Upload)

If they prefer not to share these details, they can skip this step and continue with a general resume.

---

## Step 4: Resume Template Selection

The user selects a preferred resume template.

Features available:

- Search Templates
- Category Filters
- Recommendation Tags
- Template Preview
- Load More Templates

---

## Step 5: Career Information Collection

The application collects structured career information through an organized form.

The user provides:

- Personal Details
- Education
- Skills
- Projects
- Experience
- Certifications
- Career Goals (Optional)
- Job Preferences (Optional)

Available actions:

- Save Draft
- Create Resume

---

## Step 6: AI Resume Generation

The AI engine analyzes the provided information and generates a professional resume containing:

- Professional Summary
- Optimized Skills Section
- Enhanced Project Descriptions
- Enhanced Experience Descriptions
- ATS-friendly formatting

---

## Step 7: Resume Preview & Editing

The generated resume is displayed in an editable workspace.

The user can modify any section manually before finalizing the resume.

Editable sections include:

- Summary
- Education
- Skills
- Projects
- Experience
- Certifications
- Career Objective

---

## Step 8: Resume Strength Analysis

The application evaluates the resume and displays:

- Overall Resume Strength Score
- Resume Rating
- Strengths
- Improvement Areas
- AI Insights

The user may click **Analyze Resume** after making edits to receive an updated analysis.

---

## Step 9: AI Regeneration

After editing the resume, the user can select one or more sections and regenerate them using AI.

Available options:

- Improve Selected Sections
- Regenerate Selected Sections
- Regenerate Entire Resume

The AI only modifies the sections selected by the user.

---

## Step 10: Resume Version Management

Users can create multiple resume versions from the same career profile without re-entering their information.

Example versions:

- General Resume
- Google Resume
- Deloitte Resume
- Microsoft Resume

Each version can have a different template or AI optimization.

---

## Step 11: Resume Download

After reviewing the final resume, the user can download it.

Version 1 supports:

- PDF

Additional formats may be added in future versions.

---

## Step 12: Session Completion

The resume-building session ends after the download process.

Users can return to edit, analyze, regenerate, or create another resume version before exiting the application.

Website Opens
        │
        ▼
Landing Page
        │
        ▼
AI Welcome Screen
        │
        ▼
Choose Resume Type
        │
        ├─────────────────────┐
        │                     │
        ▼                     ▼
General Resume      Personalized Resume
                           │
                           ▼
              (Optional Job Details)
                           │
                           ▼
Resume Template Selection
        │
        ▼
Career Information Collection
        │
        ▼
Create Resume
        │
        ▼
AI Resume Generation
        │
        ▼
Resume Preview & Editing
        │
        ▼
Resume Strength Analysis
        │
        ▼
User Edits Resume
        │
        ▼
Select Sections
        │
        ▼
AI Regenerate
        │
        ▼
Analyze Resume Again (Optional)
        │
        ▼
Create Resume Version (Optional)
        │
        ▼
Download PDF
        │
        ▼
Finish

# 10. Features

NextHire AI provides a comprehensive set of features designed to simplify resume creation while giving users complete control over their resume content.

## 10.1 User Experience Features

- Modern and intuitive landing page
- AI-powered welcome screen
- Beginner-friendly interface
- Guided resume creation workflow
- Save Draft
- Continue Previous Session
- Live editable resume preview

---

## 10.2 Resume Management Features

- General Resume creation
- Personalized Resume creation
- Multiple resume templates
- Resume version management
- Template switching without re-entering data
- PDF download

---

## 10.3 AI Features

- AI-generated Professional Summary
- AI-enhanced Project Descriptions
- AI-enhanced Experience Descriptions
- ATS-aware resume optimization
- AI Resume Strength Analysis
- AI-powered resume insights
- Improve Selected Sections
- Regenerate Selected Sections
- Regenerate Entire Resume

---

## 10.4 Resume Analysis Features

- Resume Strength Score
- Resume Rating
- Strength Analysis
- Improvement Suggestions
- Progress Tracking after improvements

---

## 10.5 Personalization Features

- Job Role-based resume customization
- Company-specific resume generation
- Job Description analysis (Optional)
- General resume generation without job details
- Optional personalization through Skip functionality

---

## 10.6 Editing Features

- Edit any resume section
- Select multiple sections
- AI regeneration after editing
- Manual editing before download
- Reanalyze resume after modifications

---

## 10.7 Template Features

- Search templates
- Category filters
- Recommendation tags
- Template preview
- Load More templates

# 11. Technology Stack

NextHire AI is developed entirely using free and open-source technologies to ensure accessibility, scalability, and ease of maintenance. The selected technologies provide a balance between AI capabilities, development simplicity, and deployment flexibility.

| Technology | Purpose |
|------------|---------|
| Python | Core programming language used for application development and AI integration. |
| Jupyter Notebook | Primary development environment for building and testing the application modules during development. |
| Streamlit | Used to develop the interactive web application interface for end users. |
| Pandas | Handles structured data processing and management of user information. |
| NumPy | Performs numerical operations and supports data manipulation tasks. |
| Hugging Face Transformers | Generates AI-powered resume content such as Professional Summary and section improvements. |
| PyTorch | Backend deep learning framework required for running Transformer models. |
| ReportLab | Generates professional PDF resumes for download. |
| PyMuPDF | Reads and analyzes PDF resumes for Resume Strength Analysis and future enhancements. |
| HTML | Provides structured content for the web interface where required. |
| CSS | Enhances the appearance and responsiveness of the user interface. |
| Git | Version control system used to manage source code throughout development. |
| GitHub | Stores the project repository and maintains version history for collaboration and backup. |

## Development Approach

The project follows a modular development approach.

- Individual features are first developed and tested in Jupyter Notebook.
- Once validated, they are integrated into the Streamlit application.
- The complete application is tested before deployment.

This approach simplifies debugging, improves code quality, and allows each module to be independently maintained.

# 12. Constraints

The development of NextHire AI is subject to the following constraints:

## Technical Constraints

- The application is developed using only free and open-source technologies.
- AI functionality is executed using a locally hosted Transformer model.
- Version 1 supports PDF export only.
- Internet connectivity is required only for the initial download of AI models and required libraries.

## Hardware Constraints

- The application is optimized for standard personal computers with moderate hardware specifications.
- AI generation speed depends on the user's CPU performance since Version 1 does not require a dedicated GPU.

## Project Constraints

- User authentication is not included in Version 1.
- Cloud storage is not included in Version 1.
- Resume data is stored locally during development.
- The project focuses on resume creation and optimization only.

## Development Constraints

- The project is implemented using Python.
- Jupyter Notebook is used for development and testing.
- Streamlit is used for the final web application.

# 13. Future Enhancements

The following features are planned for future versions of NextHire AI:

- User authentication and account management.
- Cloud synchronization for resumes and drafts.
- DOCX resume export.
- AI-powered cover letter generation.
- AI interview preparation module.
- Portfolio builder integration.
- Resume sharing through secure links.
- Multi-language resume generation.
- Advanced ATS compatibility analysis.
- Mobile application support.
- AI-powered career recommendations.
- Integration with professional networking platforms.

# 14. Conclusion

- NextHire AI aims to provide an intelligent, user-friendly, and accessible platform for creating professional resumes. By combining Artificial Intelligence
  with a structured and interactive workflow, the system assists users in generating high-quality resumes while ensuring they remain in full control of their
  content.

- The application is designed to simplify resume creation, improve resume quality through AI-powered analysis and suggestions, and support users in preparing
  resumes for both future opportunities and specific job applications.

- The Software Requirements Specification presented in this document establishes the functional and non-functional requirements of the system and serves as the
  foundation for the design, development, testing, and deployment of NextHire AI.