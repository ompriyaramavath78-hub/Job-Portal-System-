import os
from datetime import datetime
from flask import Blueprint, render_template, redirect, url_for, flash, request, current_app, send_file
from flask_login import login_required, current_user
from werkzeug.utils import secure_filename
from models import db
from models.resume import Resume
from models.application import Application
from models.job import Job
from utils import is_allowed_file, save_upload_file, delete_upload_file, format_file_size, get_file_size

candidate_bp = Blueprint('candidate', __name__)

@candidate_bp.route('/dashboard')
@login_required
def dashboard():
    if not current_user.is_candidate():
        flash('Candidates only.','danger')
        return redirect(url_for('index'))
    
    apps = Application.query.filter_by(user_id=current_user.user_id).all()
    stats = {k: sum(1 for a in apps if a.status==v) for k,v in [
        ('applied','Applied'),('under_review','Under Review'),
        ('shortlisted','Shortlisted'),('selected','Selected'),('rejected','Rejected')]}
    stats['total'] = len(apps)
    
    recent_apps = Application.query.filter_by(user_id=current_user.user_id)\
                    .order_by(Application.applied_date.desc()).limit(5).all()
    recent_jobs = Job.query.filter_by(is_active=True)\
                    .order_by(Job.posted_date.desc()).limit(4).all()
    resumes = Resume.query.filter_by(user_id=current_user.user_id).all()
    
    return render_template('candidate/dashboard.html', stats=stats,
                           recent_apps=recent_apps, recent_jobs=recent_jobs,
                           resumes=resumes, title='My Dashboard')

@candidate_bp.route('/profile')
@login_required
def profile():
    if not current_user.is_candidate():
        return redirect(url_for('index'))
    
    return render_template('candidate/profile.html', title='My Profile')

@candidate_bp.route('/profile/edit', methods=['GET', 'POST'])
@login_required
def edit_profile():
    if not current_user.is_candidate():
        flash('Candidates only.', 'danger')
        return redirect(url_for('index'))
    
    if request.method == 'POST':
        try:
            # Personal Details
            current_user.full_name = request.form.get('full_name', '').strip()
            current_user.phone = request.form.get('phone', '').strip()
            current_user.professional_title = request.form.get('professional_title', '').strip()
            current_user.date_of_birth = request.form.get('date_of_birth', None) or None
            current_user.gender = request.form.get('gender', '').strip()
            current_user.address = request.form.get('address', '').strip()
            current_user.city = request.form.get('city', '').strip()
            current_user.state = request.form.get('state', '').strip()
            current_user.country = request.form.get('country', '').strip()
            current_user.pin_code = request.form.get('pin_code', '').strip()
            
            # Professional Details
            current_user.skills = request.form.get('skills', '').strip()
            current_user.experience = request.form.get('experience', '').strip()
            current_user.qualification = request.form.get('qualification', '').strip()
            current_user.college = request.form.get('college', '').strip()
            current_user.current_company = request.form.get('current_company', '').strip()
            current_user.current_salary = request.form.get('current_salary', '').strip()
            current_user.expected_salary = request.form.get('expected_salary', '').strip()
            current_user.preferred_job_role = request.form.get('preferred_job_role', '').strip()
            current_user.preferred_location = request.form.get('preferred_location', '').strip()
            current_user.bio = request.form.get('bio', '').strip()
            
            # Social Links
            current_user.linkedin_url = request.form.get('linkedin_url', '').strip()
            current_user.github_url = request.form.get('github_url', '').strip()
            current_user.portfolio_url = request.form.get('portfolio_url', '').strip()
            
            # Handle profile picture upload
            if 'profile_picture' in request.files:
                file = request.files['profile_picture']
                if file and file.filename:
                    if not is_allowed_file(file.filename, 'profile'):
                        flash('Only JPG, JPEG, PNG, and WEBP images are allowed.', 'danger')
                    else:
                        # Delete old profile picture if exists
                        if current_user.profile_picture:
                            delete_upload_file(current_user.profile_picture)
                        
                        # Save new profile picture
                        orig_name, rel_path, full_path = save_upload_file(file, current_user.user_id, 'profile')
                        if rel_path:
                            current_user.profile_picture = rel_path
                            flash('Profile picture updated!', 'success')
                        else:
                            flash('Error uploading profile picture.', 'danger')
            
            db.session.commit()
            flash('Profile updated successfully!', 'success')
            return redirect(url_for('candidate.profile'))
        
        except Exception as e:
            db.session.rollback()
            flash(f'Error updating profile: {str(e)}', 'danger')
            return redirect(url_for('candidate.edit_profile'))
    
    return render_template('candidate/edit_profile.html', title='Edit Profile')

