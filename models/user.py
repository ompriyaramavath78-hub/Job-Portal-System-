from datetime import datetime
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from models import db

class User(UserMixin, db.Model):
    __tablename__ = 'users'
    user_id    = db.Column(db.Integer, primary_key=True, autoincrement=True)
    full_name  = db.Column(db.String(150), nullable=False)
    email      = db.Column(db.String(150), unique=True, nullable=False, index=True)
    password   = db.Column(db.String(255), nullable=False)
    role       = db.Column(db.Enum('candidate','recruiter','admin'), nullable=False, default='candidate')
    phone      = db.Column(db.String(20))
    location   = db.Column(db.String(150))
    skills     = db.Column(db.Text)
    experience = db.Column(db.String(50))
    bio        = db.Column(db.Text)
    
    # Profile Picture
    profile_picture = db.Column(db.String(500))
    
    # Personal Details
    professional_title = db.Column(db.String(100))
    date_of_birth = db.Column(db.Date)
    gender = db.Column(db.String(20))
    address = db.Column(db.Text)
    city = db.Column(db.String(100))
    state = db.Column(db.String(100))
    country = db.Column(db.String(100))
    pin_code = db.Column(db.String(20))
    
    # Professional Details
    qualification = db.Column(db.String(100))
    college = db.Column(db.String(200))
    current_company = db.Column(db.String(200))
    current_salary = db.Column(db.String(50))
    expected_salary = db.Column(db.String(50))
    preferred_job_role = db.Column(db.String(100))
    preferred_location = db.Column(db.String(150))
    
    # Social Links
    linkedin_url = db.Column(db.String(255))
    github_url = db.Column(db.String(255))
    portfolio_url = db.Column(db.String(255))
    
    is_active  = db.Column(db.Boolean, default=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    resumes      = db.relationship('Resume',      backref='user',      lazy=True, cascade='all, delete-orphan')
    applications = db.relationship('Application', backref='applicant', lazy=True, cascade='all, delete-orphan')
    companies    = db.relationship('Company',     backref='recruiter', lazy=True, cascade='all, delete-orphan')

    def get_id(self):            return str(self.user_id)
    def set_password(self, p):   self.password = generate_password_hash(p)
    def check_password(self, p): return check_password_hash(self.password, p)
    def is_candidate(self):      return self.role == 'candidate'
    def is_recruiter(self):      return self.role == 'recruiter'
    def is_admin_user(self):     return self.role == 'admin'

    def profile_pct(self):
        """Calculate profile completion percentage based on filled fields"""
        if not self.is_candidate():
            return 0
        fields = [
            self.full_name, self.email, self.phone, self.location,
            self.skills, self.experience, self.bio, self.profile_picture,
            self.professional_title, self.date_of_birth, self.gender, self.address,
            self.city, self.state, self.country, self.pin_code,
            self.qualification, self.college, self.current_company,
            self.current_salary, self.expected_salary
        ]
        return int(sum(1 for f in fields if f) / len(fields) * 100)
