-- ============================================================
-- Job Portal System – Sample Data
-- Run AFTER schema.sql
-- ============================================================

USE job_portal_system;

-- --------------------------------------------------------
-- USERS  (passwords are hashed via werkzeug – plain: Test@1234)
-- We insert pre-hashed values. To generate fresh hashes, run:
--   python -c "from werkzeug.security import generate_password_hash; print(generate_password_hash('Test@1234'))"
-- --------------------------------------------------------
INSERT INTO users (full_name, email, password, role, phone, location, skills, experience, bio) VALUES
('Rahul Sharma',    'rahul@example.com',    'pbkdf2:sha256:600000$abc$demo_hash_replace', 'candidate', '9876543210', 'Hyderabad', 'Python, Flask, MySQL, Django', '2-3 Years', 'Full-stack Python developer with 2+ years of experience.'),
('Priya Reddy',     'priya@example.com',    'pbkdf2:sha256:600000$abc$demo_hash_replace', 'candidate', '9876543211', 'Bangalore', 'React, JavaScript, Node.js, MongoDB', '1-2 Years', 'Frontend developer passionate about UI/UX.'),
('Anil Kumar',      'anil@example.com',     'pbkdf2:sha256:600000$abc$demo_hash_replace', 'candidate', '9876543212', 'Chennai', 'Java, Spring Boot, Microservices', '3-5 Years', 'Senior Java developer specializing in microservices.'),
('TechCorp HR',     'hr@techcorp.com',      'pbkdf2:sha256:600000$abc$demo_hash_replace', 'recruiter', '9876543213', 'Hyderabad', NULL, NULL, NULL),
('InfoSys Recruit', 'recruit@infosys.com',  'pbkdf2:sha256:600000$abc$demo_hash_replace', 'recruiter', '9876543214', 'Bangalore', NULL, NULL, NULL),
('Admin User',      'admin@jobportal.com',  'pbkdf2:sha256:600000$abc$demo_hash_replace', 'admin',     '9000000000', 'Hyderabad', NULL, NULL, NULL);

-- --------------------------------------------------------
-- COMPANIES
-- --------------------------------------------------------
INSERT INTO companies (recruiter_id, company_name, industry, website, description, location, company_size, founded_year) VALUES
(4, 'TechCorp India Pvt Ltd',        'Information Technology',    'https://techcorp.example.com', 'Leading IT solutions provider in India with 500+ clients.', 'Hyderabad, Telangana', '201-500', 2010),
(5, 'Infosys Technologies Ltd',      'IT Services & Consulting',  'https://infosys.com',          'Global leader in next-generation digital services and consulting.', 'Bangalore, Karnataka', '1000+', 1981);

-- --------------------------------------------------------
-- JOBS
-- --------------------------------------------------------
INSERT INTO jobs (company_id, title, description, skills_required, salary_min, salary_max, experience_required, location, job_type, vacancies) VALUES
(1, 'Python Flask Developer',
 'We are looking for a skilled Python Flask Developer to join our backend team.\n\nResponsibilities:\n- Design and build RESTful APIs\n- Work with MySQL databases\n- Collaborate with frontend teams\n- Write clean, testable code\n\nRequirements:\n- Strong Python programming skills\n- Experience with Flask or Django\n- Knowledge of SQL databases\n- Git version control',
 'Python, Flask, MySQL, REST API, Git', 5, 10, '1-2 Years', 'Hyderabad, Telangana', 'Full-Time', 2),

(1, 'React Frontend Developer',
 'Join our growing frontend team to build modern web applications.\n\nResponsibilities:\n- Build responsive UI components\n- Integrate REST APIs\n- Optimize application performance\n\nRequirements:\n- Proficiency in React.js\n- HTML, CSS, JavaScript expertise\n- Experience with REST APIs',
 'React, JavaScript, HTML, CSS, Bootstrap', 4, 8, '0-1 Years', 'Hyderabad, Telangana', 'Full-Time', 3),

(1, 'Data Science Intern',
 'Exciting internship opportunity for final year students.\n\nYou will work on real data problems, build ML models and create dashboards.\n\nRequirements:\n- Basic Python knowledge\n- Familiarity with Pandas, NumPy\n- Interest in Machine Learning',
 'Python, Pandas, NumPy, Machine Learning, Jupyter', 1, 2, 'Fresher', 'Hyderabad, Telangana', 'Internship', 5),

(2, 'Senior Java Developer',
 'We need an experienced Java developer to lead our microservices architecture.\n\nResponsibilities:\n- Design microservices\n- Code review and mentoring\n- Performance optimization\n\nRequirements:\n- 3+ years Java experience\n- Spring Boot expertise\n- Docker & Kubernetes knowledge',
 'Java, Spring Boot, Microservices, Docker, Kubernetes', 12, 20, '3-5 Years', 'Bangalore, Karnataka', 'Full-Time', 1),

(2, 'DevOps Engineer',
 'Looking for a DevOps engineer to strengthen our CI/CD pipelines.\n\nResponsibilities:\n- Maintain AWS infrastructure\n- Automate deployments\n- Monitor system performance\n\nRequirements:\n- AWS or Azure experience\n- Jenkins/GitLab CI knowledge\n- Linux administration skills',
 'AWS, Docker, Kubernetes, Jenkins, Linux, Terraform', 10, 18, '2-3 Years', 'Bangalore, Karnataka', 'Full-Time', 2),

(2, 'Business Analyst – Remote',
 'Remote opportunity for a Business Analyst to work with global clients.\n\nResponsibilities:\n- Gather and document requirements\n- Create process flow diagrams\n- Liaise between business and tech teams\n\nRequirements:\n- Strong analytical skills\n- Experience with Agile/Scrum\n- Excellent communication skills',
 'Business Analysis, Agile, Scrum, SQL, JIRA', 6, 12, '1-2 Years', 'Remote', 'Remote', 4);

-- --------------------------------------------------------
-- APPLICATIONS (sample)
-- --------------------------------------------------------
INSERT INTO applications (user_id, job_id, status, cover_letter, applied_date) VALUES
(1, 1, 'Shortlisted',  'I have 2+ years of Python and Flask experience and am excited about this role.', NOW()),
(1, 3, 'Applied',      'I am a final year CS student eager to apply ML skills.', NOW()),
(2, 2, 'Under Review', 'Frontend development is my passion. I have built 10+ React projects.', NOW()),
(3, 4, 'Applied',      'With 3+ years in Java microservices, I am confident I will add value.', NOW()),
(2, 6, 'Selected',     'I am interested in the remote BA role and have Agile experience.', NOW());

SELECT 'Sample data inserted successfully!' AS Status;
