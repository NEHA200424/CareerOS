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
- Job Management
- Applicant Management

### Platform Features

- RESTful API
- Swagger Documentation
- Django Admin
- Modular Service Architecture
- JWT Authentication

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

| Module | Status |
|---------|--------|
| Authentication | Complete |
| Student Profiles | Complete |
| Recruiter Profiles | Complete |
| Company Management | Complete |
| Job Management | Complete |
| Job Applications | Complete |
| Swagger Documentation | Complete |
| Django Admin | Complete |

---

# Development Roadmap

### Phase 1

- Authentication
- Student Profiles
- Recruiter Profiles
- Companies
- Jobs
- Applications

### Phase 2

- Recruiter Dashboard
- Application Status Workflow
- Notifications
- Search & Filters

### Phase 3

- Career Score
- AI Resume Analyzer
- AI Career Roadmaps
- Recommendation Engine

### Phase 4

- Frontend Dashboard
- Deployment
- Production Release

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

- AI Resume Analysis
- Career Recommendation Engine
- Resume Builder
- Interview Preparation
- Email Notifications
- Placement Analytics
- Learning Roadmaps
- Career Score Prediction

---

# Author

**Neha Vinod Varma**

B.Tech – Artificial Intelligence & Machine Learning

Python Full Stack Developer

GitHub: https://github.com/NEHA200424

---

# License

This project is licensed under the MIT License.