import os

class Config:
    # Secret Key
    SECRET_KEY = os.environ.get("SECRET_KEY", "jobportal_secret_key")

    # Database Configuration
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        "DATABASE_URL",
        "mysql+pymysql://root:Bannu%40123@localhost:3306/job_portal_system"
    )

    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # File Upload Configuration
    BASE_DIR = os.path.abspath(os.path.dirname(__file__))

    UPLOAD_FOLDER = os.path.join(BASE_DIR, "static", "uploads")

    MAX_CONTENT_LENGTH = 10 * 1024 * 1024  # 10 MB

    ALLOWED_PROFILE_EXTENSIONS = {"jpg", "jpeg", "png", "webp"}
    ALLOWED_RESUME_EXTENSIONS = {"pdf", "doc", "docx"}