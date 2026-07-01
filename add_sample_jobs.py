"""
Script to populate the database with 50+ realistic sample jobs.
Run this script to add sample data to the job_portal_system database.

Usage: python add_sample_jobs.py
"""

from app import create_app, db
from models.company import Company
from models.job import Job
from models.user import User
from datetime import datetime, timedelta

def create_sample_data():
    """Create sample companies and jobs for testing"""
    
    # Sample Companies Data
    companies_data = [
        {
            'name': 'Google',
            'industry': 'Technology',
            'website': 'https://careers.google.com',
            'location': 'Hyderabad, India',
            'size': '10,000+',
            'founded': 1998,
            'description': 'Google is a technology company specializing in search engines, cloud computing, and AI.'
        },
        {
            'name': 'Microsoft',
            'industry': 'Technology',
            'website': 'https://careers.microsoft.com',
            'location': 'Bangalore, India',
            'size': '5,000+',
            'founded': 1975,
            'description': 'Microsoft is a leading software and cloud services company.'
        },
        {
            'name': 'Amazon',
            'industry': 'Technology/E-commerce',
            'website': 'https://www.amazon.jobs/en/',
            'location': 'Bangalore, India',
            'size': '5,000+',
            'founded': 1994,
            'description': 'Amazon is a global e-commerce and cloud computing platform.'
        },
        {
            'name': 'IBM',
            'industry': 'Technology/IT Services',
            'website': 'https://www.ibm.com/careers',
            'location': 'Bangalore, India',
            'size': '3,000+',
            'founded': 1911,
            'description': 'IBM is a multinational IT services and consulting company.'
        },
        {
            'name': 'Accenture',
            'industry': 'IT Services/Consulting',
            'website': 'https://www.accenture.com/careers',
            'location': 'Bangalore, Hyderabad',
            'size': '10,000+',
            'founded': 1989,
            'description': 'Accenture is a global professional services company.'
        },
        {
            'name': 'Deloitte',
            'industry': 'Consulting/Professional Services',
            'website': 'https://www2.deloitte.com/global/en/careers.html',
            'location': 'Hyderabad, Bangalore, Pune',
            'size': '5,000+',
            'founded': 1845,
            'description': 'Deloitte is a global consulting and professional services firm.'
        },
        {
            'name': 'Infosys',
            'industry': 'IT Services',
            'website': 'https://www.infosys.com/careers',
            'location': 'Bangalore, Pune, Hyderabad',
            'size': '250,000+',
            'founded': 1981,
            'description': 'Infosys is one of India\'s leading IT services companies.'
        },
        {
            'name': 'TCS (Tata Consultancy Services)',
            'industry': 'IT Services',
            'website': 'https://www.tcs.com/careers',
            'location': 'Hyderabad, Bangalore, Mumbai, Pune',
            'size': '500,000+',
            'founded': 1968,
            'description': 'TCS is one of the world\'s largest IT services companies.'
        },
        {
            'name': 'Wipro',
            'industry': 'IT Services',
            'website': 'https://careers.wipro.com',
            'location': 'Bangalore, Hyderabad',
            'size': '200,000+',
            'founded': 1980,
            'description': 'Wipro is a leading global IT services company.'
        },
        {
            'name': 'Capgemini',
            'industry': 'IT Services/Consulting',
            'website': 'https://www.capgemini.com/careers/',
            'location': 'Bangalore, Mumbai, Hyderabad',
            'size': '5,000+',
            'founded': 1967,
            'description': 'Capgemini is a global consulting and technology services company.'
        },
        {
            'name': 'Cognizant',
            'industry': 'IT Services',
            'website': 'https://careers.cognizant.com',
            'location': 'Hyderabad, Pune, Chennai',
            'size': '300,000+',
            'founded': 1994,
            'description': 'Cognizant is a multinational IT services and consulting company.'
        },
        {
            'name': 'Oracle',
            'industry': 'Technology/Software',
            'website': 'https://www.oracle.com/careers/',
            'location': 'Hyderabad, Bangalore',
            'size': '5,000+',
            'founded': 1977,
            'description': 'Oracle is a leading cloud computing and database software company.'
        },
        {
            'name': 'Adobe',
            'industry': 'Technology/Software',
            'website': 'https://adobe.wd5.myworkdayjobs.com',
            'location': 'Noida, Bangalore',
            'size': '2,000+',
            'founded': 1982,
            'description': 'Adobe is a leading provider of creative and document management software.'
        },
        {
            'name': 'Salesforce',
            'industry': 'Cloud Software/CRM',
            'website': 'https://www.salesforce.com/careers/',
            'location': 'Hyderabad, Bangalore',
            'size': '3,000+',
            'founded': 1999,
            'description': 'Salesforce is a leading cloud-based CRM platform.'
        },
        {
            'name': 'Zoho',
            'industry': 'Software/SaaS',
            'website': 'https://www.zoho.com/careers/',
            'location': 'Chennai, Bangalore',
            'size': '10,000+',
            'founded': 1996,
            'description': 'Zoho is a SaaS company offering productivity and business software.'
        },
        {
            'name': 'Tech Mahindra',
            'industry': 'IT Services',
            'website': 'https://careers.techmahindra.com/',
            'location': 'Hyderabad, Pune, Bangalore',
            'size': '150,000+',
            'founded': 1986,
            'description': 'Tech Mahindra is an IT services and business process management company.'
        },
        {
            'name': 'HCL Technologies',
            'industry': 'IT Services',
            'website': 'https://www.hcltech.com/careers',
            'location': 'Bangalore, Noida, Hyderabad',
            'size': '200,000+',
            'founded': 1976,
            'description': 'HCL Technologies is a global IT services company.'
        },
        {
            'name': 'Intel',
            'industry': 'Technology/Semiconductors',
            'website': 'https://www.intel.com/content/www/us/en/jobs.html',
            'location': 'Bangalore, Pune',
            'size': '2,000+',
            'founded': 1968,
            'description': 'Intel is a leading semiconductor and computing company.'
        },
        {
            'name': 'Cisco',
            'industry': 'Technology/Networking',
            'website': 'https://jobs.cisco.com',
            'location': 'Bangalore, Hyderabad',
            'size': '3,000+',
            'founded': 1984,
            'description': 'Cisco is a leading networking and cybersecurity company.'
        },
        {
            'name': 'Nvidia',
            'industry': 'Technology/AI/GPUs',
            'website': 'https://www.nvidia.com/en-us/careers/',
            'location': 'Bangalore, Pune',
            'size': '2,000+',
            'founded': 1993,
            'description': 'Nvidia is a leading AI computing and GPU company.'
        },
    ]

    # Sample Jobs Data
    jobs_data = [
        # Google Jobs
        {'title': 'Senior Software Engineer - Backend', 'company': 'Google', 'location': 'Hyderabad', 'min_salary': 20, 'max_salary': 35, 'type': 'Full-Time', 'exp': '3-5 Years', 'apply': 'https://careers.google.com/jobs/results/?q=backend',
         'desc': 'Join Google\'s backend team to build scalable systems. We\'re looking for experienced engineers with strong problem-solving skills. You\'ll work on projects that impact millions of users worldwide.', 'skills': 'Java, Python, C++, System Design, Microservices, Cloud, Kubernetes'},
        {'title': 'Senior Software Engineer - Frontend', 'company': 'Google', 'location': 'Hyderabad', 'min_salary': 18, 'max_salary': 32, 'type': 'Full-Time', 'exp': '2-3 Years', 'apply': 'https://careers.google.com/jobs/results/?q=frontend',
         'desc': 'Build amazing user experiences for Google\'s products. We need talented frontend engineers to create intuitive and performant web applications.', 'skills': 'React, TypeScript, JavaScript, HTML/CSS, Web Performance'},
        {'title': 'Product Manager', 'company': 'Google', 'location': 'Bangalore', 'min_salary': 25, 'max_salary': 40, 'type': 'Full-Time', 'exp': '5-7 Years', 'apply': 'https://careers.google.com/jobs/results/?q=product+manager',
         'desc': 'Lead product strategy for Google\'s cutting-edge products. Shape the future of technology with your product vision and leadership.', 'skills': 'Product Strategy, Data Analysis, Leadership, Communication'},
        {'title': 'Data Scientist - Analytics', 'company': 'Google', 'location': 'Hyderabad', 'min_salary': 18, 'max_salary': 30, 'type': 'Full-Time', 'exp': '1-2 Years', 'apply': 'https://careers.google.com/jobs/results/?q=data+scientist',
         'desc': 'Build machine learning models to solve complex problems. Work with Google\'s massive datasets and latest ML technologies.', 'skills': 'Python, Machine Learning, SQL, TensorFlow, Statistics'},
        
        # Microsoft Jobs
        {'title': 'Cloud Solutions Architect', 'company': 'Microsoft', 'location': 'Bangalore', 'min_salary': 22, 'max_salary': 38, 'type': 'Full-Time', 'exp': '5-7 Years', 'apply': 'https://careers.microsoft.com/us/en/job/1234567/Cloud-Solutions-Architect',
         'desc': 'Design and implement cloud solutions using Azure. Partner with clients to transform their business using Microsoft technologies.', 'skills': 'Azure, Cloud Architecture, .NET, SQL Server, Leadership'},
        {'title': 'Software Engineer - C# .NET', 'company': 'Microsoft', 'location': 'Bangalore', 'min_salary': 16, 'max_salary': 28, 'type': 'Full-Time', 'exp': '1-2 Years', 'apply': 'https://careers.microsoft.com/us/en/job/search?q=csharp',
         'desc': 'Develop robust backend services using C# and .NET. Build the infrastructure that powers Microsoft\'s enterprise solutions.', 'skills': 'C#, .NET, SQL, Azure, RESTful APIs'},
        {'title': 'AI/ML Engineer', 'company': 'Microsoft', 'location': 'Bangalore', 'min_salary': 20, 'max_salary': 35, 'type': 'Full-Time', 'exp': '2-3 Years', 'apply': 'https://careers.microsoft.com/us/en/job/search?q=ai',
         'desc': 'Work on cutting-edge AI and machine learning projects. Help build intelligent applications that transform industries.', 'skills': 'Python, TensorFlow, PyTorch, Azure ML, Deep Learning'},
        
        # Amazon Jobs
        {'title': 'SDE II - Backend', 'company': 'Amazon', 'location': 'Bangalore', 'min_salary': 20, 'max_salary': 32, 'type': 'Full-Time', 'exp': '2-3 Years', 'apply': 'https://www.amazon.jobs/en/job_search?base_query=SDE+backend',
         'desc': 'Build scalable backend systems for Amazon Web Services. Work on distributed systems that handle billions of requests.', 'skills': 'Java, Python, AWS, Distributed Systems, Databases'},
        {'title': 'AWS Solutions Architect', 'company': 'Amazon', 'location': 'Bangalore', 'min_salary': 25, 'max_salary': 40, 'type': 'Full-Time', 'exp': '5-7 Years', 'apply': 'https://www.amazon.jobs/en/job_search?base_query=Solutions+Architect',
         'desc': 'Design and implement AWS solutions for enterprise clients. Drive cloud transformation and innovation.', 'skills': 'AWS, Cloud Architecture, Linux, Networking, Leadership'},
        {'title': 'Data Engineer', 'company': 'Amazon', 'location': 'Bangalore', 'min_salary': 18, 'max_salary': 30, 'type': 'Full-Time', 'exp': '2-3 Years', 'apply': 'https://www.amazon.jobs/en/job_search?base_query=Data+Engineer',
         'desc': 'Build data pipelines and ETL systems. Work with massive datasets to enable analytics and business intelligence.', 'skills': 'Python, Spark, SQL, AWS, Big Data'},
        
        # IBM Jobs
        {'title': 'Senior Developer - Java', 'company': 'IBM', 'location': 'Bangalore', 'min_salary': 18, 'max_salary': 28, 'type': 'Full-Time', 'exp': '3-5 Years', 'apply': 'https://www.ibm.com/careers/job-search',
         'desc': 'Develop enterprise Java applications for IBM\'s global clients. Work on mission-critical systems.', 'skills': 'Java, Spring Boot, Microservices, Cloud, Docker'},
        {'title': 'Blockchain Developer', 'company': 'IBM', 'location': 'Hyderabad', 'min_salary': 16, 'max_salary': 26, 'type': 'Full-Time', 'exp': '1-2 Years', 'apply': 'https://www.ibm.com/careers/job-search',
         'desc': 'Develop blockchain solutions using Hyperledger. Build decentralized systems for enterprise clients.', 'skills': 'Blockchain, Hyperledger, Solidity, Cryptography, GoLang'},
        {'title': 'QA Automation Engineer', 'company': 'IBM', 'location': 'Bangalore', 'min_salary': 10, 'max_salary': 18, 'type': 'Full-Time', 'exp': '0-1 Years', 'apply': 'https://www.ibm.com/careers/job-search',
         'desc': 'Test and automate testing for IBM\'s software products. Ensure quality and reliability.', 'skills': 'Selenium, Python, JIRA, TestNG, API Testing'},
        
        # Accenture Jobs
        {'title': 'Associate Manager - Cloud Services', 'company': 'Accenture', 'location': 'Hyderabad', 'min_salary': 12, 'max_salary': 20, 'type': 'Full-Time', 'exp': '2-3 Years', 'apply': 'https://www.accenture.com/careers',
         'desc': 'Lead cloud transformation initiatives. Manage teams and deliver cloud solutions to global clients.', 'skills': 'Cloud (AWS/Azure), Project Management, Leadership, Consulting'},
        {'title': 'Senior Consultant - Digital', 'company': 'Accenture', 'location': 'Bangalore', 'min_salary': 15, 'max_salary': 25, 'type': 'Full-Time', 'exp': '3-5 Years', 'apply': 'https://www.accenture.com/careers',
         'desc': 'Advise clients on digital transformation. Implement innovative solutions that drive business value.', 'skills': 'Digital Strategy, Technology, Change Management, Analytics'},
        {'title': 'Application Developer', 'company': 'Accenture', 'location': 'Hyderabad', 'min_salary': 6, 'max_salary': 12, 'type': 'Full-Time', 'exp': 'Fresher', 'apply': 'https://www.accenture.com/careers',
         'desc': 'Start your career as an application developer. Learn and grow in a global organization.', 'skills': 'Java, JavaScript, SQL, Git, Problem Solving'},
        
        # Deloitte Jobs
        {'title': 'Consultant - Management Consulting', 'company': 'Deloitte', 'location': 'Bangalore', 'min_salary': 14, 'max_salary': 23, 'type': 'Full-Time', 'exp': '0-1 Years', 'apply': 'https://www2.deloitte.com/global/en/careers.html',
         'desc': 'Join Deloitte\'s consulting practice. Help clients solve complex business problems.', 'skills': 'Business Analysis, Communication, Problem Solving, Excel'},
        {'title': 'Senior Manager - Technology Consulting', 'company': 'Deloitte', 'location': 'Hyderabad', 'min_salary': 25, 'max_salary': 38, 'type': 'Full-Time', 'exp': '7-10 Years', 'apply': 'https://www2.deloitte.com/global/en/careers.html',
         'desc': 'Lead technology consulting engagements. Build and mentor teams to deliver transformational technology solutions.', 'skills': 'Technology Strategy, Leadership, Enterprise Architecture'},
        
        # Infosys Jobs
        {'title': 'Senior Software Engineer', 'company': 'Infosys', 'location': 'Bangalore', 'min_salary': 15, 'max_salary': 24, 'type': 'Full-Time', 'exp': '3-5 Years', 'apply': 'https://www.infosys.com/careers',
         'desc': 'Build scalable software solutions. Work on projects across diverse industries and technologies.', 'skills': 'Java, Cloud, Microservices, Agile, Testing'},
        {'title': 'Program Manager', 'company': 'Infosys', 'location': 'Pune', 'min_salary': 18, 'max_salary': 30, 'type': 'Full-Time', 'exp': '5-7 Years', 'apply': 'https://www.infosys.com/careers',
         'desc': 'Manage large-scale transformation programs. Drive delivery excellence and client satisfaction.', 'skills': 'Program Management, Leadership, Client Management, Process'},
        
        # TCS Jobs
        {'title': 'Software Engineer - Full Stack', 'company': 'TCS (Tata Consultancy Services)', 'location': 'Hyderabad', 'min_salary': 8, 'max_salary': 15, 'type': 'Full-Time', 'exp': 'Fresher', 'apply': 'https://www.tcs.com/careers',
         'desc': 'Start your IT career with TCS. Develop full-stack web applications and grow your skills.', 'skills': 'HTML, CSS, JavaScript, React, Node.js, SQL'},
        {'title': 'Project Manager', 'company': 'TCS (Tata Consultancy Services)', 'location': 'Bangalore', 'min_salary': 12, 'max_salary': 20, 'type': 'Full-Time', 'exp': '2-3 Years', 'apply': 'https://www.tcs.com/careers',
         'desc': 'Manage IT projects. Ensure timely delivery, quality, and client satisfaction.', 'skills': 'Project Management, Team Leadership, Communication, JIRA'},
        
        # Wipro Jobs
        {'title': 'Senior Software Engineer', 'company': 'Wipro', 'location': 'Bangalore', 'min_salary': 14, 'max_salary': 22, 'type': 'Full-Time', 'exp': '2-3 Years', 'apply': 'https://careers.wipro.com',
         'desc': 'Develop enterprise applications using modern technologies. Grow with one of India\'s leading IT firms.', 'skills': 'Java, Python, Cloud, Databases, Agile'},
        {'title': 'Cloud Engineer', 'company': 'Wipro', 'location': 'Hyderabad', 'min_salary': 16, 'max_salary': 26, 'type': 'Full-Time', 'exp': '2-3 Years', 'apply': 'https://careers.wipro.com',
         'desc': 'Build cloud infrastructure and solutions. Work with AWS, Azure, and GCP.', 'skills': 'AWS, Azure, Terraform, Linux, CI/CD'},
        
        # Capgemini Jobs
        {'title': 'Analyst - Technology', 'company': 'Capgemini', 'location': 'Bangalore', 'min_salary': 6, 'max_salary': 12, 'type': 'Full-Time', 'exp': 'Fresher', 'apply': 'https://www.capgemini.com/careers/',
         'desc': 'Begin your tech career. Learn latest technologies and consulting methodologies.', 'skills': 'Java, JavaScript, SQL, Git, Communication'},
        {'title': 'Senior Consultant - Cloud & Infrastructure', 'company': 'Capgemini', 'location': 'Mumbai', 'min_salary': 18, 'max_salary': 30, 'type': 'Full-Time', 'exp': '5-7 Years', 'apply': 'https://www.capgemini.com/careers/',
         'desc': 'Lead cloud and infrastructure projects. Architect solutions for enterprise clients.', 'skills': 'Cloud Architecture, AWS/Azure, Leadership, Infrastructure'},
        
        # Cognizant Jobs
        {'title': 'GenC Elevate - Software Developer', 'company': 'Cognizant', 'location': 'Hyderabad', 'min_salary': 5, 'max_salary': 10, 'type': 'Full-Time', 'exp': 'Fresher', 'apply': 'https://careers.cognizant.com',
         'desc': 'Join Cognizant\'s graduate program. Build a career in software development.', 'skills': 'Java, Python, SQL, Git, Problem Solving'},
        {'title': 'Senior Programmer Analyst', 'company': 'Cognizant', 'location': 'Pune', 'min_salary': 14, 'max_salary': 23, 'type': 'Full-Time', 'exp': '3-5 Years', 'apply': 'https://careers.cognizant.com',
         'desc': 'Develop enterprise applications. Lead technical teams and deliver innovative solutions.', 'skills': 'Java, Microservices, Cloud, Leadership, Agile'},
        
        # Oracle Jobs
        {'title': 'Database Administrator', 'company': 'Oracle', 'location': 'Bangalore', 'min_salary': 12, 'max_salary': 22, 'type': 'Full-Time', 'exp': '1-2 Years', 'apply': 'https://www.oracle.com/careers/',
         'desc': 'Manage and optimize Oracle databases. Ensure database performance and security.', 'skills': 'Oracle DB, SQL, Backup/Recovery, Performance Tuning'},
        {'title': 'Senior Software Engineer', 'company': 'Oracle', 'location': 'Bangalore', 'min_salary': 20, 'max_salary': 32, 'type': 'Full-Time', 'exp': '3-5 Years', 'apply': 'https://www.oracle.com/careers/',
         'desc': 'Develop cloud and database software. Build enterprise solutions used by millions.', 'skills': 'Java, C++, Cloud Computing, System Design'},
        
        # Adobe Jobs
        {'title': 'Software Engineer - UX Platform', 'company': 'Adobe', 'location': 'Noida', 'min_salary': 18, 'max_salary': 30, 'type': 'Full-Time', 'exp': '2-3 Years', 'apply': 'https://adobe.wd5.myworkdayjobs.com',
         'desc': 'Build amazing UX tools. Work on products used by millions of creative professionals.', 'skills': 'JavaScript, React, Design Systems, WebGL'},
        {'title': 'Security Engineer', 'company': 'Adobe', 'location': 'Bangalore', 'min_salary': 20, 'max_salary': 35, 'type': 'Full-Time', 'exp': '3-5 Years', 'apply': 'https://adobe.wd5.myworkdayjobs.com',
         'desc': 'Protect Adobe\'s infrastructure and products. Implement security solutions and frameworks.', 'skills': 'Cybersecurity, Networking, Cloud Security, Python'},
        
        # Salesforce Jobs
        {'title': 'Salesforce Developer', 'company': 'Salesforce', 'location': 'Bangalore', 'min_salary': 14, 'max_salary': 24, 'type': 'Full-Time', 'exp': '1-2 Years', 'apply': 'https://www.salesforce.com/careers/',
         'desc': 'Build Salesforce solutions and applications. Help organizations transform their businesses.', 'skills': 'Apex, Lightning, Salesforce API, JavaScript'},
        {'title': 'Solution Architect', 'company': 'Salesforce', 'location': 'Hyderabad', 'min_salary': 22, 'max_salary': 35, 'type': 'Full-Time', 'exp': '5-7 Years', 'apply': 'https://www.salesforce.com/careers/',
         'desc': 'Design cloud solutions for enterprise clients. Lead digital transformation initiatives.', 'skills': 'Salesforce, Cloud Architecture, Consulting, Leadership'},
        
        # Zoho Jobs
        {'title': 'Software Developer', 'company': 'Zoho', 'location': 'Chennai', 'min_salary': 8, 'max_salary': 16, 'type': 'Full-Time', 'exp': 'Fresher', 'apply': 'https://www.zoho.com/careers/',
         'desc': 'Build innovative SaaS products. Join a startup-like culture within an established company.', 'skills': 'Java, JavaScript, SQL, Git, Problem Solving'},
        {'title': 'Senior Product Engineer', 'company': 'Zoho', 'location': 'Bangalore', 'min_salary': 16, 'max_salary': 28, 'type': 'Full-Time', 'exp': '3-5 Years', 'apply': 'https://www.zoho.com/careers/',
         'desc': 'Design and develop SaaS products. Shape the future of productivity software.', 'skills': 'Full Stack Development, System Design, Cloud, Leadership'},
        
        # Tech Mahindra Jobs
        {'title': 'Software Developer', 'company': 'Tech Mahindra', 'location': 'Hyderabad', 'min_salary': 8, 'max_salary': 14, 'type': 'Full-Time', 'exp': 'Fresher', 'apply': 'https://careers.techmahindra.com/',
         'desc': 'Start your career with Tech Mahindra. Develop software for global clients.', 'skills': 'Java, Python, SQL, Git, Agile'},
        {'title': 'Senior Engineer', 'company': 'Tech Mahindra', 'location': 'Bangalore', 'min_salary': 14, 'max_salary': 22, 'type': 'Full-Time', 'exp': '3-5 Years', 'apply': 'https://careers.techmahindra.com/',
         'desc': 'Lead development teams. Deliver transformational technology solutions.', 'skills': 'Java, Cloud, Microservices, Team Leadership'},
        
        # HCL Jobs
        {'title': 'Software Engineer', 'company': 'HCL Technologies', 'location': 'Bangalore', 'min_salary': 7, 'max_salary': 13, 'type': 'Full-Time', 'exp': 'Fresher', 'apply': 'https://www.hcltech.com/careers',
         'desc': 'Develop enterprise software. Grow your skills in a global IT services company.', 'skills': 'Java, JavaScript, SQL, Git, Linux'},
        {'title': 'Project Lead', 'company': 'HCL Technologies', 'location': 'Noida', 'min_salary': 12, 'max_salary': 20, 'type': 'Full-Time', 'exp': '3-5 Years', 'apply': 'https://www.hcltech.com/careers',
         'desc': 'Lead software development teams. Manage projects and deliver results.', 'skills': 'Leadership, Project Management, Technical Skills, Communication'},
        
        # Intel Jobs
        {'title': 'Software Engineer - Compiler Optimization', 'company': 'Intel', 'location': 'Bangalore', 'min_salary': 18, 'max_salary': 30, 'type': 'Full-Time', 'exp': '2-3 Years', 'apply': 'https://www.intel.com/content/www/us/en/jobs.html',
         'desc': 'Optimize compilers and development tools. Work on cutting-edge processor technology.', 'skills': 'C++, LLVM, Compiler Design, Performance Optimization'},
        {'title': 'Hardware Engineer', 'company': 'Intel', 'location': 'Bangalore', 'min_salary': 20, 'max_salary': 35, 'type': 'Full-Time', 'exp': '3-5 Years', 'apply': 'https://www.intel.com/content/www/us/en/jobs.html',
         'desc': 'Design next-generation Intel processors. Work on hardware validation and testing.', 'skills': 'VHDL, SystemVerilog, Hardware Design, Simulation'},
        
        # Cisco Jobs
        {'title': 'Software Engineer - Networking', 'company': 'Cisco', 'location': 'Bangalore', 'min_salary': 16, 'max_salary': 28, 'type': 'Full-Time', 'exp': '2-3 Years', 'apply': 'https://jobs.cisco.com',
         'desc': 'Develop networking software and protocols. Build secure communication solutions.', 'skills': 'C/C++, Python, Networking Protocols, Security'},
        {'title': 'Security Research Engineer', 'company': 'Cisco', 'location': 'Hyderabad', 'min_salary': 18, 'max_salary': 32, 'type': 'Full-Time', 'exp': '3-5 Years', 'apply': 'https://jobs.cisco.com',
         'desc': 'Research and develop cybersecurity solutions. Protect networks from evolving threats.', 'skills': 'Cybersecurity, Network Security, Threat Analysis, Python'},
        
        # Nvidia Jobs
        {'title': 'Deep Learning Software Engineer', 'company': 'Nvidia', 'location': 'Bangalore', 'min_salary': 20, 'max_salary': 35, 'type': 'Full-Time', 'exp': '2-3 Years', 'apply': 'https://www.nvidia.com/en-us/careers/',
         'desc': 'Develop deep learning frameworks and tools. Power the AI revolution with GPU computing.', 'skills': 'Python, CUDA, Deep Learning, Frameworks'},
        {'title': 'CUDA Graphics Engineer', 'company': 'Nvidia', 'location': 'Bangalore', 'min_salary': 22, 'max_salary': 38, 'type': 'Full-Time', 'exp': '3-5 Years', 'apply': 'https://www.nvidia.com/en-us/careers/',
         'desc': 'Optimize graphics and AI applications. Leverage GPU technology to solve complex problems.', 'skills': 'CUDA, C++, Graphics Programming, Performance Optimization'},
    ]

    app = create_app()
    with app.app_context():
        # Create a dummy recruiter user if it doesn't exist
        recruiter = User.query.filter_by(email='recruiter@jobportal.com').first()
        if not recruiter:
            recruiter = User(
                full_name='Job Portal Admin',
                email='recruiter@jobportal.com',
                role='recruiter'
            )
            recruiter.set_password('password123')
            db.session.add(recruiter)
            db.session.commit()

        # Create companies and jobs
        for company_data in companies_data:
            # Check if company already exists
            company = Company.query.filter_by(company_name=company_data['name']).first()
            if not company:
                company = Company(
                    recruiter_id=recruiter.user_id,
                    company_name=company_data['name'],
                    industry=company_data['industry'],
                    website=company_data['website'],
                    location=company_data['location'],
                    company_size=company_data['size'],
                    founded_year=company_data['founded'],
                    description=company_data['description']
                )
                db.session.add(company)
                db.session.commit()

        # Add jobs for each company
        for job_data in jobs_data:
            # Check if job already exists
            company = Company.query.filter_by(company_name=job_data['company']).first()
            if company:
                existing_job = Job.query.filter_by(
                    company_id=company.company_id,
                    title=job_data['title']
                ).first()
                if not existing_job:
                    job = Job(
                        company_id=company.company_id,
                        title=job_data['title'],
                        description=job_data['desc'],
                        skills_required=job_data['skills'],
                        salary_min=job_data['min_salary'],
                        salary_max=job_data['max_salary'],
                        experience_required=job_data['exp'],
                        location=job_data['location'],
                        job_type=job_data['type'],
                        vacancies=1,
                        is_active=True,
                        apply_url=job_data['apply'],
                        posted_date=datetime.utcnow() - timedelta(days=int(job_data.get('days', 0)) or 5)
                    )
                    db.session.add(job)
        
        db.session.commit()
        print("✅ Sample data created successfully!")
        print(f"   - Companies: {Company.query.count()}")
        print(f"   - Jobs: {Job.query.count()}")

if __name__ == '__main__':
    create_sample_data()
