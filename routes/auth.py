from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_user, logout_user, login_required, current_user
from models import db
from models.user import User
from forms.login_form import LoginForm
from forms.register_form import RegisterForm

auth_bp = Blueprint('auth', __name__)

def _redir(user):
    if user.is_recruiter() or user.is_admin_user():
        return redirect(url_for('recruiter.dashboard'))
    return redirect(url_for('candidate.dashboard'))

@auth_bp.route('/login', methods=['GET','POST'])
def login():
    if current_user.is_authenticated:
        return _redir(current_user)
    form = LoginForm()
    if form.validate_on_submit():
        u = User.query.filter_by(email=form.email.data.lower().strip()).first()
        if u and u.check_password(form.password.data) and u.is_active:
            login_user(u, remember=form.remember_me.data)
            flash(f'Welcome back, {u.full_name}!', 'success')
            nxt = request.args.get('next')
            return redirect(nxt) if nxt else _redir(u)
        flash('Invalid email or password.', 'danger')
    return render_template('login.html', form=form, title='Login')

@auth_bp.route('/register', methods=['GET','POST'])
def register():
    if current_user.is_authenticated:
        return _redir(current_user)
    form = RegisterForm()
    if form.validate_on_submit():
        u = User(full_name=form.full_name.data.strip(),
                 email=form.email.data.lower().strip(),
                 phone=form.phone.data.strip() if form.phone.data else None,
                 role=form.role.data)
        u.set_password(form.password.data)
        db.session.add(u)
        db.session.commit()
        flash('Account created! Please login.', 'success')
        return redirect(url_for('auth.login'))
    return render_template('register.html', form=form, title='Register')

@auth_bp.route('/logout')
@login_required
def logout():
    name = current_user.full_name
    logout_user()
    flash(f'Goodbye, {name}!', 'info')
    return redirect(url_for('index'))
