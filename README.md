# 🧳 Job Portal System

A complete **Industry-Level Job Portal** built with **Python Flask**, **MySQL**, **SQLAlchemy**, and **Bootstrap 5**.

---

## 🚀 Tech Stack

| Layer     | Technology                          |
|-----------|-------------------------------------|
| Backend   | Python 3.x · Flask · SQLAlchemy     |
| Database  | MySQL 8.x                           |
| Frontend  | HTML5 · CSS3 · Bootstrap 5 · JS     |
| Auth      | Flask-Login · Werkzeug Security     |
| Forms     | Flask-WTF · WTForms                 |
| Charts    | Chart.js                            |

---

## 📁 Project Structure

```
Job_Portal_System/
├── app.py                  ← Flask app factory
├── config.py               ← Configuration
├── requirements.txt
├── README.md
├── database/
│   ├── schema.sql          ← MySQL schema
│   └── sample_data.sql     ← Test data
├── models/                 ← SQLAlchemy ORM models
│   ├── user.py
│   ├── company.py
│   ├── job.py
│   ├── application.py
│   └── resume.py
├── routes/                 ← Flask Blueprints
│   ├── auth.py
│   ├── candidate.py
│   ├── recruiter.py
│   ├── jobs.py
│   └── applications.py
├── forms/                  ← WTForms
│   ├── login_form.py
│   ├── register_form.py
│   └── job_form.py
├── templates/              ← Jinja2 HTML templates
│   ├── base.html
│   ├── index.html
│   ├── login.html
│   ├── register.html
│   ├── candidate/
│   ├── recruiter/
│   └── jobs/
└── static/
    ├── css/style.css
    ├── js/main.js
    └── uploads/            ← Resume files (auto-created)
```

---

## ⚙️ Setup Instructions

### Prerequisites
- Python 3.9+
- MySQL 8.x
- VS Code (recommended)

---

### Step 1 – Clone / Extract the Project

```bash
cd Desktop
# extract the ZIP or copy the folder
```

### Step 2 – Create a Virtual Environment

```bash
cd Job_Portal_System

# Windows
python -m venv venv
venv\Scripts\activate

# macOS / Linux
python3 -m venv venv
source venv/bin/activate
```

### Step 3 – Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 4 – Create MySQL Database

Open **MySQL Workbench** or the MySQL CLI and run:

```sql
CREATE DATABASE job_portal_system CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
```

Or run the provided script:

```bash
mysql -u root -p < database/schema.sql
```

### Step 5 – Configure Database Connection

Open `config.py` and update the URI with your MySQL credentials:

```python
SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://YOUR_USER:YOUR_PASSWORD@localhost:3306/job_portal_system'
```

### Step 6 – (Optional) Load Sample Data

```bash
mysql -u root -p job_portal_system < database/sample_data.sql
```

> ⚠️ The sample data contains placeholder password hashes. To create working test accounts, register via the web UI instead.

### Step 7 – Run the Application

```bash
python app.py
```

Open your browser and navigate to: **http://127.0.0.1:5000**

---

## 🔑 Default Test Accounts (register via UI)

| Role      | Steps                                        |
|-----------|----------------------------------------------|
| Candidate | Register → select "Job Seeker"               |
| Recruiter | Register → select "Recruiter" → add company  |

---

## 🌟 Features

### Candidate
- Register & Login
- Update profile (skills, experience, bio)
- Upload PDF/DOCX resume
- Browse & search jobs (title, location, type, experience)
- Apply to jobs with cover letter
- Track application status (Applied → Shortlisted → Selected)
- Withdraw applications
- Dashboard with Chart.js analytics

### Recruiter
- Register & Login
- Create company profile
- Post / Edit / Delete jobs
- Activate / Deactivate job listings
- View all applicants per job
- Update application status with notes
- Dashboard with application analytics

---

## 📊 Application Status Flow

```
Applied → Under Review → Shortlisted → Selected
                      ↘ Rejected
```

---

## 🔒 Security Features

- **Password Hashing** – Werkzeug PBKDF2-SHA256
- **CSRF Protection** – Flask-WTF tokens on every form
- **Role-Based Access Control** – Candidate / Recruiter / Admin
- **Session Management** – Flask-Login
- **SQL Injection Prevention** – SQLAlchemy ORM (no raw SQL)
- **File Upload Validation** – extension + size checks

---

## 📬 Contact

**Support:** support@jobportal.com  
**Location:** Hyderabad, India