@candidate_bp.route('/profile/picture/delete', methods=['POST'])
@login_required
def delete_profile_picture():
    if not current_user.is_candidate():
        flash('Candidates only.', 'danger')
        return redirect(url_for('index'))
    
    if current_user.profile_picture:
        if delete_upload_file(current_user.profile_picture):
            current_user.profile_picture = None
            db.session.commit()
            flash('Profile picture deleted.', 'success')
        else:
            flash('Error deleting profile picture.', 'danger')
    
    return redirect(url_for('candidate.edit_profile'))

@candidate_bp.route('/resumes', methods=['GET', 'POST'])
@login_required
def upload_resume():
    if not current_user.is_candidate():
        return redirect(url_for('index'))
    
    if request.method == 'POST':
        file = request.files.get('resume')
        
        if not file or not file.filename:
            flash('No file selected.', 'danger')
        elif not is_allowed_file(file.filename, 'resume'):
            flash('Only PDF, DOC, and DOCX files are allowed.', 'danger')
        else:
            # Save resume file
            orig_name, rel_path, full_path = save_upload_file(file, current_user.user_id, 'resume')
            
            if rel_path and full_path:
                file_size = get_file_size(full_path)
                r = Resume(user_id=current_user.user_id, file_name=orig_name,
                          file_path=rel_path, file_size=file_size)
                db.session.add(r)
                db.session.commit()
                flash('Resume uploaded successfully!', 'success')
            else:
                flash('Error uploading resume.', 'danger')
        
        return redirect(url_for('candidate.upload_resume'))
    
    resumes = Resume.query.filter_by(user_id=current_user.user_id)\
                .order_by(Resume.upload_date.desc()).all()
    
    return render_template('candidate/upload_resume.html', resumes=resumes, title='My Resumes')

@candidate_bp.route('/resumes/<int:rid>/download')
@login_required
def download_resume(rid):
    if not current_user.is_candidate():
        flash('Candidates only.', 'danger')
        return redirect(url_for('index'))
    
    resume = Resume.query.filter_by(resume_id=rid, user_id=current_user.user_id).first_or_404()
    file_path = os.path.join(current_app.root_path, 'static', resume.file_path)
    
    if not os.path.exists(file_path):
        flash('File not found.', 'danger')
        return redirect(url_for('candidate.upload_resume'))
    
    return send_file(file_path, as_attachment=True, download_name=resume.file_name)

@candidate_bp.route('/resumes/<int:rid>/delete', methods=['POST'])
@login_required
def delete_resume(rid):
    if not current_user.is_candidate():
        flash('Candidates only.', 'danger')
        return redirect(url_for('index'))
    
    resume = Resume.query.filter_by(resume_id=rid, user_id=current_user.user_id).first_or_404()
    
    # Delete file
    if delete_upload_file(resume.file_path):
        db.session.delete(resume)
        db.session.commit()
        flash('Resume deleted.', 'success')
    else:
        flash('Error deleting resume.', 'danger')
    
    return redirect(url_for('candidate.upload_resume'))

@candidate_bp.route('/applications')
@login_required
def my_applications():
    if not current_user.is_candidate():
        return redirect(url_for('index'))
    
    page = request.args.get('page', 1, type=int)
    status = request.args.get('status', '')
    
    q = Application.query.filter_by(user_id=current_user.user_id)
    if status:
        q = q.filter_by(status=status)
    
    apps = q.order_by(Application.applied_date.desc())\
             .paginate(page=page, per_page=10, error_out=False)
    
    return render_template('candidate/applications.html', applications=apps,
                           status_filter=status, title='My Applications')

