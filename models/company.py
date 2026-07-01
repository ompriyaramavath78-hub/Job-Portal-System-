from datetime import datetime
from models import db

class Company(db.Model):
    __tablename__ = 'companies'
    company_id   = db.Column(db.Integer, primary_key=True, autoincrement=True)
    recruiter_id = db.Column(db.Integer, db.ForeignKey('users.user_id', ondelete='CASCADE'), nullable=False)
    company_name = db.Column(db.String(200), nullable=False)
    industry     = db.Column(db.String(100))
    website      = db.Column(db.String(255))
    description  = db.Column(db.Text)
    location     = db.Column(db.String(150))
    company_size = db.Column(db.String(50))
    founded_year = db.Column(db.Integer)
    created_at   = db.Column(db.DateTime, default=datetime.utcnow)
    jobs         = db.relationship('Job', backref='company', lazy=True, cascade='all, delete-orphan')
