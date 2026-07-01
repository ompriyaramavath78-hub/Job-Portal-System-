from flask import Blueprint, render_template, request
from flask_login import current_user
from sqlalchemy import or_
from models.job import Job
from models.application import Application

jobs_bp = Blueprint('jobs', __name__)

@jobs_bp.route('/')
def list_jobs():
    page  = request.args.get('page', 1, type=int)
    q     = request.args.get('q','').strip()
    loc   = request.args.get('location','').strip()
    jtype = request.args.get('job_type','').strip()
    exp   = request.args.get('experience','').strip()

    query = Job.query.filter_by(is_active=True)
    if q:
        query = query.filter(or_(Job.title.ilike(f'%{q}%'),
                                  Job.skills_required.ilike(f'%{q}%'),
                                  Job.description.ilike(f'%{q}%')))
    if loc:   query = query.filter(Job.location.ilike(f'%{loc}%'))
    if jtype: query = query.filter_by(job_type=jtype)
    if exp:   query = query.filter_by(experience_required=exp)

    jobs = query.order_by(Job.posted_date.desc())\
                .paginate(page=page, per_page=12, error_out=False)

    applied_ids = set()
    if current_user.is_authenticated and current_user.is_candidate():
        applied_ids = {a.job_id for a in
                       Application.query.filter_by(user_id=current_user.user_id).all()}

    return render_template('jobs/list.html', jobs=jobs, applied_ids=applied_ids,
                           q=q, location=loc, job_type=jtype, experience=exp, title='Browse Jobs')

@jobs_bp.route('/<int:jid>')
def job_detail(jid):
    job = Job.query.filter_by(job_id=jid, is_active=True).first_or_404()
    already_applied = False
    if current_user.is_authenticated and current_user.is_candidate():
        already_applied = Application.query.filter_by(
            user_id=current_user.user_id, job_id=jid).first() is not None
    similar = Job.query.filter(Job.company_id==job.company_id,
                               Job.job_id!=jid, Job.is_active==True).limit(3).all()
    return render_template('jobs/detail.html', job=job,
                           already_applied=already_applied, similar=similar, title=job.title)
