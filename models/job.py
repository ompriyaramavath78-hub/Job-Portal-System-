from datetime import datetime
from models import db

class Job(db.Model):
    __tablename__ = 'jobs'
    job_id              = db.Column(db.Integer, primary_key=True, autoincrement=True)
    company_id          = db.Column(db.Integer, db.ForeignKey('companies.company_id', ondelete='CASCADE'), nullable=False)
    title               = db.Column(db.String(200), nullable=False)
    description         = db.Column(db.Text, nullable=False)
    skills_required     = db.Column(db.Text)
    salary_min          = db.Column(db.Integer)
    salary_max          = db.Column(db.Integer)
    experience_required = db.Column(db.String(50))
    location            = db.Column(db.String(150))
    job_type            = db.Column(db.Enum('Full-Time','Part-Time','Contract','Internship','Remote'), default='Full-Time')
    vacancies           = db.Column(db.Integer, default=1)
    is_active           = db.Column(db.Boolean, default=True)
    posted_date         = db.Column(db.DateTime, default=datetime.utcnow)
    deadline            = db.Column(db.DateTime)
    
    # External Links
    apply_url           = db.Column(db.String(500))  # Official apply portal URL
    company_logo        = db.Column(db.String(255))  # Company logo URL
    
    applications        = db.relationship('Application', backref='job', lazy=True, cascade='all, delete-orphan')

    def salary_display(self):
        if self.salary_min and self.salary_max:
            return f"₹{self.salary_min}–{self.salary_max} LPA"
        if self.salary_min:  return f"₹{self.salary_min}+ LPA"
        if self.salary_max:  return f"Up to ₹{self.salary_max} LPA"
        return "Not Disclosed"

    def apps_count(self): return len(self.applications)
