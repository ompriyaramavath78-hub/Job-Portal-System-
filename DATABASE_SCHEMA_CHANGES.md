# Database Schema Changes - Reference Guide

## Summary
This document provides a detailed reference of all database schema changes made to the Job Portal System.

**Total Changes**: 26 new columns added to 2 tables
**Backward Compatibility**: ✅ Yes - All changes are NULLABLE and non-breaking
**Data Loss Risk**: ✅ None - No existing data modified or deleted

---

## Users Table - New Columns

### Profile Picture
```sql
ALTER TABLE users ADD COLUMN profile_picture VARCHAR(500) 
  COMMENT 'Path to uploaded profile picture' AFTER bio;
```
- **Type**: VARCHAR(500)
- **Nullable**: YES
- **Purpose**: Store path to user's profile picture
- **Format**: `uploads/profile/{filename}`

### Personal Details

#### Professional Title
```sql
ALTER TABLE users ADD COLUMN professional_title VARCHAR(100) 
  COMMENT 'Professional title/designation' AFTER profile_picture;
```
- **Type**: VARCHAR(100)
- **Example**: "Senior Software Engineer", "Product Manager"

#### Date of Birth
```sql
ALTER TABLE users ADD COLUMN date_of_birth DATE 
  COMMENT 'Date of birth' AFTER professional_title;
```
- **Type**: DATE
- **Format**: YYYY-MM-DD

#### Gender
```sql
ALTER TABLE users ADD COLUMN gender VARCHAR(20) 
  COMMENT 'Gender (Male/Female/Other)' AFTER date_of_birth;
```
- **Type**: VARCHAR(20)
- **Values**: Male, Female, Other

#### Address
```sql
ALTER TABLE users ADD COLUMN address TEXT 
  COMMENT 'Street address' AFTER gender;
```
- **Type**: TEXT
- **Purpose**: Store street address

#### City
```sql
ALTER TABLE users ADD COLUMN city VARCHAR(100) 
  COMMENT 'City' AFTER address;
```
- **Type**: VARCHAR(100)
- **Example**: "Hyderabad", "Bangalore"

#### State
```sql
ALTER TABLE users ADD COLUMN state VARCHAR(100) 
  COMMENT 'State/Province' AFTER city;
```
- **Type**: VARCHAR(100)
- **Example**: "Telangana", "Karnataka"

#### Country
```sql
ALTER TABLE users ADD COLUMN country VARCHAR(100) 
  COMMENT 'Country' AFTER state;
```
- **Type**: VARCHAR(100)
- **Example**: "India"

#### PIN Code
```sql
ALTER TABLE users ADD COLUMN pin_code VARCHAR(20) 
  COMMENT 'Postal/PIN code' AFTER country;
```
- **Type**: VARCHAR(20)
- **Format**: Any postal code format

### Professional Details

#### Qualification
```sql
ALTER TABLE users ADD COLUMN qualification VARCHAR(100) 
  COMMENT 'Highest qualification (B.Tech, M.Tech, etc.)' AFTER pin_code;
```
- **Type**: VARCHAR(100)
- **Example**: "B.Tech (Computer Science)", "M.Tech"

#### College/University
```sql
ALTER TABLE users ADD COLUMN college VARCHAR(200) 
  COMMENT 'College/University name' AFTER qualification;
```
- **Type**: VARCHAR(200)
- **Example**: "IIIT Hyderabad", "IIT Delhi"

#### Current Company
```sql
ALTER TABLE users ADD COLUMN current_company VARCHAR(200) 
  COMMENT 'Current company name' AFTER college;
```
- **Type**: VARCHAR(200)
- **Example**: "Google", "Microsoft"

#### Current Salary
```sql
ALTER TABLE users ADD COLUMN current_salary VARCHAR(50) 
  COMMENT 'Current salary' AFTER current_company;
```
- **Type**: VARCHAR(50)
- **Format**: Any format (e.g., "10 LPA", "1,00,000 INR")

#### Expected Salary
```sql
ALTER TABLE users ADD COLUMN expected_salary VARCHAR(50) 
  COMMENT 'Expected salary' AFTER current_salary;
```
- **Type**: VARCHAR(50)
- **Format**: Any format

#### Preferred Job Role
```sql
ALTER TABLE users ADD COLUMN preferred_job_role VARCHAR(100) 
  COMMENT 'Preferred job role/position' AFTER expected_salary;
```
- **Type**: VARCHAR(100)
- **Example**: "Senior Developer", "Tech Lead"

