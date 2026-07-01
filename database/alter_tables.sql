-- ============================================================
-- ALTER TABLE Statements for Job Portal System
-- Date: 2026-06-29
-- ============================================================
-- These statements add new columns to support:
-- 1. Profile picture upload
-- 2. Enhanced profile information
-- 3. Job apply URL and company logos
-- ============================================================

USE job_portal_system;

-- --------------------------------------------------------
-- ALTER TABLE: users
-- Add profile picture and enhanced profile fields
-- --------------------------------------------------------

-- Profile Picture
ALTER TABLE users ADD COLUMN profile_picture VARCHAR(500) 
  COMMENT 'Path to uploaded profile picture' AFTER bio;

-- Personal Details
ALTER TABLE users ADD COLUMN professional_title VARCHAR(100) 
  COMMENT 'Professional title/designation' AFTER profile_picture;

ALTER TABLE users ADD COLUMN date_of_birth DATE 
  COMMENT 'Date of birth' AFTER professional_title;

ALTER TABLE users ADD COLUMN gender VARCHAR(20) 
  COMMENT 'Gender (Male/Female/Other)' AFTER date_of_birth;

ALTER TABLE users ADD COLUMN address TEXT 
  COMMENT 'Street address' AFTER gender;

ALTER TABLE users ADD COLUMN city VARCHAR(100) 
  COMMENT 'City' AFTER address;

ALTER TABLE users ADD COLUMN state VARCHAR(100) 
  COMMENT 'State/Province' AFTER city;

ALTER TABLE users ADD COLUMN country VARCHAR(100) 
  COMMENT 'Country' AFTER state;

ALTER TABLE users ADD COLUMN pin_code VARCHAR(20) 
  COMMENT 'Postal/PIN code' AFTER country;

-- Professional Details
ALTER TABLE users ADD COLUMN qualification VARCHAR(100) 
  COMMENT 'Highest qualification (B.Tech, M.Tech, etc.)' AFTER pin_code;

ALTER TABLE users ADD COLUMN college VARCHAR(200) 
  COMMENT 'College/University name' AFTER qualification;

ALTER TABLE users ADD COLUMN current_company VARCHAR(200) 
  COMMENT 'Current company name' AFTER college;

ALTER TABLE users ADD COLUMN current_salary VARCHAR(50) 
  COMMENT 'Current salary' AFTER current_company;

ALTER TABLE users ADD COLUMN expected_salary VARCHAR(50) 
  COMMENT 'Expected salary' AFTER current_salary;

ALTER TABLE users ADD COLUMN preferred_job_role VARCHAR(100) 
  COMMENT 'Preferred job role/position' AFTER expected_salary;

ALTER TABLE users ADD COLUMN preferred_location VARCHAR(150) 
  COMMENT 'Preferred job location' AFTER preferred_job_role;

-- Social Links
ALTER TABLE users ADD COLUMN linkedin_url VARCHAR(255) 
  COMMENT 'LinkedIn profile URL' AFTER preferred_location;

ALTER TABLE users ADD COLUMN github_url VARCHAR(255) 
  COMMENT 'GitHub profile URL' AFTER linkedin_url;

ALTER TABLE users ADD COLUMN portfolio_url VARCHAR(255) 
  COMMENT 'Portfolio website URL' AFTER github_url;

-- --------------------------------------------------------
-- ALTER TABLE: jobs
-- Add external application links and company logo
-- --------------------------------------------------------

ALTER TABLE jobs ADD COLUMN deadline DATETIME 
  COMMENT 'Application deadline' AFTER posted_date;

ALTER TABLE jobs ADD COLUMN apply_url VARCHAR(500) 
  COMMENT 'Official job application URL' AFTER deadline;

ALTER TABLE jobs ADD COLUMN company_logo VARCHAR(255) 
  COMMENT 'URL to company logo image' AFTER apply_url;

-- ============================================================
-- NOTE: These changes are backward compatible and do not
-- modify existing columns or delete any data.
-- ============================================================
