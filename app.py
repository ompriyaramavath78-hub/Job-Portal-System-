from flask import Flask, render_template, redirect, url_for
from flask_login import LoginManager, current_user
from flask_wtf.csrf import CSRFProtect
from config import Config
from models import db
from models.user import User

csrf = CSRFProtect()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)
    csrf.init_app(app)

    login_manager = LoginManager()
    login_manager.init_app(app)
    login_manager.login_view = 'auth.login'
    login_manager.login_message = 'Please log in to access this page.'
    login_manager.login_message_category = 'warning'

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    from routes.auth import auth_bp
    from routes.candidate import candidate_bp
    from routes.recruiter import recruiter_bp
    from routes.jobs import jobs_bp
    from routes.applications import applications_bp

    app.register_blueprint(auth_bp,          url_prefix='/auth')
    app.register_blueprint(candidate_bp,     url_prefix='/candidate')
    app.register_blueprint(recruiter_bp,     url_prefix='/recruiter')
    app.register_blueprint(jobs_bp,          url_prefix='/jobs')
    app.register_blueprint(applications_bp,  url_prefix='/applications')

    @app.route('/')
    def index():
        from models.job import Job
        from models.company import Company
        from models.application import Application
        total_jobs         = Job.query.filter_by(is_active=True).count()
        total_companies    = Company.query.count()
        total_candidates   = User.query.filter_by(role='candidate').count()
        total_applications = Application.query.count()
        recent_jobs        = Job.query.filter_by(is_active=True)\
                               .order_by(Job.posted_date.desc()).limit(6).all()
        return render_template('index.html',
                               total_jobs=total_jobs,
                               total_companies=total_companies,
                               total_candidates=total_candidates,
                               total_applications=total_applications,
                               recent_jobs=recent_jobs)

    with app.app_context():
        db.create_all()

    return app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
