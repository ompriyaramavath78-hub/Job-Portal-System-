from functools import wraps
from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_required, current_user
from models import db
from models.company import Company
from models.job import Job
from models.application import Application
from forms.job_form import JobForm, CompanyForm

recruiter_bp = Blueprint('recruiter', __name__)

def recruiter_only(f):
    @wraps(f)
    def w(*a, **kw):
        if not current_user.is_authenticated or not current_user.is_recruiter():
            flash('Recruiters only.','danger'); return redirect(url_for('index'))
        return f(*a, **kw)
    return w

@recruiter_bp.route('/dashboard')
@login_required
@recruiter_only
def dashboard():
    co = Company.query.filter_by(recruiter_id=current_user.user_id).first()
    if not co:
        flash('Please create your company profile first.','warning')
        return redirect(url_for('recruiter.company_profile'))
    jobs    = Job.query.filter_by(company_id=co.company_id).all()
    jids    = [j.job_id for j in jobs]
    all_a   = Application.query.filter(Application.job_id.in_(jids)).all() if jids else []
    stats   = {
        'total_jobs': len(jobs), 'active_jobs': sum(1 for j in jobs if j.is_active),
        'total_applications': len(all_a),
        'under_review': sum(1 for a in all_a if a.status=='Under Review'),
        'shortlisted':  sum(1 for a in all_a if a.status=='Shortlisted'),
        'selected':     sum(1 for a in all_a if a.status=='Selected'),
        'rejected':     sum(1 for a in all_a if a.status=='Rejected'),
    }
    recent_apps = Application.query.filter(Application.job_id.in_(jids))\
                    .order_by(Application.applied_date.desc()).limit(6).all() if jids else []
    recent_jobs = Job.query.filter_by(company_id=co.company_id)\
                    .order_by(Job.posted_date.desc()).limit(5).all()
    return render_template('recruiter/dashboard.html', company=co, stats=stats,
                           recent_apps=recent_apps, recent_jobs=recent_jobs, title='Dashboard')

@recruiter_bp.route('/company', methods=['GET','POST'])
@login_required
@recruiter_only
def company_profile():
    co   = Company.query.filter_by(recruiter_id=current_user.user_id).first()
    form = CompanyForm(obj=co)
    if form.validate_on_submit():
        if co:
            form.populate_obj(co)
        else:
            co = Company(recruiter_id=current_user.user_id)
            form.populate_obj(co)
            db.session.add(co)
        db.session.commit()
        flash('Company profile saved!','success')
        return redirect(url_for('recruiter.dashboard'))
    return render_template('recruiter/company_profile.html', form=form, company=co, title='Company Profile')

@recruiter_bp.route('/jobs')
@login_required
@recruiter_only
def my_jobs():
    co = Company.query.filter_by(recruiter_id=current_user.user_id).first()
    if not co:
        return redirect(url_for('recruiter.company_profile'))
    page = request.args.get('page',1,type=int)
    jobs = Job.query.filter_by(company_id=co.company_id)\
             .order_by(Job.posted_date.desc())\
             .paginate(page=page, per_page=10, error_out=False)
    return render_template('recruiter/my_jobs.html', jobs=jobs, company=co, title='My Jobs')

@recruiter_bp.route('/jobs/post', methods=['GET','POST'])
@login_required
@recruiter_only
def post_job():
    co = Company.query.filter_by(recruiter_id=current_user.user_id).first()
    if not co:
        return redirect(url_for('recruiter.company_profile'))
    form = JobForm()
    if form.validate_on_submit():
        job = Job(company_id=co.company_id)
        form.populate_obj(job)
        db.session.add(job); db.session.commit()
        flash('Job posted!','success')
        return redirect(url_for('recruiter.my_jobs'))
    return render_template('recruiter/post_job.html', form=form, company=co, title='Post Job')

@recruiter_bp.route('/jobs/edit/<int:jid>', methods=['GET','POST'])
@login_required
@recruiter_only
def edit_job(jid):
    co  = Company.query.filter_by(recruiter_id=current_user.user_id).first_or_404()
    job = Job.query.filter_by(job_id=jid, company_id=co.company_id).first_or_404()
    form= JobForm(obj=job)
    if form.validate_on_submit():
        form.populate_obj(job); db.session.commit()
        flash('Job updated!','success')
        return redirect(url_for('recruiter.my_jobs'))
    return render_template('recruiter/post_job.html', form=form, job=job, company=co, title='Edit Job')

@recruiter_bp.route('/jobs/delete/<int:jid>', methods=['POST'])
@login_required
@recruiter_only
def delete_job(jid):
    co  = Company.query.filter_by(recruiter_id=current_user.user_id).first_or_404()
    job = Job.query.filter_by(job_id=jid, company_id=co.company_id).first_or_404()
    db.session.delete(job); db.session.commit()
    flash('Job deleted.','info')
    return redirect(url_for('recruiter.my_jobs'))

@recruiter_bp.route('/jobs/toggle/<int:jid>', methods=['POST'])
@login_required
@recruiter_only
def toggle_job(jid):
    co  = Company.query.filter_by(recruiter_id=current_user.user_id).first_or_404()
    job = Job.query.filter_by(job_id=jid, company_id=co.company_id).first_or_404()
    job.is_active = not job.is_active; db.session.commit()
    flash(f'Job {"activated" if job.is_active else "deactivated"}.','success')
    return redirect(url_for('recruiter.my_jobs'))

@recruiter_bp.route('/applications/<int:jid>')
@login_required
@recruiter_only
def job_applications(jid):
    co  = Company.query.filter_by(recruiter_id=current_user.user_id).first_or_404()
    job = Job.query.filter_by(job_id=jid, company_id=co.company_id).first_or_404()
    st  = request.args.get('status','')
    q   = Application.query.filter_by(job_id=jid)
    if st: q = q.filter_by(status=st)
    apps= q.order_by(Application.applied_date.desc()).all()
    return render_template('recruiter/job_applications.html', job=job, applications=apps,
                           status_filter=st, title=f'Applications – {job.title}')

@recruiter_bp.route('/applications/update/<int:aid>', methods=['POST'])
@login_required
@recruiter_only
def update_status(aid):
    app = Application.query.get_or_404(aid)
    co  = Company.query.filter_by(recruiter_id=current_user.user_id).first_or_404()
    Job.query.filter_by(job_id=app.job_id, company_id=co.company_id).first_or_404()
    ns  = request.form.get('status')
    if ns in ['Applied','Under Review','Shortlisted','Rejected','Selected']:
        app.status = ns
        app.recruiter_notes = request.form.get('notes','')
        db.session.commit()
        flash(f'Status updated to "{ns}".','success')
    return redirect(url_for('recruiter.job_applications', jid=app.job_id))
