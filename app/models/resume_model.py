"""
===========================================================
Project     : NextHire AI
File        : resume_model.py
Author      : Santosh Kolagani

Purpose:
    Data models defining structured Resume schemas.
===========================================================
"""

from typing import List, Optional
from pydantic import BaseModel, Field


class PersonalInfo(BaseModel):
    full_name: str = ""
    email: str = ""
    phone: str = ""
    location: str = ""
    linkedin: str = ""
    github: str = ""
    portfolio: str = ""
    summary: str = ""


class EducationItem(BaseModel):
    degree: str = ""
    field_of_study: str = ""
    institution: str = ""
    location: str = ""
    start_year: str = ""
    end_year: str = ""
    grade: str = ""
    achievements: str = ""


class ExperienceItem(BaseModel):
    job_title: str = ""
    company: str = ""
    location: str = ""
    start_date: str = ""
    end_date: str = ""
    is_current: bool = False
    bullet_points: List[str] = Field(default_factory=list)


class ProjectItem(BaseModel):
    title: str = ""
    technologies: str = ""
    link: str = ""
    description: str = ""
    bullet_points: List[str] = Field(default_factory=list)


class SkillCategory(BaseModel):
    category_name: str = ""  # e.g., "Programming Languages", "Frameworks & Tools"
    skills: List[str] = Field(default_factory=list)


class CertificationItem(BaseModel):
    name: str = ""
    issuing_organization: str = ""
    issue_date: str = ""
    credential_url: str = ""


class JobTarget(BaseModel):
    job_title: str = ""
    company_name: str = ""
    job_description: str = ""
    personalized_mode: bool = False


class AnalysisResult(BaseModel):
    overall_score: int = 0
    ats_compatibility_score: int = 0
    content_quality_score: int = 0
    formatting_score: int = 0
    strengths: List[str] = Field(default_factory=list)
    improvements: List[str] = Field(default_factory=list)
    missing_keywords: List[str] = Field(default_factory=list)
    actionable_suggestions: List[str] = Field(default_factory=list)


class ResumeData(BaseModel):
    personal_info: PersonalInfo = Field(default_factory=PersonalInfo)
    education: List[EducationItem] = Field(default_factory=list)
    experience: List[ExperienceItem] = Field(default_factory=list)
    projects: List[ProjectItem] = Field(default_factory=list)
    skills: List[SkillCategory] = Field(default_factory=list)
    certifications: List[CertificationItem] = Field(default_factory=list)
    job_target: JobTarget = Field(default_factory=JobTarget)
    selected_template: str = "ats_classic"
    analysis: Optional[AnalysisResult] = None
