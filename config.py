import os

class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY") or "jobportal_secret_key"

    SQLALCHEMY_DATABASE_URI = (
        "mysql+pymysql://root:Bannu%40123@localhost:3306/job_portal_system"
    )

    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # File Upload Configuration
    UPLOAD_FOLDER = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'static', 'uploads')
    MAX_CONTENT_LENGTH = 10 * 1024 * 1024  # 10MB max file size
    ALLOWED_PROFILE_EXTENSIONS = {'jpg', 'jpeg', 'png', 'webp'}
    ALLOWED_RESUME_EXTENSIONS = {'pdf', 'doc', 'docx'}