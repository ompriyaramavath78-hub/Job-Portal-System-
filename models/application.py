from datetime import datetime
from models import db

class Application(db.Model):
    __tablename__ = 'applications'
    application_id  = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id         = db.Column(db.Integer, db.ForeignKey('users.user_id', ondelete='CASCADE'), nullable=False)
    job_id          = db.Column(db.Integer, db.ForeignKey('jobs.job_id',   ondelete='CASCADE'), nullable=False)
    status          = db.Column(db.Enum('Applied','Under Review','Shortlisted','Rejected','Selected'), default='Applied')
    cover_letter    = db.Column(db.Text)
    applied_date    = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at      = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    recruiter_notes = db.Column(db.Text)
    __table_args__  = (db.UniqueConstraint('user_id','job_id', name='uq_user_job'),)

    COLOR = {
        'Applied':      'primary',
        'Under Review': 'warning',
        'Shortlisted':  'info',
        'Rejected':     'danger',
        'Selected':     'success',
    }
    def badge_color(self): return self.COLOR.get(self.status, 'secondary')
