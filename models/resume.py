from datetime import datetime
from models import db

class Resume(db.Model):
    __tablename__ = 'resumes'
    resume_id   = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id     = db.Column(db.Integer, db.ForeignKey('users.user_id', ondelete='CASCADE'), nullable=False)
    file_name   = db.Column(db.String(255), nullable=False)
    file_path   = db.Column(db.String(500), nullable=False)
    file_size   = db.Column(db.Integer)
    upload_date = db.Column(db.DateTime, default=datetime.utcnow)

    def size_display(self):
        if not self.file_size: return ''
        kb = self.file_size / 1024
        return f"{kb:.0f} KB" if kb < 1024 else f"{kb/1024:.1f} MB"
