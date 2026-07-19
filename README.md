<div align="center">

# CareerOS

### AI-Powered Career Development & Recruitment Platform

A modern full-stack platform that connects students, recruiters, and companies through secure recruitment workflows and AI-driven career guidance.

---

![Python](https://img.shields.io/badge/Python-3.13-blue?style=for-the-badge&logo=python)
![Django](https://img.shields.io/badge/Django-6.0-0C4B33?style=for-the-badge&logo=django)
![DRF](https://img.shields.io/badge/Django_REST_Framework-API-red?style=for-the-badge)
![React](https://img.shields.io/badge/React-Frontend-61DAFB?style=for-the-badge&logo=react)
![JWT](https://img.shields.io/badge/JWT-Authentication-orange?style=for-the-badge)
![SQLite](https://img.shields.io/badge/SQLite-Database-003B57?style=for-the-badge&logo=sqlite)
![Status](https://img.shields.io/badge/Status-Under_Development-success?style=for-the-badge)

</div>

---

# Overview

CareerOS is an AI-powered career development and recruitment platform built using **Django REST Framework** and **React**.

The platform enables students to build professional profiles, discover opportunities, and apply for jobs, while helping recruiters manage companies, publish job openings, and review applications through a secure REST API.

The long-term vision of CareerOS is to become an intelligent placement platform by integrating AI-powered resume analysis, career scoring, interview preparation, and personalized learning roadmaps.

---

> **Current Progress:** Backend Core APIs Completed • Recruiter Dashboard Implemented • React Frontend Coming Soon

# Key Features

### Student Module

- Student Registration
- Secure JWT Authentication
- Profile Management
- Browse Jobs
- Apply for Jobs
- Track Applications

### Recruiter Module

- Recruiter Authentication
- Company Management
- Job Management (Create, Update, Delete)
- View All Applications
- Update Application Status
- Recruiter Analytics Dashboard

### Platform Features

- RESTful REST APIs
- JWT Authentication & Authorization
- Swagger / OpenAPI Documentation
- Django Admin Panel
- Clean Service Layer Architecture
- Role-Based Access Control
- Recruiter Dashboard Analytics

---

# Technology Stack

| Layer | Technology |
|-------|------------|
| Backend | Python, Django, Django REST Framework |
| Authentication | JWT (SimpleJWT) |
| Database | SQLite (Development), PostgreSQL (Production) |
| Frontend | React, Vite, Tailwind CSS |
| API Documentation | Swagger / OpenAPI |
| Deployment | Render & Vercel |
| Version Control | Git & GitHub |

---

# Project Structure

```text
CareerOS
│
├── backend/
│   ├── accounts/
│   ├── profiles/
│   ├── recruiters/
│   ├── companies/
│   ├── jobs/
│   ├── applications/
│   ├── common/
│   └── config/
│
├── frontend/
│
├── docs/
│
├── assets/
│
└── README.md
```

---

# Completed Modules

# Completed Modules

| Module | Status |
|---------|--------|
| Authentication (JWT) | ✅ Complete |
| Student Profiles | ✅ Complete |
| Recruiter Profiles | ✅ Complete |
| Company Management | ✅ Complete |
| Job Management (CRUD) | ✅ Complete |
| Student Job Applications | ✅ Complete |
| Recruiter Application Status Workflow | ✅ Complete |
| Recruiter Analytics Dashboard | ✅ Complete |
| Swagger / OpenAPI Documentation | ✅ Complete |
| Django Admin Integration | ✅ Complete |
| Service Layer Architecture | ✅ Complete |
| Role-Based Authorization | ✅ Complete |

---

# Recent Development (July 2026)

### Recruiter Dashboard

Implemented a recruiter analytics dashboard providing real-time recruitment insights including:

- Total Jobs Posted
- Active Jobs
- Total Applications
- Applied Candidates
- Reviewed Candidates
- Shortlisted Candidates
- Interview Pipeline
- Selected Candidates
- Rejected Candidates

### Application Status Workflow

Implemented a complete application lifecycle management system.

Recruiters can now update candidate application status through secured REST APIs.

Supported workflow:

```
Applied
   ↓
Reviewed
   ↓
Shortlisted
   ↓
Interview
   ↓
Selected / Rejected
```

### Backend Improvements

- Added Dashboard Service Layer
- Improved API Architecture
- Added Role-Based Authorization
- Enhanced Swagger Documentation
- Fixed API Schema Generation
- Improved Recruiter Workflows

# Development Roadmap

## Phase 1 (Completed)

- JWT Authentication
- Student Profiles
- Recruiter Profiles
- Company Management
- Job Management
- Job Applications
- Recruiter Application Status Workflow
- Recruiter Dashboard Analytics
- Swagger API Documentation

---

##  Phase 2 (In Progress)

- Student Dashboard
- Job Search & Filters
- Pagination
- Resume Upload
- Saved Jobs

---

##  Phase 3

- Career Score
- AI Resume Analyzer
- AI Job Recommendations
- Learning Roadmaps
- Notifications

---

##  Phase 4

- React Frontend
- Dashboard UI
- Production Deployment
- CI/CD

---

# API Documentation

After starting the backend server:

```text
http://127.0.0.1:8000/api/docs/
```

---

# Local Setup

Clone the repository

```bash
git clone https://github.com/NEHA200424/careeros.git
```

Move into the backend

```bash
cd backend
```

Create virtual environment

```bash
python -m venv venv
```

Activate virtual environment

```bash
venv\Scripts\activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run migrations

```bash
python manage.py migrate
```

Start the development server

```bash
python manage.py runserver
```

---

# Future Enhancements

- Student Analytics Dashboard
- Resume Upload & Parsing
- AI Resume Analysis
- Career Score Prediction
- Job Recommendation Engine
- Saved Jobs
- Email Notifications
- Interview Scheduler
- Learning Roadmaps
- Placement Analytics

---

# Author

**Neha Vinod Varma**

B.Tech – Artificial Intelligence & Machine Learning

Python Full Stack Developer

GitHub: https://github.com/NEHA200424

---

# License

This project is licensed under the MIT License.