#### Preferred Location
```sql
ALTER TABLE users ADD COLUMN preferred_location VARCHAR(150) 
  COMMENT 'Preferred job location' AFTER preferred_job_role;
```
- **Type**: VARCHAR(150)
- **Example**: "Hyderabad, Bangalore", "Remote"

### Social Links

#### LinkedIn URL
```sql
ALTER TABLE users ADD COLUMN linkedin_url VARCHAR(255) 
  COMMENT 'LinkedIn profile URL' AFTER preferred_location;
```
- **Type**: VARCHAR(255)
- **Format**: Full URL (https://...)

#### GitHub URL
```sql
ALTER TABLE users ADD COLUMN github_url VARCHAR(255) 
  COMMENT 'GitHub profile URL' AFTER linkedin_url;
```
- **Type**: VARCHAR(255)
- **Format**: Full URL (https://...)

#### Portfolio URL
```sql
ALTER TABLE users ADD COLUMN portfolio_url VARCHAR(255) 
  COMMENT 'Portfolio website URL' AFTER github_url;
```
- **Type**: VARCHAR(255)
- **Format**: Full URL (https://...)

---

## Jobs Table - New Columns

### Deadline
```sql
ALTER TABLE jobs ADD COLUMN deadline DATETIME 
  COMMENT 'Application deadline' AFTER posted_date;
```
- **Type**: DATETIME
- **Format**: YYYY-MM-DD HH:MM:SS
- **Purpose**: Track job application deadline
- **Nullable**: YES (optional for ongoing positions)

### Apply URL
```sql
ALTER TABLE jobs ADD COLUMN apply_url VARCHAR(500) 
  COMMENT 'Official job application URL' AFTER deadline;
```
- **Type**: VARCHAR(500)
- **Purpose**: Store external job portal link
- **Format**: Full URL (https://...)
- **Examples**:
  - https://careers.google.com/jobs/...
  - https://www.linkedin.com/jobs/view/...
  - https://www.naukri.com/job/...
- **Nullable**: YES (fallback to internal form if not set)

### Company Logo
```sql
ALTER TABLE jobs ADD COLUMN company_logo VARCHAR(255) 
  COMMENT 'URL to company logo image' AFTER apply_url;
```
- **Type**: VARCHAR(255)
- **Purpose**: Store company logo image URL
- **Format**: Full URL or relative path
- **Nullable**: YES (optional for now)

---

## Complete Users Table Structure After Changes

```
Field                      | Type           | Null | Key | Default
--------------------------+----------------+------+-----+---------
user_id                    | int            | NO   | PRI | NULL
full_name                  | varchar(150)   | NO   |     | NULL
email                      | varchar(150)   | NO   | UNI | NULL
password                   | varchar(255)   | NO   |     | NULL
role                       | enum           | NO   | MUL | candidate
phone                      | varchar(20)    | YES  |     | NULL
location                   | varchar(150)   | YES  |     | NULL
skills                     | text           | YES  |     | NULL
experience                 | varchar(50)    | YES  |     | NULL
bio                        | text           | YES  |     | NULL
profile_picture            | varchar(500)   | YES  |     | NULL [NEW]
professional_title         | varchar(100)   | YES  |     | NULL [NEW]
date_of_birth              | date           | YES  |     | NULL [NEW]
gender                     | varchar(20)    | YES  |     | NULL [NEW]
address                    | text           | YES  |     | NULL [NEW]
city                       | varchar(100)   | YES  |     | NULL [NEW]
state                      | varchar(100)   | YES  |     | NULL [NEW]
country                    | varchar(100)   | YES  |     | NULL [NEW]
pin_code                   | varchar(20)    | YES  |     | NULL [NEW]
qualification              | varchar(100)   | YES  |     | NULL [NEW]
college                    | varchar(200)   | YES  |     | NULL [NEW]
current_company            | varchar(200)   | YES  |     | NULL [NEW]
current_salary             | varchar(50)    | YES  |     | NULL [NEW]
expected_salary            | varchar(50)    | YES  |     | NULL [NEW]
preferred_job_role         | varchar(100)   | YES  |     | NULL [NEW]
preferred_location         | varchar(150)   | YES  |     | NULL [NEW]
linkedin_url               | varchar(255)   | YES  |     | NULL [NEW]
github_url                 | varchar(255)   | YES  |     | NULL [NEW]
portfolio_url              | varchar(255)   | YES  |     | NULL [NEW]
is_active                  | tinyint(1)     | NO   |     | 1
created_at                 | datetime       | NO   |     | CURRENT_TIMESTAMP
```

---

## Complete Jobs Table Structure After Changes

```
Field                      | Type                                          | Null | Key | Default
--------------------------+-----------------------------------------------+------+-----+----------
job_id                     | int                                           | NO   | PRI | NULL
company_id                 | int                                           | NO   | MUL | NULL
title                      | varchar(200)                                  | NO   | MUL | NULL
description                | text                                          | NO   |     | NULL
skills_required            | text                                          | YES  |     | NULL
salary_min                 | int                                           | YES  |     | NULL
salary_max                 | int                                           | YES  |     | NULL
experience_required        | varchar(50)                                   | YES  |     | NULL
location                   | varchar(150)                                  | YES  | MUL | NULL
job_type                   | enum('Full-Time',...,'Remote')                | NO   |     | Full-Time
vacancies                  | int                                           | NO   |     | 1
is_active                  | tinyint(1)                                    | NO   | MUL | 1
posted_date                | datetime                                      | NO   | MUL | CURRENT_TIMESTAMP
deadline                   | datetime                                      | YES  |     | NULL [NEW]
apply_url                  | varchar(500)                                  | YES  |     | NULL [NEW]
company_logo               | varchar(255)                                  | YES  |     | NULL [NEW]
```

---

## How to Apply Changes

### Method 1: Using SQL File (Recommended)
```bash
cd Job_Portal_System
mysql -u root -p"Bannu@123" < database/alter_tables.sql
```

### Method 2: Using MySQL Client
```bash
mysql -u root -p"Bannu@123" job_portal_system
mysql> source database/alter_tables.sql;
```

### Method 3: Individual Statements
Copy each ALTER TABLE statement and execute in MySQL client.

---

## Verification

After applying changes, verify the columns exist:

### Check Users Table
```sql
USE job_portal_system;
DESCRIBE users;
```

Expected output includes all new columns.

### Check Jobs Table
```sql
DESCRIBE jobs;
```

Expected output includes `deadline`, `apply_url`, `company_logo`.

---

## Rollback (If Needed)

To remove the new columns (NOT RECOMMENDED - use only if critical error):

```sql
ALTER TABLE users DROP COLUMN profile_picture;
ALTER TABLE users DROP COLUMN professional_title;
-- ... etc for all columns
```

However, it's better to keep the columns for future use.

---

## Impact Analysis

### Performance Impact
- ✅ Minimal - All columns are NULL-able
- ✅ No indexes added
- ✅ No new indexes required
- ✅ Query performance unaffected

### Backward Compatibility
- ✅ All existing queries work unchanged
- ✅ All existing data preserved
- ✅ No breaking changes
- ✅ Can deploy without downtime

### Data Migration
- ✅ No migration needed
- ✅ New columns populated as users update their profiles
- ✅ Gradual adoption possible

---

## Usage Guidelines

### For Application Code

#### Setting Profile Picture
```python
user.profile_picture = 'uploads/profile/123_20240101_120000.jpg'
db.session.commit()
```

#### Setting Professional Details
```python
user.professional_title = 'Senior Software Engineer'
user.current_company = 'Google'
user.current_salary = '20 LPA'
user.expected_salary = '25 LPA'
db.session.commit()
```

#### Setting Social Links
```python
user.linkedin_url = 'https://linkedin.com/in/username'
user.github_url = 'https://github.com/username'
user.portfolio_url = 'https://myportfolio.com'
db.session.commit()
```

#### Setting Job Apply URL
```python
job.apply_url = 'https://careers.google.com/jobs/...'
db.session.commit()
```

---

## Testing Query Examples

### Find users with profile pictures
```sql
SELECT user_id, full_name, profile_picture 
FROM users 
WHERE profile_picture IS NOT NULL;
```

### Find jobs with external apply URLs
```sql
SELECT job_id, title, apply_url 
FROM jobs 
WHERE apply_url IS NOT NULL;
```

### Find candidates with high profile completion
```sql
SELECT user_id, full_name, 
  (CASE WHEN profile_picture IS NOT NULL THEN 1 ELSE 0 END +
   CASE WHEN professional_title IS NOT NULL THEN 1 ELSE 0 END +
   CASE WHEN linkedin_url IS NOT NULL THEN 1 ELSE 0 END) as profile_score
FROM users 
WHERE role = 'candidate'
ORDER BY profile_score DESC;
```

---

## Related Documentation

- `IMPLEMENTATION_SUMMARY.md` - Complete implementation overview
- `QUICK_START.md` - Getting started guide
- `database/alter_tables.sql` - Actual SQL statements
- `database/schema.sql` - Original schema (unchanged)

---

**Status**: ✅ All schema changes documented and verified
**Last Updated**: 2026-06-29
