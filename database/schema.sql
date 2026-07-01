-- ============================================================
-- Job Portal System – MySQL Schema
-- Database: job_portal_system
-- ============================================================

CREATE DATABASE IF NOT EXISTS job_portal_system
  CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

USE job_portal_system;

-- --------------------------------------------------------
-- TABLE: users
-- --------------------------------------------------------
CREATE TABLE IF NOT EXISTS users (
  user_id    INT            NOT NULL AUTO_INCREMENT,
  full_name  VARCHAR(150)   NOT NULL,
  email      VARCHAR(150)   NOT NULL,
  password   VARCHAR(255)   NOT NULL,
  role       ENUM('candidate','recruiter','admin') NOT NULL DEFAULT 'candidate',
  phone      VARCHAR(20),
  location   VARCHAR(150),
  skills     TEXT,
  experience VARCHAR(50),
  bio        TEXT,
  is_active  TINYINT(1)     NOT NULL DEFAULT 1,
  created_at DATETIME       NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (user_id),
  UNIQUE KEY uq_email (email),
  INDEX idx_role (role)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------
-- TABLE: companies
-- --------------------------------------------------------
CREATE TABLE IF NOT EXISTS companies (
  company_id   INT          NOT NULL AUTO_INCREMENT,
  recruiter_id INT          NOT NULL,
  company_name VARCHAR(200) NOT NULL,
  industry     VARCHAR(100),
  website      VARCHAR(255),
  description  TEXT,
  location     VARCHAR(150),
  company_size VARCHAR(50),
  founded_year INT,
  created_at   DATETIME     NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (company_id),
  INDEX idx_recruiter (recruiter_id),
  CONSTRAINT fk_company_recruiter
    FOREIGN KEY (recruiter_id) REFERENCES users(user_id) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------
-- TABLE: jobs
-- --------------------------------------------------------
CREATE TABLE IF NOT EXISTS jobs (
  job_id              INT          NOT NULL AUTO_INCREMENT,
  company_id          INT          NOT NULL,
  title               VARCHAR(200) NOT NULL,
  description         TEXT         NOT NULL,
  skills_required     TEXT,
  salary_min          INT,
  salary_max          INT,
  experience_required VARCHAR(50),
  location            VARCHAR(150),
  job_type            ENUM('Full-Time','Part-Time','Contract','Internship','Remote') NOT NULL DEFAULT 'Full-Time',
  vacancies           INT          NOT NULL DEFAULT 1,
  is_active           TINYINT(1)   NOT NULL DEFAULT 1,
  posted_date         DATETIME     NOT NULL DEFAULT CURRENT_TIMESTAMP,
  deadline            DATETIME,
  PRIMARY KEY (job_id),
  INDEX idx_company   (company_id),
  INDEX idx_title     (title),
  INDEX idx_location  (location),
  INDEX idx_posted    (posted_date),
  INDEX idx_active    (is_active),
  CONSTRAINT fk_job_company
    FOREIGN KEY (company_id) REFERENCES companies(company_id) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------
-- TABLE: resumes
-- --------------------------------------------------------
CREATE TABLE IF NOT EXISTS resumes (
  resume_id   INT          NOT NULL AUTO_INCREMENT,
  user_id     INT          NOT NULL,
  file_name   VARCHAR(255) NOT NULL,
  file_path   VARCHAR(500) NOT NULL,
  file_size   INT,
  upload_date DATETIME     NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (resume_id),
  INDEX idx_user_resume (user_id),
  CONSTRAINT fk_resume_user
    FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------
-- TABLE: applications
-- --------------------------------------------------------
CREATE TABLE IF NOT EXISTS applications (
  application_id  INT  NOT NULL AUTO_INCREMENT,
  user_id         INT  NOT NULL,
  job_id          INT  NOT NULL,
  status          ENUM('Applied','Under Review','Shortlisted','Rejected','Selected') NOT NULL DEFAULT 'Applied',
  cover_letter    TEXT,
  applied_date    DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
  updated_at      DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  recruiter_notes TEXT,
  PRIMARY KEY (application_id),
  UNIQUE KEY uq_user_job (user_id, job_id),
  INDEX idx_app_user   (user_id),
  INDEX idx_app_job    (job_id),
  INDEX idx_app_status (status),
  CONSTRAINT fk_app_user
    FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE,
  CONSTRAINT fk_app_job
    FOREIGN KEY (job_id)  REFERENCES jobs(job_id)  ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
