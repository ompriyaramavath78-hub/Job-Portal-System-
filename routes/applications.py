import os
from datetime import datetime
from flask import Blueprint, render_template, redirect, url_for, flash, request, current_app
from flask_login import login_required, current_user
from werkzeug.utils import secure_filename
from models import db
from models.job import Job
from models.application import Application
from models.resume import Resume
from utils import is_allowed_file, save_upload_file

applications_bp = Blueprint('applications', __name__)

@applications_bp.route('/apply/<int:jid>', methods=['GET', 'POST'])
@login_required
def apply(jid):
    if not current_user.is_candidate():
        flash('Only candidates can apply.', 'warning')
        return redirect(url_for('jobs.job_detail', jid=jid))
    
    job = Job.query.filter_by(job_id=jid, is_active=True).first_or_404()
    
    # Check if already applied
    if Application.query.filter_by(user_id=current_user.user_id, job_id=jid).first():
        flash('You already applied for this job.', 'info')
        return redirect(url_for('jobs.job_detail', jid=jid))
    
    # If job has external apply URL, redirect there instead
    if job.apply_url:
        # Record the application in database
        app = Application(user_id=current_user.user_id, job_id=jid,
                         cover_letter='', status='Applied')
        db.session.add(app)
        db.session.commit()
        
        flash(f'Redirecting to {job.company.company_name}\'s official application page...', 'info')
        return redirect(job.apply_url, code=302)
    
    # Fallback to internal application form if no external URL
    resumes = Resume.query.filter_by(user_id=current_user.user_id).all()
    
    if request.method == 'POST':
        cover = request.form.get('cover_letter', '').strip()
        file = request.files.get('resume')
        
        if file and file.filename and is_allowed_file(file.filename, 'resume'):
            orig_name, rel_path, full_path = save_upload_file(file, current_user.user_id, 'resume')
            if full_path:
                file_size = os.path.getsize(full_path)
                r = Resume(user_id=current_user.user_id, file_name=orig_name,
                          file_path=rel_path, file_size=file_size)
                db.session.add(r)
        
        app = Application(user_id=current_user.user_id, job_id=jid,
                         cover_letter=cover, status='Applied')
        db.session.add(app)
        db.session.commit()
        flash(f'Applied to "{job.title}" successfully!', 'success')
        return redirect(url_for('candidate.my_applications'))
    
    return render_template('applications/apply.html', job=job, resumes=resumes, title=f'Apply - {job.title}')


    return render_template('jobs/apply.html', job=job, resumes=resumes, title=f'Apply – {job.title}')

@applications_bp.route('/withdraw/<int:aid>', methods=['POST'])
@login_required
def withdraw(aid):
    app = Application.query.filter_by(application_id=aid, user_id=current_user.user_id).first_or_404()
    if app.status in ['Selected','Rejected']:
        flash('Cannot withdraw a finalised application.','warning')
    else:
        db.session.delete(app); db.session.commit()
        flash('Application withdrawn.','info')
    return redirect(url_for('candidate.my_applications'))
